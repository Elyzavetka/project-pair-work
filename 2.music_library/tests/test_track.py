from lib.track import Track

def test_construct_track_and_title_and_artists():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"

def test_formats_title_and_artists():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"
