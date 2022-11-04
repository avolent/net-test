<h1 align="center">Net-Test</h1>

> A Python wrapper for the Speedtest CLI from [Speedtest.net](https://www.speedtest.net/apps/cli) with my own twist.

## Goal

The goal is to add more features that I can use to track my internet speed over a period of time at certain intervals.

## Design

Tool is built with the https://3musketeers.io framework in mind.



## Requirements
- Unix-like System or Windows Subsystem Linux.
- Make - If not already installed, `sudo apt update && sudo apt install make` or using your OS own package manager commands.
- Docker & Docker Compose - Linux instructions [here](https://docs.docker.com/engine/install/) or install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Enable WSL Support in setup)
- Google OAuth Key for Google Sheet/Drive API - Follow instructions [here](#google-0auth-setup-for-sheets) for Auth0.

## Usage
1. First `git clone https://github.com/avolent/net-test.git && cd net-test`
2. Run `make run_test` within the root of the repository. **You will need to run the tool once and authorise your google account before being able to use google sheets.** 

(If you're using Docker Desktop then make sure to have it open and you can put it to a side or command will not run, while the command is executing you should see a container called 'net-test' popup)

3. Once completed, results will be outputted into the file "./app/output.csv". It will give your google sheet url, every other run will append the results to the same sheet.
4. Use [crontab](https://crontab.guru) to schedule executions automatically.

### More Commands

```bash
make run # Run the docker without rebuilding the image.
make build # Build the docker image
make help # Show the help output for speedtest cli.
make servers # List the current preferred servers, based on your location and latency.
make bash # Enter the docker containers bash terminal. (Useful for debugging and developing new features on the fly)
make clean # Remove and delete all docker images, configuration and network adapters
```
### Google 0Auth Setup for Sheets
1. Create a project for the speedtest [here](https://console.cloud.google.com/projectcreate)
1. Enable the following two APIs in your Google Console:
[Google Drive API](https://console.cloud.google.com/apis/api/drive.googleapis.com/) &
[Google Sheets API](https://console.cloud.google.com/apis/api/sheets.googleapis.com/)
1. Configure your OAuth Consent screen first [here](https://console.cloud.google.com/apis/credentials/consent)
    ```
    *Minimum Configuration*
    User Type: External
    > Create
    App Name: Speedtest
    User Support Email: $Your_email
    Developer contact information: $Your_email
    > Save and Continue
    > Save and Continue
    Test Users: $Your_email
    > Save and Continue
    ```
1. Create an OAuth Credential [here](https://console.cloud.google.com/apis/credentials/oauthclient).
    ```
    Application Type: Desktop
    Name: Speedtest
    ```
1. Download the JSON file, place into your the "/app" directory in the clone repository. Rename it to `client_secret.json`.
1. On first run of the script you will be asked to click a link and authorise your account. Paste in the code given and after this the app will be able create/edit spreadsheets in your google drive.

## Developing

If you would like to develop/test new features for the python script, run `make bash`.
This will enter you into the docker container bash environment and allow you to run the script on the fly (`python net-test.py`). You can test new changes within the app folder live from using this method.
