import requests

# The API endpoint you want to request
url = "https://publicapi.challengermode.com/graphql"

# Your access token obtained from the OAuth process
access_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IldFU1RaRlk5V09CR0RNREJET0U0MjRQRzBNQ0xaSzhHVk40N19LUDIiLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3MiOiJodHRwczovL2NoYWxsZW5nZXJtb2RlLmNvbS8iLCJleHAiOjE3MzAyNDY0MDMsImlhdCI6MTcyOTM4MjQwMywianRpIjoiMmRmYTVjMjMtNGQ3YS00MGFkLTkzNDktZjJhNTJmNTlhNzk2Iiwic3ViIjoiNzE5MmNmZTAtNWMwMy00MjcwLTk2YzEtMGFiY2I0NDAxMTA3Iiwib2lfcHJzdCI6ImFiZDFiMmNlLWNiYzItNGIyYi04NTlmLTA4ZGNlOTIzZThiYSIsIm9pX2F1X2lkIjoiYTQ3MTA2YmMtMGFhNy00NDgzLWEwOTAtZTY2NDgyNzYwNzE2IiwiY206YXBwLWlkIjoiYWJkMWIyY2UtY2JjMi00YjJiLTg1OWYtMDhkY2U5MjNlOGJhIiwiYXVkIjoiaHR0cHM6Ly9wdWJsaWNhcGkuY2hhbGxlbmdlcm1vZGUuY29tIiwiY206dG9rZW4tdHlwZSI6IjkiLCJjbGllbnRfaWQiOiJhYmQxYjJjZS1jYmMyLTRiMmItODU5Zi0wOGRjZTkyM2U4YmEiLCJvaV90a25faWQiOiI0YzI4MGE0Yi05OTFlLTQzYWUtYjUxYS00NDZkMWU4OGRkOTAifQ.tZIO-71XLH-cpaYFTuB1yfyp6eR3OEUj2MtFWReaO-FtXwxvRHTDm1LsTAqlb1_wPtBovh9_t9QikwKhp3rzRTVqLALeyf0ebS2E3BRWOun5O8vp8iTNpJGYe_3YRPVx4ljKESKUqjy0_uy5iD0AKQE5u7EnapF4jf35carqde7F3oggNDBIO0PmMxzTqnVOuA4EQOfAZ4gjmt4WFWZKsTzmW17DNuzb4o6BlzSQ6lnDGOcdgmEXnmyAv3wtpzLPCnmNYPCdmjYu4txXJcZAppfwjrQXKKUDeK51V7dK1KveB6PuXGLGc866jgr0HtXi8iS3plqrfQZi5Ip8TDgpr65ZEHK9TxGhtHk55yVMpAvHyB9REPLH0IQrfZ4gazNqc5tm4JtPePYoCZc6pNPiRPLIdGVgFZnW_5RIlp3vGB5bRypEkg2drNGbRSopNuD0-6SdDueOUR0s59O2jmifezdYbmEmC5z-8LRXSqNi1p_JI6NJrPC_RS0VXSMLeOeTWqjYmm84lwRQCQCiBe44aBiurZ7BDiEFe0LEEFO0eAIJudIUvl55fM-p8eetwltlp0HeVhCj9cM9rGF2V5E5F4X5Zh3IzmfZOxsaDMQ7D_QxhzYMnzxgFisJtRlEnUxbXHyyw3dbTZ3fNlwYKDAthLRIR7j3b0PYmqIhfVex5Hc"

query = """
{
  me {
    user {
        username
    }
  }
}
"""

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
