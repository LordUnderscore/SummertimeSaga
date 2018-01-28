default treehouse_first_visit = True
default treehouse_closeup_first_visit = True
default treehouse_interior_first_visit = True

label treehouse_dialogue:
    $ location_count = "Treehouse"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    if treehouse_first_visit:
        $ treehouse_first_visit = False
        scene expression gTimer.image("treehouse{}_b")
        show player 32 with dissolve
        player_name "Cool! Our old treehouse is still holding up."
        hide player with dissolve
    $ callScreen(location_count)

label treehouse_closeup_dialogue:
    $ location_count = "Treehouse Closeup"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    if treehouse_closeup_first_visit:
        $ treehouse_closeup_first_visit = False
        scene expression gTimer.image("treehouse_c{}")
        player_name "( That doesn't look too safe... )"
    $ callScreen(location_count, False)

label treehouse_interior_dialogue:
    $ location_count = "Treehouse Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 1 to 114>audio/ambience_treehouse.ogg", 0)
    if treehouse_interior_first_visit:
        $ treehouse_interior_first_visit = False
        scene expression gTimer.image("treehouse_inside{}_b")
        show player 2 with dissolve
        player_name "( Wow! It hasn't changed at all! )"
        player_name "( Let's have a look around... )"
        hide player with dissolve
    $ callScreen(location_count)

label lure_02:
    scene expression "backgrounds/location_treehouse_box.jpg"
    show expression "objects/closeup_bait02.png" with dissolve
    $ inventory.get_item(item = lure01)
    show unlock36 at truecenter with dissolve
    pause
    hide unlock36 with dissolve
    $ callScreen(location_count)