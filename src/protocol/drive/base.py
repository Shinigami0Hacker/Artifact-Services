from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from abstracts.protocol import Protocol
from google_auth_oauthlib.flow import InstalledAppFlow
from pathlib import Path
import os

class DriveAuthetication:
    def __init__(self, token_path) -> None:
        self.__token_path = Path(token_path)
        self.SCOPES = 'https://www.googleapis.com/auth/drive'
        self.__default_autheticate_dir = Path("./authetication")

    def __generate_credentials(self):
        self.credential = None
        if self.__token_path.exists:
            creds = Credentials.from_authorized_user_file(self.__token_path)
        if (not self.credential) or (not self.credential.valid):
            if (creds and creds.expired) and (creds.refresh_token):
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open( self.__default_autheticate_dir.joinpath("token.json"), 'w') as token:
                token.write(creds.to_json())

    def __get_drive_service(self):
        service = build('drive', 'v3', credentials=self.__generate_credentials())
        return service
class DriveProtocol(Protocol):
    def __init__(self) -> None:
        self.__authetication = DriveAuthetication()
        pass
