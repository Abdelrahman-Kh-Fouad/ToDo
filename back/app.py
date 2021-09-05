from flask import Flask     
from flask_restful import reqparse, abort, Api, Resource
from DBOperations import DataBase
from flask_cors import CORS
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__ )
Cors = CORS(app)
CORS(app , CORS_SUPPORTS_CREDENTIALS = False)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://database:27017'
db =DataBase()
dbUsers = SQLAlchemy()
dbUsers.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
parser = reqparse.RequestParser()
parser.add_argument('text', type=str)


class DeleteAndChange(Resource):
    def delete(self, todo_id):
        db.RemoveById(todo_id)
        
        return '', 201

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

class ListAndInsert(Resource):
    def get(self):
        return db.GetAllForJsonfy() , 201

    def post(self):
        args = parser.parse_args()
        print(args['text'])
        insetedId = db.Insert(args['text'])
        return insetedId, 201


    
api.add_resource(ListAndInsert, '/todo/')
api.add_resource(DeleteAndChange, '/todo/<todo_id>')
# @app.route('/data' )
# def SendData():    
#     dataAsDict = db.GetAllForJsonfy()
#     #print(db.GetAllForJsonfy()) 
#     return json.dumps(dataAsDict)



# @app.route('/del/<id>')
# def Delete(id):
#     db.RemoveById((id))
#     return 'OK'


# @app.route('/pro' , methods=['POST'])
# def Pro():
#     print(request.data)
#     if request.method=='POST':
#         if request.json['action']=='Add':
#             db.Insert(request.json['text'])
#     return 'OK'


# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0" , port=5000) 
