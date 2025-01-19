from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from datetime import datetime

def upload_to_drive():
    # Nastavení přístupu pomocí service account
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Vytvoření služby
    service = build('drive', 'v3', credentials=credentials)
    
    # ID složky na Google Drive (musíš nahradit skutečným ID své složky)
    folder_id = '1AHXQUszEIhsyhT-qB9YraJg3Qf9WZiIJ'
    
    # Název souboru s datumem
    today = datetime.now().strftime('%d-%m-%Y')
    file_name = f'nabidky_{today}.docx'
    
    # Metadata souboru
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    
    # Upload souboru
    media = MediaFileUpload('nabidky.docx', 
                          mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                          resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    print(f'Soubor nahrán na Google Drive, ID: {file.get("id")}')

if __name__ == '__main__':
    upload_to_drive()