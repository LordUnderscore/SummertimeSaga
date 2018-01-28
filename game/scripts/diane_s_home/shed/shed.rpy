label shed:
    $ location_count = "Diane's Shed"
    if aunt_had_sex:
        if gTimer.is_dark():
            if quest12 in completed_quests and quest13 not in quest_list and aunt.started(aunt_breeding_help):
                scene shed_night with None
                show aunt 89 at right
                show player 11 at left
                dia "I have a {b}little request{/b} to ask of you."
                show aunt 88
                player_name "..."
                show player 21
                player_name "Sure! What can I do for you?"
                show aunt 87
                show player 13
                dia "I have, this... {b}Package{/b}, I'd like you to pickup for me."
                show aunt 88
                show player 10
                player_name "Oh, okay."
                player_name "Where is it?"
                show aunt 89
                show player 13
                dia "You'll have to pick it up at the {b}mall{/b}..."
                show aunt 90
                show player 11
                dia "...It's at a shop, called {b}Pink{/b}."
                dia "It should be under my name!"
                show aunt 88
                show player 29
                player_name "At the {b}Pink{/b} store?!"
                show player 21
                player_name "..."
                player_name "But, what is it?"
                show aunt 87
                show player 13
                dia "It's a little something for you... But it's a {b}surprise{/b}!"
                show aunt 88
                show player 11
                player_name "!!!"
                show player 21
                player_name "Really?"
                show player 108f
                player_name "The mall is closed right now, though..."
                show player 21
                player_name "I'll have to go tomorrow."
                show aunt 90
                show player 13
                dia "That's my good boy..."
                show aunt 89
                $ quest_list.append(quest13)
                $ aunt_breeding_help.status = True
    else:

        scene expression gTimer.image("shed{}")
        if pump not in inventory.items and quest08 not in completed_quests:
            show pump_object at Position(xpos = 118, ypos = 437)

        if shed_dialogue == 0:
            show player 35 at left with dissolve
            player_name "Woah..."
            show player 34
            player_name "...What a strange looking shed."
            player_name "What's up with all the containers... And those chains?!"
            show player 43
            player_name "Anyway, let's try and {b}find that pump{/b}..."
            $ shed_dialogue = 1
            hide player 43 with dissolve

        elif shed_dialogue == 1 and drink_milk_offer == True and aunt_shed_scene == False and gTimer.is_evening():
            scene shed_blur_night
            show aunt 57 at right with dissolve
            window hide
            pause
            show aunt 58 at right
            window hide
            pause
            show aunt 57 at right
            window hide
            pause
            show aunt 58 at right
            window hide
            pause
            show aunt 57 at right
            show player 11 at left with dissolve
            player_name "..."
            show player 23 at left
            player_name "{b}Aunt Diane{/b}!??"
            show aunt 59 at right with hpunch
            show player 22 at left
            dia "!!!"
            show aunt 60 at right
            dia "What are you doing here??!"
            show aunt 64 at right
            show player 29 at left
            player_name "I saw the door was open! And-"
            show player 3 at left
            player_name "..."
            show player 21 at left
            player_name "...Is that a {b}milk pump{/b}?"
            show aunt 61 at right
            show player 5 at left
            dia "{b}*Sigh*{/b}"
            show aunt 62 at right
            show player 11 at left
            dia "Yes, {b}[firstname]{/b}... I... like to milk myself sometimes..."
            show aunt 64 at right
            show player 12 at left
            player_name "Wait..."
            if drank_milk == True:
                player_name "Is that the milk you had me drink the other day?!"
            else:

                player_name "Is that the milk you gave me to drink the other day?!"
            show aunt 61 at right
            show player 11 at left
            dia "I know... I should have told you..."
            show aunt 60 at right
            show player 5 at left
            dia "But it's all natural, and I had no one else to try it with!!"
            show aunt 61 at right
            dia "I hope you can forgive me?"
            menu:
                "It's ok.":
                    show aunt 64 at right
                    show player 21 at left
                    player_name "It's fine, {b}Aunt Diane{/b}."
                    player_name "You don't have to be sorry..."
                    show aunt 63 at right
                    show player 17 at left
                    if drank_milk == True:
                        player_name "...I actually liked it!"
                    else:

                        player_name "...I'm glad you offered me some!"
                    show aunt 62 at right
                    show player 13 at left
                    dia "That's... very sweet of you to say..."
                    show aunt 63 at right
                    show player 29 at left
                    player_name "I... should go home now."
                    show aunt 62 at right
                    show player 3 at left
                    dia "Yeah, I'm going inside now..."
                    dia "And can you please-"
                    show aunt 64 at right
                    show player 21 at left
                    player_name "I won't tell {b}[mom_name]{/b}. Don't worry."
                    show aunt 63 at right
                    show player 13 at left
                    dia "Thanks."
                    hide player 13 at left with dissolve
                    hide aunt 63 at right with dissolve
                "No, it was wrong.":

                    show aunt 64 at right
                    show player 12 at left
                    player_name "I don't know, {b}Aunt Diane{/b}."
                    if drank_milk == True:
                        player_name "That was pretty wrong to make me drink that..."
                    else:

                        player_name "That was pretty wrong to offer me that..."
                    show aunt 61 at right
                    show player 90 at left
                    dia "I know..."
                    dia "I'm so sorry!"
                    show aunt 64 at right
                    show player 12 at left
                    player_name "I'm going {b}home{/b} now..."
                    show aunt 60 at right
                    show player 13 at left
                    dia "But-"
                    show aunt 64 at right
                    show player 24 at left
                    player_name "Bye..."
                    hide aunt 64 at right with dissolve
                    hide player 24 at left with dissolve
            $ aunt_shed_scene = True
    $ callScreen(location_count)

label locked_shed_dialogue:
    scene garden
    if seen_shed_locked == True:
        show player 34 with dissolve
        player_name "Hmm..."
        show player 35
        player_name "The door's locked."
        hide player 35 with dissolve
    else:

        show player 35 at left with dissolve
        player_name "Hmm.. The shed is locked. I wonder what's in there?"
        show aunt 8 at right with dissolve
        show player 22 at left
        dia "Are you snooping around?"
        show aunt 9 at right
        show player 10 at left
        player_name "Uhh, sorry. I was just looking for tools..."
        show aunt 10 at right
        show player 11 at left
        dia "It's okay. Perhaps one day I'll give you a little tour..."
        show player 21 at left
        show aunt 9 at right
        player_name "Sure, {b}Aunt Diane{/b}..."
        $ seen_shed_locked = True
        hide player 21 at left with dissolve
        hide aunt 9 at right with dissolve
    $ callScreen(location_count)

label aunt_dialogue_button_night:
    scene location_shed01_night_closeup
    show player 1 at left with dissolve
    show aunt 89 at right with dissolve
    dia "Hey there, Handsome."
    dia "Ready to learn how to milk?"
    show aunt 88
    show player 17
    player_name "Sure! I'd love to help!"
    show aunt 89
    show player 1
    dia "That's my good boy..."
    dia "Is there anything you want to talk about before we get started?"
    label dia_default_dialogue_options_night:
        menu:
            "Package." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show aunt 88
                show player 10
                player_name "I forgot where to pick up the {b}package{/b}."
                show player 29
                player_name "How do I find it again?"
                show aunt 89
                show player 13
                dia "You'll have to pick it up at the {b}mall{/b}."
                show aunt 87
                dia "It's at a shop called {b}Pink{/b}."
                show aunt 89
                dia "It should be under my name!"
                show aunt 88
                show player 21
                player_name "Oh. All right. gotcha!"
                show aunt 89
                show player 13
                dia "Is there anything else you want to talk about?"
                jump dia_default_dialogue_options_night

            "Package." if quest13 in quest_list and quest13 not in completed_quests and package in inventory.items:
                show player 239_240
                pause
                show aunt 88
                show player 170
                player_name "I have the {b}package{/b} you asked for!"
                show aunt 90
                show player 169
                dia "Excellent!"
                $ completed_quests.append(quest13)
                $ inventory.items.remove(package)
                show aunt 119
                show player 11
                dia "Now, stay right here..."
                dia "...I'll be right back with a surprise for you."
                scene black with dissolve
                $ renpy.pause(0.5)
                scene shed_night

                show aunt 113 at right
                show player 23 at left
                with dissolve
                player_name "!!!" with hpunch
                show aunt 114
                show player 22
                dia "So?"
                show aunt 115
                dia "...You like it?"
                show aunt 113
                show player 29
                player_name "That's... really sexy, {b}Aunt Diane{/b}."
                show aunt 114
                show player 13
                dia "I always wanted to wear this... I just never had anyone to wear it for..."
                show aunt 113
                show player 11
                player_name "..."
                show aunt 116
                show player 23
                dia "I like the way my breasts can hang naturally, like this..."
                show player 22
                player_name "..."
                show aunt 114
                dia "I figured it would help you get in the mood for... {b}milking{/b}..."
                show aunt 113
                show player 29
                player_name "Well, it's working! Haha..."
                show aunt 114
                show player 13
                dia "So... Uhm..."
                dia "What do you feel like doing, now?"
                jump dia_default_dialogue_options_night

            "Let's milk!" if quest12 not in completed_quests or quest13 not in completed_quests:
                show aunt 88
                show player 21
                player_name "I'm ready to start if you want."
                show aunt 87
                show player 11
                dia "Not just yet!"
                show aunt 89
                show player 13
                dia "You need to {b}take care of the few things{/b} I asked you about earlier, before we get started..."
                show aunt 88
                show player 21
                player_name "Oh, right!"
                show player 17
                player_name "My bad, I'll tend to those first..."
                show aunt 90
                show player 13
                dia "Don't worry. We'll be having fun, soon..."


            "Let's milk!" if quest12 in completed_quests and quest13 in completed_quests:
                if shed_had_sex == False:
                    show aunt 113
                    show player 17
                    player_name "Let's make some milk!"
                    show aunt 114
                    show player 2
                    dia "I was hoping you'd say that..."
                    show aunt 112
                    dia "But before we start, I have to prepare for the milk extraction!"
                    show aunt 113
                    show player 12
                    player_name "How do you do that?"
                    show aunt 117
                    show player 11
                    dia "With these!"
                    dia "I have to attach these suction pumps..."
                    player_name "!!!"
                    show aunt 113
                    show player 21
                    player_name "Do they... hurt?"
                    show aunt 115
                    show player 13
                    dia "Haha. Not really..."
                    show aunt 114
                    dia "It feels a bit strange when it pumps, but I kind of like it!"
                    show aunt 113
                    show player 21
                    player_name "Cool!"
                    show aunt 114
                    show player 11
                    dia "You know, they say that cows lactate more when they are... {b}Fertilized{/b}..."
                    show aunt 113
                    player_name "..."
                    show player 29
                    player_name "I... I don't understand-"
                    show aunt 112
                    show player 13
                    dia "I'm just saying... Pregnant cows produce a lot more milk!"
                    show player 11
                    show aunt 114
                    dia "I guess what I'm trying to say is... Your Aunt needs a bull to... {b}Breed{/b} her..."
                    show aunt 113
                    show player 23
                    player_name "!!!"
                    show aunt 114
                    show player 22
                    dia "...You think you could help your {b}Auntie{/b} with that?"
                    show aunt 113
                    show player 29
                    player_name "...Yeah, I... I'd like to help you..."
                    show aunt 114
                    show player 13
                    dia "That's my good boy!"
                    show player 11
                else:

                    show aunt 113
                    show player 17
                    player_name "Let's make some milk!"
                    show aunt 114
                    show player 2
                    dia "I was hoping you'd say that..."
                    dia "I couldn't wait for you to come back!"
                    show aunt 112
                    show player 11
                    dia "But before we start, Let me get into character!"

                    show player 11
                    show aunt 116
                    dia "How do I look?"
                    show player 21
                    player_name "You're beautiful, {b}Aunt Diane{/b}!"
                    show player 13
                    show aunt 112
                    dia "Now, when you mount me on the chair..."
                    dia "Make sure you cum {b}deep{/b} inside me...."
                    show player 11
                    show aunt 113
                    player_name "!!!"
                    show player 23
                    show aunt 114
                    dia "I need my bull to.... {b}breed{/b} me good..."
                    show aunt 112
                    show player 22
                    dia "...You think you could help your {b}Auntie{/b} with that?"
                    show aunt 113
                    show player 29
                    player_name "...Yeah, I... I can do that for you..."
                    show aunt 115
                    show player 13
                    dia "That's my good boy!"
                    show player 11
                    show aunt 114
                dia "Let's get set up on the {b}breeding chair{/b}..."
                scene shed_closeup 1
                show auntsex 36 at Position (xpos = 571, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_37.png" at Position (xpos = 528, ypos = 769)
                with dissolve
                dia "Now just slide it in nice and slow..."
                dia "...And don't let go until you finish {b}deep{/b} inside..."

                hide expression "characters/aunt/char_aunt_sex_37.png"
                show auntsex 38 at Position (xpos = 544, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_39.png" at Position (xpos = 552, ypos = 769)
                dia "That's it..."
                hide expression "characters/aunt/char_aunt_sex_39.png"
                show auntsex 40 at Position (xpos = 547, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_41.png" at Position (xpos = 549, ypos = 769)
                dia "{b}*Moan*{/b}"
                hide expression "characters/aunt/char_aunt_sex_41.png"
                $ anim_toggle = False
                $ shed_xray_toggle = False
                $ shed_cow_outfit = True
                $ shed_sex_angle = 0
                $ M_aunt.set('sex speed', .4)

                label shed_sex_loop:
                    scene shed_closeup 1

                    if anim_toggle == True:
                        hide auntsex_cowoutfit
                        hide auntsex_xray
                        hide auntsex_cowoutfit_xray
                        hide auntsex
                        hide screen shed_sex_visuals

                        if shed_sex_angle == 0:
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)
                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                            else:
                                show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                        else:

                            scene shed_closeup 2
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                            else:
                                show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                    else:

                        $ xray = 0
                        $ cow_outfit = 0
                        if shed_sex_angle == 0:
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                        else:

                            scene shed_closeup 2
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                        show screen shed_sex_visuals

                    show screen shed_sex_buttons
                    hide screen shed_sex_options
                    pause
                    if shed_sex_angle == 0:
                        scene shed_closeup 1
                        if anim_toggle == True:
                            hide auntsex_cowoutfit
                            hide auntsex_xray
                            hide auntsex_cowoutfit_xray
                            hide auntsex
                            hide screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)

                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)

                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                            else:

                                show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                            pause 8
                        else:

                            show screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                    else:

                        scene shed_closeup 2
                        if anim_toggle == True:
                            hide auntsex_cowoutfit
                            hide auntsex_xray
                            hide auntsex_cowoutfit_xray
                            hide auntsex
                            hide screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)

                            elif shed_cow_outfit == False and shed_xray_toggle == True:

                                show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:

                                show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                            else:
                                show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                            pause 8
                        else:

                            show screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                    call screen shed_sex_options

                label shed_ride:
                    $ shed_xray_toggle = False
                    hide screen shed_sex_visuals
                    scene shed_closeup 3
                    show auntsex 54
                    player_name "You're so wet, Aunt Diane."
                    dia "I just love the feeling of my clit against your hard cock, Sweetie."
                    dia "Stay still..."

                    label shed_ride_loop:
                        show screen shed_sex_buttons
                        hide screen shed_sex_options
                        pause
                        hide screen shed_sex_buttons
                        if anim_toggle == True:
                            show auntsex 54_55
                            pause 8.4
                        else:

                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                        call screen shed_sex_options

                label shed_fuck:
                    show auntsex 56
                    dia "I want it inside me now..."
                    label shed_fuck_loop:
                        show screen shed_sex_buttons
                        hide screen shed_sex_options
                        pause
                        hide screen shed_sex_buttons
                        if anim_toggle == True:
                            show auntsex 58_59_58_57
                            pause 8.5
                        else:

                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                        call screen shed_sex_options

                label shed_milk:

                    if anim_toggle == True:
                        show auntsex 61_60
                    else:
                        show auntsex 60 at Position(xoffset = -45)
                    show screen shed_sex_buttons
                    hide screen shed_sex_options
                    pause
                    hide screen shed_sex_buttons
                    if anim_toggle == True:
                        show auntsex 61_60
                        pause 8
                    else:

                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                    pause .3
                    show auntsex 62 at Position(xoffset = -45)
                    player_name "Woa..."
                    player_name "It squirted so much!"
                    dia "{b}*Panting*{/b}"
                    dia "You milked me..."
                    call screen shed_sex_options

                label shed_sex_cum_in:
                    dia "Don't hold back..."
                    hide auntsex_cowoutfit
                    hide auntsex_xray
                    hide auntsex_cowoutfit_xray
                    hide screen shed_sex_options
                    label shed_sex_loop_2:
                        $ xray = 0
                        $ cow_outfit = 0
                        if shed_sex_angle == 0:
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                        else:

                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                        show screen shed_sex_visuals
                        show screen shed_sex_buttons
                        pause
                        if shed_sex_angle == 0:
                            scene shed_closeup 1
                            if anim_toggle == True:
                                hide auntsex 38
                                hide screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                if shed_cow_outfit == True and shed_xray_toggle == False:
                                    show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)

                                elif shed_cow_outfit == False and shed_xray_toggle == True:
                                    show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)

                                elif shed_cow_outfit == True and shed_xray_toggle == True:
                                    show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                                else:

                                    show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                                pause 8
                                hide auntsex_cowoutfit 39_41
                                hide auntsex_xray 42_43
                                hide auntsex_cowoutfit_xray 39_41_42_43
                                hide auntsex 38_40
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                            else:

                                show screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                        else:

                            scene shed_closeup 2
                            if anim_toggle == True:
                                hide auntsex 50
                                hide screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                if shed_cow_outfit == True and shed_xray_toggle == False:
                                    show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)

                                elif shed_cow_outfit == False and shed_xray_toggle == True:
                                    show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)

                                elif shed_cow_outfit == True and shed_xray_toggle == True:
                                    show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                                else:

                                    show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                                pause 8
                                hide auntsex_cowoutfit 51_53
                                hide auntsex_xray 46_47
                                hide auntsex_cowoutfit_xray 51_53_46_47
                                hide auntsex 50_52
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                            else:

                                show screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                        show screen shed_sex_visuals
                        $ shed_sex_count += 1
                    if shed_sex_count == 1:
                        hide screen shed_sex_buttons
                        dia "Cum deep inside me..."
                        jump shed_sex_loop_2

                    elif shed_sex_count == 2:
                        hide screen shed_sex_buttons
                        dia "Breed me!!!"
                        jump shed_sex_loop_2

                    elif shed_sex_count == 3:
                        $ shed_sex_count = 0
                        $ xray = 1
                        $ cow_outfit = 1
                        if shed_sex_angle == 0:
                            scene shed_closeup 1
                            show auntsex 40 at Position (xpos = 547, ypos = 729)
                            show screen shed_sex_visuals
                        else:
                            scene shed_closeup 2
                            show auntsex 52 at Position (xpos = 595, ypos = 768)
                            show screen shed_sex_visuals
                        $ shed_cum = True
                        dia "{b}AAaaahh!!{/b}"
                        hide screen shed_sex_visuals
                        jump shed_sex_end

                label shed_sex_end:


                    if shed_sex_angle == 0:
                        show auntsex 36 at Position (xpos = 571, ypos = 729)
                        show expression "characters/player/char_player_sex_45.png" at Position (xpos = 725, ypos = 264)
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_37.png" at Position (xpos = 528, ypos = 769)
                    else:

                        show auntsex 48
                        show expression "characters/player/char_player_sex_49.png" at Position(xpos = 567, ypos = 495)
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_49.png" at Position (xpos = 481, ypos = 766)
                        pause
                        hide expression "characters/player/char_player_sex_49.png"
                        hide expression "characters/aunt/char_aunt_sex_49.png"
                        show auntsex 46
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_47.png" at Position (xpos = 478, ypos = 766)
                        show expression "characters/player/char_player_sex_50.png" at Position(xpos = 598, ypos = 539)
                    dia "That was... So much cum..."
                    player_name "I did okay?"
                    dia "You bred me well."
                    dia "Thank you..."
                    scene shed_night
                    show player 1 at left
                    show aunt 89 at right
                    with dissolve
                    dia "Thank you so much for your help..."
                    show aunt 87
                    dia "Your {b}Aunt{/b} will have some of the finest milk in town!"
                    show player 2
                    show aunt 88
                    player_name "I really enjoyed this. I hope I can help you again soon!"
                    show player 1
                    show aunt 89
                    dia "I plan on expanding my milk business, so..."
                    show aunt 90
                    dia "There's plenty of work to be done around here!"
                    show aunt 89
                    dia "I can always use a hand..."
                    show player 17
                    show aunt 88
                    player_name "That would be amazing!"
                    show player 1
                    show aunt 89
                    dia "It's getting late. You should probably get going..."
                    show aunt 92
                    dia "You don't want to keep your mom waiting!"
                    show player 21
                    show aunt 91
                    player_name "Yeah."
                    show player 13
                    show aunt 87
                    dia "Remember: We have to keep this our little secret."
                    show player 21
                    show aunt 88
                    player_name "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone."
                    show player 13
                    show aunt 90
                    dia "That's my handsome boy!"
                    show aunt 111 at left
                    dia "We're gonna have a lot of {b}fun{/b} together..."
                    hide aunt 111 at left
                    $ shed_cum = False
                    $ shed_had_sex = True
                    $ gTimer.tick()
                    $ in_garden = True
                    hide shed
                    jump garden_dialogue
            "I should go.":

                show aunt 88 at right
                show player 10 at left
                player_name "I'd love to stay here and milk with you..."
                show aunt 91
                player_name "But It's getting late and {b}[mom_name]'s{/b} gonna be worried."
                show aunt 92
                show player 5
                dia "That's too bad."
                dia "I was looking forward to getting help with my milk..."
                show aunt 91
                show player 10
                player_name "I'm sorry... Maybe another night?"
                show aunt 87
                show player 13
                dia "Sure... You know where to find me."
                show aunt 88
                show player 21
                player_name "Okay!"
                hide aunt 88 at right with dissolve
                hide player 21 at left with dissolve
    $ callScreen(location_count)

label aunt_shed_faster_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') - 0.1)
    if shed_sex_action == 0:
        jump shed_sex_loop
    if shed_sex_action == 1:
        jump shed_ride_loop
    if shed_sex_action == 2:
        jump shed_fuck_loop
    if shed_sex_action == 3:
        jump shed_milk

label aunt_shed_slower_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') + 0.1)
    if shed_sex_action == 0:
        jump shed_sex_loop
    if shed_sex_action == 1:
        jump shed_ride_loop
    if shed_sex_action == 2:
        jump shed_fuck_loop
    if shed_sex_action == 3:
        jump shed_milk