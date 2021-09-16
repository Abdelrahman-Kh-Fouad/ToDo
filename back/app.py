from urllib.parse import urlencode

from flask import Flask ,redirect
from flask_restful import reqparse, abort, Api, Resource ,request
from DBOperations import MongoDataBase , SQLDataBase
from flask_cors import CORS
from flask_login import LoginManager 
import requests
from nacl.signing import VerifyKey
import nacl
import json
from uuid import uuid4
from urllib.parse import urlencode, quote, unquote
import base64

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
k = nacl.signing.SigningKey.generate()  # Ususally the key is generated using a seed
kstr = k.encode(encoder=nacl.encoding.Base64Encoder).decode()
PRIV_KEY = nacl.signing.SigningKey(kstr, encoder=nacl.encoding.Base64Encoder)





class CallBack(Resource):

    def get(self):
        session = request.environ.get("beaker.session")
        data = request.args["signedAttempt"]
        state = request.get_data("state")
        if not data:
            return 400,

        data = json.loads(data)
        username = data["doubleName"]

        res = requests.get(f"https://login.threefold.me/api/users/{username}", {"Content-Type": "application/json"})
        pub_key = res.json()["publicKey"]
        user_pub_key = nacl.signing.VerifyKey(res.json()["publicKey"], encoder=nacl.encoding.Base64Encoder)

        signedData = data["signedAttempt"]
        verifiedData = user_pub_key.verify(base64.b64decode(signedData)).decode()
        data = json.loads(verifiedData)

        if "doubleName" not in data or "signedState" not in data or data["doubleName"] != username:
            return (400, "Error")


        return redirect(f'/todo/{username}') ,201


class ThreeUrl(Resource):
    def get(self):
        public_key = PRIV_KEY.verify_key
        public_key = public_key.to_curve25519_public_key().encode(encoder=nacl.encoding.Base64Encoder).decode()
        HOST ="https://login.threefold.me"
        session = request.environ.get("beaker.session", {})
        state = str(uuid4()).replace("-", "")
        session["state"] = state

        params = {
            "state": state,
            "appid": request.host+'/todo',
            "scope": json.dumps({"user": True, "email": True}),
            "redirecturl": '/call_back',
            "publickey": public_key.encode(),
        }
        params = urlencode(params)
        return f"{HOST}?{params}", 201



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



api.add_resource(ListAndInsert, '/todo/<user>')
api.add_resource(DeleteAndChange, '/todo/<user>/<todo_id>')
api.add_resource(GithubToken , '/todo/githubToken/<code>')
api.add_resource(GithubAuth ,'/todo/githubAuth/<token>')
api.add_resource(ThreeUrl ,'/todo/threeUrl')
api.add_resource(CallBack , '/todo/call_back')

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
