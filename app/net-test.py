import os, subprocess, sys
from datetime import datetime

# Global Variables
HEADER = '"timestamp","server name","server id","idle latency","idle jitter","packet loss","download","upload","download bytes","upload bytes","share url","download server count","download latency","download latency jitter","download latency low","download latency high","upload latency","upload latency jitter","upload latency low","upload latency high","idle latency low","idle latency high"\n'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# File write function
def file_write(input: str):
    """Write string to output file.

    :param input: str - What will be written to the file
    """
    f = open("output.csv", "a")
    f.write(input)
    f.close()

def speedtest(args: list) -> str:
    """Run the speedtest command with the output format of CSV.
    More details of command can be seen with speedtest --help

    :return results: str - Return the results of the speedtest.
    """
    print("Starting speedtest.")
    # Update argument one to Speedtest CLI name.
    args[0] = "speedtest"
    results = subprocess.run(args, capture_output=True, text=True)
    # If license has not been accepted yet. go ahead and accept it.
    if "--accept-license" in results.stderr:
        args.append("--accept-license")
        results = subprocess.run(args, capture_output=True, text=True)
    if not set(["CSV", "csv"]).isdisjoint(set(args)): 
        file_write(f'"{TIMESTAMP}", {results.stdout}')
    print(results.stdout)
    return results

def main(args: list):
    """Main speedtest function"""
    # Checks for output.csv file, creates if not available.
    if not os.path.exists(f"{DIR_PATH}/output.csv"):
        print("CSV file doesnt exist. Creating!")
        file_write(HEADER)
    # Runs speedtest function and sets results to a variable
    speedtest(args)

if __name__ == "__main__":
    main(sys.argv)