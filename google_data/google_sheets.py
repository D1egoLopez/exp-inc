import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet(sheet_name):
    # Set up the credentials and authorize the client
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    spreadsheet = client.open(sheet_name)
    return spreadsheet
