# kafka/app.py
from flask import Flask, request, jsonify
from models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
import jwt
from datetime import datetime, timedelta
import os
import bcrypt

app = Flask(__name__)

# Konfiguriere die Datenbankverbindung
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@postgres_new:5432/livinglabvisualization",
)
SECRET_KEY = os.getenv("SECRET_KEY", "your_jwt_secret")

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

migrate = Migrate(app, Base.metadata)


# Registrierungsroute
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if session.query(User).filter_by(email=email).first():
        return jsonify({"message": "Email bereits registriert"}), 400

    new_user = User(email=email)
    new_user.set_password(password)

    session.add(new_user)
    session.commit()

    return jsonify({"message": "Benutzer erfolgreich registriert"}), 201


# Login-Route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = session.query(User).filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode(
            {"user_id": user.id, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY,
            algorithm="HS256",
        )
        return jsonify({"token": token})

    return jsonify({"message": "Ungültige Anmeldedaten"}), 401


# Authentifizierte Route zum Abrufen von Benutzerdaten
@app.route("/me", methods=["GET"])
def me():
    auth_header = request.headers.get("Authorization")
    if auth_header:
        try:
            token = auth_header.split(" ")[1]
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user = session.query(User).get(decoded["user_id"])
            return jsonify({"id": user.id, "email": user.email})
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token abgelaufen"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Ungültiges Token"}), 401
    return jsonify({"message": "Token fehlt"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
