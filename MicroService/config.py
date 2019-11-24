"""This module is to configure app to connect with database."""
import os
from pymongo import MongoClient
serverIp=os.environ['SERVERIP']

DATABASE = MongoClient()['restfulapi'] # DB_NAME
DEBUG = True
client = MongoClient(serverIp, 27017)
print("SERVER RUNNING AT:"+ serverIp)