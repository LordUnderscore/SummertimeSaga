label stairs_dialogue:
    $ location_count = "School Right Hallway"
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not gTimer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if stairs_dialogue_count == 0:
        scene stairs
        show player 4 at left with dissolve
        player_name "Hmmm..."
        player_name "( Not too many people going into the Cafeteria, yet. )"
        show player 12 at left
        player_name "( It's not lunch time yet. )"
        hide player 12 at left with dissolve
        $ stairs_dialogue_count = 1
    $ callScreen(location_count)

label annie_button_dialogue:
    scene location_stairs_closeup
    show player 14 at left with dissolve
    show annie 1 at right
    player_name "Hey Annie!"
    show annie 5
    show player 1
    ann "Make it quick!"
    show annie 6
    show player 17
    player_name "Oh, nothing... I was just saying hi!"
    show annie 4
    show player 18
    ann "I'm on hall monitoring duty... And you're wasting my time."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "All right. Sorry to bother you. Sheesh!"

label unfinished_dialogue2:
    scene stairs
    show player 18 at left
    player_name "This content is not ready yet! Come back when the next game update is released!"
    $ callScreen(location_count)

label quest09_1:
    scene stairs
    show player 166 with dissolve
    player_name "( I can't leave. )"
    if not quest09_2:
        player_name "( I have to give {b}Mrs. Smith{/b} the {b}receipt{/b}, so I can give {b}Annie{/b} the delivery. )"
    else:
        player_name "( I still have to give {b}Annie{/b} the delivery. )"
    $ callScreen(location_count)