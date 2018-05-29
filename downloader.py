from pytube import YouTube

# input_link = 'https://www.youtube.com/watch?v=sf_9w653xdE&t=1s&index=2&list=PLTxllHdfUq4d-DE16EDkpeb8Z68DU7Z_Q'
destination_path = '/Users/kebba'


class Downloader:
    def __init__(self, link):
        self.link = link

    def single_video(self):
        yt = YouTube(self.link)
        stream = yt.streams.first()
        stream.download(destination_path)


if __name__ == '__main__':

    input_link = f"'{input('Please input the youtube link: ')}'"




