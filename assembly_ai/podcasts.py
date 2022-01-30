import requests
import pprint
import json
import time
import threading
from api_secrets import API_KEY_LISTENNOTES, API_KEY_ASSEMBLYAI


#this changes based on podcast
listennotes_episode_endpoint = 'https://listen-api.listennotes.com/api/v2/episodes/f39e6f35513945d9a5e421269d95c69c?show_transcript=1'

headers_listennotes = {
  'X-ListenAPI-Key': API_KEY_LISTENNOTES,
}


transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_assemblyai = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}
'''
def printit():
    threading.Timer(5.0, printit).start()
    print
'''


def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=headers_listennotes)

    data = response.json()
    #pprint.pprint(data)

    episode_title = data['title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    audio_url = data['audio']
    return audio_url, thumbnail, podcast_title, episode_title



def transcribe(audio_url, auto_chapters=False):
    transcript_request = {
        'audio_url': audio_url,
        'auto_chapters': 'True' if auto_chapters else 'False'
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers_assemblyai)
    pprint.pprint(transcript_response.json())
    return transcript_response.json()['id']


def poll(transcript_id, **kwargs):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers_assemblyai)

    if polling_response.json()['status'] == 'completed':
        filename = transcript_id + '.txt'
        with open(filename, 'w') as f:
            f.write(polling_response.json()['text'])

        filename = transcript_id + '_chapters.json'
        with open(filename, 'w') as f:
            chapters = polling_response.json()['chapters']

            data = {'chapters': chapters}
            for key, value in kwargs.items():
                data[key] = value

            json.dump(data, f, indent=4)

        print('Transcript saved')
        return True
    
    return False


def pipeline(episode_id):
    audio_url, thumbnail, podcast_title, episode_title = get_episode_audio_url(episode_id)
    # print(audio_url, thumbnail, podcast_title, episode_title)
    transcribe_id = transcribe(audio_url, auto_chapters=True)
    
    firstTimeThrough = True
    while True:
        result = poll(transcribe_id, audio_url=audio_url, thumbnail=thumbnail, podcast_title=podcast_title,
                  episode_title=episode_title)
        if result:
            break
        if (firstTimeThrough == True):
            print("Summary in progress.")
            firstTimeThrough = False
        else:
            print(".")


if __name__ == '__main__':
   #this changes based on podcast
   pipeline("f39e6f35513945d9a5e421269d95c69c")
