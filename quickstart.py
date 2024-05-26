import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1f14zhwBtHENvrwaFrCkW2GqUxPlDAz-B0L_8MT1jUKc"
SAMPLE_RANGE_NAME = "Sheet1!A1:B6"



"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists("token.json"):
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_889713889304-vaheleab642p6ebgqp10al1ec8hldlbm.apps.googleusercontent.com.json", SCOPES
    )
    creds = flow.run_local_server(port=0)
  # Save the credentials for the next run
  with open("token.json", "w") as token:
    token.write(creds.to_json())

try:
  service = build("sheets", "v4", credentials=creds)

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = (
      sheet.values()
      .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
      .execute()
  )
  values = result.get("values", [])

  if not values:
    print("No data found.")
    
  
  for row in values:
    # Print columns A and B, which correspond to indices 0 and 5.
    print(f"{row[0]} {row[1]}")
except HttpError as err:
  print(err)

try:
    service = build("sheets", "v4", credentials=creds)
    values = [
        [
          # Cell values ...
      ],
      # Additional rows ...

    ]
    body = {"values": [["A", "B"], ["C", "D"]]}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId="1vfmsZO32tXyoBTzpWpNrNn_F4Lg5-NTpGRQRlCiF0bg",
            range="A1:C2",
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )
    print(f"{result.get('updatedCells')} cells updated.")
    
except HttpError as error:
    print(f"An error occurred: {error}")
    





