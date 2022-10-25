FROM python:3.10-slim

WORKDIR /app

# Copy necessary files
COPY ./app/requirements.txt requirements.txt
COPY ./ookla /root/.config/ookla

# Install requirements (Python and Speedtest CLI)
RUN python -m pip install -r requirements.txt && \
    apt update && \
    apt install -y curl && \
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash && \
    apt install -y speedtest

# Run the script
CMD ["python", "net-test.py"]
