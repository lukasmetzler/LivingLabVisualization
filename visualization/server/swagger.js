const swaggerJsDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "API Documentation",
      version: "1.0.0",
      description: "API documentation for your application",
    },
    servers: [
      {
        url: "/auth",
      },
    ],
  },
  apis: ["./routes/*.js"], // Pfad zu den API-Routen
};

const specs = swaggerJsDoc(options);

module.exports = {
  swaggerUi,
  specs,
};
