const pgp = require("pg-promise")();
const db = pgp({
  host: "postgres_new",
  port: 5432,
  database: "evi",
  user: "lukasmetzler",
  password: "lukasmetzler",
});

module.exports = db;
