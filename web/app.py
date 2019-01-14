import sys
import os 

from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

sys.path.append(os.path.abspath('.') + '/resource')
from register import Register
from classify import Classify
from refill import Refill


app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://database:27017")
db = client.ImageRecognition
users = db["users"]


# Add resources
api.add_resource(
    Register, 
    "/register", 
    resource_class_kwargs={'db':users})
api.add_resource(
    Classify,
    "/classify", 
    resource_class_kwargs={'db':users})
api.add_resource(
    Refill,
    "/refill", 
    resource_class_kwargs={'db':users})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
