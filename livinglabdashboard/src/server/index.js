const express = require("express");
const bodyParser = require("body-parser");
const jwt = require("jsonwebtoken");
const { Sequelize, DataTypes } = require("sequelize");

const app = express();
app.use(bodyParser.json());

const sequelize = new Sequelize(
  "postgres://user:password@postgres_new:5432/livinglabvisualization"
);

// Definieren Sie Ihr User-Modell
const User = sequelize.define("User", {
  email: {
    type: DataTypes.STRING,
    unique: true,
  },
  password: DataTypes.STRING,
});

// Definieren Sie Ihr Data-Modell
const Data = sequelize.define("Data", {
  name: DataTypes.STRING,
  value: DataTypes.FLOAT,
  timestamp: {
    type: DataTypes.DATE,
    defaultValue: Sequelize.NOW,
  },
});

// Authentifizierungs-Endpoint
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ where: { email } });
  if (user && user.password === password) {
    // Passwort-Hashing empfohlen
    const token = jwt.sign({ id: user.id }, "your_jwt_secret", {
      expiresIn: "1h",
    });
    res.json({ token });
  } else {
    res.status(401).json({ message: "Invalid credentials" });
  }
});

// Middleware zur Überprüfung des Tokens
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (authHeader) {
    const token = authHeader.split(" ")[1];
    jwt.verify(token, "your_jwt_secret", (err, user) => {
      if (err) {
        return res.sendStatus(403);
      }
      req.user = user;
      next();
    });
  } else {
    res.sendStatus(401);
  }
};

// Endpoint zum Abrufen der aktuellen Benutzerdaten
app.get("/me", authenticate, async (req, res) => {
  const user = await User.findByPk(req.user.id, {
    attributes: ["id", "email"],
  });
  res.json(user);
});

// Endpoint zum Abrufen der Daten
app.get("/data", authenticate, async (req, res) => {
  const limit = parseInt(req.query.limit) || 500;
  const data = await Data.findAll({
    limit,
    order: [["timestamp", "DESC"]],
  });
  res.json(data);
});

// Starten des Servers
const startServer = async () => {
  try {
    await sequelize.authenticate();
    await sequelize.sync();
    app.listen(3001, () => {
      console.log("Backend läuft auf Port 3001");
    });
  } catch (error) {
    console.error("Unable to connect to the database:", error);
  }
};

startServer();
