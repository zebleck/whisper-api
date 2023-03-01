FROM python:3.9-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y gcc && apt-get -y install portaudio19-dev
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]
#CMD ["sh", "-c", "while true; do sleep 1; done"]