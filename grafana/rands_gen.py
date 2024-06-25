import secrets
import string

# Funktion zur Generierung einer zufälligen Zeichenfolge
def generate_random_string(length=16):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Zufällige Zeichenfolge generieren
random_string = generate_random_string()
print(f"Generated random string: {random_string}")
