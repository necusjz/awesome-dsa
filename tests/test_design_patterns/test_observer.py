from src.design_patterns.observer import YoutubeChannel, YoutubeUser


def test_observer():
    channel = YoutubeChannel("3blue1brown")

    channel.subscribe(YoutubeUser("sub1"))
    channel.subscribe(YoutubeUser("sub2"))
    channel.subscribe(YoutubeUser("sub3"))

    channel.notify("A new video released.")
