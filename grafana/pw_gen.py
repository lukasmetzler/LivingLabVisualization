import bcrypt

password = "admin"
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed.decode())
