from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, playlist):
        pass


class SortByNameStrategy(SortStrategy):
    def sort(self, playlist):
        return sorted(playlist, key=lambda song: song["name"])


class SortByArtiseStrategy(SortStrategy):
    def sort(self, playlist):
        return sorted(playlist, key=lambda song: song["artist"])


class Playlist:
    def __init__(self, songs, sort_strategy: SortStrategy):
        self.songs = songs
        self.sort_strategy = sort_strategy

    def sort_strategy(self, sort_strategy: SortStrategy):
        self.sort_strategy = sort_strategy

    def sort(self):
        self.sort_strategy.sort(self.songs)


songs = [
    {"name": "Bohemian Rhapsody", "artist": "Queen"},
    {"name": "Billie Jean", "artist": "Michael Jackson"},
    {"name": "Thriller", "artist": "Michael Jackson"},
]

playlist = Playlist(songs, SortByNameStrategy())
playlist.sort()
print("Sorted by name:", playlist.songs)

playlist = Playlist(songs, SortByArtiseStrategy())
playlist.sort()
print("Sorted by artist:", playlist.songs)
