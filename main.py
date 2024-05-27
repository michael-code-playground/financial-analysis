from auth import authenticate
from read_cells import *
from write_cells import *

if __name__ == "__main__":
    SAMPLE_SPREADSHEET_ID = "1f14zhwBtHENvrwaFrCkW2GqUxPlDAz-B0L_8MT1jUKc"
    SAMPLE_RANGE_NAME = "Sheet1!A1:B6"
    
    # Authenticate once and pass the credentials to the functions
    creds = authenticate()
    
    # Read data from the sheet
    values = read_sheet(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
    if values:
        for row in values:
            print(f"{row[0]} {row[1]}")
    else:
        print("No data found.")
    
    # Update data in the sheet
    UPDATE_SPREADSHEET_ID = "1vfmsZO32tXyoBTzpWpNrNn_F4Lg5-NTpGRQRlCiF0bg"
    UPDATE_RANGE_NAME = "A1:C2"
    UPDATE_VALUES = [["A", "B"], ["C", "D"]]
    
    update_sheet(creds, UPDATE_SPREADSHEET_ID, UPDATE_RANGE_NAME, UPDATE_VALUES)

