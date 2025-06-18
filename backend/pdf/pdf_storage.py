import os
import requests
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Google Drive API Credentials
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def authenticate_google_drive():
    """Authenticate with Google Drive API."""
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return build("drive", "v3", credentials=creds)

def upload_pdf(file_path, filename):
    """Upload PDF to Google Drive."""
    service = authenticate_google_drive()
    file_metadata = {"name": filename, "mimeType": "application/pdf"}
    
    with open(file_path, "rb") as pdf_file:
        media = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers={"Authorization": f"Bearer {service._http.credentials.token}"},
            files={"file": pdf_file}
        )
    
    print(f"Uploaded {filename} to Google Drive!")

