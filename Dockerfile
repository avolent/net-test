FROM python:3.10-slim

# Update workdir to app folder and copy python requirements
WORKDIR /app
COPY ./app/requirements.txt requirements.txt

# Install requirements (Python and Speedtest CLI)
RUN python -m pip install -r requirements.txt && \
    apt update && \
    apt install -y curl && \
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash && \
    apt install -y speedtest

# Set entry point to python. This can be manually changed with the docker compose run command.
ENTRYPOINT ["python"]