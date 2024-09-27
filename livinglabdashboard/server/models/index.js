const express = require("express");
const bodyParser = require("body-parser");
const { Sequelize, DataTypes } = require("sequelize");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

// Initialize Express App
const app = express();

app.use(bodyParser.json());

// Database Connection
const sequelize = new Sequelize(
  "livinglabvisualization",
  "lukasmetzler",
  "lukasmetzler",
  {
    host: "localhost",
    dialect: "postgres",
  }
);

// User Model
const User = require("./models/user")(sequelize, DataTypes);

// Routes
app.post("/api/login", async (req, res) => {
  const { username, password } = req.body;
  // Find user by username
  const user = await User.findOne({ where: { username } });
  if (!user)
    return res.status(401).json({ message: "Invalid username or password" });

  // Check password
  const valid = await bcrypt.compare(password, user.password);
  if (!valid)
    return res.status(401).json({ message: "Invalid username or password" });

  // Generate JWT
  const token = jwt.sign({ id: user.id }, "your_jwt_secret");
  res.json({ token });
});

app.post("/api/register", async (req, res) => {
  const { username, email, password } = req.body;

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Create user
  try {
    const user = await User.create({
      username,
      email,
      password: hashedPassword,
    });
    res.json({ message: "User created", user });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Export the app
module.exports = app;
