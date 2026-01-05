import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1mrVluZuP-iJwieoRcJylSLV8nU0NkSdehJRJ2LH9fHo"
SAMPLE_RANGE_NAME = "MaidenVeil!A:E"
SAMPLE_WRITE_RANGE_NAME = "MaidenVeil!A3:B225"
HEADERS = [['STOCK', '', '', 'GOALS'], ['Quantity', 'Name', '', 'Quantity', 'Name']]
creds = None





def authentication_sheets():
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
    
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

def read(range = "MaidenVeil!A:E"):
  
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return
    
    print(f"{values}")

    i = 0
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
        rowstr = ""
        for pos in row:
            rowstr += pos + " "
        print(rowstr)
  except HttpError as err:
    print(err)


def update_values(_values, spreadsheet_id = SAMPLE_SPREADSHEET_ID, range_name = SAMPLE_WRITE_RANGE_NAME, value_input_option = 'USER_ENTERED'):
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
    try:
        service = build('sheets', 'v4', credentials=creds)
        values = _values
        body = {'values': values}
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error