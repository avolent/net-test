import os, subprocess

# Global Variables
HEADER = '"server name","server id","idle latency","idle jitter","packet loss","download","upload","download bytes","upload bytes","share url","download server count","download latency","download latency jitter","download latency low","download latency high","upload latency","upload latency jitter","upload latency low","upload latency high","idle latency low","idle latency high"\n'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


# File write function
def file_write(input: str):
    """Write string to output file.

    :param input: str - What will be written to the file
    """
    f = open("output.csv", "a")
    f.write(input)
    f.close()

def speedtest() -> str:
    """Run the speedtest command with the output format of CSV.
    More details of command can be seen with speedtest --help

    :return results: str - Return the results of the speedtest.
    """
    print("Starting speedtest.")
    results = subprocess.run(['speedtest', '-f', 'csv', '-A'], capture_output=True, text=True)
    print(results.stdout)
    print("Test complete.")
    return results

def main():
    """Main speedtest function
    Will run all the other functions from here
    Checks if output file exists, if not will create one.
    Writes results to the output file on completion of speedtest.
    """
    if not os.path.exists(f"{DIR_PATH}/output.csv"):
        print("CSV file doesnt exist. Creating!")
        file_write(HEADER)
    results = speedtest()
    file_write(results.stdout)

if __name__ == "__main__":
    main()