default seen_garage_locked = False
default shovel_taken = False
default stool_taken = False

label home_garage:
    $ location_count = "Garage"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")
    $ callScreen(location_count)

label shovel:
    scene expression gTimer.image("home_garage{}")
    show expression "boxes/popup_item_shovel1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_shovel1.png"
    jump home_garage

label stool:
    scene expression gTimer.image("home_garage{}")
    show expression "boxes/popup_item_stool1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_stool1.png"
    jump home_garage

label lawnmower_dialogue:
    $ location_count = "Garage"
    if M_mom.get_state() == S_mom_fill_mower and gas_can not in inventory.items:
        if not gTimer.is_dark():
            scene home_garage_closeup
            show player 428f at right
            player_name "( I haven’t used a lawn mower in years... do I even remember how to use one? )"
            player_name "( {b}Dad{/b} used to pull the cord and it would start. Let me try that. )"
            scene home_garage_closeup
            show player 197
            with dissolve
            $ renpy.pause()
            show player 200 at Position (xpos=566)
            $ renpy.pause()
            show player 197 at center
            scene home_garage
            show player 35f
            with dissolve
            player_name "( It must be out of gas. It barely started, so at least I know it’s running. )"
            show player 2f
            player_name "( Well it’s not going to start without gas. I should probably get some from {b}CONSUM-R{/b}. )"
        else:

            scene expression gTimer.image("home_garage{}")
            show player 35f with dissolve
            player_name "( Why would I use the lawn mower at night? I should return during the day... )"
            hide player 35 with dissolve

    elif M_mom.get_state() == S_mom_fill_mower and gas_can in inventory.items:
        if not gTimer.is_dark():
            scene home_garage_closeup
            show player 202 at Position (xpos=521) with dissolve
            player_name "( I finally have some gas for the mower. )"
            show player 201 at Position (xpos=509)
            player_name "( That should be enough. )"
            show player 196 at Position (xpos=521)
            player_name "Hope this works. I don’t know what else to do after this..."
            show player 197 at center
            $ renpy.pause()
            show player 200 at Position (xpos=566)
            $ renpy.pause()
            show player 197 at center
            $ renpy.pause()
            show player 200 at Position (xpos=566)
            $ renpy.pause()
            show player 199 at center
            player_name "Hmm... it's not working. I'll try pulling it a bit harder..."
            show player 200 at Position (xpos=566)
            $ renpy.pause()
            show player 198 at center
            player_name "It worked!"
            $ lock_ui()
            $ inventory.items.remove(gas_can)
            $ M_mom.trigger(T_mom_filled_mower)
            jump home_front
        else:

            scene expression gTimer.image("home_garage{}")
            show player 35 with dissolve
            player_name "( Why would I use the lawn mower at night? I should return during the day... )"
            hide player 35 with dissolve
    else:

        scene expression gTimer.image("home_garage{}")
        show player 35 with dissolve
        player_name "( Why would I use the lawn mower? The grass looks fine... )"
        hide player 35 with dissolve
    $ callScreen(location_count)

label car_dialogue:
    if M_mom.get_state() == S_mom_mall_outing:
        scene location_car_cutscene01 with fade
        show text "So we hopped in the car and made our way to the mall." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "I found that time passed quickly when I was with [mom_name]..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "... Her pleasant company and infectious smile never failed to brighten my mood." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text with dissolve
        jump mall_dialogue

    scene expression gTimer.image("home_garage{}")

    if M_mom.get_state() == S_mom_check_car:
        $ location_count = "Car Engine"
        show player 4 with dissolve
        player_name "( She's right. The car doesn't even try to start. )"
        show player 5
        player_name "( I'd better check the engine. )"
        if gTimer.is_dark():
            player_name "( It sure is dark in here. )"
        $ callScreen(location_count, False)
    else:

        if seen_garage_locked:
            show player 34 at left with dissolve
            player_name "Hmm..."
            show player 35
            player_name "I don't need to use {b}Mom's{/b} car."
            hide player 35 with dissolve
        else:

            show player 2 at left with dissolve
            player_name "{b}Mom's{/b} car ... wish I had a reason to drive it..."
            $ seen_garage_locked = True
            hide player 2 at left with dissolve
    $ callScreen(location_count)

label engine_broken_dialogue:
    scene expression gTimer.image("home_garage{}")
    show player 23 with dissolve
    player_name "!!!"
    show player 22
    player_name "The engine's a wreck! What happened?"
    pause
    show player 16
    player_name "( I wonder if this has something to do with those guys coming around the house... )"
    player_name "( It looks like someone hit it with a crowbar. )"
    show player 11
    player_name "( There's no way I can fix this. We have to get a whole new engine or something. )"
    player_name "( I should probably tell {b}Mom{/b} about this. She won't be happy! )"
    $ M_mom.trigger(T_mom_check_engine)
    jump home_garage

label car_sex:
    scene car_interior
    show player car 2d
    show player_arms car 1

    show mom car 4 at right
    show mom_arms car 5_5b_5c_5b
    show xtra 30 at right
    with dissolve
    if not M_mom.is_set("car sex"):
        pause
        show mom car 4b
        mom "You know."
        show mom car 5g
        mom "I always wanted to...pleasure...your father when we went for a drive."
        show player car 3
        mom "But he always shooed me away."
        mom "He said he didn't want to crash or something like that."
        mom "Your father was always so concerned for his family's safety."
        mom "He'd be proud to see you following in his footsteps..."
        show mom car 5f
        show player car 4g
        player_name "Do you think he'd be mad at me for..."
        show player car 5
        player_name "...You know..."
        show player car 5b
        show mom car 5c
        show mom_arms car 5

        mom "..."
        show mom car 5g
        mom "I... I don't think he'd be mad, Sweetie."
        mom "He'd appreciate knowing you've been taking care of things for us."
        mom "Besides, I'm the one who wanted to go further with our relationship, too."
        mom "You're a good son."
        mom "There's nothing to worry about."
        show mom car 5f
        show player car 4h
        player_name "..."
        show player car 5
        player_name "Thanks, {b}[mom_name]{/b}."
        show player car 5b
        show mom car 3b
        mom "Now. You want me to jerk you off, Sweetie?"
        mom "Or, would you like {b}Mommy{/b} to give you some road head?"
        show mom car 3
        show player car 2d
        $ M_mom.set("car sex", True)
    else:

        show mom car 4b
        show mom_arms car 5c
        mom "I like feeling this big guy stiffen up in my hand."
        show mom car 4
        pause
        show player car 4b
        show mom car 3b
        show mom_arms car 5 with dissolve
        mom "Young cocks sure do get hard."
        show mom car 4
        pause
        show player car 2d
        show mom car 5b with dissolve
        mom "My mouth is starting to water...along with something else."
        show mom car 3b
        mom "Want me to take you in my mouth?"
        show mom car 3
    $ M_mom.set("sex speed", .175)
    menu:
        "Jerk me off.":
            $ M_mom.set("car jerk", True)
            show player car 2c
            player_name "Keep using your hand."
            show player car 2d
            show mom car 3b
            mom "Alright, Sweetie."
            show mom car 4
            label car_mom_jerk_loop:
                show screen sex_anim_buttons
                pause
                if anim_toggle == True:
                    $ animcounter = 0
                    while animcounter < 4:
                        hide screen sex_anim_buttons

                        show mom_arms car 5_5b_5c_5b
                        pause 4
                        if randomizer() <= 50:
                            if animcounter == 3:
                                show mom car 4b
                                show player car 5b
                                mom "You've got such a big cock.{p=2}{nw}"
                                mom "I love how soft it feels.{p=2}{nw}"
                                show mom car 4
                        else:
                            if animcounter == 3:
                                show mom car 5b
                                show player car 5b
                                mom "Just let me know when your close, will you?{p=2}{nw}"
                                mom "I just cleaned out the car.{p=2}{nw}"
                                show player car 4b
                                pause 1
                                show mom car 4
                                show player car 4c
                                player_name "Okay...{p=2}{nw}"
                                show player car 4h

                        pause 3
                        $ animcounter += 1
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        hide screen sex_anim_buttons
                        show mom_arms car 5
                        pause
                        show mom_arms car 5b
                        pause
                        show mom_arms car 5c
                        pause
                        show mom_arms car 5b
                        pause
                        if randomizer() <= 50:
                            if animcounter == 3:
                                show mom car 4b
                                show player car 5b
                                mom "You've got such a big cock."
                                mom "I love how soft it feels."
                                show mom car 4
                        else:
                            if animcounter == 3:
                                show mom car 5b
                                show player car 5b
                                mom "Just let me know when your close, will you?"
                                mom "I just cleaned out the car."
                                show player car 4b
                                pause 1
                                show mom car 4
                                show player car 4c
                                player_name "Okay..."
                                show player car 4h
                        $ animcounter += 1

                call screen car_mom_sex_options

            label car_mom_jerk_cum:
                show player car 4c
                pause
                show player car 4d
                show player_arms car 2
                show mom_arms car 5d
                with dissolve
                player_name "!!!"
                show mom car 4b
                mom "Woah!!!"
                show mom car 5b
                mom "Oh, Sweetie!"
                show player car 2b
                show player_arms car 1 with dissolve
                mom "I forget you always have so much in you!"
                show mom car 4b
                mom "At least it looks like you didn't get any on the car."
                show mom car 3
                show player car 2c
                player_name "That was great..."
                scene car_interior kiss
                show mom car 6 at right
                show player_boner car 1b
                show xtra 30 at right
                with dissolve
                pause
                scene car_interior
                show player car 2c
                show player_arms car 1
                show player_boner car 1b
                show mom car 3 at right
                show mom_arms car 1
                show xtra 30 at right
                with dissolve
                player_name "Thanks, {b}[mom_name]{/b}."
                show player car 2d
                show mom car 3b
                mom "You're welcome, Sweetie."
                show mom car 4b
                mom "Let me know if you want to...play with me."
                show mom car 3b
                mom "There should be somewhere else we can hide from your sister."
        "Blowjob.":

            $ M_mom.set("car jerk", False)
            show player car 2c
            player_name "A blowjob sounds nice."
            show player car 2d
            show mom car 3b
            mom "I was hoping you'd want me to."
            scene car_interior bj
            show player car 4c
            show player_arms car 1
            show mom car bj 11 at right
            show xtra 30 at right
            with dissolve
            pause
            show mom car bj 12 with dissolve
            pause
            show mom car bj 7
            show player_boner car 3
            with dissolve
            pause
            show mom car bj 8 zorder 1 with dissolve
            pause
            show player car 4c
            label car_mom_bj_loop:
                show screen sex_anim_buttons
                pause
                if anim_toggle == True:
                    $ animcounter = 0
                    while animcounter < 4:
                        hide screen sex_anim_buttons
                        hide player_boner
                        show mom car bj 8_8b_8c_8d_8e_8f_8g
                        pause 4
                        if animcounter == 1:
                            mom "*Mmmm*{p=1}{nw}"
                        if animcounter == 3:
                            player_name "Oh...{p=1}{nw}"
                            show player car 4d
                            player_name "Right there, {b}[mom_name]{/b}.{p=2}{nw}"
                            show player car 4c
                        pause 3
                        $ animcounter += 1
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        hide screen sex_anim_buttons
                        show mom car bj 8
                        pause
                        show mom car bj 8b
                        pause
                        show mom car bj 8c
                        pause
                        show mom car bj 8d
                        pause
                        show mom car bj 8e
                        pause
                        show mom car bj 8f
                        pause
                        show mom car bj 8g
                        pause
                        if animcounter == 1:
                            mom "*Mmmm*"
                        if animcounter == 3:
                            player_name "Oh..."
                            show player car 4d
                            player_name "Right there, {b}[mom_name]{/b}."
                            show player car 4c
                        $ animcounter += 1
                call screen car_mom_sex_options

            label car_mom_bj_cum:
                show player_arms car 2
                show player car 4d
                player_name "{b}[mom_name]{/b}-"
                player_name "!!!"
                show mom car bj 9
                show player_arms car 2
                with flash
                mom "!!!"
                scene car_interior
                show player car 4d
                show player_arms car 1
                show player_boner car 2
                show mom car bj 10 at right
                show xtra 30 at right
                with dissolve
                pause
                show player car 2d
                mom "Dats a lawt oh cum..."
                mom "{b}*Gulp*{/b}"
                show mom car 2 at right
                hide mom_arms
                show mom_arms car 1
                hide xtra
                show xtra 30 at right
                with dissolve
                pause
                show mom car 3b
                mom "...You naughty boy!"
                mom "Give me a bit of a heads up next time!"
                show mom car 3
                show player car 2c
                player_name "Sorry...but that was awesome..."
                show player car 2d
                show mom car 3b
                mom "I could tell you liked it!"
                show mom car 3b
                mom "We better get back inside before your sister catches us out here."
                show mom car 3
                show player car 5
                player_name "Sounds good."
                player_name "Thanks-"
                show player car 3
                show mom car 3b
                mom "No, thank you, Sweetie."
                show player car 5b
                show mom car 4b
                mom "I love giving my man head."
        "Leave.":

            show player car 5
            player_name "I think I'm good for now."
            player_name "That felt good."
            show player car 5b
            show mom car 5g
            mom "Really?"
            mom "But you haven't even cum yet?"
            show mom car 5f
            show player car 2
            player_name "That's fine."
            show player car 5b
            show mom car 5g
            mom "Did I do something wrong?"
            show mom car 5f
            show player car 2c
            player_name "It was good {b}[mom_name]{/b}! Don't worry."
            player_name "I have to get going is all."
            show player car 5b
            mom "..."
            show mom car 5g
            mom "Alright..."
    hide player
    hide player_arms
    hide player_boner
    hide mom
    hide mom_arms
    hide xtra
    with dissolve
    $ location_count = "Garage"
    $ gTimer.tick()
    $ callScreen(location_count)

label car_mom_faster_bj:
    show player car 4c
    player_name "Faster, {b}[mom_name]{/b}."
    show player car 4h
    $ M_mom.set("sex speed", M_mom.get("sex speed") - 0.05)
    jump car_mom_bj_loop

label car_mom_slower_bj:
    show player car 4c
    player_name "Go slower..."
    show player car 4h
    $ M_mom.set("sex speed", M_mom.get("sex speed") + 0.05)
    jump car_mom_bj_loop

label car_mom_faster_jerk:
    show player car 4c
    player_name "Faster, {b}[mom_name]{/b}."
    show player car 4h
    $ M_mom.set("sex speed", M_mom.get("sex speed") - 0.05)
    jump car_mom_jerk_loop

label car_mom_slower_jerk:
    show player car 4c
    player_name "Go slower..."
    show player car 4h
    $ M_mom.set("sex speed", M_mom.get("sex speed") + 0.05)
    jump car_mom_jerk_loop