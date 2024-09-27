const express = require("express");
const bodyParser = require("body-parser");
const { Sequelize, DataTypes } = require("sequelize");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const cors = require("cors");

// Initialize Express App
const app = express();

// Use body-parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Enable CORS if needed
app.use(cors());

// Database Connection
const sequelize = new Sequelize(
  process.env.DB_NAME || "livinglabvisualization",
  process.env.DB_USER || "lukasmetzler",
  process.env.DB_PASSWORD || "lukasmetzler",
  {
    host: process.env.DB_HOST || "localhost",
    dialect: "postgres",
  }
);

// Test Database Connection
sequelize
  .authenticate()
  .then(() => {
    console.log(
      "Connection to the database has been established successfully."
    );
  })
  .catch((error) => {
    console.error("Unable to connect to the database:", error);
  });

// Define User Model
const User = sequelize.define("User", {
  username: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
    validate: {
      isEmail: true,
    },
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

// Sync Model with Database
sequelize
  .sync()
  .then(() => {
    console.log("User model synchronized with the database.");
  })
  .catch((error) => {
    console.error("Error synchronizing the User model:", error);
  });

// Secret Key for JWT (Use environment variable in production)
const JWT_SECRET = process.env.JWT_SECRET || "your_jwt_secret";

// Routes

// Registration Route
app.post("/api/register", async (req, res) => {
  const { username, email, password } = req.body;

  try {
    // Check if user already exists
    const userExists = await User.findOne({ where: { username } });
    if (userExists) {
      return res.status(400).json({ message: "Username already taken" });
    }

    // Hash Password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create User
    const user = await User.create({
      username,
      email,
      password: hashedPassword,
    });

    // Respond with success message
    res.status(201).json({
      message: "User registered successfully",
      user: { username: user.username, email: user.email },
    });
  } catch (error) {
    console.error("Registration Error:", error);
    res.status(500).json({ message: "An error occurred during registration" });
  }
});

// Login Route
app.post("/api/login", async (req, res) => {
  const { username, password } = req.body;

  try {
    // Find User
    const user = await User.findOne({ where: { username } });
    if (!user) {
      return res.status(401).json({ message: "Invalid username or password" });
    }

    // Compare Passwords
    const valid = await bcrypt.compare(password, user.password);
    if (!valid) {
      return res.status(401).json({ message: "Invalid username or password" });
    }

    // Generate JWT Token
    const token = jwt.sign(
      { id: user.id, username: user.username },
      JWT_SECRET,
      { expiresIn: "1h" }
    );

    // Respond with token
    res.json({ token });
  } catch (error) {
    console.error("Login Error:", error);
    res.status(500).json({ message: "An error occurred during login" });
  }
});

// Protected Route Example (Optional)
app.get("/api/profile", authenticateToken, async (req, res) => {
  try {
    // Get user from database
    const user = await User.findByPk(req.user.id, {
      attributes: ["username", "email"],
    });

    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    // Respond with user profile
    res.json({ user });
  } catch (error) {
    console.error("Profile Error:", error);
    res
      .status(500)
      .json({ message: "An error occurred while fetching the profile" });
  }
});

// Middleware to Authenticate Token
function authenticateToken(req, res, next) {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1]; // Bearer TOKEN

  if (!token) return res.status(401).json({ message: "Access token missing" });

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      console.error("Token Verification Error:", err);
      return res.status(403).json({ message: "Invalid access token" });
    }
    req.user = user;
    next();
  });
}

// Export the Express app
module.exports = app;
