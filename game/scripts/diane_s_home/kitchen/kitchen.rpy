label kitchen_dialogue:
    $ location_count = "Diane's Kitchen"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if aunt.started(aunt_breeding_bull) and quest12 in completed_quests:
        scene location_diane_kitchen_closeup with None
        show player 1 at left
        show aunt 88 at right
        with dissolve
        pause
        show aunt 89
        dia "Good morning, handsome!"
        show aunt 88
        show player 36
        player_name "Good morning, {b}Aunt Diane{/b}."
        show player 13
        show aunt 92
        dia "So... I've been thinking about what you said ALL night."
        dia "It's not an easy decision, and I don't want it to be something I regret."
        show aunt 87
        dia "But, your proposal sounds so tempting and it has several benefits, so..."
        show aunt 89
        dia "I've decided to entertain your idea and be bred!"
        show player 17
        show aunt 88
        player_name "Really? I'm glad you liked the idea!"
        show player 13
        show aunt 90
        dia "If I'm going to make it in this milking business, I'm going to need real, working udders!"
        show aunt 87
        dia "I want this to succeed, so we better stick to the guide."
        show aunt 89
        dia "Plus, the thought is a huge turn on for me. It's so... primal!"
        show aunt 88
        show player 21
        player_name "Really?"
        show player 13
        show aunt 90
        dia "Of course!"
        show aunt 92
        show player 11
        dia "But, I have this little problem..."
        show aunt 89
        dia "I'm just not sure I can find, you know... a young, healthy bull!"
        dia "But, it's okay. I can start working out the details."
        show aunt 88
        show player 14
        player_name "Glad I could help! I'm happy that you're happy!"
        show player 13
        show aunt 89
        dia "Thank you."
        dia "Oh, and if you think you know anyone who would, you know, be suitable for me, will you let me know?"
        show aunt 88
        show player 21
        player_name "Uhh... Alright!"
        hide player
        hide aunt
        with dissolve
        $ aunt_breeding_bull.finish()

    elif aunt.started(aunt_mouse_attack):
        scene dianekitchen with None
        show player 10 with dissolve
        player_name "Weird. She's not in here either."
        player_name "( I thought for sure... )"
        show player 11
        dia "EEEEEEKKKKKKK!"
        show player 23f
        player_name "What the..."
        player_name "( Is that {b}Aunt Diane{/b} screaming?! )"
        hide player with dissolve

    elif aunt_drink_active == True:
        $ callScreen(location_count)
    else:

        if not aunt.known(aunt_drunken_splur) and aunt_count < 8 or aunt.over(aunt_drunken_splur) and aunt_count < 8:
            scene dianekitchen1
            player_name "( There's no one here. )"
            player_name "( {b}Aunt Diane{/b} is outside by the garden. )"
    $ callScreen(location_count)

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( I can't just leave, {b}Aunt Diane{/b} might be in trouble. )"
    hide player with dissolve
    $ callScreen(location_count)

label kitchen_drink:
    scene dianekitchen
    show player 133 with dissolve
    player_name "( This should be it... )"
    show player 135
    player_name "Annnd... there."
    show player 132
    show expression "characters/xtra/char_xtra_01.png" at Position(xpos = 638, ypos = 519)
    player_name "Hmm..."
    show player 133
    player_name "( Maybe I should add a bit more? )"
    $ aunt_drink_made = True
    menu:
        "No.":
            show player 133
            player_name "Nah. That should be enough..."
            player_name "( {b}Aunt Diane{/b} gets a little bit too... Loving, when she has a few drinks. )"
            show player 134
            player_name "( That'll do... )"
            $ in_garden = True
            $ ui_lock_count = 1
            jump garden_dialogue
        "Yes.":

            show player 135
            player_name "Juuuust... a {b}little bit more{/b}!"
            show player 134
            player_name "( That'll do... )"
            $ aunt_extra_shot = True
            $ in_garden = True
            $ ui_lock_count = 1
            jump garden_dialogue