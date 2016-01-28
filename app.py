from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import serviceLDA


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root"
app.config['MYSQL_DATABASE_DB'] = "climateService"
app.config['MYSQL_DATABASE_HOST'] = "localhost"


@app.route('/serviceRecommendation', methods=['POST'])
def main():
    print request.json.get('keywords')
    string = request.json.get('keywords')
    strList = string.split(' ')
    serviceId = serviceLDA.getService(strList)
    cursor = mysql.get_db().cursor()
    sql = "SELECT id, name, url FROM ClimateService WHERE id=%d"%(int(serviceId))
    cursor.execute(sql)
    res = cursor.fetchall()[0]
    return jsonify(id=res[0], name=res[1], url=res[2])

if __name__ == "__main__":
    app.debug = True
    app.run(port=9033)
