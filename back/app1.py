import re
from flask import Flask, redirect, render_template ,request ,json
from dbOperations import DataBase
from flask_cors import CORS, cross_origin


app = Flask(__name__ )
Cors = CORS(app)


CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["MONGO_URI"] = 'mongodb://mongo:27017'


@app.route('/data' )
def SendData():    
    dataAsDict = db.GetAllForJsonfy()
    print(db.GetAllForJsonfy()) 
    return json.dumps(dataAsDict)



@app.route('/del/<id>')
def Delete(id):
    db.RemoveById((id))
    return 'OK'


@app.route('/pro' , methods=['POST'])
def Pro():
    print(request.data)
    if request.method=='POST':
        if request.json['action']=='Add':
            db.Insert(request.json['text'])
    return 'OK'


if __name__ == '__main__':
    global db
    db =DataBase()

    app.run(debug=True, host='0.0.0.0', port=5000) 
