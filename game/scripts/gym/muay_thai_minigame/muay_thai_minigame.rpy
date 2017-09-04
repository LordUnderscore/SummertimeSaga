init python:
    panty_lie_seen = False
    class Arrow:
        def __init__(self, image = "", passive = ""):
            self.image = image
            self.passive = passive

    class Key:
        def __init__(self, image = "", passive = ""):
            self.image = image
            self.passive = passive

    def add_arrow(Arrow):
        task_list.append(Arrow)

    def add_key(Key):
        task_list.append(Key)

label bag_minigame_listing:
    $ renpy.random.shuffle(arrow_list)
    $ renpy.random.shuffle(keyboard_list)
    $ task_list = []
    $ move_list = []
    if training_tier == 1:
        $ move_list_number = 4
        $ time_count = 3
        $ timer_range = 3

    elif training_tier == 2:
        $ move_list_number = 6
        $ time_count = 4.5
        $ timer_range = 4.5

    elif training_tier == 3:
        $ move_list_number = 8
        $ time_count = 6
        $ timer_range = 6

    elif training_tier == 4:
        $ move_list_number = 10
        $ time_count = 7.5
        $ timer_range = 7.5
    $ a = 0
    while (a < move_list_number):
        if renpy.variant("pc"):
            $ b = renpy.random.randint(0, 1)
            if b == 0:
                $ move_list += [renpy.random.choice(arrow_list)]
            else:

                $ move_list += [renpy.random.choice(keyboard_list)]
        else:

            $ move_list += [renpy.random.choice(arrow_list)]
        $ a += 1
    $ renpy.random.shuffle(move_list)
    $ arrow_index = 0
    call screen bag_minigame

label bag_minigame_attack:
    if cheat_pass:
        $ training_done = True
        $ cheat_pass = False
    if training_tier == 1:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a with hpunch
    elif training_tier == 2:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a2 with hpunch
    elif training_tier == 3:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a3 with hpunch
    elif training_tier == 4:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a4 with hpunch
    player_name "Huah!!"
    jump training01_done_dialogue

label training01_payment_dialogue:
    scene expression gTimer.image("training{}_b")
    pause 0.001
    show player 1 at left
    show master 2 at right
    with dissolve
    if (not sister.completed(sis_panty02) and pStats.dex() == 2) or (not sister.completed(sis_panty03) and pStats.dex() == 5) or (not sister.completed(sis_panty04) and pStats.dex() == 7):
        mas "I can't teach you anything more for now."
        mas "Go out into the world, and get some more life experience! Maybe spend some more time with the nice woman who gave you those panties!"
        show player 40 at left
        show master 6 at right
        player_name "Yes, {b}Master Somrak{/b}!!!"

    elif training_skip_payment:
        mas "Ahh!"
        mas "You have returned!"
        mas "Are you ready to continue your training, young apprentice?"
        show master 1
        menu:
            "Train.":
                show player 40 at left
                show master 6 at right
                player_name "Yes, {b}Master Somrak{/b}!!!"
                show master 2
                show player 1
                mas "Good, good! Let us begin, then!"
                hide player
                hide master
                with dissolve
                jump training_during_dialogue

            "Skip Mini-Game (Cheat)" if cheat_mode:
                $ cheat_pass = True
                show player 40 at left
                show master 6 at right
                player_name "Yes, {b}Master Somrak{/b}!!!"
                show master 2
                show player 1
                mas "Good, good. Let us begin, then."
                hide player
                hide master
                with dissolve
                jump training_during_dialogue
            "Nevermind.":

                show master 5 at right
                show player 10 at left
                player_name "Actually, nevermind..."
                show master 4
                show player 11
                mas "Then return when you have changed your mind, young apprentice!"
                show master 6
                show player 40
                player_name "Yes, {b}Master Somrak{/b}!!!"
                hide player
                hide master
                with dissolve
    else:

        mas "Ahh!"
        mas "You have returned!"
        mas "Have you brought what I seek?"
        show master 1
        if panties in inventory.items:
            menu:
                "I have the panties." if training_tier == 1 and sister.completed(sis_panty01):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Yes..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Very good!" with fastdissolve
                    show player 12
                    player_name "Those cost me a lot... The training better be worth it."
                    show player 1
                    show master 4
                    mas "The art of Muay Thai is invaluable, young apprentice!"
                    show master 2
                    mas "Are you ready to train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "I have the panties. (Cheat)" if training_tier == 1 and sister.completed(sis_panty01) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Yes..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff({/b}"
                    show master 3
                    mas "Very good!" with fastdissolve
                    show player 12
                    player_name "Those cost me a lot... The training better be worth it."
                    show player 1
                    show master 4
                    mas "The art of Muay Thai is invaluable, young apprentice!"
                    show master 2
                    mas "Are you ready to train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "I have the panties." if training_tier == 2 and sister.completed(sis_panty02):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Yes..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Very good!" with fastdissolve
                    show player 12
                    player_name "Those cost me a lot... The training better be worth it."
                    show player 1
                    show master 4
                    mas "The art of Muay Thai is invaluable, young apprentice!"
                    show master 2
                    mas "Are you ready to train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)


                    jump training_during_dialogue

                "I have the panties. (Cheat)" if training_tier == 2 and sister.completed(sis_panty02) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Yes, {b}Master Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Yes..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    mas "You've done well, young apprentice!" with fastdissolve
                    show player 1
                    mas "Are you ready train?"
                    show player 40
                    show master 16
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)


                    jump training_during_dialogue

                "I have the panties." if training_tier == 3 and sister.completed(sis_panty03):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Yes, {b}Master Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Yes..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 14
                    pause
                    mas "You've done well, young apprentice!" with fastdissolve
                    show player 1
                    show master 2
                    mas "Are you ready train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam02)
                    jump training_during_dialogue

                "I have the panties. (Cheat)" if training_tier == 3 and sister.completed(sis_panty03) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Yes, {b}Master Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Yes..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 3
                    mas "Very good!" with fastdissolve
                    show player 1
                    show master 2
                    mas "Are you ready train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam02)
                    jump training_during_dialogue

                "I have the panties." if training_tier == 4 and sister.completed(sis_panty04):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Yes, {b}Master Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Yes..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    show master 3
                    mas "You've done well, young apprentice!" with fastdissolve
                    show player 40
                    show master 16
                    mas "Are you ready train?"
                    show player 40
                    show master 17
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam03)
                    jump training_during_dialogue

                "I have the panties. (Cheat)" if training_tier == 4 and sister.completed(sis_panty04) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Yes..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Very good!" with fastdissolve
                    show player 12
                    player_name "Those cost me a lot... The training better be worth it."
                    show player 1
                    show master 4
                    mas "The art of Muay Thai is invaluable, young apprentice!"
                    show master 2
                    mas "Are you ready to train?"
                    show player 40
                    show master 6
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam03)
                    jump training_during_dialogue
                "Nevermind.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Actually, nevermind..."
                    show master 4
                    show player 11
                    mas "Then return when you have changed your mind, young apprentice!"
                    show master 6
                    show player 40
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
        else:


            menu:
                "I have the panties." if not panty_lie_seen:
                    show master 2 at right
                    show player 11 at left
                    mas "I don't see any panties, apprentice."
                    show master 5
                    show player 10
                    player_name "Oh, right, about that..."
                    player_name "I haven't exactly found them yet..."
                    show master 4
                    show player 11
                    mas "Keep looking, my young apprentice!"
                    show player 1
                    mas "Return to me when you have found them!"
                    show master 6
                    show player 40
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master with dissolve
                    $ panty_lie_seen = True

                "<>I have the panties." if panty_lie_seen:
                    $ pass
                "Nevermind.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Actually, nevermind..."
                    show master 4
                    show player 11
                    mas "Then return when you have changed your mind, young apprentice!"
                    show master 6
                    show player 40
                    player_name "Yes, {b}Master Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
    $ callScreen(location_count)

label training_during_dialogue:
    scene minigame02b
    if training_skip_payment:
        scene minigame02b
        show master 3f at left
        with dissolve
        mas "You know what to do, young apprentice!"
        show master 2f
        mas "Just like we practiced last time."
        show master 4f
        mas "Now, show me!!"
    else:

        if training_tier == 1:
            show master 3f at left
            with dissolve
            mas "First, you will learn to use punches!"
            show master 2f
            mas "You must build power from the hips! Start from there..."
            show master 4f
            mas "...then turn your shoulder, extend your elbow straight..."
            show master 10f
            mas "...and {b}STRIKE{/b}!" with hpunch
            show master 4f
            mas "Now, show me!!"

        elif training_tier == 2:
            show master 3f at left
            with dissolve
            mas "Now, you will learn to use elbows!"
            show master 2f
            mas "It is most useful technique at short range; it can cut skin around the eyes..."
            show master 4f
            mas "...come from any angle, straight from your shoulder..."
            show master 10f
            mas "...and {b}STRIKE{/b}!" with hpunch
            show master 4f
            mas "Now, show me!!"

        elif training_tier == 3:
            show master 3f at left
            with dissolve
            mas "Now, you will learn to use kicks!"
            show master 2f
            mas "Anchor your feet to the mat, your momentum starts from there!"
            show master 4f
            mas "Pivot from your hips, turn your body..."
            show master 10f
            mas "...and {b}STRIKE{/b}!" with hpunch
            show master 4f
            mas "Now, show me!!"

        elif training_tier == 4:
            show master 3f at left
            with dissolve
            mas "Finally, you will learn to use knees!"
            show master 2f
            mas "You must to aim at the plexus or the head, then with tremendous power..."
            show master 4f
            mas "...turn your hips, prepare to jump..."
            show master 10f
            mas "...and {b}STRIKE{/b}!" with hpunch
            show master 4f
            mas "Now, show me!!"
    $ training_skip_payment = True
    hide master
    with dissolve
    hide minigame02b
    if cheat_pass:
        jump bag_minigame_attack
    jump bag_minigame_listing

label training01_done_dialogue:
    $ gTimer.tick()
    if training_tier == 1:
        if pStats.dex() < 2:
            $ pStats.increase("dex")
        if pStats.dex() > 1:
            $ training_skip_payment = False

    elif training_tier == 2:
        if pStats.dex() < 5:
            $ pStats.increase("dex")
        if pStats.dex() > 4:
            $ training_skip_payment = False

    elif training_tier == 3:
        if pStats.dex() < 7:
            $ pStats.increase("dex")
        if pStats.dex() > 6:
            $ training_skip_payment = False

    elif training_tier == 4:
        $ pStats.increase("dex")
    scene expression gTimer.image("training{}_b")
    if training_skip_payment:
        show masterplayer 28 at left
        show master 3 at right
        with dissolve
        mas "You did well, young apprentice!"
        show master 6
        show unlock9 at truecenter
        pause
        hide unlock9 with dissolve
        show master 2
        show masterplayer 27
        mas "However, I still see room for improvement!"
        show master 3
        mas "Go! rest!"
        mas "We will continue your training when you return."
        show masterplayer 40
        show master 6
        player_name "Yes! Thank you, {b}Master Somrak{/b}!!!"
        hide masterplayer
        hide master
        with dissolve
    else:

        if training_tier == 1:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Well done, young apprentice!"
            show master 2
            mas "You have improved, I can sense it!"
            show masterplayer 28
            mas "Here! You have have earned yourself a new belt!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            show masterplayer 27
            mas "Now... to continue your training, all you have to do..."
            show master 2
            show masterplayer 21
            mas "...is bring me more {b}panties{/b}!"
            show masterplayer 40
            show master 6
            player_name "Yes! Thank you, {b}Master Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "I have a good feeling about that one..."
            $ training_tier = 2

        elif training_tier == 2:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Well done, young apprentice!"
            show master 2
            show masterplayer 28
            mas "You have improved, I can sense it!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Now, rest!"
            mas "We will discuss the next part of your training when you return."
            show masterplayer 40
            show master 6
            player_name "Yes! Thank you, {b}Master Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "He learns fast..."
            $ training_tier = 3

        elif training_tier == 3:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Well done, young apprentice!"
            show master 2
            show masterplayer 28
            mas "You have improved, I can sense it!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Now, rest!"
            mas "We will discuss the next part of your training when you return."
            show masterplayer 40
            show master 6
            player_name "Yes! Thank you, {b}Master Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "He learns fast..."
            $ training_tier = 4

        elif training_tier == 4:
            show masterplayer 28 at left
            show master 3 at right
            with dissolve
            mas "Well done, young apprentice!"
            show master 2
            show masterplayer 28
            mas "Or should I say, young {b}master{/b}?"
            mas "You have excelled in every task I have given you."
            mas "You have improved much since the first time we met!"
            mas "And now..."
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "There is nothing more I can teach you."
            show master 2
            mas "...but I won't say \"no\" to more {b}panties{/b}!"
            show master 6
            pause
            show master 4
            mas "Now go out there and use your new skills!" with hpunch
            show masterplayer 40
            show master 6
            player_name "Yes, {b}Master Somrak{/b}!!!"
            player_name "Thank you!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "He reminds me of myself when I was young..."
    hide master
    with dissolve
    $ callScreen(location_count)

label training_failed_dialogue:
    scene expression gTimer.image("training{}_b")
    show masterplayer 27 at left
    show master 7 at right
    mas "{b}WRONG!!{/b}" with vpunch


    mas "You don't listen! You fight like foolish dog!"
    mas "Focus! Use less muscle, more brain!"
    show master 4
    mas "Train more, then come back..."
    hide masterplayer
    hide master
    with dissolve
    $ callScreen(location_count)