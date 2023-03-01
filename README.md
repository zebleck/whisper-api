This repository is meant as a easy-to-use docker container for setting up an API using whisper AI.

Original from [here](https://lablab.ai/t/whisper-api-flask-docker).

# How to run?

Run `docker-compose up` to start the container.

# Whisper API

An API for Whisper runs at `http://localhost:5000/whisper`.

To process a file yourself, use `curl -F "file=@/path/to/file" http://localhost:5000/whisper`

# Record

The record service will record continuously and write the transcript to the file `transcript.txt` located in the `record` folder.

# Testing

Running

`curl http://localhost:5000`

should return

`Whisper Hello World!`