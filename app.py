from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import serviceLDA


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root"
app.config['MYSQL_DATABASE_DB'] = "climateService"
app.config['MYSQL_DATABASE_HOST'] = "localhost"

topic_word_, doc_topic_ = serviceLDA.getModel()


@app.route('/serviceRecommendation', methods=['POST'])
def getRecommendation():
    res_dict = {}
    string = request.json.get('keywords')
    strList = string.split(' ')
    if string in res_dict.keys():
        return jsonify(id=res_dict[string][0], name=res_dict[string][1], url=res_dict[string][2])
    serviceId = serviceLDA.getService(strList, topic_word_, doc_topic_)
    cursor = mysql.get_db().cursor()
    sql = "SELECT id, name, url FROM ClimateService WHERE id=%d"%(int(serviceId))
    cursor.execute(sql)
    res = cursor.fetchall()[0]
    res_dict[string] = [res[0], res[1], res[2]]
    return jsonify(id=res[0], name=res[1], url=res[2])

if __name__ == "__main__":
    app.debug = True
    app.run(port=9033)
