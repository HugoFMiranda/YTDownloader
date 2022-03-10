# Import
import os

from pytube import YouTube
from termcolor import colored

os.system('color')
print(colored("-------------------FALCON YT DOWNLOADER 3000--------------------", "magenta", attrs=['bold']))
url = input(colored(" > Insira o link do video: ", "cyan"))
my_video = YouTube(url)


# download
def download(video_resolutions, videos):
    while True:
        # Looping through the video_resolutions list to be displayed on the screen for user selection...
        i = 1
        print(colored("\nEscolha uma resolução: ", "yellow"))
        for resolution in video_resolutions:
            print(f'{i}. {resolution} ')
            i += 1

        # To Download the video with the users Choice of resolution
        choice = int(input(colored('\nEscolha: ', "yellow")))

        # To validate if the user enters a number displayed on the screen...
        if 1 <= choice < i:
            resolution_to_download = video_resolutions[choice - 1]
            print(colored(f"A baixar o video em {resolution_to_download}...", "green"))

            # command for downloading the video
            videos[choice - 1].download()

            print(colored("\nSucesso!", "green"))
            break
        elif choice == 0:
            break
        else:
            print(colored(":(!!\n\n", "red"))


# AUDIO ONLY
def sort_audio(url):
    audio_resolutions = []
    audio = []
    for stream in my_video.streams.filter(only_audio=True):
        if audio_resolutions.__contains__(stream.mime_type):
            pass
        else:
            audio_resolutions.append(stream.mime_type)
            audio.append(stream)
    return audio_resolutions, audio


# VIDEO_ONLY
def sort_video(url):
    video_resolutions = []
    videos = []
    for stream in my_video.streams.order_by('resolution').filter(only_video=True):
        # print(stream)
        video_resolutions.append(stream.resolution + "tipo: " + stream.mime_type)
        videos.append(stream)
    return video_resolutions, videos


# VIDEO+SOM
def sort_res(url):
    video_resolutions = []
    videos = []
    for stream in my_video.streams.order_by('resolution'):
        # print(stream)
        video_resolutions.append(stream.resolution + " tipo: " + stream.mime_type)
        videos.append(stream)
    return video_resolutions, videos


# Info
print(colored(" \nINFORMAÇÔES DO VIDEO: ", "yellow"))
print(colored(" > Titulo: ", "cyan"), my_video.title)
print(colored(" > Duração: ", "cyan"), my_video.length, "seconds")
print(colored(" > Views: ", "cyan"), my_video.views, "\n")

# Download
sn = input(colored("Deseja fazer download? (s/n) ", "yellow"))
if sn.__eq__("s"):
    print(colored("\nSelecione o tipo de download: ", "yellow"))
    print(colored("0. Cancelar", "red"))
    print(colored("1. Video + Audio", "cyan"))
    print(colored("2. Video", "cyan"))
    print(colored("3. Audio", "cyan"))
    choice = input(colored("Opção: ", "yellow"))
    if choice == "1":
        # sort_res(url)
        video_resolutions, videos = sort_res(url)
        download(video_resolutions, videos)
    elif choice == "2":
        # sort_video(url)
        video_resolutions, videos = sort_video(url)
        download(video_resolutions, videos)
    elif choice == "3":
        # sort_audio(url)
        video_resolutions, videos = sort_audio(url)
        download(video_resolutions, videos)
    else:
        pass
input(colored('\n\nObrigado por usar FalconYTDownloader3000, pressione qualquer tecla para sair.', "magenta"))