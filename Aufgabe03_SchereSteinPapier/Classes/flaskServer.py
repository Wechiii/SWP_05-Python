from flask import Flask, request
import sqlite3

app = Flask(__name__)


def setup_db():
    connection = sqlite3.connect('schereSteinPapierEchseSpock.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS counts (id INTEGER PRIMARY KEY AUTOINCREMENT, symbole TEXT, count TEXT)")


def speichern(symbole):
    connection = sqlite3.connect('schereSteinPapierEchseSpock.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO counts (symbole, count) VALUES ('{}','{}').format(symbole['symbol'], symbole['count'])")

    connection.commit()


@app.route('/saveStats', methods=['POST'])
def post_statistics():
    if request.is_json:
        speichern(request.json)
        return 'Daten eingelesen'
    else:
        return 'Speicherfehler'


if __name__ == '__main__':
    setup_db()
    app.run(debug=True)