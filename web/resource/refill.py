import json

from flask import jsonify, request 
from flask_restful import Resource

from common import keyExists, genJSON


class Refill(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        # Get posted data and extract information
        data = request.get_json()

        # Check if the api key & the number 
        # of tokens exists
        if not "api_key" in data \
            or not "amount" in data:
            return genJSON(
                400, 
                "API Key or number of tokens is missing"
            )

        # Extract the data
        apiKey  = data["api_key"]
        amount = data["amount"]
        
        # Check if the amount is negative
        if int(amount) <= 0:
            return genJSON(
                400,
                "amount should only be greater than 0"
            )

        # Check if API key exists in the database
        if not keyExists(self.db, apiKey):
            return genJSON(400, "Invalid API Key")

        # Update the users token count
        tokens = self.db.find(
            {"api_key":apiKey})[0]["tokens"]
        newAmount = tokens + int(amount)
        self.db.update({
            "api_key": apiKey
        },  {
                "$set": {
                    "tokens": newAmount
                }    
            } 
        )
        
        return genJSON(
            200,
            "Token count has been updated (now: %s)" 
                % newAmount
        )
