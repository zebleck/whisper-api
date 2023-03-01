This repository is meant as a easy-to-use docker container for setting up an API using whisper AI.

Original from [here](https://lablab.ai/t/whisper-api-flask-docker).

# How to run the container?

1. Open a terminal and navigate to the folder where you created the files.
2. Run the following command to build the container:<br>
 `docker build -t whisper-api .`
3. Run the following command to run the container:<br>`docker run -p 5000:5000 whisper-api`