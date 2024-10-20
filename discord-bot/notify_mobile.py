
import requests
import json
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Path to the downloaded service account JSON file
SERVICE_ACCOUNT_FILE = 'acadarena-semcomp-3ca9dff0ae46.json'

# Firebase Cloud Messaging v1 endpoint
url = 'https://fcm.googleapis.com/v1/projects/464761177582/messages:send'

# Device token to which you want to send the notification
device_token = 'fRmv_9B_T4Wh_v0ffj0Yyv:APA91bHyFAlATOEvA-pW-wJPs5mcs2Sh7yTaq-5OmMVbeImRbumpA9XEq9oZDHdOwrflhijSc3UPK4sFZDQVNvnbZjhhjOJmk32wcj3uvtlSNpQvDMOkBZ9CKQb6HzpTVJ_oERrlh8Gq'

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Obtain an access token from the credentials
def get_access_token(credentials):
    request = Request()
    credentials.refresh(request)
    return credentials.token

# Get the access token
access_token = get_access_token(credentials)

# Create the headers with the OAuth 2.0 token
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json; UTF-8',
}

# Define the notification payload
payload = {
    "message": {
        "token": device_token,
        "notification": {
            "title": "",
            "body": "",
        },
        "data": {
            "confirmation": "false"
        }
    }
}

def send_notification(title, message):
    payload["message"]["notification"]["title"] = title
    payload["message"]["notification"]["body"] = message
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status Code:", response.status_code)
    print("Response:", response.text)

