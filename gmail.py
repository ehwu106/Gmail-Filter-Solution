from Google import Create_Service
from googleapiclient.errors import HttpError
import bot
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class Gmail_App:
    def __init__(self):
        self.service = self.create_Google_service()

    def create_Google_service(self):
        SCOPES = ['https://mail.google.com/']
        return Create_Service(SCOPES)

    def audit_log(self,string):
        fd = open("logfile.txt", 'a')
        fd.writelines(string)
        fd.close()
        bot.run_bot(string)                 #If you don't have discord or don't want discord notification simply comment this line out and logs will be written to a txt file called "logfile.txt" in the same directory

    def add_quarantine(self, message_ids):
        try:
            body={
                "addLabelIds": ['SPAM'],
                "ids": message_ids,
                "removeLabelIds": ['INBOX']
            }
            self.service.users().messages().batchModify(userId='me', body=body).execute()
        except HttpError as error:
            self.audit_log("Error", f'{error}')

    def add_to_inbox(self, message_ids):
        try:
            body={
                "addLabelIds": ['INBOX'],
                "ids": message_ids
            }
            self.service.users().messages().batchModify(userId='me', body=body).execute()
        except HttpError as error:
            self.audit_log("Error", f'{error}')
            

