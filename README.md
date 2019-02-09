## Image Processing API
A simple Flask API that uses tensorflow for image classification.

## Endpoints
There are 3 main endpoints.

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
    
- refill