#!/bin/bash

# Install curl if missing
if ! command -v curl &> /dev/null; then
    apt-get update && apt-get install -y curl
fi

# Start Ollama in background
echo "Starting Ollama server..."
/usr/bin/ollama serve &

# Wait for server to be ready
echo "Waiting for Ollama to be ready..."
while ! curl -s http://localhost:11434 >/dev/null; do
    echo "Ollama not ready yet - sleeping"
    sleep 5
done
echo "Ollama is ready!"

# Keep container running by waiting on Ollama process
wait $(pidof ollama)