from pytube import YouTube
import tkinter as tk

# destination_path = '/Usgiers/kebba/YoutubeDownloads'


class Downloader:
    def __init__(self, youtube_link, destination):
        self.link = youtube_link
        self.destination = destination

    def single_video(self):
        yt = YouTube(self.link)
        stream = yt.streams.first()
        stream.download(self.destination)
        print(f'Downloading - {yt.title}')


if __name__ == '__main__':
    yes = 'yes y'.split()
    no = 'no n'.split()

    is_single = input('Downloading a single video? (Y/N):  ').lower()
    if is_single in yes:
        input_link = f"'{input('Please input the youtube link: ')}'"
        destination_path = input('Please input the destination path: ')
        print('Downloading video...')
        new_download = Downloader(input_link, destination_path)
        new_download.single_video()
        print('Done!')

    elif is_single in no:
        destination_path = input('Please input the destination path: ')
        print('Downloading videos...')
        with open('download_links.txt', 'r') as file:
            for input_link in file:
                new_download = Downloader(input_link, destination_path)
                new_download.single_video()
            print('Done!')
    else:
        print('Wrong input')




