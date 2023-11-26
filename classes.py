class Video:
    def __init__(self, title, stream):
        self.title = title
        self.stream = stream

class Wrapper:
    def __init__(self, title, videos):
        self.title = title
        self.videos = videos