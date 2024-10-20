#!/usr/bin/env python


from flask import Flask, request

app = Flask(__name__)

# The callback route where the user will be redirected after authorization
@app.route('/callback', methods=['GET'])
def callback():
    # Get the 'code' parameter from the query string
    authorization_code = request.args.get('code')

    if authorization_code:
        # Print the authorization code to the console
        print(f"Authorization Code received: {authorization_code}")
        return f"Authorization Code: {authorization_code}"
    else:
        return "No authorization code received", 400

# Run the app on localhost
if __name__ == '__main__':
    app.run(host='localhost', port=5000)