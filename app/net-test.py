import os, subprocess

# Global Variables
HEADER = '"server name","server id","idle latency","idle jitter","packet loss","download","upload","download bytes","upload bytes","share url","download server count","download latency","download latency jitter","download latency low","download latency high","upload latency","upload latency jitter","upload latency low","upload latency high","idle latency low","idle latency high"\n'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# File write function
def file_write(input):
    f = open("output.csv", "a")
    f.write(input)
    f.close()

def speedtest():
    print("Starting speedtest.")
    results = subprocess.run(['speedtest', '-f', 'csv', '-A'], input='YES', capture_output=True, text=True)
    print(results.stdout)
    print("Test complete.")
    return results

def main():
    # Check output file exist, create if not.
    if not os.path.exists(f"{DIR_PATH}/output.csv"):
        print("CSV file doesnt exist. Creating!")
        file_write(HEADER)

    results = speedtest()
    file_write(results.stdout)

if __name__ == "__main__":
    main()