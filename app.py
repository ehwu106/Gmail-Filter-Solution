from gmail import Gmail_App
from googleapiclient.errors import HttpError
import re
import fnmatch
from datetime import datetime,timedelta
import pytz
from pytz import timezone

def handler(app):
    try:
        black_lists = open('blacklist.txt', 'r')
        white_lists = open('whitelist.txt', 'r')
        white_address = white_lists.readlines()
        blocked_address = black_lists.readlines()
        now = datetime.now(pytz.timezone('US/Pacific'))
        past_24_hours = now - timedelta(hours=24)
        emails = app.service.users().messages().list(userId='me', q='(in:spam OR in:all) after:{}'.format(past_24_hours.strftime('%Y/%m/%d'))).execute()
        blacklist_ids = []
        whitelist_ids = []
        logging=[]
        for messages in emails['messages']:
            m = app.service.users().messages().get(userId='me', id=messages.get('id'), format='metadata').execute()
            headers = (m.get("payload")).get("headers")
            subject = next((header.get("value") for header in headers if header["name"] == "Subject"), None)
            sender = next((header.get("value") for header in headers if header["name"] == "From"), None)
            sender_email = re.search('<(.*)>', sender)
            blocked = [x for x in blocked_address if fnmatch.fnmatch(sender_email.group(1), x.strip())]
            allowed = [y for y in white_address if fnmatch.fnmatch(sender_email.group(1), y.strip())]
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            if allowed and "INBOX" not in m.get('labelIds'):
                whitelist_ids.append(messages.get('id'))
                logging.append(f"{date.strftime(date_format)} | Released To Inbox"+" | "+f'{sender} | {subject}\n')
            elif blocked and "INBOX" in m.get('labelIds'):
                blacklist_ids.append(messages.get('id'))
                logging.append(f"{date.strftime(date_format)} | Quarantined"+" | "+f'{sender} | {subject}\n')
        if blacklist_ids:
            app.add_quarantine(blacklist_ids)
            app.audit_log(''.join(logging))
        elif whitelist_ids:
            app.add_to_inbox(whitelist_ids)
            app.audit_log(''.join(logging))
            
    except HttpError as error:
        app.audit_log("Error", f'{error}')

if __name__ == "__main__":
    app = Gmail_App()
    handler(app)