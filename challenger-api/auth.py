import requests
import challenger

# API endpoint for server authentication
url = "https://auth.challengermode.com/oauth/token"

# Replace these with your actual client credentials
payload = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "grant_type": "client_credentials"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Send the POST request to get an access token
response = requests.post(url, data=payload, headers=headers)

# Check for a successful request
if response.status_code == 200:
    # Get the token from the response
    data = response.json()
    access_token = data["access_token"]
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code}, {response.text}")
