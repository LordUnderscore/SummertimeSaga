label church_graveyard_dialogue:
    $ location_count = "Church Graveyard"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 2>audio/ambience_graveyard.ogg"):
            $ playSound("<loop 2>audio/ambience_graveyard.ogg")
    $ callScreen(location_count)