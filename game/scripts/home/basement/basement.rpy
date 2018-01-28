label home_basement_dialogue:
    $ location_count = "Basement"
    if M_mom.get_state() == S_mom_wash_clothes:
        scene home_basement_sideview
        show player 324 at Position(xpos=860)
        show mom 136 at Position(xpos=550,ypos=805)
        mom "Oh my goodness!!"
        show mom 137
        mom "{b}*Giggle*{/b}"
        show player 325
        show mom 135
        player_name "What is it, {b}[mom_name]{/b}?"
        show player 326
        show mom 136
        mom "Your clothes! They're a mess!"
        show player 324
        show mom 137
        mom "I can see somebody's been working really hard outside!"
        show player 325
        show mom 135
        player_name "Sorry, I should've worn something else..."
        show player 324
        show mom 136
        mom "It's okay, Sweetie! We'll get you all cleaned up."
        mom "Just give me your shirt and your shorts, so I can add them to the laundry."
        show player 325
        show mom 135
        player_name "It's okay, {b}[mom_name]{/b}. I can do it myself."
        show player 324
        show mom 136
        mom "Oh, come on! I was just about to turn the washing machine on."
        show mom 135
        show player 327 at Position(xoffset=-27) with fastdissolve
        pause
        scene home_basement_cutscene with fade
        show text "That was the first time I had ever undressed in front of {b}[mom_name]{/b}. \nI was a bit shy, but she was surprisingly fine with it. \nShe bent over to add them to the laundry... revealing herself to me.\nI wanted to look away, but couldn't... I was aroused by it." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
        scene home_basement_sideview
        show player 330 at Position(xpos=860)
        show mom 142 at Position(xpos=550,ypos=805)
        with fade
        mom "( He's probably going to wear those stinky boxers all day now. )"
        mom "( I should clean them now before he leaves them in his room for a week... )"
        show mom 136
        mom "Sweetie..."
        show player 332
        mom "Did you... want me to do ALL of your clothes?"
        show mom 135
        player_name "!!!"
        show player 331
        player_name "Oh, no, it's fine, {b}[mom_name]{/b}..."
        show mom 136
        show player 330
        mom "You've been sweating in those all day... You should take them off, and jump in the shower!"
        show mom 135
        show player 333
        player_name "Mooom-"
        show mom 136
        show player 330
        mom "Oh, please! It's not the first time I've seen you naked, Sweetie!"
        mom "You'll feel better once you get all cleaned up."
        show mom 138
        show player 334 with fastdissolve
        pause
        show player 335 with fastdissolve
        pause
        show player 336 with fastdissolve
        pause 0.1
        show mom 139
        show player 337 at Position(xpos=855) with vpunch
        pause
        show mom 140
        show player 338 at Position(xpos=853)
        mom "Ooops!!"
        mom "Oh my..."
        mom "Sweetie, here... Let's just... Umm..."
        mom "I have some clean towels you could use to cover yourself..."
        show mom 141 with fastdissolve
        pause
        show player 339 at Position(xpos=845)
        show mom 142
        with fastdissolve
        pause
        show player 341
        player_name "I'm so sorry, {b}[mom_name]{/b}!"
        show player 340
        show mom 143
        mom "Oh, that's alright, Sweetie."
        mom "These things happen."
        show mom 140
        mom "It's perfectly normal!"
        show mom 142
        mom "Hmm..."
        show mom 143
        mom "That towel is a bit small but I guess that will have to do..."
        mom "Just hurry up to the shower and make sure to rub yoursel-"
        mom "Scrub yourself clean!"
        show mom 142
        show player 341
        player_name "Okay..."
        hide player with dissolve

        show mom 139
        mom "( Oh my...)"
        mom "( ...I had no idea he had such a...manhood. )"
        scene black with fade
        $ M_mom.trigger(T_mom_clean_clothes)
        $ gTimer.tick()
        $ location_count = "Bedroom"
        $ unlock_ui()

    elif M_mom.get_state() == S_mom_close_valve:
        scene home_basement
        show player 34 with dissolve
        player_name "( The water valve should be next to the water heater. )"
        player_name "( I better shut it off before the upstairs floods. )"
        hide player with dissolve

    elif M_mom.get_state() == S_mom_lotion_adventure and M_mom.is_set("retrieved lotion"):
        jump mom_lotion_fun

    elif M_mom.get_state() == S_mom_give_laundry:
        scene home_basement_c
        show mom 125 at right
        show player 277 at left
        with dissolve
        player_name "Hey, {b}[mom_name]{/b}!"
        show player 276
        player_name "Here's the laundry you asked for."
        show player 13
        show mom 121
        with dissolve
        pause
        show mom 123
        mom "Thanks, Sweetie."
        mom "But that's not what I really wanted."
        show mom 124
        show player 10
        player_name "Oh? What did I forget?"
        show player 5
        show mom 123
        mom "Silly boy."
        show mom 63 with dissolve
        mom "I left you that note this morning because I couldn't get you out of my mind."
        show mom 61
        show player 11
        player_name "!!!"
        show mom 39
        mom "I want you and that big cock of yours."
        show mom 62
        show player 1
        mom "I want you to fuck me."
        show mom 61
        show player 2
        player_name "SSS-Sure!"
        show player 13
        show mom 62
        mom "Then take off your clothes."
        show player 11
        show mom 125
        player_name "!!!"
        show player 297
        player_name "We're doing it down here?!"
        show player 13
        show mom 62
        mom "{b}[sis]{/b} won't find us down here."
        show player 21
        show mom 125
        player_name "Well... okay."
        jump basement_mom_sex
    $ callScreen(location_count)


label basement_mom_sex:
    $ M_mom.set('sex speed', .175)
    $ location_count = "Basement"
    $ cum = False
    $ anim_toggle = False
    $ xray = False
    if M_mom.get_state() != S_mom_give_laundry and randomizer() <= 50:
        $ mom_basement_rand = True
    else:
        $ mom_basement_rand = False
    if mom_basement_rand:
        scene home_basement_c
        show mom 62 at right
        show player 13 at left
        with dissolve
        mom "Sit up on the washer for {b}Mommy{/b}."
    scene home_basement_sex_01
    show player 270 zorder 1 at Position(xpos=466,ypos=768)
    show mom 107 zorder 0 at Position(xpos=200)
    with fade
    pause
    show player 271 at Position(xpos=655,ypos=768)
    pause
    if mom_basement_rand:
        player_name "Good?"
        show mom 108
        mom "Perfect."
        mom "That cock of yours is just perfect."
    else:
        show mom 108
        mom "My turn..."
    show mom 109 at Position(xpos=205)
    pause
    show mom 110
    pause
    show mom 111 at Position(xpos=207)
    pause
    show mom 112 at Position(xpos=196)
    pause
    show mom 113 at Position(xpos=203)
    pause
    show mom 114
    pause
    show mom 115
    if mom_basement_rand:
        mom "Now sit back and let {b}[mom_name]{/b} help you with your dirty sticky load."
    else:
        mom "Like what you see?"
        show mom 114
        player_name "You're beautiful, {b}[mom_name]{/b}."
        show mom 115
        mom "Just sit back and relax, Sweetie."
        mom "Let's start nice and slow..."
    hide player
    hide mom
    show moms 124 at Position(xpos=650)
    with dissolve
    pause
    show moms 125 at Position(xpos=655) with dissolve
    pause
    show moms 126f with dissolve
    mom "Oh!"
    show moms 126e
    pause
    show moms 126d
    pause
    show moms 126c
    pause
    show moms 126b
    pause
    show moms 126
    if mom_basement_rand:
        mom "Mmmm..."
        mom "I can barely fit you all in."
    else:
        mom "Ahh..."
        player_name "!!!"
        player_name "You're so warm..."
    label basement_mom_sex_loop:
        hide screen basement_mom_sex_options
        show screen sex_anim_buttons
        pause
        if anim_toggle == True:
            $ animcounter = 0
            while animcounter < 4:
                hide screen sex_anim_buttons
                show moms 126_126b_126c_126d_126e_126f_126g_126h_126i_126j at Position(xpos=655)
                pause 4
                if mom_basement_rand:
                    if animcounter == 1:
                        mom "Oh, baby!{p=1}{nw}"
                        mom "Yes!{p=1}{nw}"
                    if animcounter == 2:
                        mom "Ahh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh!{p=1}{nw}"
                else:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, Sweetie!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:
            $ animcounter = 0
            while animcounter < 4:
                hide screen sex_anim_buttons
                show moms 126
                pause
                show moms 126b
                pause
                show moms 126c
                pause
                show moms 126d
                pause
                show moms 126e
                pause
                show moms 126f
                pause
                show moms 126g
                pause
                show moms 126h
                pause
                show moms 126i
                pause
                show moms 126j
                pause
                if mom_basement_rand:
                    if animcounter == 1:
                        mom "Oh, baby!{p=1}{nw}"
                        mom "Yes!{p=1}{nw}"
                    if animcounter == 2:
                        mom "Ahh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh!{p=1}{nw}"
                else:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, Sweetie!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                $ animcounter += 1
        show screen basement_mom_sex_options
        pause
        jump basement_mom_sex_loop

label basement_mom_sex_cum:
    hide screen basement_mom_sex_options
    player_name "{b}[mom_name]{/b}!"
    show white
    show moms 129 at Position(xpos=609) with vpunch
    hide white with dissolve
    if mom_basement_rand:
        mom "Oh, Sweetie!"
        mom "I'm cumming too!"
        show moms 129 with flash
        mom "AHH!!!"
    else:
        mom "Ahh!!!"
    jump basement_mom_sex_after

label basement_mom_sex_after:
    if M_mom.get_state() == S_mom_give_laundry:
        show moms 132 at Position(xpos=650) with fade
        mom "Thanks for bringing me the laundry..."
        show moms 131
        player_name "Anytime, {b}[mom_name]{/b}."
        show moms 132
        mom "Let me know if you want to do it again down here."
        show moms 131
        player_name "Definitely."
    elif mom_basement_rand:
        show moms 130 at Position(xpos=650) with fade
        mom "You should warn me when you're about to do it, Sweetie."
        show moms 131
        player_name "Sorry, {b}[mom_name]{/b}."
        player_name "I just couldn't help it..."
        player_name "It felt too good..."
        show moms 132
        mom "It's okay. Let's get cleaned up..."
    else:
        show moms 132 at Position(xpos=650) with fade
        mom "That was good, Sweetie."
        mom "Thanks for the invite!"
        show moms 131
        player_name "Anytime!"
    $ gTimer.tick()
    if M_mom.get_state() == S_mom_give_laundry:
        jump basement_confession_kiss
    $ callScreen(location_count)

label basement_confession_kiss:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show mom 73 at Position(xpos=650)
    with fade
    mom "Sweetie..."
    if randomizer() <= M_mom.get('mom concerned'):
        if M_mom.get('mom concerned') > 0:
            $ M_mom.set('mom concerned', M_mom.get('mom concerned') - 20)
        if M_mom.get('mom concerned') < 0:
            $ M_mom.set('mom concerned', 0)
        mom "I want you to tell me if you don't want to do this anymore, okay?"
        show player 228
        show mom 76
        player_name "No, it's fine, {b}[mom_name]{/b}..."
        player_name "I always feel like doing it with you."
        show player 227
        show mom 77
        mom "Really?"
        show player 228
        player_name "Yeah, that's all I think about doing when I see you..."
        show player 227
        show mom 75
        mom "You're always so sweet..."
    mom "Give me a kiss."
    hide player
    show mom 80 at Position(xpos=500)
    with dissolve
    pause
    show mom 79 with dissolve
    pause
    show mom 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show mom 78 at Position(xpos=650)
    with dissolve
    player_name "I love you, {b}[mom_name]{/b}!"
    show player 227
    show mom 75
    mom "I love you too, Sweetie..."
    scene home_basement
    hide mom
    hide player
    with fade
    $ M_mom.trigger(T_mom_basement_fun)
    $ unlock_ui()
    $ callScreen(location_count)

label broken_pipe:
    scene expression gTimer.image("home_basement")
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed with dissolve
    scene home_basement_c
    show player 2
    with dissolve
    player_name "Okay, the valve's shut."
    player_name "I should go back to the {b}bathroom{/b} to see if I can fix the {b}sink{/b}."
    hide player
    with dissolve
    $ M_mom.trigger(T_mom_closed_valve)
    $ callScreen(location_count)

label laundry_dialogue:
    scene home_basement_c
    show mom 123 at right
    show player 1 at left
    with dissolve
    mom "Oh! Hi Sweetie!"
    mom "You need something?"
    show mom 124
    menu:
        "Let me help.":
            show mom 124
            show player 14
            player_name "{b}[mom_name]{/b}, hand me the basket. I'll do the laundry."
            show mom 123
            show player 5
            mom "It's fine. I can do it."
            show mom 122
            show player 10
            player_name "You deserve a rest. You do so much work around the house."
            player_name "Let me, please"
            show mom 123
            show player 11
            mom "So stubborn..."
            show player 1
            mom "Okay, Sweetie."
            show player 275
            show mom 62
            mom "Just make sure you don't mix the colored clothes with the white clothes."
            show mom 125
            show player 276
            player_name "Will do, {b}[mom_name]{/b}."
            show mom 63
            show player 275
            mom "Sweetie..."
            mom "Thanks for helping out lately."
            mom "It's making life a lot easier..."
            show mom 125
            show player 277
            player_name "No problem!"
            scene help_mom_basement_cutscene with fade
            show text "Recently, I've been looking forward to helping {b}[mom_name]{/b} around the house. \nI could tell she enjoyed it too, always hanging around and asking me how things were going with girls at school... \nI feel like she's been so close to me lately... \nThe way she stands by me, touches me, and keeps staring at me all the time." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            scene home_basement_c with fade
            show mom 2 at right
            show player 13 at left
            with dissolve
            mom "Thank you for all the help around the house."
            mom "I really appreciate it."
            show mom 1
            show player 14
            player_name "You're welcome, {b}[mom_name]{/b}."
            show player 13
            show mom 13
            mom "Oh, before you leave!"
            mom "Could you run upstairs and bring me my {b}lotion{/b}, please?"
            mom "My legs are feeling a bit dry."
            show mom 1
            show player 12
            player_name "Where is it upstairs?"
            show player 5
            show mom 13
            mom "Just look in the {b}drawer in my bedroom{/b}."
            mom "It should be in there."
            show mom 1
            show player 14
            player_name "Okay, I'll be right back!"
            hide player
            hide mom
            with dissolve
            show popup_mombedroom at truecenter with dissolve
            pause
            hide popup_mombedroom with dissolve
            $ M_mom.trigger(T_mom_cleaned_laundry)
            $ lock_ui()
        "You're busy.":

            show player 14
            player_name "Looks like you're busy."
            player_name "I'll come back later."
    $ M_mom.set("chores", False)
    $ callScreen(location_count)

label mom_lotion_fun:
    if M_mom.is_set("lotion fun"):
        if location_count == "Basement":
            scene home_basement_c
        elif location_count == "Kitchen":
            scene homekitchen_closeup
            if M_mom.is_set("sex available"):
                show mom 1 at right
                show player 485 at left
                with dissolve
                player_name "Here it is, {b}[mom_name]{/b}!"
                show player 484
                show mom 2
                mom "Thanks, Sweetie."
                mom "Let me just sit up on the counter so you don't have to bend over."
                show mom 183 with dissolve
                pause
                show mom 184 zorder 2
                show mom_robe 184f zorder 2
                with dissolve
                pause
                show mom 185
                show mom_robe 185j
                with dissolve
                pause
                hide player
                show player 487c zorder 1
                show player_arms 488 zorder 3
                with dissolve
                pause
                show player_arms 488b
                with dissolve
                pause
                show player_arms 488c_488d with dissolve
                show player 487g
                show mom 185b
                mom "Oh, that tickles!"
                show mom 185g
                mom "You like taking care of your Momma, don't you?"
                show mom 185f
                show player 487f
                player_name "Always!"
                show player 487g
                show player_arms 488c_488d_488e with dissolve
                pause
                show mom 185b
                mom "I'd say you're such a good boy..."
                mom "...But I know why you like to do this."
                show mom 185f
                show player 487
                player_name "..."
                show mom 185g
                mom "You just like the little show I give you..."
                show mom 185f
                show player 487g
                player_name "!!!"
                show mom 185g
                mom "You're little massage makes me so horny."
                show mom 185b
                show player 487d
                mom "Keep massaging and maybe you can help me with a little something else..."
                show mom 185f
                show player 487f
                player_name "Yes, ma'am!"
                show player 487g
                show mom_robe 185k
                show player_arms 488e_488f
                with dissolve
                pause
                show mom 185b
                mom "That feels really good. I'm like butter in your hands."
                hide player_arms
                show player 13 at Position (xoffset=-118)
                hide mom_robe
                show mom 189
                with dissolve
                mom "Even my clothes want to slip off it seems."
                show mom 188
                show player 26 at Position (xoffset=-118)
                player_name "And when did your panties come off?"
                show player 13 at Position (xoffset=-118)
                show mom 189
                mom "{b}*Giggle*{/b}"
                show mom 187
                mom "I wondered if you'd notice."
                show mom 189
                mom "Well then, are you up for trying something else?"
                show mom 188
                show player 14 at Position (xoffset=-118)
                player_name "Of course!"
                show player 110f at Position (xoffset=-118)
                show mom 191
                show mom_robe 191b zorder 2
                with dissolve
                mom "Then be a good young man and use your fingers to make me cum..."
                show mom 190
                show player 26 at Position (xoffset=-119)
                player_name "Yes, {b}[mom_name]{/b}."
                show player finger 193b zorder 3
                show mom 192
                show mom_robe 194b
                with dissolve
                $ inventory.items.remove(lotion)
                $ M_mom.set("fetch lotion", False)
                $ M_mom.set("retrieved lotion", False)
                $ unlock_ui()
                pause
                $ M_mom.set("sex speed", .225)
                $ M_mom.set("sex flip", False)
                $ M_mom.set("robe on", True)
                $ first_pass = True
                jump mom_finger_loop
        show mom 1 at right
        show player 485 at left
        with dissolve
        player_name "Got it!"
        show player 484
        show mom 2
        mom "Great! One sec."
        show player 486
        show mom 183 with dissolve
        pause
        show mom 184b zorder 2
        show mom_robe 184e zorder 2
        with dissolve
        mom "Ready!"
        show player 484
        show mom 185
        show mom_robe 185h
        with dissolve
        pause
        hide player
        show player 487c zorder 1
        show player_arms 488 zorder 3
        with dissolve
        pause
        show player_arms 488b
        with dissolve
        show mom 185d
        mom "Oh! That's cold."
        show player 487d
        mom "Rub the lotion in your hands a bit before you apply it."
        show player 487c
        show mom 185
        show player_arms 488c_488d with dissolve
        show mom 185b
        mom "That feels good."
        show mom 185
        show player 487f
        show player_arms 488b with dissolve
        player_name "Good!"
        show player 487g
        show player_arms 488c_488d with dissolve
        pause
        show player 487f
        show player_arms 488 with dissolve
        player_name "Anywhere else?"
        show player 487g
        show mom 185c
        mom "Hmm?"
        show player 487e
        player_name "Did you want me any lotion anywhere else?"
        show player 487d
        show mom 185d
        mom "Oh..."
        show mom 185g
        mom "Umm... If you don't mind you could rub some a bit higher on my leg..."
        show mom 185f
        show player 487e
        player_name "O... Okay..."
        show player_arms 488b with dissolve
        show player 487c
        pause
        show player_arms 488c_488d_488e with dissolve
        show mom 185d
        mom "Mmm... Dig your hands in a bit deeper there."
        show player_arms 488e with dissolve
        mom "Feel that knot?"
        mom "Try and rub that out..."
        show mom 185c
        show player 487b
        player_name "O... Okay..."
        show player 487c
        show player_arms 488e_488f with dissolve
        pause
        show mom 185b
        mom "Mmm... That feels good."
        show mom 185
        show player 487f
        player_name "!!!"
        show player 487g
        player_name "( She's really relaxing now! )"
        player_name "( I wonder if she realizes I can see through her panties! )"
        show mom 185d
        mom "Oh, your fingers feel so good."
        mom "Have you been practicing?"
        show mom 185g
        mom "Some little lady is going to love how helpful and attentive you are."
        show mom 185d
        mom "Oh! Right there..."
        show mom 185f
        pause
        show mom_robe 185i with dissolve
        pause
        show mom 185e
        mom "!!!"
        hide player_arms
        show player 3 at Position (xpos=420)
        show xtra 21 zorder 2 at Position (xpos=289)
        hide mom_robe
        show mom 187
        with dissolve
        mom "...Um... Thank you, Sweetie..."
        show mom 186
        show player 29
        player_name "...You're welcome..."
        show player 3
        show mom 187
        mom "Listen, I should... um..."
        if location_count == "Basement":
            mom "I should probably finish this load... of laundry..."
            mom "Go on upstairs and... um..."
        elif location_count == "Kitchen":
            mom "I should probably finish the dishes..."
        show mom 186
        show player 29
        player_name "Yeah... I was just about done."
        show player 3
        show mom 187
        mom "Thanks... again, Sweetie."
        show mom 186
        show player 29
        player_name "You're welcome."

        if location_count == "Basement":
            $ location_count = "Living Room"
            scene home_livingroom_b with fade
        elif location_count == "Kitchen":
            $ location_count = "Entrance"
            scene home_entrance with fade
        show player 24 with dissolve
        player_name "Damn..."
        player_name "I think she noticed me looking..."
        show player 34
        pause
        show player 35
        player_name "Was she getting wet?"
        show player 43
        pause
        show player 81 with dissolve
        pause
        show player 83
        player_name "I better find something else to do."
    else:

        scene home_basement_c
        show mom 1 at right
        show player 485 at left
        with dissolve
        player_name "Here it is, {b}[mom_name]{/b}!"
        show player 484
        show mom 2
        mom "Thanks, Sweetie."
        show mom 8b
        mom "Ow!"
        show player 486
        pause
        show mom 11b
        mom "My back has been killing me lately."
        mom "It stinks getting old..."
        show mom 10b
        menu:
            "Help her.":
                show player 485
                player_name "Want me to help you?"
                show player 484
                show mom 13
                mom "Oh?"
                mom "You mean... with my lotion?"
                show mom 10b
                show player 485
                player_name "Well, yeah... If you want?"
                show player 484
                show mom 11b
                mom "You'd do that for your old mother?"
                show mom 10b
                show player 485
                player_name "You're not old {b}[mom_name]{/b}."
                player_name "But I can see you are in pain."
                player_name "Why dont you sit up and I can do the rest!"
                show player 484
                show mom 14
                mom "..."
                show mom 2
                mom "Well, that's... a very nice offer."
                mom "Thank you, Sweetie."
                mom "One sec."
                mom "Let me just sit up on this here..."
                show player 486
                show mom 183 with dissolve
                pause
                show mom 184 zorder 2
                show mom_robe 184e zorder 2
                with dissolve
                show player 485
                player_name "Where do you want lotion?"
                show player 484
                show mom 184b
                mom "Put a little near my ankle."
                show mom 184
                show player 485
                player_name "Okay."
                show player 484
                show mom 185
                show mom_robe 185h
                with dissolve
                pause
                hide player
                show player 487c zorder 1
                show player_arms 488 zorder 3
                with dissolve
                pause
                show player_arms 488b
                with dissolve
                player_name "!!!"
                show mom 185c
                show player 487b
                player_name "Oops!"
                show player 487d
                show mom 185b
                mom "Oh, Sweetie..."
                show mom 185d
                mom "That's a bit too much lotion."
                show mom 185
                show player 487b
                player_name "Sorry, {b}[mom_name]{/b}."
                show player 487c
                show player_arms 488c_488d with dissolve
                show player 487
                show mom 185d
                mom "That feels good."
                show mom 185
                show player 487c
                show player_arms 488b with dissolve
                player_name "..."
                show player_arms 488c_488d with dissolve
                pause
                show player_arms 488 with dissolve
                show player 487e
                player_name "I rubbed in most of the lotion."
                player_name "What do you want me to do with the rest?"
                show player 487d
                show mom 185b
                mom "I suppose you could put some a bit higher on my leg."
                show mom 185
                show player 487b
                player_name "Alright..."
                show player 487c
                show player_arms 488b with dissolve
                pause
                show player_arms 488c_488d_488e with dissolve
                pause
                show mom 185d
                mom "Mmm... Dig your hands in a bit deeper there."
                show player_arms 488e with dissolve
                mom "Feel that knot?"
                mom "Try and rub that out..."
                show mom 185c
                show player 487b
                player_name "O... Okay..."
                show player 487c
                show player_arms 488e_488f with dissolve
                pause
                show mom 185b
                mom "Mmm... That feels good."
                show mom 185
                show player 487f
                player_name "!!!"
                show player 487g
                player_name "( She's really relaxing now! )"
                player_name "( I wonder if she realizes I can see through her panties! )"
                show mom 185d
                mom "Oh, your fingers feel so good."
                mom "Have you been practicing?"
                show mom 185g
                mom "Some little lady is going to love how helpful and attentive you are."
                show mom 185d
                mom "Oh! Right there..."
                show mom 185f
                pause
                show mom_robe 185i with dissolve
                pause
                show mom 185e
                mom "!!!"
                hide player_arms
                show player 3 at Position (xpos=420)
                show xtra 21 zorder 2 at Position (xpos=289)
                hide mom_robe
                show mom 187
                with dissolve
                mom "...Um... Thank you, Sweetie..."
                show mom 186
                show player 29
                player_name "...You're welcome..."
                show player 3
                show mom 187
                mom "Listen, I should... um..."
                mom "I should probably finish this load... of laundry..."
                mom "Go on upstairs and... um..."
                show mom 186
                show player 29
                player_name "Yeah... I was just about done."
                show player 3
                show mom 187
                mom "Thanks... again, Sweetie."
                show mom 186
                show player 29
                player_name "You're welcome."
                scene home_livingroom_b with fade
                $ location_count = "Living Room"
                show player 24 with dissolve
                player_name "Damn..."
                player_name "I think she noticed me looking..."
                show player 34
                pause
                show player 35
                player_name "Was she getting wet?"
                show player 43
                pause
                show player 81 with dissolve
                pause
                show player 83
                player_name "I better find something else to do."
                $ M_mom.set("lotion fun", True)
            "Leave.":

                show player 485
                player_name "Anything else, {b}[mom_name]{/b}?"
                show player 484
                show mom 11b
                mom "No, that will do it."
                mom "Thanks, Sweetie."
                show mom 10b
                show player 485
                player_name "You're welcome, {b}[mom_name]{/b}."
        $ M_mom.trigger(T_mom_lotion_applied)
    hide player
    hide mom
    with dissolve
    $ inventory.items.remove(lotion)
    $ M_mom.set("fetch lotion", False)
    $ M_mom.set("retrieved lotion", False)
    $ gTimer.tick()
    $ unlock_ui()
    $ callScreen(location_count)

label basement_mom_faster_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') - 0.05)
    jump basement_mom_sex_loop

label basement_mom_slower_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') + 0.05)
    jump basement_mom_sex_loop