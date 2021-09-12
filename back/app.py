from flask import Flask     
from flask_restful import reqparse, abort, Api, Resource ,request
from DBOperations import MongoDataBase , SQLDataBase
from flask_cors import CORS
from flask_login import LoginManager 
import requests


app = Flask(__name__ )
Cors = CORS(app)
CORS(app , CORS_SUPPORTS_CREDENTIALS = False)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://database:27017'
dbData = None

parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

client_id = '4ebb67bce288c83e5459'
client_secret ='48efba84350d8e5111647a5d01f0f741456ae316'


class GithubToken(Resource):
    def get (self , code ):
        r = requests.post(f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}")
        result = r.text
        token = result[result.find('access_token') + 13: result.find('scope') - 1]
        print(token)
        return (token , 201)


class GithubAuth(Resource):
    def get(self , token):

        r = requests.get('https://api.github.com/user', headers={'Authorization': f'token {token}'})
        dataJson = r.json()
        userName = dataJson['login']
        dbUsers = SQLDataBase()
        print(dbUsers.GetAll())


        if not (dbUsers.Exist(userName , '0' )[0]):
             dbUsers.Insert(userName , '0')
        key = dbUsers.Exist(userName, '0')[1]
        dbData = MongoDataBase(key)

        return (userName ,201)

class Registration(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        result = dbUsers.Exist(username , password)
        if not result[0]:
            dbUsers.Insert(username , password)
            userId = dbUsers.GetOne(username ,password)
            dbData[userId]=MongoDataBase(userId)
            return ('' , 201)
        else:
            return('' , 201) 
        


class Login(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        


class DeleteAndChange(Resource):
    def delete(self, todo_id):
        dbData.RemoveById(todo_id)

        return '', 201

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

class ListAndInsert(Resource):
    def get(self):
        return dbData.GetAllForJsonfy() , 201

    def post(self):
        args = parser.parse_args()
        print(args['text'])
        insetedId = dbData.Insert(args['text'])
        return insetedId, 201




api.add_resource(GithubAuth ,'/githubAuth/<token>')
api.add_resource(ListAndInsert, '/todo')
api.add_resource(DeleteAndChange, '/todo/<todo_id>')
api.add_resource(GithubToken , '/githubToken/<code>')
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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0" , port=5000) 
