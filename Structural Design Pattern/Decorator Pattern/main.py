from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play():
        pass


class VLCMediaPlayer(MediaPlayer):
    def play(self):
        return "Playing ..."


class PlayerDecorator:
    def __init__(self, media_player: MediaPlayer):
        self._media_player = media_player

    def play(self):
        self._media_player.play()


class SubtitlePlayer(PlayerDecorator):
    def play(self):
        return f"{self._media_player.play()}, subtitles"


class HDPlayer(PlayerDecorator):
    def play(self):
        return f"{self._media_player.play()}, HD"


vlc = VLCMediaPlayer()
print(vlc.play())
vlc_with_subtitles = SubtitlePlayer(vlc)
print(vlc_with_subtitles.play())

vlc_with_subtitles_hd = HDPlayer(vlc_with_subtitles)
print(vlc_with_subtitles_hd.play())
