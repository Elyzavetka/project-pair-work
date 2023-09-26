from lib.music_library import MusicLibrary
from lib.track import Track

def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

def test_initially_searches_return_empty():
    library = MusicLibrary()
    assert library.search_by_title("hello") == []
