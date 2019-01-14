import secrets

from flask import jsonify, request 
from flask_restful import Resource
import bcrypt

from common import userExists, genJSON

class Register(Resource):
    """ Controller class for registering new users  """
    
    def __init__(self, db):
        self.db = db
    
    def post(self):
        """ 
            Create new users by validating given 
            credentials and returning API keys.
        """

        # Get posted data and extract information
        data = request.get_json()

        # Check if username and password keywords exist
        if not "username" in data \
            or not "password" in data:
            return genJSON(
                400,
                "username or password is missing"
            )

        # Extract the username & password
        username = data["username"]
        password = data["password"]

        # Check if user exists in the database
        if userExists(self.db, username):
            return genJSON(
                400,
                "username already exists please try again"
            )
        
        # Hash password and create the API key
        hashed = bcrypt.hashpw(
            password.encode("utf-8"), 
            bcrypt.gensalt()
        )
        apiKey = secrets.token_urlsafe(24)

        # Insert info in database
        self.db.insert({
            "username": username,
            "password": hashed,
            "api_key": apiKey,
            "tokens": 5
        })

        # Return API Key with message
        return jsonify({
            "status_code": 200,
            "api_key": apiKey,
            "message": "You have successfully registered"
        })
