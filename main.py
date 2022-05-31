# Import
import os

from pytube import YouTube
from pytube import Playlist
from termcolor import colored

os.system('color')


# DOWNLOAD
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


# AUDIO_ONLY
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
def videoInfo(my_video):
    print(colored(" \nINFORMAÇÔES DO VIDEO: ", "yellow"))
    print(colored(" > Titulo: ", "cyan"), my_video.title)
    print(colored(" > Duração: ", "cyan"), my_video.length, "seconds")
    print(colored(" > Views: ", "cyan"), my_video.views, "\n")


# LER E CRIAR TXT
def txtreader():
    links = []
    f = open("links.txt", "x")
    print(colored("Insira os links no ficheiro txt criado após isso confirme a operação. (1 link por linha)", "yellow"))
    if input(colored("Continuar? (s/n) ", "yellow")).__eq__("s"):
        f = open("links.txt", "r")
        links = f.readlines()
    return links


# TXT
def txt():
    links = txtreader();
    if links == []:
        print(colored("Ficheiro vazio, operação cancelada...", "red"))
        os.remove("links.txt")
        return links
    else:
        return links


def downloadF(url):
    # streams = url.streams.get_audio_only()
    streams = my_video.streams.filter(only_audio=True, file_extension='mp4').first()
    streams.download()


# ESCOLHER TIPO DE FICHEIRO
def escolhertipo():
    print(colored("\nSelecione o tipo de ficheiro que deseja baixar: ", "yellow"))
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


# MAIN
print(colored("-------------------FALCON YT DOWNLOADER 3002--------------------", "magenta", attrs=['bold']))
print(colored("\nSelecione o tipo de download: ", "yellow"))
print(colored("0. Cancelar", "red"))
print(colored("1. Link (1 video)", "cyan"))
print(colored("2. Ficheiro (1+ videos)", "cyan"))
print(colored("3. Playlist", "cyan"))
choice = input(colored("Opção: ", "yellow"))
if choice == "1":
    url = input(colored(" > Insira o link do video: ", "cyan"))
    my_video = YouTube(url)
    videoInfo(my_video)
    sn = input(colored("Deseja fazer download? (s/n) ", "yellow"))
    if sn.__eq__("s"):
        escolhertipo()
    else:
        pass
elif choice == "2":
    url = txt()
    if url == []:
        pass
    else:
        for line in url:
            my_video = YouTube(line)
            print(colored("A baixar: " + my_video.title, "green"))
            downloadF(my_video)
        os.remove("links.txt")
        print(colored("\nSucesso!", "green"))
elif choice == "3":
    playlist = Playlist(input(colored(" > Insira o link da playlist: ", "cyan")))
    for video in playlist.videos:
        print('A baixar : {} - url : {}'.format(video.title, video.watch_url))
        my_video = video
        downloadF(my_video)
    print(colored("\nSucesso!", "green"))

input(colored('\n\nObrigado por usar FalconYTDownloader, pressione "enter" para sair.', "magenta"))
