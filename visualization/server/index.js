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

app.use("/", authRoutes);
app.use("/api-docs", swaggerUi.serve, (req, res) => {
  const options = {
    swaggerOptions: {
      url: "/api-docs/swagger.json",
    },
  };
  swaggerUi.setup(specs, options)(req, res);
});

/*app.get("/", (req, res) => {
  res.send("Hello World!");
});
 */
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
