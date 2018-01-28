default art_classroom_first_visit = True

label art_classroom_dialogue:
    $ location_count = "Art Classroom"
    if art_classroom_first_visit == True:
        scene art_classroom_c
        show ross 1 zorder 1 at left
        show player 1f zorder 1 at right
        show xtra 22 as table zorder 0
        show xtra 23 as basket zorder 0 at Position (ypos = 635)
        show xtra 24 as fruit zorder 0 at Position (ypos = 565)
        with dissolve
        show ross 2
        ross "{b}[firstname]{/b}!!"
        ross "It's so wonderful to see you in class again!"
        show ross 1
        show player 14f
        player_name "Hi, {b}Ms. Ross{/b}!"
        player_name "I missed coming to your class."
        show ross 2
        show player 13f
        ross "You missed a whole month of fruit studies, but we can fix that."
        show ross 1
        show player 12f
        player_name "Fruit studies?"
        show ross 2
        show player 11f
        ross "Well of course!"
        ross "We've been exploring the beautiful forms and curves of fruits!"
        show ross 1
        show player 10f
        player_name "I see..."
        show ross 2
        show player 5f
        ross "Don't worry. You'll catch up."
        ross "I know you have a creative eye, {b}[firstname]{/b}!"
        show ross 1
        show player 14f
        player_name "I guess so... I do like to draw stuff..."
        show ross 2
        show player 13f
        ross "With my tutoring, and the right kind of life drawing studies..."
        ross "...You WILL graduate with a perfect mark!"
        show ross 1
        show player 14f
        player_name "Really?! Thanks, {b}Ms. Ross{/b}!"
        show player 18f
        player_name "I'll do my best!"
        show ross 2
        show player 13f
        ross "That's the art spirit!"
        hide ross
        hide player
        hide fruit
        hide basket
        hide table
        with dissolve
        $ art_classroom_first_visit = False

    if M_mia.get_state() == S_mia_find_easel:
        scene art_classroom_b
        show player 4 with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "Let's see if I can find an {b}easel{/b} I could use to draw some tattoo ideas..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_easel_found)
    $ callScreen(location_count)

label ross_button_dialogue:
    scene art_classroom_c with None
    show ross 1 zorder 1 at left
    show player 1f zorder 1 at right
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    show player 14f
    player_name "Hi, {b}Ms. Ross{/b}."
    show ross 2
    show player 13f
    ross "Hello, {b}[firstname]{/b}!"
    ross "Ready to get your hands dirty today?"
    show ross 1
    show player 17f
    player_name "Haha. I suppose."
    show ross 2
    show player 13f
    ross "Is there anything you want to talk about?"
    show ross 1
    show player 4f
    menu:
        "Not really.":
            show player 2f
            player_name "Nothing specific, {b}Ms. Ross{/b}."
            player_name "I was wondering what we're doing today."
            show ross 2
            show player 1f
            ross "That's okay."
            ross "Why don't you stick around and grab a canvas?"
            ross "We can paint happy little fruits together!!"
            show ross 1
            show player 14f
            player_name "Sure, {b}Ms. Ross{/b}."
            show ross 2
            show player 13f
            ross "That's the art spirit!"
    hide ross
    hide player
    hide fruit
    hide basket
    hide table
    with dissolve
    $ callScreen(location_count)

label easel_dialogue:
    scene art_classroom_b
    if M_mia.get_state() == S_mia_show_tattoo:
        show player 14 with dissolve
        player_name "( I should show the drawing I made to {b}Mia{/b} first, before I make another one. )"
        hide player with dissolve
    else:

        show player 35 with dissolve
        player_name "( What should I draw today? )"
        menu:
            "Tattoo ideas.":
                scene school_art_tattoos
                player_name "Hmm..."
                player_name "( What should I draw for {b}Mia{/b}... )"
                call screen tattoos
                hide player with dissolve
                scene school_art_cs01
                with fade
                show text "I've drawn so many pictures before...\n...But, doing something like this for {b}Mia{/b} made me super nervous!\nI hope it's what she wants..." at Position (xpos= 512, ypos = 700) with dissolve
                with dissolve
                pause
                hide text
                hide school_art_cs01
                with dissolve
                scene art_classroom_b
                show player 381 with dissolve
                player_name "Not bad!"
                show player 386
                player_name "( I should go and show {b}Mia{/b} what I made. )"
                player_name "( Hopefully, she'll like it... )"
                hide player with dissolve
                $ M_mia.trigger(T_mia_visit)
                show expression [drawn_tattoo] at truecenter with dissolve
                $ inventory.items.append(tattoo_choices[drawn_tattoo])
                pause
                hide expression [drawn_tattoo] with dissolve
    $ callScreen(location_count)