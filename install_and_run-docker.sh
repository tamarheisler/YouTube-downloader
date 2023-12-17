#!/bin/bash

# Build the Docker image
docker build -t youtube-downloader .

# Run the Docker container
docker run -p 5000:5000 youtube-downloader
