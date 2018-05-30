from pytube import YouTube

# destination_path = '/Users/kebba'


class Downloader:
    def __init__(self, youtube_link, destination):
        self.link = youtube_link
        self.destination = destination

    def single_video(self):
        yt = YouTube(self.link)
        stream = yt.streams.first()
        stream.download(self.destination)


if __name__ == '__main__':

    input_link = f"'{input('Please input the youtube link: ')}'"
    destination_path = input('Please input the destination path: ')
    print('Downloading...')
    new_download = Downloader(input_link, destination_path)
    new_download.single_video()
    print('Done!')



