#!/usr/local/bin/python
import os
import sys
from pytube import YouTube


PATH = {
    'HOME': os.path.expanduser("~"),
    # 'DOWNLOADS': os.path.join(os.path.expanduser("~"), "Downloads")
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
        response = input(
            'Do you want to Download Youtube videos? (Y/N):  ').lower()
        if response in yes:
            return True
        elif response in no:
            sys.exit()
        print('Wrong Input')


def get_destination_path():

    print('Save Video(s) in:')
    while True:
        try:
            response = int(input('1) Home Folder \n2) Make new Folder \n3)'
                                 ' List Folders \n4) To exit \n'))

            if response == 1:
                return PATH['HOME']

            elif response == 2:
                folder_name = input('Enter Folder Name: ')
                if not os.path.exists(os.path.join(PATH['HOME'], folder_name)):
                    os.makedirs(os.path.join(PATH['HOME'], folder_name))
                return os.path.join(PATH['HOME'], folder_name)

            elif response == 3:
                position = 0
                folder = {}
                for name in os.listdir(PATH['HOME']):
                    if os.path.isdir(os.path.join(PATH['HOME'], name)) and not name.startswith('.'):
                        position += 1
                        folder[position] = os.path.join(PATH['HOME'], name)
                        print(position, name)
                print('')

                choice = int(input('Chose a folder from list: '))
                return folder[choice]

            elif response == 4:
                sys.exit()

            else:
                print('Input has to be either 1, 2, 3 or 4')

        except ValueError:
            print('Wrong value')


def get_youtube_links():

    links = []
    link_count = int(input('How many videos are you downloading? '))

    for i in range(link_count):
        input_value = input(f'Enter Link {i+1}: ')
        links.append(input_value)

    return links


def download():

    if prompt():
        insert_links = input('1) Insert link(s) \n2) Exit ')
        if insert_links == str(1):
            youtube_links = get_youtube_links()
            destination_path = get_destination_path()

            print('Downloading video(s)...')
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
