label third_floor_dialogue:
    $ location_count = "School Third Floor"
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not gTimer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)
    $ callScreen(location_count)