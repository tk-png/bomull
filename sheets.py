import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def get_colors():
    scope = ["https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope)
    client = gspread.authorize(credentials)
    sheet = client.open("Jotunfarger").sheet1.get_all_records()
    df = pd.DataFrame(sheet)
    return df
