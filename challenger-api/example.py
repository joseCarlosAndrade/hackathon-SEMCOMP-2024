import requests
import json

# Define the GraphQL endpoint (replace with your actual endpoint)
url = "https://your-graphql-server.com/graphql"

# Define the query you want to send (replace with your actual query)
query = """
{
  users {
    id
    e
    emailnam
  }
}
"""

# Headers for the request (optional, but often required for auth or content type)
headers = {
    "Content-Type": "application/json"
}

# Payload for the POST request (GraphQL uses POST)
payload = {
    "query": query
}

# Send the POST request to the GraphQL server
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check for a successful request
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(json.dumps(data, indent=2))  # Pretty-print the result
else:
    print(f"Error: {response.status_code}, {response.text}")