from watson_developer_cloud import speech_to_text_v1
import json


def set_audio(audio_path):
    translator_bot = speech_to_text_v1.SpeechToTextV1(username='4b0f1f1b-a66d-4eb9-b72a-ec0357741892',
                                                      password='aNYRbXKSMPY2')
    audio = open(audio_path, 'rb')
    audio_data = translator_bot.recognize(audio=audio.read(), content_type='audio/mp3',
                                          model='en-US_BroadbandModel', timestamps=True)
    f = open(audio_path+'out.txt', 'w')
    res = json.dumps(audio_data, sort_keys=True, indent=4)
    f.write(res)
    f.close()


def get_timestamp(query, data):
    ans = []
    sections_json = data['results'] #outer_json['results']
    for section in sections_json:
        for item in section.items():
            words_list = item[1]
            if type(words_list) is not bool:
                words = words_list[0]
                transcription = words['transcript']
                if query in transcription:
                    start = query.split()[0]
                    for word in words['timestamps']:
                        if word[0] == start:
                            ans.append(word[1])
    return ans


def js_get_timestamps(audio_path, query):
    f = open(audio_path+'out.txt', 'r')
    data = f.read()
    data = json.loads(data)
    return get_timestamp(query, data)

if __name__ == '__main__':
    #set_audio('./testAudio/bpn5min.mp3')
    print(js_get_timestamps('./testAudio/bpn5min.mp3', 'gradient'))
