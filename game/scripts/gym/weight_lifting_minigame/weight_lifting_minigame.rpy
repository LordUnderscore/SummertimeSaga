label weightlifting_dialogue:
    scene lifting
    show player 1 at left with dissolve
    show kevin 9 at right with dissolve
    kev "Hey there, bud!"
    show kevin 8 at right
    show player 14 at left
    player_name "Hey {b}Kevin{/b}!"
    show kevin 10 at right
    show player 11 at left
    kev "You ready to lift some lead, bro?"
    menu:
        "Yeah, bro!":
            show player 17 at left
            show kevin 8 at right
            player_name "Yeah, bro!"
            show kevin 9 at right
            show player 11 at left
            kev "You have to start with some light reps!"
            show kevin 8 at right
            show player 12 at left
            player_name "What exercise are we doing?"
            show kevin 13 at right
            show player 24 at left
            kev "Take those light dumbbells..."
            show kevin 9 at right
            show player 85 at left
            if pStats.str() < 3:
                show player 85 at left
            elif pStats.str() < 7:
                show player 307 at left
            else:
                show player 308 at left
            kev "We're gonna do some {b}shoulder presses{/b}!!"
            hide player 85 at left
            hide player 307 at left
            hide player 308 at left
            hide kevin 9 at right
            with dissolve
            hide lifting
            jump weightlifting
        "Can't right now.":

            show player 10 at left
            show kevin 8 at right
            player_name "I can't, right now."
            player_name "I gotta do something else first..."
            show kevin 9 at right
            show player 1 at left
            kev "No worries, bro!"
            show kevin 11 at right
            show player 84 at left
            kev "I'll see you next time, bro!"
            player_name "See ya!"
            hide player 84 at left with dissolve
            hide kevin 11 at right with dissolve
            hide lifting
            jump training_dialogue


        "Skip Mini-Game (Cheat)" if cheat_mode:
            $ pStats.increase("str")
            $ gTimer.tick()
            show unlock25 at truecenter with dissolve
            $ renpy.pause()
            jump training_dialogue

label weightlifting:
    $ wl_win = 0
    $ time_y_value = 586
    $ y_value = 610
    $ pic_count = 0
    $ press_count = 0
    $ time_count = 12
    $ timer_range = 12
    $ style.time_bar.left_bar = "buttons/bar_full.png"
    $ style.time_bar.right_bar = "buttons/bar_empty.png"
    call screen weightlifting

label weightlifting_done:
    scene weightlifting03
    $ renpy.checkpoint()
    $ renpy.pause()
    scene lifting with dissolve
    show player 28 at left with dissolve
    show kevin 10 at right with dissolve
    kev "Right on! Dude!"
    show kevin 8 at right
    player_name "Wow... My arms and shoulders are burning..."
    show kevin 7 at right
    show player 11 at left
    kev "You keep pumping that lead bro, and you gonna get mad guns like these!!"
    show kevin 8 at right
    show player 17 at left
    player_name "Thanks for spotting me, {b}Kevin{/b}!"
    show kevin 11 at right
    show player 84 at left
    kev "No problem, bro! Come back tomorrow!"
    hide player 84 at left with dissolve
    hide kevin 11 at right with dissolve
    show unlock25 at truecenter with dissolve
    $ renpy.pause()
    hide unlock25 with dissolve
    $ pStats.increase("str")
    $ gTimer.tick()
    hide weightlifting03
    jump training_dialogue

label weightlifting_fail:
    scene weightlifting04
    $ renpy.checkpoint()
    $ renpy.pause()
    scene lifting with dissolve
    show player 27 at left with dissolve
    show kevin 9 at right with dissolve
    kev "...It's alright, dude."
    kev "You'll do better next time."
    show kevin 8 at right
    show player 24 at left
    player_name "Damn... I thought I could do it..."
    show kevin 10 at right
    show player 13 at left
    kev "Take a day off, and come back fresh!"
    show kevin 8 at right
    show player 21 at left
    player_name "Okay. See ya, {b}Kevin{/b}!"
    hide player 21 at left with dissolve
    hide kevin 8 at right with dissolve
    show unlock26 at truecenter with dissolve
    $ renpy.pause()
    hide unlock26 with dissolve
    $ gTimer.tick()
    hide weightlifting04
    jump training_dialogue