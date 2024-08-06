from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'credentials.json' 

def get_credentials():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        return credentials
    except Exception as e:
        print(f"Error loading credentials: {e}")
        raise

def upload_file_to_drive(file_path, file_name):
    try:
        credentials = get_credentials()
        service = build('drive', 'v3', credentials=credentials)

        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_path, mimetype='image/jpeg')

        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
        request_body = {
            'role': 'reader',
            'type': 'anyone',
        }
        service.permissions().create(fileId=file['id'], body=request_body).execute()

        return file.get('id')
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise

def get_public_url(file_id):
    return f"https://drive.google.com/uc?id={file_id}"
