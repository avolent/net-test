import pygsheets
from datetime import datetime

SHEET_NAME = "Speedtest"
MONTH = datetime.now().strftime("%Y-%m")

def main(results: str, header: str):
    # Authorise with google sheets
    google = pygsheets.authorize()
    # Check if speedtest sheet is available, if not create it.
    try:
        sheet = google.open(SHEET_NAME)
    except pygsheets.exceptions.SpreadsheetNotFound:
        print("Spreadsheet not found, creating a one!")
        sheet = google.create(SHEET_NAME)
    # Confirm if sheet1 is the current month.
    try:
        worksheet = sheet.worksheet_by_title(MONTH)
    except pygsheets.exceptions.WorksheetNotFound:
        print(f"Worksheet for {MONTH} doesnt exist, creating!")
        # Create worksheet
        worksheet = sheet.add_worksheet(MONTH)
        # Add header row
        worksheet.update_row(1, header.replace('"', "").strip().split(","))
    # Append results to next row
    worksheet.append_table(results.replace('"', "").strip().split(","), "A1")
      
if __name__ == "__main__":
    main(results, header)