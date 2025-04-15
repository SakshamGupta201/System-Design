class Video:
    def __init__(self, title):
        self.title = title
        self.load_video()

    def load_video(self):
        print(f"Loading video: {self.title}...")

    def play(self):
        print(f"Playing video: {self.title}")


class VideoProxy:
    def __init__(self, title):
        self.title = title
        self.video = None

    def play(self):

        if self.check_permissions():

            if not self.video:
                print("Video not loaded yet. Loading now...")
                self.video = Video(self.title)
            self.video.play()
        else:
            print("Access denied: You don't have permissions to watch this video.")

    def check_permissions(self):

        print("Checking user permissions...")
        return True


if __name__ == "__main__":

    proxy = VideoProxy("Avengers")
    proxy.play()
