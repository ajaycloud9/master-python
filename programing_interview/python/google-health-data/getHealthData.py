import os
import pickle
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define the SCOPES you need for the app (for Google Fit API)
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read',  # Read activity data
          'https://www.googleapis.com/auth/fitness.body.read']  # Read body data like weight

# Path to your OAuth 2.0 credentials JSON file (downloaded from the Google Cloud Console)
CLIENT_SECRET_FILE = 'client-secret.json'  # Replace with the actual path to your credentials file

# Token file to store the access and refresh tokens
TOKEN_FILE = 'token.pickle'

def authenticate():
    """Authenticate using OAuth 2.0 and return an API client."""
    creds = None

    # If the token.pickle file exists, load the credentials from it
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # If the credentials have expired, refresh them.
            creds.refresh(Request())
        else:
            # Otherwise, let the user authenticate using the client secret
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=8888)  # Open a local server for the user to authenticate

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Fit API client using the credentials
    service = build('fitness', 'v1', credentials=creds)
    return service

def get_weight_data(service):
    """Fetch weight data from Google Fit."""
    # Prepare the request body to fetch the weight data (example start and end times)
    data = {
        "aggregateBy": [
            {
                "dataTypeName": "com.google.weight"
            }
        ],
        "bucketByTime": {
            "durationMillis": 86400000  # 24 hours in milliseconds (daily buckets)
        },
        "startTimeMillis": 1732294836000,  # Example start time (Nov 23, 2024)
        "endTimeMillis": 1732514436000    # Example end time (Nov 30, 2024)
    }

    # Make the request to the Google Fit API to get aggregated data
    request = service.users().dataset().aggregate(userId='me', body=data)
    response = request.execute()

    # Print the response or process the data as needed
    print(json.dumps(response, indent=2))

if __name__ == '__main__':
    # Authenticate and build the service
    service = authenticate()

    # Fetch and print weight data (or other data you need)
    get_weight_data(service)
