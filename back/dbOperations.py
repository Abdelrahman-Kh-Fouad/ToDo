from  pymongo import MongoClient
from bson import ObjectId
import os

class DataBase:
    def __init__(self):
      
        # # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # # mydb = myclient["mydatabase"]
        # # mycol = mydb["customers"]

        # self.MONGODB_HOST = 'localhost'
        # self.MONGODB_PORT = 27017   
        # # client = pymongo.MongoClient('localhost', MONGO_PORT)

        self.mongoCluster = MongoClient("mongodb://database:27017/")
        print(self.mongoCluster.list_database_names())

        self.mongoDB = self.mongoCluster["testingdb"]
        self.mongoCollection = self.mongoDB["todo"]



    def GetAll(self):
        todoItems = []
        for item in self.mongoCollection.find():            
            todoItems.append(item)
        return todoItems

    def GetAllForJsonfy(self):
        res =[]
        for i in self.GetAll() :
            newDic = i.copy()
            newDic['_id'] = str(i['_id'])
            res.append(newDic)
        return res


    def GetById(self , id:str ):
        self.mongoCollection.find(id)

    def RemoveById(self , id:str ):
        self.mongoCollection.remove( ObjectId(id))

    def Insert(self , todoText:str):
        insertedId = self.mongoCollection.insert_one({"text":todoText}).inserted_id
        return insertedId


