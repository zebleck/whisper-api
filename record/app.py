import requests
import time

while True:
    # wait until port 5000/whisper is available
    while True:
        try:
            print('Trying to connect.')
            requests.get('http://api:5000/whisper')
            break
        except:
            time.sleep(1)

    print('Connection established.')
    # send the recording to the api
    with open('recording.wav', 'rb') as file:
        response = requests.post('http://api:5000/whisper', files={'file': file})
        if response.status_code == 200:
            with open('transcript.txt', 'a') as outfile:
                outfile.write(response.json()['results'][0]['transcript'] + '\n')
    time.sleep(10)