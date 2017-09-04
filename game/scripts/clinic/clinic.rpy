label hospital_dialogue:
    $ location_count = "Hospital"
    $ callScreen(location_count)

label roz_dialogue:
    scene hospital_desk
    show roz 1 at left
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Hi!"
    show player 13f
    show roz 2
    roz "Yes?"
    roz "What is it I can do for you?"
    show roz 1
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_repeat:
        "1st floor?":
            show player 12f
            player_name "What can I find on the 1st floor?"
            show player 5f
            roz "..."
            show roz 2
            roz "It's the lobby."
            show roz 1
            show player 10f
            player_name "Oh... Is there anything else?"
            show player 5f
            show roz 3 with dissolve
            roz "Do you see anything else?"
            show roz 1 with dissolve
            show player 24f
            player_name "I guess not..."
            show player 25f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "2nd floor?":

            show player 12f
            player_name "What can I find on the 2nd floor?"
            show player 5f
            show roz 2
            roz "We have sick rooms, and a storage room on the 2nd floor."
            show roz 1
            show player 12f
            player_name "Oh... I see."
            show player 5f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "Schedule.":

            show player 12f
            player_name "Is there always someone at the reception?"
            show player 5f
            show roz 2
            roz "Yes."
            roz "I'm always here."
            show roz 1
            show player 12f
            player_name "You never leave your desk?"
            show player 5f
            show roz 2
            roz "Why do you ask?"
            show roz 1
            show player 10f
            player_name "Err... Just wondering?"
            show player 5f
            show roz 2
            roz "I only leave my desk in case of an emergency."
            show player 11f
            roz "If I don't get a {b}phone call{/b}, I don't leave."
            show roz 1 with dissolve
            show player 14f
            player_name "Oh... I see."
            show player 13f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            jump roz_dialogue_repeat
        "Nothing.":

            show player 14f
            player_name "No, I think that's all!"
            show player 13f
            show roz 2
            roz "Bye."
            hide player
            hide roz
            hide roz_desk
            with dissolve
    $ callScreen(location_count)