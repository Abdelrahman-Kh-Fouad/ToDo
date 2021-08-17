# from flask import Flask, jsonify, request
# from pymongo import MongoClient 
# from time import time
# from bson.objectid import ObjectId
# import os
# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app)


# # ----> Creating/Connecting Db

# MONGO_INITDB_ROOT_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
# MONGO_INITDB_ROOT_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
# DATABASE_URL = f'mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@mongo:27017'

# client = MongoClient(DATABASE_URL)
# database = client['dome_database']
# col = database['tasks']

# app.config["MONGO_URI"] = DATABASE_URL

# # ----> CRUD API
# @app.route('/tasks', methods=["GET"])
# def get():
#     cursor = col.find({})
#     tasks = list_queries(cursor)
#     return jsonify({'Tasks': tasks})

# @app.route('/tasks', methods=["POST"])
# def post():
#     new_task = {'title' : request.json['title'], 'status': False, 'due': time()} 
#     col.insert_one(new_task)
#     return 'OK'

# @app.route('/tasks/<int:index>', methods=["DELETE"])
# def delete(index):
#     id = get_id(index)
#     col.delete_one({"_id": ObjectId(id)})
#     return 'OK'

# @app.route('/tasks/<int:index>', methods=["PUT"])
# def update(index):
#     id = get_id(index)
#     col.update_one({"_id": ObjectId(id)}, {"$set": {'title': request.json['title']}}, upsert=True)
#     return 'OK'

# # Which is the right one? PUT method becouse we update the resources 
# # Or GET becouse i just need to reverse and the body will be empty
# @app.route('/tasks/<int:index>/check', methods=['PUT'])
# def check(index):
#     id = get_id(index)
#     col.update_one({'_id': ObjectId(id)}, {"$set": {'status': request.json['status']}}, upsert=True)
#     return 'OK'


# @app.route('/')
# def base():
#     return str(client.database_names())
    


# # ----> Helper functions
# def get_id(index):
#     tasks = col.find({})
#     task = tasks[index]
#     id = task["_id"]
#     return id

# def list_queries(cursor):
#     tasks = []
#     for query in cursor:
#         tasks.append({'title': query['title'], 'status': query['status'], 'due': query['due']})
#     return tasks

# # ----> WSGI
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000) # host and port in flask container


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
