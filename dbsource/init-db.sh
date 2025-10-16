#!/bin/bash
# Start CockroachDB in the background
cockroach start-single-node --insecure --background

# Wait for the node to be ready
sleep 5

# Run your initialization SQL
cockroach sql --insecure --file=/init.sql

# Keep container running
tail -f /dev/null
