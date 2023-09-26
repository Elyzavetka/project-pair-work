from lib.music_library import MusicLibrary
from lib.track import Track


def test_add_multiple_tracks_and_lists_them():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1, track_2]

def test_searches_by_title():
    library = MusicLibrary()
    track_1 = Track("My title 1", "My Artist 1")
    track_2 = Track("My title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("My title 2") == [track_2]

def test_searches_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("One song", "My Artist 1")
    track_2 = Track("My title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("One") == [track_1]