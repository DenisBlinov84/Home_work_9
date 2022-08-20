import requests

audio_url = 'https://ru.hitmotop.com/songs/74615948'


def download_audio(url=''):
    try:
        response = requests.get(url=url)
        with open('new_song.mp3', 'wb') as audio:
            audio.write(response.content)
    except Exception as ex:
        return 'Check the url-address please'


def main():
    print(download_audio(url=audio_url))


if __name__ == '__main__':
    main()
