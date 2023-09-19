from pytube import Playlist, YouTube
from pytube.cli import on_progress
import os
from string import ascii_letters
from random import choices

'''
    pip freeze >
    add git
    push to repository
'''

if not os.path.exists("textVideo"):
    os.mkdir("textVideo")

if not os.path.exists("Video"):
    os.mkdir("textVideo")

url = input("Enter playlist url: ")
if "playlist" in url:
    playlist = Playlist(url)
    title = playlist.title

    #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

    count = 0

    for video in playlist.videos:
        video.register_on_progress_callback(on_progress)

        d_stream = video.streams.get_highest_resolution()
        d_stream.download(output_path=f'Video/{title}')

        v_title = d_stream.default_filename

        file = f'{title}/{v_title}'
    # os.rename(file, f'{title}/Tutorial{count} {video.title}')
        print('Downladed {video.title}')

        count +=1
else:
    yt = YouTube(url=url)
    title = "".join(choices(ascii_letters, k=10))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="Video/"+title+".mp4")

    #os.system(f"vosk-transcriber -i Video/{title}.mp4 -o textVideo/{title}.txt")