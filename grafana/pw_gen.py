import bcrypt

# Passwort im Klartext
password_plain = 'admin'

# Salt generieren
salt = bcrypt.gensalt()

# Passwort hashen
password_hashed = bcrypt.hashpw(password_plain.encode('utf-8'), salt)

print(f"Password Hash: {password_hashed.decode('utf-8')}")
print(f"Salt: {salt.decode('utf-8')}")