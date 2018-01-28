label home_basement_dialogue:
    $ location_count = "Basement"
    if player.in_progress(lawn_mowed):
        scene home_basement_sideview
        show player 324 at Position(xpos=860)
        show mom 136 at Position(xpos=550)
        mom "Oh my goodness!!"
        show mom 137
        mom "{b}*Giggle*{/b}"
        show player 325
        show mom 135
        player_name "What is it, {b}Mom{/b}?"
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
        player_name "It's okay, {b}Mom{/b}. I can do it myself."
        show player 324
        show mom 136
        mom "Oh, come on! I was just about to turn the washer machine on."
        show mom 135
        show player 327 at Position(xoffset=-27) with fastdissolve
        pause
        scene home_basement_cutscene with fade
        show text "That was the first time I had ever undressed in front of {b}Mom{/b}. \nI was a bit shy, but she was surprisingly fine with it. \nShe bent over to add them to the laundry... revealing herself to me.\nI wanted to look away, but couldn't... I was aroused by it." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
        scene home_basement_sideview
        show player 330 at Position(xpos=860)
        show mom 142 at Position(xpos=550)
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
        player_name "Oh, no, it's fine, {b}Mom{/b}..."
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
        mom "Better cover you up, dear!"
        show mom 141 with fastdissolve
        pause
        show player 339 at Position(xpos=845)
        show mom 142
        with fastdissolve
        pause
        show player 341
        player_name "I'm so sorry, {b}Mom{/b}!"
        show player 340
        show mom 143
        mom "Oh, that's alright, Sweetie."
        mom "These things happen."
        mom "It's perfectly normal!"
        show mom 142
        mom "( Oh my... )"
        mom "( That's definitely something I have NOT seen before... )"
        mom "( ... I had no idea it was so BIG! )"
        show player 341
        player_name "Uhh, {b}Mom{/b}? Are you okay?"
        show player 340
        show mom 136
        mom "...Oh! Of course, Sweetie!"
        mom "Let's get you upstairs, so you can change!"
        show mom 135
        show player 341
        player_name "Okay..."
        $ player.complete_events(lawn_mowed)
        $ completed_quests.append(quest14)
        $ mom_dialogue_advance = True
        $ gTimer.tick()
        $ ui_lock_count = 0

    elif mom_count == 12 and not mom_dialogue_advance and fetched_laundry:
        scene home_basement_c
        show mom 125 at right
        show player 277 at left
        with dissolve
        player_name "Hey, {b}Mom{/b}!"
        show player 276
        player_name "Here's the laundry you asked for."
        show player 275
        show mom 60
        mom "Sweetie, I..."
        show player 276
        show mom 125
        player_name "What is it, {b}Mom{/b}?"
        show player 275
        show mom 60
        mom "I don't need help with the laundry."
        mom "You can put the basket down."
        show player 5
        show mom 125
        with dissolve
        player_name "..."
        show mom 60
        mom "I wanted to talk to you about something..."
        show player 297
        show mom 125
        player_name "...Yeah?"
        show player 13
        show mom 60
        mom "You've been taking care of us since... since your dad left us..."
        show player 297
        show mom 125
        player_name "I like helping you."
        show player 13
        show mom 39
        mom "I know."
        mom "And... We've also been getting a lot... closer."
        show player 297
        show mom 125
        player_name "I guess so..."
        show player 13
        show mom 60
        mom "I just want you to know that I don't mind it."
        mom "I've been quite enjoying it, actually."
        show player 297
        show mom 125
        player_name "Really?"
        show player 13
        show mom 60
        mom "I realized that I missed having someone close to me."
        mom "Someone who can hold me... touch me..."
        show player 297
        show mom 125
        player_name "I like doing that with you."
        show player 13
        show mom 60
        mom "I know."
        show mom 125
        mom "I like feeling your hands touching me..."
        show mom 63
        show player 11
        mom "Would you like to feel me more intimately?"
        show mom 125
        player_name "..."
        show player 297
        player_name "You mean... a hug?"
        show mom 63
        show player 13
        mom "No, Sweetie..."
        mom "I want to feel you {b}closer{/b}."
        mom "{b}Inside{/b} me."
        show mom 125
        show player 11 with vpunch
        player_name "!!!"
        show mom 63
        mom "Would you... want that?"
        show player 297
        show mom 125
        player_name "Yes, {b}Mom{/b}."
        player_name "I've always wanted to..."
        player_name "...I think about it, all the time."
        show player 13
        show mom 63
        mom "Then take off your clothes."
        show player 11
        show mom 125
        player_name "!!!"
        show player 297
        player_name "We're doing it down here?!"
        show player 13
        show mom 63
        mom "{b}[sis]{/b} won't find us down here."
        show player 21
        show mom 125
        player_name "Well... okay."

        label basement_mom_sex:
            $ M_mom.set('sex speed', .4)
            $ location_count = "Basement"
            $ cum = False
            $ anim_toggle = False
            $ xray = False
            scene home_basement_sex_01
            show player 270 zorder 1 at Position(xpos=466,ypos=768)
            show mom 107 zorder 0 at Position(xpos=200)
            with fade
            pause
            show player 271 at Position(xpos=655,ypos=768)
            pause
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
            mom "Like what you see?"
            show mom 114
            player_name "You're beautiful, {b}Mom{/b}."
            show mom 115
            mom "Just sit back and relax, Sweetie."
            mom "Let's start nice and slow..."
            hide player
            hide mom
            show moms 124 at Position(xpos=650)
            with dissolve
            pause
            show moms 125 at Position(xpos=655)
            pause
            show moms 126 with dissolve
            mom "Ahh..."
            player_name "!!!"
            player_name "It's so warm..."
            show moms 127 at Position(xpos=655)
            pause

            label basement_mom_sex_loop:
                hide screen basement_mom_sex_options
                show screen xray_scr
                pause
                if anim_toggle == True:
                    $ animcounter = 0
                    while animcounter < 4:
                        hide screen xray_scr
                        show moms 126_127_128 at Position(xpos=655)
                        pause 4
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
                        hide screen xray_scr
                        show moms 126
                        pause
                        show moms 127
                        pause
                        show moms 128
                        pause
                        $ animcounter += 1
                        if animcounter == 2:
                            mom "Ahhhh!!!"

                        if animcounter == 3:
                            mom "Oh, Sweetie!!!"
                            player_name "Uhhh..."

                show screen basement_mom_sex_options
                pause
                jump basement_mom_sex_loop

            label basement_mom_sex_cum:
                hide screen basement_mom_sex_options
                player_name "{b}Mom{/b}!!!"
                show white
                show moms 129 at Position(xpos=609) with vpunch
                hide white with dissolve
                mom "Ahh!!!"
                jump basement_mom_sex_after

            label basement_mom_sex_after:
                show moms 130 at Position(xpos=650) with fade
                mom "You should warn me when you're about to do it, Sweetie."
                show moms 131
                player_name "Sorry, {b}Mom{/b}."
                player_name "I just couldn't help it..."
                player_name "It felt too good..."
                show moms 132
                mom "It's okay. Let's get you cleaned up..."
                if mom_count == 12 and not mom_dialogue_advance:
                    jump basement_confession_kiss
                $ gTimer.tick()
    $ callScreen(location_count)

label basement_confession_kiss:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show mom 73 at Position(xpos=650)
    with fade
    mom "Sweetie..."
    mom "I want you to tell me if you don't want to do this anymore, okay?"
    show player 228
    show mom 76
    player_name "No, it's fine, {b}Mom{/b}..."
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
    player_name "I love you {b}Mom{/b}!"
    show player 227
    show mom 75
    mom "I love you too, Sweetie..."
    scene home_basement
    hide mom
    hide player
    with fade
    $ ui_lock_count = 0
    $ gTimer.tick()
    $ mom_basement_sex = True
    $ mom_dialogue_advance = True
    $ callScreen(location_count)

label broken_pipe:
    scene expression gTimer.image("home_basement")
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed
    $ closed_valve = 2
    scene home_basement_c
    show player 1
    with dissolve
    player_name "Okay, the valve's shut."
    player_name "I should go back to the {b}bathroom{/b} to see if I can fix the {b}sink{/b}."
    scene home_basement
    hide player
    with dissolve
    $ callScreen(location_count)

label laundry_dialogue:
    $ location_count = "Basement"
    scene home_basement_c with None
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
            player_name "{b}Mom{/b}, hand me the basket. I'll do the laundry."
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
            player_name "Will do, {b}Mom{/b}."
            show mom 63
            show player 275
            mom "Sweetie..."
            mom "Thanks for helping out lately."
            mom "It's making life a lot easier..."
            show mom 125
            show player 277
            player_name "No problem!"
            scene home_basement
            with dissolve
            scene help_mom_basement_cutscene with fade
            show text "Recently, I've been looking forward to helping {b}Mom{/b} around the house. \nI could tell she enjoyed it too, always hanging around and asking me how things were going with girls at school... \nI feel like she's been so close to me lately... \nThe way she stands by me, touches me, and keeps staring at me all the time." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            $ mom_helped += 1
        "You're busy.":

            show player 14
            player_name "Looks like you're busy."
            player_name "I'll come back later."
            scene home_basement
            with dissolve
    if mom_helped >= 3:
        $ mom_dialogue_advance = True
    $ mom_vacuuming = False
    $ callScreen(location_count)

label basement_mom_faster_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') - 0.1)
    jump basement_mom_sex_loop

label basement_mom_slower_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') + 0.1)
    jump basement_mom_sex_loop