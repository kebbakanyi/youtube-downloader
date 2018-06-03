from pytube import YouTube
from os.path import expanduser
import sys

PATHS = {
    'HOME': expanduser("~"),
    'YOUTUBE_DOWNLOADS': '/Users/kebba/YoutubeDownloads',
    'DOWNLOADS': '/Users/kebba/Downloads'
}

yes = 'yes y'.split()
no = 'no n'.split()


def download_videos(input_links, destination):

    for link in input_links:
        yt = YouTube(link)
        stream = yt.streams.first()
        print(f'Downloading - {yt.title}')
        stream.download(destination)


def prompt():
    while True:
        response = input('Do you want to Download Youtube videos? (Y/N):  ').lower()
        if response in yes:
            return True
        elif response in no:
            sys.exit()
        print('Wrong Input')


def get_destination_path():

    print('Save Files in:')
    while True:
        try:
            response = int(input('1) Home Folder \n2) Youtube Downloads Folder \n3) Downloads folder '))
            if response == 1:
                return PATHS['HOME']
            elif response == 2:
                return PATHS['YOUTUBE_DOWNLOADS']
            elif response == 3:
                return PATHS['DOWNLOADS']
            else:
                print('Input has to be either 1, 2 or 3')
        except ValueError:
            print('Wrong value')


def get_youtube_links():
    links = []
    link_count = int(input('How many videos are you downloading? '))

    for i in range(link_count):
        input_value = input(f'Enter link {i+1}: ')
        links.append(input_value)

    return links


def download():

    if prompt():
        insert_links = input('Enter: \n1) To insert link(s) \n2) To exit ')
        if insert_links == str(1):
            youtube_links = get_youtube_links()
            destination_path = get_destination_path()

            print('Downloading video...')
            download_videos(youtube_links, destination_path)

            print('Done!')
        elif insert_links == str(2):
            sys.exit()
        else:
            print('Wrong Input')

    else:
        print('Wrong input')


if __name__ == '__main__':
    download()






