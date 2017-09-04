default tattoo_interior_first_visit = True

label tattoo_parlor_dialogue:
    $ location_count = "Tattoo Parlor"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label tattoo_parlor_interior_dialogue:
    $ location_count = "Tattoo Parlor Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")
    if tattoo_interior_first_visit:
        $ tattoo_interior_first_visit = False
        scene tattoo_indoor_b
        show player 13 with dissolve
        player_name "( I've never been in a tattoo shop before. )"
        show player 34
        player_name "( Maybe I should get a tattoo one day... )"
        hide player with dissolve
    $ callScreen(location_count)

label grace_dialogue:
    scene tattoo_indoor_c
    if not Grace.known(grace_intro):
        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Hey there!"
        grace "Are you here for an appointment?"
        show grace 1
        show player 10
        player_name "I was just-"
        show player 12
        player_name "Uhh."
        show player 34
        show grace 3
        grace "Is everything okay?"
        show grace 1
        show player 30
        player_name "You look...familiar."
        show player 5
        show grace 3
        grace "Huh?"
        show grace 2
        grace "Hmm... Maybe you're thinking of my sister?"
        show grace 1
        show player 12
        player_name "Sister?"
        show player 11
        show grace 3
        grace "My little sister? {b}Eve{/b}?"
        show grace 1
        show player 38 with dissolve
        player_name "Oh! Of course!"
        show player 14 with dissolve
        player_name "I can see the connection, now."
        show player 13
        show grace 4
        grace "Ha ha."
        show grace 2
        grace "Anyway, is there anything I can do for you?"
        $ Grace.add_event(grace_intro)
        $ grace_intro.finish()
    else:

        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Hey there!"
        grace "Are you here for an appointment?"
    show grace 1

    menu grace_menu_dialogue:
        "Nothing.":
            show player 14
            player_name "I'm just looking around."
            show player 13
            show grace 2
            grace "Cool! Have a look."
            grace "I do all styles and designs showcased in my shop!"
            grace "Just let me know if you ever think about getting something, and we can make an appointment!"
            show grace 1
            show player 14
            player_name "Okay, thanks!"
            show player 13
            show grace 2
            grace "See ya."
            hide grace
            hide player
            hide tattoo_desk
            with dissolve
    $ callScreen(location_count)