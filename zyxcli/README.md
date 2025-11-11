# zyxcli (Docker-only)

This is a Docker-only CLI scaffold for the ZYX project.

## Build image
```bash
docker build -t zyxcli:latest .
```

## Run commands
Example (explicit credentials):
```bash
ZYX_SERVER=http://localhost:8081 ZYX_USER=admin ZYX_PASS=secret docker run --rm -it zyxcli:latest service list
```

Or use the included wrapper script (after `chmod +x zyxcli_wrapper.sh`):
```bash
./zyxcli_wrapper.sh service list --server http://localhost:8081 --user admin --password secret
```

Notes:
- Ephemeral mode: no credentials are stored in the container.
- Supports env vars: ZYX_SERVER, ZYX_USER, ZYX_PASS, ZYX_TOKEN
