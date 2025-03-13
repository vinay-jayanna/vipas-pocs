#!/bin/bash

# Check if /data is initialized, if not, initialize it
if [ ! -f "/data/.serverversion" ]; then
    echo "Initializing /data directory..."
    # Replace this line with the correct initialization command or sequence
    devpi-init --serverdir /data
fi

# Start devpi-server
exec devpi-server --host 0.0.0.0 --port 3141 --serverdir /data

