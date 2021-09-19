from sqlite3.dbapi2 import connect
from  pymongo import MongoClient
from bson import ObjectId
import os
import sqlite3


class MongoDataBase:
    def __init__(self ):
      
        # # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # # mydb = myclient["mydatabase"]
        # # mycol = mydb["customers"]

        # self.MONGODB_HOST = 'localhost'
        # self.MONGODB_PORT = 27017   
        # # client = pymongo.MongoClient('localhost', MONGO_PORT)
        #MONGO_INITDB_ROOT_USERNAME

        MONGO_INITDB_ROOT_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
        MONGO_INITDB_ROOT_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
        DATABASE_URL = f'mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@database:27017'
        self.id = id
        print(self.id)
        self.mongoCluster = MongoClient(DATABASE_URL)
        #print(self.mongoCluster.list_database_names())

        self.mongoDB = self.mongoCluster["db"]


    def GetAll(self , id ):
        todoItems = []
        for item in self.mongoDB[str(id)].find():
            todoItems.append(item)
        return todoItems

    def GetAllForJsonfy(self ,id ):
        print('id - > ' , id)
        res =[]
        for i in self.GetAll(id) :
            newDic = i.copy()
            newDic['_id'] = str(i['_id'])
            if newDic['text']==' ':
                continue
            res.append(newDic)
        return res

    def GetById(self , id:str ,userId ):
        self.mongoDB[str(userId)].find(id)

    def RemoveById(self , id:str , userId ):
        self.mongoDB[str(userId)].remove( ObjectId(id))

    def Insert(self , todoText:str , userId ):
        insertedId = self.mongoDB[str(userId)].insert_one({"text":todoText}).inserted_id
        
        return insertedId


    def UserIn(self , userName):
        return str(userName) in self.mongoDB.list_collection_names()



class SQLDataBase :
    def __init__(self) :
        self.connection = sqlite3.connect('./users.db') 
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , username TEXT , password text );''')
        self.connection.commit()
        


    def Insert(self , username:str , password:str ):
        self.cursor.execute('INSERT into users (username , password) values (? , ? );' , (username , password))
        self.connection.commit()
        
    
    def GetAll(self):
        self.cursor.execute("SELECT * FROM users;")
        return self.cursor.fetchall()
    
    def GetOne(self , username:str , password :str):
        self.cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")
        return self.cursor.fetchone()


    def Exist(self , username:str , password :str):
        self.cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")
        result = self.cursor.fetchone()
        #print(result)
        if result==None:
            return (False , )
        else :
            return (True ,result[0])

if __name__ == '__main__':
    mog = MongoDataBase()
    idd = input()
    print(mog.GetAllForJsonfy(idd))
    print(mog.mongoDB.list_collection_names())

