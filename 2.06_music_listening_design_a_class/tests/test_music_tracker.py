from lib.music_tracker import MusicTracker

def test_adding_the_song():
    music_tracker = MusicTracker()
    music_tracker.add("Morning song")
    assert music_tracker.music_list == ["Morning song"]
    assert music_tracker.show_music_list() == ["Morning song"]