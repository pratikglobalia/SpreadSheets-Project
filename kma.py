from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import pygsheets
import pandas as pd

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = 'kma.json'

gc = pygsheets.authorize(service_file='kma.json')
credentials = None
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def create(title):

    try:
        service = build('sheets', 'v4', credentials=credentials)
        drive_service = build('drive', 'v3', credentials=credentials)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                    fields='spreadsheetId') \
            .execute()
        print(f"Spreadsheet ID: {spreadsheet}")
        spreadsheet_id = spreadsheet.get('spreadsheetId')
        permission1 = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'pbh.globaliasoft@gmail.com'
        }
        drive_service.permissions().create(
            fileId=spreadsheet_id, body=permission1).execute()
        return spreadsheet_id

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


create("pandas")

json = []


df = pd.DataFrame.from_dict(json)
sh = gc.open('pandas')
wq = sh[0]
print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: kma.py ~ line 73 ~ wq", wq)
wq.set_dataframe(df, (1, 1))