const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const authRoutes = require("./routes/auth");
const { swaggerUi, specs } = require("./swagger");

const app = express();
const port = process.env.PORT || 5000;

// CORS-Konfiguration
const corsOptions = {
  origin: "*",
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
  credentials: true,
  optionsSuccessStatus: 200,
};

app.use(cors(corsOptions));
app.use(bodyParser.json());

app.use("/auth", authRoutes);
app.use("/auth/api-docs", swaggerUi.serve, swaggerUi.setup(specs));

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
