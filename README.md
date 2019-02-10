## Image Processing API
A simple Flask API that uses tensorflow for image classification.

## EC2 URL
ec2-54-209-80-71.compute-1.amazonaws.com:5000

## Dependencies
Docker is needed to run this application.
If you do not have Docker installed visit [here](https://hub.docker.com/search/?type=edition&offering=community)

## How to use?
In order to start the server in the docker container run the following command:
```
docker-compose up
```
(Note: When classifying your first image there will be a delay because of the time required to download the image models.)

## Endpoints
There are 3 main endpoints (register/, classify/, refill/).

- register
    - Parameters
        - username
        - password
    - Returned
        - On Success
            - api_key - Generated API Key for your user
            - message - Success message
            - status_code - HTTP 200 OK
        - On Failure
            - message - Failure message
            - status_code - HTTP 400 BAD REQUEST
- classify
    - Parameters
        - api_key - You're users API Key. If you don't have one use the register endpoint to create one.
        - url - A valid url pointing to an image for classification.
    - Returned
        - JSON object with the image classification.
- refill
    - Parameters
        - api_key - You're users API Key. If you don't have one use the register endpoint to create one.
        - amount - The number of tokens to add to your account. The API is expecting a string value.