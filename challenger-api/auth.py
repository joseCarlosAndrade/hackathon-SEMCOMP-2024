import hashlib
import requests
from urllib.parse import urlencode

# key encryption
import base64
import os

# Step 1: Redirect user to authorize
client_id = "abd1b2ce-cbc2-4b2b-859f-08dce923e8ba"
client_secret = "JUoQJTtDkhmGdkSGLNnFyoJQFbIdIruK"
redirect_uri = "http://localhost:5000/callback"
auth_url = "https://challengermode.com/oauth/authorize"

# generating keys
random_bytes = os.urandom(32)

# Step 2: Base64 URL-safe encoding (without padding)
code_verifier = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')

# Step 3: Replace '+' with '-', and '/' with '_'
code_verifier = code_verifier.replace('+', '-').replace('/', '_')

print("code verifier:" , code_verifier)

sha256_hash = hashlib.sha256(code_verifier.encode('utf-8')).digest()

# Step 2: Encode the hash using Base64 URL-safe encoding
code_challenge = base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')

# Step 3: Output the code_challenge
print("code challenge", code_challenge)

# Parameters for the authorization URL
# params = {
#     "response_type": "code",
#     "client_id": client_id,
#     "redirect_uri": redirect_uri,
#     "scope": "your_required_scopes",
# }

# Construct the full authorization URL
# full_auth_url = f"{auth_url}?{urlencode(params)}"

#  generating url
url = f"https://www.challengermode.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&code_challenge={code_challenge}&code_challenge_method=S256"

# Direct the user to this URL (in a real application, you'd redirect them)
print("Go to the following URL to authorize:")
print(url)


authorization_code = input("insert the access code")

# Exchange the authorization code for an access token
token_url = "https://challengermode.com/oauth/token"
token_payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "code_verifier" : code_verifier,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret" : client_secret
    # "client_secret": "your_client_secret",
}

# Request the access token
token_response = requests.post(token_url, data=token_payload)
if token_response.status_code == 200:
    token_data = token_response.json()
    access_token = token_data["access_token"]
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {token_response.status_code} - {token_response.text}")