from  pymongo import MongoClient
from back.app import dbUsers

class User (dbUsers.Model):
    id = dbUsers.Column(dbUsers.Integer, primary_key=True) 
    userName = dbUsers.Column(dbUsers.String(100), unique=True)
    password = dbUsers.Column(dbUsers.String(100))
    name = dbUsers.Column(dbUsers.String(1000))

