default hill_first_visit = True

label hill_dialogue:
    $ location_count = "Hill"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    if hill_first_visit:
        scene expression gTimer.image("hill{}_b")
        show player 32 with dissolve
        player_name "Wow! What a view!"
        show player 14 at Position(xpos = 444)
        player_name "( Perfect place to bring a girl on a date... )"
        show player 4 at Position(xpos = 450)
        player_name "( ...If I only had a car! )"
        hide player with dissolve
        $ hill_first_visit = False
    $ callScreen(location_count)