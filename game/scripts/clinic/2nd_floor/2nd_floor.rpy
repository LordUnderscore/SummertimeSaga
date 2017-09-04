label hospital_second_floor_dialogue:
    $ location_count = "Hospital 2nd Floor"
    if mrsj.started(mrsj_sex_ed) and not Roz.completed(roz_storage):
        scene expression gTimer.image("hospital_second{}_b")
        if Roz.started(roz_storage) and hospital_access_card in inventory.items:
            show player 410
            with dissolve
            player_name "This must be it!"
            player_name "Let's see if it works..."

        elif Roz.started(roz_storage):
            show player 12
            with dissolve
            player_name "The receptionist probably has duplicates of all the keys..."
            player_name "Perhaps I could find some at her desk?"
        else:

            show player 35
            with dissolve
            player_name "Hmm... I wonder where they store all their medicine."
            show player 30
            player_name "I should find the {b}storage room{/b}."
        hide player
        with dissolve
    $ callScreen(location_count)

label hospital_second_floor_phone_dialogue:
    scene hospital_phone
    pause
    if mrsj.started(mrsj_sex_ed) and Roz.completed(roz_intro) and Roz.known(roz_storage) and not Roz.known(roz_trick):
        show player 404 with dissolve
        pause
        show player 406 with dissolve
        player_name "Hi!"
        pause
        player_name "I... Emm... There's an emergency on the second floor!!"
        show player 407
        pause
        show player 408
        pause
        show player 407
        pause
        pause
        show player 406
        player_name "Oh, yes, it's about an uregistered patient..."
        show player 407
        pause
        pause
        show player 406
        player_name "Yes, it's urgent!"
        show player 408
        pause
        pause
        show player 407
        pause
        show player 406
        player_name "Thank you..."
        show player 407
        pause
        show player 405 with dissolve
        player_name "Well...that should work!"
        player_name "Let's see if she left her reception desk..."
        hide player
        with dissolve
        $ Roz.add_event(roz_trick)
    else:

        player_name "( I have no reason to call anyone. )"
    $ callScreen(location_count)