from auth import authenticate
from read_cells import *
from write_cells import *
from expenses_extract import *

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
    
    # Process the CSV file
    csv_filename = 'Lista_operacji_20240421_211135.csv'
    category_totals = process_csv(csv_filename)

    # Calculate the total positive amount
    amount_total = sum(total for total in category_totals.values() if total > 0)
    
    # Print category totals and their percentages
    print("Category totals:")
    for category, total in category_totals.items():
        if total < 0:
            continue
        print(f"{category}: {round(total)} #Percentage: {round((total / amount_total) * 100)} %")
        print()
    
    
    
    # Update data in the sheet
    UPDATE_SPREADSHEET_ID = "1vfmsZO32tXyoBTzpWpNrNn_F4Lg5-NTpGRQRlCiF0bg"
    UPDATE_RANGE_NAME = "A1:C50"
    #UPDATE_VALUES = [["A", "B"], ["C", "D"]]
    
    #Prepare data to write to the Google Sheet
    sheet_data = [["Category", "Total", "Percentage"]]
    for category, total in category_totals.items():
        if total > 0:
            percentage = (total / amount_total) * 100
            sheet_data.append([category, round(total), round(percentage)])

    # Update the Google Sheet with the processed data
    #update_sheet(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, sheet_data)
    
    update_sheet(creds, UPDATE_SPREADSHEET_ID, UPDATE_RANGE_NAME, sheet_data)

