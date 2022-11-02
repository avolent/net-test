<h1 align="center">Net-Test</h1>

> A Python wrapper for the Speedtest CLI from [Speedtest.net](https://www.speedtest.net/apps/cli) with my own twist.

## Goal

The goal is to add more features that I can use to track my internet speed over a period of time at certain intervals.

## Design

Tool is built with the https://3musketeers.io framework in mind.

## Usage

### Requirements
- Unix-like System or Windows Subsystem Linux that supports docker.
- Make -  If not already installed, `apt update && apt install make` or using your OS own package manager commands.
- Docker & Docker Compose - Follow instructions [here](https://docs.docker.com/engine/install/).
- Google AUTH0 Key for Google Sheet/Drive API - Follow instructions [here](https://pygsheets.readthedocs.io/en/staging/authorization.html) for Auth0.

### Using the tool

1. `git clone git@github.com:avolent/net-test.git && cd net-test`
1. Run `make run_test` within the root of the repository. **You will need to run the tool once and authorise your google account before being able to use google sheets.**
1. Once completed, results will be outputted into the file "./app/output.csv".
1. Use [crontab](https://crontab.guru) to schedule executions automatically.

#### More Commands

make run - Run the docker without rebuilding the image.
make build - Build the docker image
make help - Show the help output for speedtest cli.
make servers - List the current preferred servers, based on your location and latency.
make bash - Enter the docker containers bash terminal. (Useful for debugging and developing new features on the fly)
make clean - Remove and delete all docker images, configuration and network adapters

### Developing

If you would like to develop/test new features for the python script, run `make bash`.
This will enter you into the docker container bash environment and allow you to run the script on the fly (`python net-test.py`). You can test new changes within the app folder live from using this method.
