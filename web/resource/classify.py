import json
import subprocess

from flask import jsonify, request 
from flask_restful import Resource
import requests

from common import keyExists, genJSON

class Classify(Resource):
    """ Controller class for classifing the given images """
    
    def __init__(self, db):
        self.db = db
    
    def post(self):
        """ Classify the given image. """

        # Get posted data and extract information
        data = request.get_json()

        # Check if the api key & url exist
        if not "api_key" in data \
            or not "url" in data:
            return genJSON(
                400, 
                "API Key or image url is missing"
            )

        # Extract the data
        apiKey  = data["api_key"]
        url = data["url"]

        # Check if API key exists in the database
        if not keyExists(self.db, apiKey):
            return genJSON(400, "Invalid API Key")
        
        # Check if the user has enough tokens
        tokens = self.db.find({"api_key":apiKey})[0]["tokens"]
        if tokens <= 0:
            return genJSON(
                400,
                "Inadequate number of tokens"
            )

        classification = {}

        # Get the image & save it
        response = requests.get(url)
        with open("temp.jpg", "wb") as f:
            # Write the image to the disk
            f.write(response.content)

            # Create a sub process
            cmd = "python3 classify_image.py --model_dir=. --image_file=./temp.jpg"
            proc = subprocess.Popen(cmd.split())
            proc.communicate()[0]
            proc.wait()

            # Get the classification 
            with open("text.txt") as g:
                classification = json.load(g) 

        # Subtract a token from the user
        self.db.update({
            "api_key":apiKey    
        },  {
                "$set": {
                    "tokens": tokens - 1        
                }    
            }
        )

        # Return classification
        return classification
