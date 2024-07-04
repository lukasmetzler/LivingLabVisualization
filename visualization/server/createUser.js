const bcrypt = require("bcryptjs");
const db = require("./db"); // Stellen Sie sicher, dass die Verbindung zur Datenbank korrekt ist

const email = "lukasx16@gmail.com"; // Ändern Sie diese E-Mail-Adresse
const password = "lukasmetzler";
const firstName = "Lukas";
const lastName = "Metzler";

async function createUser() {
  try {
    // Überprüfen, ob die E-Mail-Adresse bereits existiert
    const existingUser = await db.oneOrNone(
      "SELECT * FROM users WHERE email = $1",
      [email]
    );

    if (existingUser) {
      console.error("Error: E-Mail-Adresse existiert bereits");
      return;
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await db.one(
      "INSERT INTO users(email, password, first_name, last_name) VALUES($1, $2, $3, $4) RETURNING id, email, first_name, last_name",
      [email, hashedPassword, firstName, lastName]
    );
    console.log("User created:", result);
  } catch (error) {
    console.error("Error creating user:", error.message);
  }
}

createUser();
