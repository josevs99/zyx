FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install basic tools so you can debug inside the container
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Make CLI command executable
RUN chmod +x zyxcli.py && ln -s /app/zyxcli.py /usr/local/bin/zyxcli

CMD ["tail", "-f", "/dev/null"]

