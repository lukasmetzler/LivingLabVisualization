from flask import Flask, jsonify
import psycopg2

conn = psycopg2.connect(
    database="EVI",
    user="lukasmetzler",
    password="lukasmetzler",
    host="localhost",
    port="5432"
)

app = Flask(__name__)

@app.route('/api/metrological_data', methods=['GET'])
def get_metrological_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM metrological_data')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)


###############################################################
@app.route('/api/data', methods=['GET'])
def get_data():
    # Hier könntest du Logik hinzufügen, um Daten zu generieren
    data = {'value1': 42, 'value2': 56}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
