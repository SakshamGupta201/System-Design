class Video:
    def __init__(self, title):
        self.title = title
        self.load_video()

    def load_video(self):
        print("Loading video", self.title, '...')
    
    def play(self):
        print("Playing video", self.title, '...')
        
video = Video("Avengers")
video.play()
