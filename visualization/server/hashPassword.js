const bcrypt = require("bcryptjs");

const password = "lukasmetzler";

bcrypt.hash(password, 10, (err, hash) => {
  if (err) throw err;
  console.log("Gehashtes Passwort:", hash);
});
