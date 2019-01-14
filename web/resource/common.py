import json

from flask import jsonify 
from flask_restful import Resource


def userExists(db, username):
    if db.find({"username":username}).count() == 0:
        return False
    else:
        return True


def keyExists(db, apiKey):
    if  db.find({ "api_key": apiKey }).count() == 0:
        return False
    else:
        return True


def genJSON(status, message):
    d = {
        "status_code": status,
        "message": message
    } 
    return jsonify(d)
