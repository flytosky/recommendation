from flask import Flask
from flask import jsonify
from flaskext.mysql import MySQL
import serviceLDA


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = ""
app.config['MYSQL_DATABASE_HOST'] = "localhost"


@app.route('/serviceRecommodation')
def main(string):
    strList = string.split(' ')
    return jsonify()

if __name__ == "__main__":
    app.debug = True
    app.run(port=9033)
