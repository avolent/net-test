<h1 align="center">net-test</h1>

> A Python wrapper for the Speedtest CLI from Speedtest.net - https://www.speedtest.net/apps/cli

## Goal

The goal is to add more features that I would use to track my internet speed over a period of time at certain intervals.

## Design

Tool is built with the https://3musketeers.io framework in mind.

## Usage

### Requirements
The following tools need to be installed before running the tool.
- Docker
- Docker Compose
- Make

### Using the tool

1. Clone the git repository.
1. Run `make run_test` within the root of the repository.
1. Speedtest results will be outputted into the file "output.csv" in the app folder.

#### More Commands

make help - Show the help output for speedtest cli.
make servers - 


