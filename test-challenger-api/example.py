import requests
from queries import *

# The API endpoint you want to request
url = "https://publicapi.challengermode.com/graphql"

# Your access token obtained from the OAuth process
access_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IldFU1RaRlk5V09CR0RNREJET0U0MjRQRzBNQ0xaSzhHVk40N19LUDIiLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3MiOiJodHRwczovL2NoYWxsZW5nZXJtb2RlLmNvbS8iLCJleHAiOjE3MzAyNDkyNTYsImlhdCI6MTcyOTM4NTI1NiwianRpIjoiNGUwNThmYWEtNmM0YS00ZTAzLTljYmUtYWZmMzYyNzY4NzgwIiwic3ViIjoiZWQwOWM5ZjktNjUzNC00NjE1LTg2ODItOTMzOGFlYzE4ZmUxIiwib2lfcHJzdCI6ImFiZDFiMmNlLWNiYzItNGIyYi04NTlmLTA4ZGNlOTIzZThiYSIsIm9pX2F1X2lkIjoiZjZkYWNlNzEtYzA0NS00YTQ4LWI3YjYtYzllYzg4YmNhYTAxIiwiY206YXBwLWlkIjoiYWJkMWIyY2UtY2JjMi00YjJiLTg1OWYtMDhkY2U5MjNlOGJhIiwiYXVkIjoiaHR0cHM6Ly9wdWJsaWNhcGkuY2hhbGxlbmdlcm1vZGUuY29tIiwiY206dG9rZW4tdHlwZSI6IjkiLCJjbGllbnRfaWQiOiJhYmQxYjJjZS1jYmMyLTRiMmItODU5Zi0wOGRjZTkyM2U4YmEiLCJvaV90a25faWQiOiI5OTVjODZhNS00OGI3LTRiNDQtYTFhNS05ZTFmYjk0M2ZlOTYifQ.s0qaRYmqlCN3B7l2XYiCrj4weB_BYcBIRKFgXyGTFVeoAAbiz2tb4TTMJTz4fFPLzzun-_g-bU5h23aXbsX1VgwEZfgZMNN7g20u6_kYq3RfncNlch9k_azpkGKbqc3wRHXiAWAlyML-IO9ER9aPC1-2Aw_7GeXrfavgirTHI3q4Asqs2yQ9mtv-9d5aXJFifa3cssqErONV_BxEIWbtWBPkqI4tCAZ-hP0yVHwILAmU48Sk4O3ozmy5o53SnL3Ye1-SDWBNJaGs7CNiSFLeKmGyRznzry0d-uenVx4P2TLWwM5cZf411WaD5NHfoMBSrlpUcERdd4mtO_mAzwaKoxfpwfLtKTXTwEHz8RtxcWA8_8sQH-C_WO2Jsv-vvUc4hHJR0gCMSBZYppFo1Uz2wdugQ0YDfN7rvDuKLQHgi1_JfOolre4m6FxJyNekf2x3NqaQ12CiHoJr_O5eHlDTGKYNy3nMlwBpqsB7M3kI15iXoN7lXKPkTNiEI27PG5AxWiqROUmPSBxvCaLd511z7SKQvPEmQMJ_Cfqo2T0EJUARhGdnKT_RKK7ChpuPm9tbaR1_tVc_aOiUMEMxTaaKfdJCAJWPHwsUNjKs9UiZ4oLMq5NGDUW_pIa8Uprq2nZuUuau93A9O3mpttXM9tuAWpPJQyKKUAH1fBMsK9qzZnY"

# Select the query you want to send to the API
query = queryAllTournamentsInfo

payload = {
    "query" : query
}
# Set the authorization headers with the Bearer token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Send a GET request to the API endpoint
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("status 200")
    # Process the response data
    data = response.json()
    print("Response data:", data)
else:
    # Print an error if the request failed
    print(f"Error {response.status_code}: {response.text}")
