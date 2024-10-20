import hashlib
import requests
from urllib.parse import urlencode

# key encryption
from dotenv import load_dotenv
import base64
import os

# typing
from typing import Tuple

class AuthHandler:
    """### Auth handler for oauth (actions on behalf of user)
    """
    __CLIENT_ID = ""
    __CLIENT_SECRET = ""
    __REDIRECT_URI = ""
    __AUTH_URL = ""
    __REFRESH_KEY = ""
    __OWNER_USERNAME = ""

    

    def __init__(self):
        load_dotenv()

        # populating env variables
        AuthHandler.__CLIENT_ID = os.getenv('CLIENT_ID')
        AuthHandler.__CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        AuthHandler.__REDIRECT_URI = os.getenv('REDIRECT_URI')
        AuthHandler.__AUTH_URL = os.getenv('AUTH_URL')
        AuthHandler.__REFRESH_KEY = os.getenv('REFRESH_KEY')
        AuthHandler.__OWNER_USERNAME = os.getenv('OWNER_USERNAME')
        
        # keys used for later token requests
        self.__code_verifier = ""
        self.__code_challenge = ""
    

    def __generate_codes(self): 
        random_bytes = os.urandom(32)
        code_verifier = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')
        self.code_verifier = code_verifier.replace('+', '-').replace('/', '_')

        sha256_hash = hashlib.sha256(code_verifier.encode('utf-8')).digest()
        self.code_challenge = base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')

    def generate_auth_url (self) -> str:
        """generates the auth url based on the populated env

        Returns:
            str: "" (empty) if variables were not correctly set; "url" if else
        """
        self.__generate_codes()

        if AuthHandler.__CLIENT_ID == "" or AuthHandler.__REDIRECT_URI == "" or self.code_challenge == "":
            print("ERROR: auth variables are not properly set")
            return ""
        
        url = f"https://www.challengermode.com/oauth/authorize?client_id={AuthHandler.__CLIENT_ID}&redirect_uri={AuthHandler.__REDIRECT_URI}&response_type=code&code_challenge={self.code_challenge}&code_challenge_method=S256"

        return url

    def post_access_code(self, access_code : str) -> Tuple[int, str]:
        """post the access code granted to challengermode to retreive the access token for later oauth requests

        Args:
            access_code (str): granted access code

        Returns:
            tuple[int, str]: response status, token (if `status` == 200). if `status` = 0, the request didnt complete due to an error
        """

        token_url = "https://challengermode.com/oauth/token"
        token_payload = {
            "grant_type": "authorization_code",
            "code": access_code,
            "code_verifier" : self.code_verifier,
            "redirect_uri": AuthHandler.__REDIRECT_URI,
            "client_id": AuthHandler.__CLIENT_ID,
            "client_secret" : AuthHandler.__CLIENT_SECRET

        }

        try:
            token_response = requests.post(token_url, data=token_payload)
            if token_response.status_code != 200:
                print(f"ERROR: {token_response.status_code} - {token_response.text}")
                return (token_response.status_code, "")
            
            # successfull request
            token_data = token_response.json()
            access_token = token_data["access_token"]

            return (200, access_token)
        
        except Exception as err:
            print("ERROR: could not post access code to get token, ", err)
            return (0, err)