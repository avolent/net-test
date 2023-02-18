import os, subprocess, sys, logging, gspread
from datetime import datetime

# Configuration
CSV = True # Enable/Disable CSV Output
GOOGLE_SHEETS = True # Enable/Disable Google Sheets
LOG_LEVEL = logging.WARN # NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, CRITICAL=50

# File & Google Sheet Variables
HEADER = '"timestamp","server name","server id","idle latency","idle jitter","packet loss","download speed (bytes)","upload speed(bytes)","download bytes","upload bytes","share url","download server count","download latency","download latency jitter","download latency low","download latency high","upload latency","upload latency jitter","upload latency low","upload latency high","idle latency low","idle latency high"\n'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_FILE = "output.csv"
SHEET_NAME = "Speedtest"

# Time Variables
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
MONTH = datetime.now().strftime("%Y-%m")

# Logging Settings
logging.basicConfig(filename='run.log' ,encoding='utf-8', level=LOG_LEVEL, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
log = logging.getLogger("net-test")
log.addHandler(logging.StreamHandler())


def file_write(file: str, input: str):
    """Function for writing a string to the output csv file.

    :param input: str - The string that will be written to the file.
    """
    f = open(file, "a")
    log.info(f"Writing to {file}")
    f.write(input)
    f.close()

def sheets(results: str):
    """Function for working with google sheets and adding results

    param: results: str - Results from the speedtest which will be added to the google sheets.
    """
    # Authorise with google
    log.info("Authorising with Google")
    try:
        google = gspread.service_account("service_account.json")
    except FileNotFoundError:
        log.error("Secrets file './app/service_account.json' not available. Please follow 'Google Service Account Setup for Sheets' https://github.com/avolent/net-test")
        quit()
    except Exception as e:
        log.error(e)
        quit()
    # Check if speedtest sheet is available, if not create it.
    log.info(f"Opening Sheet '{SHEET_NAME}'")
    try:
        sheet = google.open(SHEET_NAME)
    except gspread.exceptions.SpreadsheetNotFound:
        log.error(f"Spreadsheet '{SHEET_NAME}' not found, please share access using the service account email")
        quit()
    log.info(f"Sheet can be seen here: {sheet.url}")
    # Confirm if current month has an available sheet.
    try:
        worksheet = sheet.worksheet(MONTH)
    except gspread.exceptions.WorksheetNotFound:
        log.error(f"Worksheet for '{MONTH}' doesnt exist, creating!")
        # Create worksheet
        worksheet = sheet.add_worksheet(title=MONTH, rows=9999, cols=22)
        # Add header row & format it
        worksheet.update("A1", [HEADER.replace('"', "").strip().split(",")])
        worksheet.format("1", {
            "backgroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 0.0
            },
            "horizontalAlignment": "CENTER",
            "wrapStrategy": "WRAP",
            "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            },
            "fontSize": 10,
            "bold": True
            }
        })
        worksheet.freeze("1", "0")
    # Append results to next row
    log.info(f"Appending results to '{SHEET_NAME} - {MONTH}'")
    worksheet.append_row(results.replace('"', "").strip().split(","), value_input_option='USER_ENTERED')

def speedtest(args: list) -> str:
    """Function for running the speedtest command.
    More details of command can be seen with speedtest --help

    :param args: list - A list of arguments that will be passed to the speedtest CLI command.

    :return results: str - Return the results of the speedtest.
    """
    log.info("Starting speedtest.")
    # Update argument one to Speedtest CLI name.
    args[0] = "speedtest"
    results = subprocess.run(args, capture_output=True, text=True)
    # If license has not been accepted yet, ask user for acceptance and if not quit the program.
    if results.returncode == 1:
        log.error(results.stderr)
        # Confirm if error is not because of license not being accepted.
        if len(os.listdir("/root/.config/ookla")) == 0:
            if not input("Do you accept the license? [type YES to accept]: ").upper() == 'YES':
                log.error("License not accepted, quiting.")
                quit()
            log.info("License accepted, continuing.")
            args.append("--accept-license")
            results = subprocess.run(args, capture_output=True, text=True)
        else:
            quit()
    log.debug(results)
    return results.stdout

def main(args: list):
    """Main net-test function. All other functions are called from here when run from command line.

    param: args: list - A list of arguments from the command line.
    """
    # Checks for output.csv file, creates if not available.
    log.debug(args)
    if not os.path.exists(f"{DIR_PATH}/{OUTPUT_FILE}"):
        log.error(f"Output file '{OUTPUT_FILE}' doesnt exist. Creating!")
        file_write(OUTPUT_FILE, HEADER)
    # Runs speedtest function and sets results to a variable
    results = speedtest(args)
    if not set(["CSV", "csv"]).isdisjoint(set(args)):
        # Write to local file
        if CSV:
            file_write(OUTPUT_FILE, f'"{TIMESTAMP}",{results}')
        # Google sheets
        if GOOGLE_SHEETS:
            sheets(f'"{TIMESTAMP}",{results}')
    log.info(results)

if __name__ == "__main__":
    main(sys.argv)