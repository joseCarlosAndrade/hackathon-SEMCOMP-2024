#!/usr/bin/env python


from flask import Flask, request, jsonify
import Auth

import sqlite3

class FlaskServer:
    def __init__(self):
        """Initializes the main flask server"
        """
    
        FlaskServer.app = Flask(__name__)

        # adding url rules to manage callbacks for each endpoint
        self.app.add_url_rule('/', view_func=self.__root_callback, methods=["GET"])
        self.app.add_url_rule('/auth', view_func=self.__auth_callback, methods=["GET"])
        self.app.add_url_rule('/callback', view_func=self.__access_code_callback, methods=["GET"])

        # secret access code and auth
        self.__access_code = ""
        self.__auth_handler = Auth.AuthHandler()

    # check server health
    def __root_callback(self):  
        return ":)", 200

    # auth
    def __auth_callback(self):
        print("generating auth url")

        # auth = Auth.AuthHandler()
        url = self.__auth_handler.generate_auth_url()
        if url == "":
            return jsonify({"status" : "error", "url" : ""})

        return jsonify({f"status" : "ok" , "url" : f"{url}"})

    # auth
    def __access_code_callback(self): # redirect callback - for development environment only
        # code param 
        print("getting access token")
        authorization_code = request.args.get('code')

        if authorization_code:
            # Print the authorization code to the console
            print(f"Authorization Code received: {authorization_code}")  # teste also
            
            self.__access_code = authorization_code
            status, token = self.__auth_handler.post_access_code(authorization_code)

            if status != 200:
                print("ERROR on server: status from posting access token not 200, status and message: ", status, f" {token}")
                return f"fail! status: {status}, message: {token}"

            print("[INFO] Success! token granted")

            return f"success! Authorization Code: {authorization_code}\nToken: {token}"
        else:
            return "No authorization code received", 400

    # simualate message streaming
    def __stream_messages(self):
        print("streaming messages")

        # push notifications

        # save on db


    # run!!
    def run(self):
        print("flask running on port 5000")
        self.app.run(host="0.0.0.0", port=5000)

# running for debug 
if __name__ == '__main__':
    flask_server = FlaskServer()
    flask_server.run()