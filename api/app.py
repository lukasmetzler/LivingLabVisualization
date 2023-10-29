from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Hier könntest du Logik hinzufügen, um Daten zu generieren
    data = {'value1': 42, 'value2': 56}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
