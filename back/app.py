from flask import Flask     
from flask_restful import reqparse, abort, Api, Resource ,request
from DBOperations import MongoDataBase , SQLDataBase
from flask_cors import CORS
from flask_login import LoginManager 
import requests


app = Flask(__name__ )
Cors = CORS(app)
CORS(app , CORS_SUPPORTS_CREDENTIALS = True)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://database:27017'
app.config['PROPAGATE_EXCEPTIONS'] = True
parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

client_id = '4ebb67bce288c83e5459'
client_secret ='48efba84350d8e5111647a5d01f0f741456ae316'


class Var:
    def __init__(self):
        self.dbData = MongoDataBase()
        self.conUserName = ''

global myVar

myVar = Var()


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
        myVar.consUserName = userName
        if not myVar.dbData.UserIn(userName):
             myVar.dbData.Insert(' ', userName)

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
    def delete(self, user,todo_id):
        myVar.dbData.RemoveById(todo_id ,user)

        return '', 201

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

class ListAndInsert(Resource):
    def get(self,user):
        if len(myVar.dbData.GetAllForJsonfy(user)) !=0 :
            return myVar.dbData.GetAllForJsonfy(user),201
        else :
            return '',201


    def post(self ,user):
        args = parser.parse_args()
        print(args['text'])
        insetedId = myVar.dbData.Insert(args['text'] , user)
        print(insetedId)
        return str(insetedId), 201

# @app.route('/todo/<user>' ,methods = ['GET' ,'POST'])
# def ListAndInsert(user):
#     if request.method =='POST':
#         args = request.args
#         print(args['text'])
#         insetedId = myVar.dbData.Insert(args['text'], user)
#         print(insetedId)
#         return insetedId ,201
#     else :
#         if len(myVar.dbData.GetAllForJsonfy(user)) !=0 :
#             return myVar.dbData.GetAllForJsonfy(user),201
#         else :
#             return '',201



api.add_resource(GithubAuth ,'/todo/githubAuth/<token>')
api.add_resource(ListAndInsert, '/todo/<user>')
api.add_resource(DeleteAndChange, '/todo/<user>/<todo_id>')
api.add_resource(GithubToken , '/todo/githubToken/<code>')


# @app.route('/data' )
# def SendData():    
#     dataAsDict = db.GetAllForJsonfy()
#     #print(db.GetAllForJsonf  y())
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

    app.run(debug = False, host="0.0.0.0" , port=5000)
