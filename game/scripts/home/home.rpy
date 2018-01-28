default player_mail = []

label home_front:
    $ location_count = "Home Front"
    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if gTimer.is_dark():
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    else:

        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    if M_mom.get_state() == S_mom_mrsj_visit and not gTimer.is_dark():
        scene home_front with None
        show mom 164f zorder 2 at left
        show erikmom 17 at right
        with dissolve
        if mom.name.lower() in ["mom", "mother",]:
            erimom "Hi!"
        else:
            erimom "Hey, {b}[mom]{/b}!"
        show mom 165f
        show erikmom 14
        mom "Oh, hello."
        show mom 164f
        show erikmom 17
        erimom "I wanted to stop by and give my condolences for your loss..."
        show mom 165f
        show erikmom 14
        mom "Oh, thank you. That's very... thoughtful of you."
        show mom 169f
        show erikmom 19
        erimom "I just want you to know that me and my son are right next door if you ever need something."
        erimom "Or if you just need someone to talk to."
        show mom 168f
        show erikmom 14
        mom "That's very generous."
        show mom 169f
        show erikmom 17
        erimom "I know this is a completely different situation for you, but I can relate, you know?"
        show mom 168f
        show erikmom 14
        mom "You mean, because of your husband?"
        show mom 169f
        show erikmom 17
        erimom "Of course!"
        show erikmom 20
        erimom "I mean, my husband left me... so its a bit different."
        show erikmom 18
        erimom "But I had to be on my own for a long time!"
        show mom 168f
        show erikmom 14
        mom "Don't you feel lonely?"
        mom "Is it tough with just you and your son at home?"
        show mom 169f
        show erikmom 20
        erimom "Yeah... {b}Erik{/b} was sad when I had to tell him his dad wasn't coming home..."
        show erikmom 17
        erimom "... but don't worry!"
        erimom "There's ways to cheer boys up, you know? I've got some tricks for that too..."
        show mom 168f
        show erikmom 14
        mom "Oh, yeah? Like what?"
        show mom 169f
        show erikmom 17
        erimom "Girls like to talk and get emotional attention, but boys..."
        show mom 169bf
        erimom "... you need to give them {b}physical{/b} attention!"
        show mom 169f
        erimom "You know... like hugs, cuddles and more motherly love!"
        show mom 168f
        show erikmom 14
        mom "I see..."
        show mom 169f
        show erikmom 18
        erimom "{b}Erik{/b} has been SO much better ever since I started catering to his... needs."
        show mom 168f
        show erikmom 14
        mom "I just don't know If I'm strong enough to get through all of this..."
        show mom 169f
        show erikmom 17
        erimom "Listen, honey. If I could do it, so can you."
        erimom "Focus on your children, that's what i did!"
        erimom "You have to think of what they want."
        show mom 168f
        show erikmom 14
        mom "I suppose you're right."
        show mom 169f
        pause
        show player 1 zorder 1 at Position(xpos=300) with dissolve
        show mom 165f
        mom "Oh! Hi, Sweetie!"
        show mom 164f
        show player 14
        player_name "Hey, {b}[mom_name]{/b}... Hi, {b}Mrs. Johnson{/b}!"
        show player 1
        show erikmom 17
        erimom "Hello, {b}[firstname]{/b}."
        erimom "Your mom was just telling me how much she cares about you..."
        show erikmom 14
        show player 14
        player_name "Oh, heh..."
        show erikmom 17
        show player 13
        erimom "She loves you very much, so you better take good care of her!"
        show erikmom 14
        show player 14
        player_name "Uhh... Of course."
        show player 1
        show erikmom 17
        erimom "..."
        erimom "Well, I'll let you two head back home..."
        show erikmom 14
        show mom 165f
        mom "You sure you don't want to come in?"
        show mom 164f
        show erikmom 17
        erimom "No, it's fine! I should really get home. {b}Erik{/b} needs help with... something."
        show erikmom 14
        show mom 165f
        mom "Well, in any case, thanks for the chat! Come back any time!"
        show mom 164f
        show erikmom 17
        erimom "Oh, I will honey! Hang in there..."
        $ M_mom.trigger(T_mom_mrsj_condolences)
        hide erikmom
        hide mom
        hide player
        with dissolve

    elif M_mom.get_state() == S_mom_mow_lawn:
        scene black
        with Pause(0.5)
        show cutting_grass_01 with dissolve
        show text "This is a lot harder than I expected. I should've paid more attention to dad when he used to do it." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show cutting_grass_02 with dissolve
        show text "It doesn't look half bad. I Hope {b}[mom_name]{/b} thinks the same." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        show cutting_grass_03 with dissolve
        show text "Huh, she's been standing there. I was so focused on cutting the grass, I didn't notice her come out." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        hide cutting_grass_01
        hide cutting_grass_02
        hide cutting_grass_03 with dissolve
        scene black with dissolve
        with Pause(0.5)

        scene home_front
        show player 2 at left
        show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
        show mom 1 at right
        with dissolve
        player_name "{b}Mom{/b}, I'm finished with the lawn."
        show player 203
        show mom 2
        mom "Wow! I don't know what to say, Sweetie!"
        show mom 3
        mom "The yard looks amazing!"
        show mom 2
        mom "You looked so grown up handling the lawnmower, too. It was really nice to see."
        show player 2
        show mom 1
        player_name "I was just doing it the way I thought dad would."
        show player 11
        show mom 2
        mom "And you did it as quickly and nicely as he used to."
        mom "You’ve gotten really strong, Sweetie."
        show player 21
        show mom 1
        player_name "I'm just glad I was able to do it. I want to be able to help you, [mom_name]."
        show player 2
        player_name "Should we go inside now?"
        show mom 1
        mom "Sure!"
        scene home_front with None
        show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
        show player 10 zorder 1
        with dissolve
        player_name "{b}*Panting*{/b}"
        show player 14
        player_name "Wow, that was a lot of work!"
        show player 24
        player_name "Man, I really got my clothes dirty..."
        show player 4 at Position(xoffset=5)
        player_name "I think {b}[mom_name]'s{/b} doing the laundry in the basement, maybe I can bring down my dirty clothes."
        hide player with dissolve
        $ M_mom.trigger(T_mom_mowed_lawn)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_car_fixed:
        scene expression gTimer.image("home_front_mechanic{}_b")
        show jai 2 at left
        show mom 1 at right
        with dissolve
        jaing "Everything should be good as new."
        show jai 1
        show mom 3
        mom "Really? That was fast!"
        show mom 1
        show jai 2
        jaing "You know."
        jaing "Every pretty woman I talk to says that."
        jaing "If it's acting funny give me a call."
        jaing "I enjoy making pretty little ladies engines purr."
        show jai 1
        show mom 3
        mom "Oh, stop. Your hilarious!"
        mom "Ha Ha Ha."
        show jai 2
        jaing "Huck Huck Huck."
        show jai 1
        show mom 1
        show player 14 zorder 1
        player_name "Hey, {b}[mom_name]{/b}."
        show player 13
        show mom 2
        mom "There he is!"
        show mom 1
        show player 10f with dissolve
        player_name "Fixed up?"
        show player 5f
        show jai 2
        jaing "Yup."
        jaing "Just needed some blinker fluid is all."
        show player 11f
        jaing "Huck Huck."
        jaing "Well, I better go."
        show player 5f
        jaing "I'm just going to take another quick look under your hood and make sure I didn't leave a tool in her."
        show jai 1
        show mom 2
        mom "Thanks again!"
        show mom 1
        show jai 2
        jaing "You're welcome."
        hide jai with dissolve
        show player 13 with dissolve
        show mom 2
        mom "Want to give it a test drive?"
        show mom 1
        show player 14
        player_name "Sure!"
        show player 12
        player_name "I hope he really didn't just try and screw you over."
        show player 5
        show mom 14
        mom "( He was trying... )"
        hide player
        hide mom
        with dissolve

        $ location_count = "Garage"
        scene car_interior
        show mom car 2b at right
        show player car 1b
        show player_arms car 1
        show mom_arms car 1
        show xtra 30 at right
        with dissolve
        mom "Let's see..."
        show player car 2b
        show mom car 1
        hide mom_arms
        with dissolve
        mom "Hmm..."
        show mom car 2b
        show mom_arms car 1
        with dissolve
        mom "It works!"
        show mom car 3
        show player car 2
        player_name "Great!"
        show player car 1
        show mom car 2
        player_name "Sounds good, too."
        show player car 2b
        show mom car 3b
        mom "How did you get them to agree to come out so quickly?"
        show mom car 3
        show player car 2
        player_name "It was nothing {b}[mom_name]{/b}."
        show player car 5
        player_name "I'm happy I could help you."
        player_name "I just like seeing you happy again..."
        show player car 6
        pause
        show player car 5b
        show mom car 3b
        show mom_arms car 2 with dissolve
        mom "Aww..."
        mom "Thanks, Sweetie."
        scene car_interior kiss
        hide player car
        hide mom_arms car
        hide player_arms car
        show mom car 6 at right
        show xtra 30 at right
        with dissolve
        pause
        show player_boner car 1 with dissolve
        pause
        scene car_interior
        show player car 3b
        show player_arms car 2
        show mom car 3 at right
        show mom_arms car 2
        show xtra 30 at right
        show player_boner car 1
        with dissolve
        pause
        show mom car 4c
        show mom_arms car 4 with dissolve
        mom "!!!"
        show mom car 5b
        mom "Oh!"
        show mom car 4c
        show player car 4c
        player_name "Sorry, {b}[mom_name]{/b}..."
        show player car 3
        show mom car 5b
        mom "Do..."
        mom "Do you always get excited like this?"
        show mom car 4b
        show mom_arms car 2 with dissolve
        mom "I mean... I've noticed you've been getting them quite a lot lately..."
        show mom car 3
        show player car 4c
        show player_arms car 1 with dissolve
        player_name "Well... only around... you..."
        show player car 3
        show mom car 4
        mom "..."
        show mom car 5b
        mom "Oh, Sweetie..."
        hide player_boner car
        show mom_arms car 5b
        with dissolve
        mom "I guess it's not such a bad thing."
        show mom car 5
        show player car 4c
        player_name "{b}[mom_name]{/b}?"
        show player car 3
        show mom car 3b
        mom "It's okay, Sweetie."
        show mom car 5b
        show mom_arms car 5 with dissolve
        mom "It's normal for young men your age to get... erections."
        show mom car 5
        show player car 3b
        player_name "{b}*Gulp*{/b}"
        show player car 3
        show mom_arms car 5_5b_5c_5b with dissolve
        pause 1.2
        show mom_arms car 5 with dissolve
        show mom car 5b
        mom "I shouldn't be the one taking care of these you know.."
        mom "But..."
        show mom_arms car 5_5b_5c_5b with dissolve
        show mom car 3b
        mom "...I don't mind helping you for the time being."
        mom "One day you'll have to find a nice girl to help you... Promise?."
        show mom car 3
        show mom_arms car 5c with dissolve
        show player car 5
        player_name "Y-Yeah. Of course, {b}[mom_name]{/b}."
        show player car 5b
        show mom car 3b
        mom "That's good."
        show mom_arms car 5 with dissolve
        mom "Do you want me to keep going?"
        show mom car 3
        $ M_mom.set("jerk count", 0)
        $ M_mom.set("sex speed", .3)
        menu:
            "A little longer.":
                show player car 5
                player_name "Can... Can you keep going a little longer?"
                show player car 2
                player_name "It feels really nice..."
                show player car 2b
                show mom car 3b
                mom "Okay, but not too long."
                show mom car 3
                label mom_car_jerk_loop:
                    show screen sex_anim_buttons
                    pause
                    hide screen sex_anim_buttons
                    if anim_toggle:
                        show mom_arms car 5_5b_5c_5b with dissolve
                        $ animcounter = 0
                        while animcounter < 4:
                            if animcounter == 1 or M_mom.get("jerk count") == 1:
                                show mom car 3
                            else:

                                show mom car 4
                                show player car 4b
                            pause 2

                            if M_mom.get("jerk count") >= 1 and animcounter == 3:
                                show player car 4c
                                pause 1

                            $ animcounter += 1
                    else:

                        $ animcounter = 0
                        while animcounter < 4:
                            show mom_arms car 5
                            pause
                            show mom_arms car 5b
                            pause
                            show mom_arms car 5c
                            pause
                            show mom_arms car 5b
                            pause
                            if animcounter == 1 or M_mom.get("jerk count") == 1:
                                show mom car 3
                            else:

                                show mom car 4
                                show player car 4b
                            pause

                            if M_mom.get("jerk count") >= 1 and animcounter == 3:
                                show player car 4c
                                pause

                            $ animcounter += 1

                    $ M_mom.set("jerk count", M_mom.get("jerk count") + 1)

                    if M_mom.get("jerk count") == 2:
                        jump car_mom_jerk_end
                    else:

                        call screen car_mom_jerk_options
            "Leave the car.":

                label car_mom_jerk_end:
                    if M_mom.get("jerk count") == 2:
                        show player car 3
                        show player_boner car 1
                        show mom_arms car 4
                        with dissolve
                        show mom car 5b
                        mom "I... I don't think I should keep doing this..."
                        show mom car 5
                        show mom_arms car 1 with dissolve
                        show player car 5
                        player_name "but, {b}[mom_name]{/b}-"
                        show player car 3
                    else:

                        show player car 4c
                        player_name "I don't know if we should stay in here too long."
                        show player car 4b
                        show mom car 5
                        mom "..."
                        show player_boner car 1
                        show mom_arms car 4
                        with dissolve
                        show mom car 5b
                        mom "You're right. we should probably go inside now."
                        show mom car 5
                        show mom_arms car 1 with dissolve
                        show player car 5
                        player_name "Yeah."
                        show player car 5b
                    show mom car 5b
                    mom "If you keep getting those you can take care of it in your room..."
                    show mom car 3b
                    mom "...Okay, Sweetie?"
                    show mom car 3
                    show player car 4c
                    player_name "...Yes... {b}[mom_name]{/b}."
                    scene black with fade
                    hide mom
                    hide mom_arms car
                    hide xtra
                    hide player
                    hide player_arms car
                    hide player_boner car
                    $ M_mom.trigger(T_mom_car_fun)
                    $ gTimer.tick()

    elif M_mom.get_state() == S_mom_bad_guys_revisit and not gTimer.is_dark():
        scene home_front_car
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        show player 11f at right with dissolve
        player_name "!!!"
        player_name "( It's that car again! )"
        player_name "( ... with that creep who's been threatening [mom_name]! )"
        hide player
        $ playSound()
        scene henchman_cs2 1
        with dissolve
        show text "I looked through the window, and saw the guy who'd been delivering the threats.\n It seems he brought a friend with him this time." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        scene henchman_cs2 2 with dissolve
        show text "I couldn't hear what they were saying, but {b}[mom_name]{/b} looked terrified." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        play audio smack
        scene henchman_cs2 3 with hpunch
        show text "Suddenly, one of them hit her, knocking her to the floor..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "There was no way I could just stand there and watch...\nI {b}had{/b} to do something!" at Position (xpos= 512, ypos = 700)
        pause
        scene home_entrance_fight
        show mom 40 at Position(xpos=156,ypos=768)
        show henchman2 1 at right
        with dissolve
        python:
            tmp = mom_name.upper()
        player_name "{b}[tmp]{/b}!!"
        show player 205 at Position(xpos=350,ypos=768) with dissolve
        player_name "Are you okay??"
        show player 204
        mom "Yes, I’m fine..."
        show player 205
        player_name "What are you guys doing in our house?!"
        show player 204
        show henchman2 2
        henchman2 "Step aside, kid. This doesn't concern you."
        show player 205
        show henchman2 1
        player_name "Back off! If you touch her again I'm going to-"
        show player 204
        show henchman2 3
        henchman2 "Hah, what are you gonna do, Kid?."
        show henchman2 1
        player_name "..."
        show player 205
        player_name "I'm calling the cops and you can deal with-"
        show player 204
        show henchman2 3
        hide mom with dissolve
        henchman2 "I don't think so."
        show henchman2 1
        hide player
        show henchman1 7 at Position(xpos=350,ypos=768) with hpunch
        player_name "Get off me!"
        show henchman1 8
        hide henchman2
        show henchman2 3 at right
        henchman2 "Easy, there Killer..."
        henchman2 "Your family owes us a {b}LOT{/b} of money..."
        henchman2 "...And we're still waiting to get paid!"
        show henchman2 2
        henchman2 "As for the police..."
        show henchman1 9
        show henchman2 5
        with hpunch
        mom "{b}[firstname]{/b}!!!"
        show henchman2 3
        show henchman1 10 at Position(xpos=340,ypos=768)
        henchman2 "Call them and we'll know..."
        show henchman2 2
        henchman2 "...long before they can do anything about it."
        henchman2 "If you care about your family, you'll {b}bring the money{/b} to the {b}Warehouse{/b}, like we told you!"
        show henchman2 4
        henchman2 "You don't want us comin' back here! {b}Got it{/b}, Lady?"
        show player 184
        show henchman1 6f at left
        show henchman2 2
        with vpunch
        henchman2 "C'mon, Let's get out of here."
        $ playMusic()
        hide henchman1
        hide henchman2
        with dissolve
        pause
        hide player
        show mom 41 at left
        with dissolve
        mom "Easy, Sweetie. I've got you."
        show mom 44 at left
        show sis 39 at right
        with dissolve
        sis "What the hell is going on?"
        sis "I heard screams and-"
        show sis 40 at Position(xpos=0.885, ypos=1.0) with dissolve
        sis "!!!"
        sis "Oh my god, Is he alright??"
        show mom 43
        show sis 43 at Position(xpos=1.0, ypos=1.0) with dissolve
        mom "Don't worry. It's nothing..."
        mom "They left..."
        show mom 44
        show sis 39
        sis "Shouldn't we call someone??"
        show sis 43
        show mom 43
        mom "No... We can't..."
        show mom 44
        show sis 39
        sis "What do you mean?"
        sis "We have to-"
        show sis 43
        show mom 45
        mom "NOT right now, {b}[sis]{/b}!"
        show mom 43
        mom "Just..."
        mom "Go upstairs. I'll deal with this."
        show mom 44
        show sis 39
        sis "I... Okay..."
        hide sis
        with dissolve
        show mom 41
        mom "Are you okay, Sweetie?"
        show mom 42
        player_name "Sorry. I couldn't stop them, {b}[mom_name]{/b}..."
        show mom 41
        mom "That's okay. You were very brave!"
        mom "You wanted to protect us."
        show mom 42
        player_name "What do we do?"
        show mom 41
        mom "Don't worry about that; we'll be okay."
        show mom 42
        mom "..."
        show mom 41
        mom "How's your face?"
        show mom 42
        player_name "My nose hurts..."
        player_name "...and I made a mess."
        show mom 41
        mom "Come on, let's get you cleaned up."
        hide mom with dissolve
        scene shower2
        show mom 39f at left
        show player 209f
        with dissolve
        mom "Looks like the bleeding stopped..."
        show mom 63f
        mom "You should take a shower, Sweetie."
        mom "It'll help with the swelling."
        show player 210
        mom "I'll go fetch you some clean clothes."
        show mom 38f
        hide mom
        hide player
        scene hallway
        show mom 38
        with fade
        mom "..."
        mom "( I feel like I should be in there with him... making sure he's okay. )"
        mom "( Maybe it's better that I give him some privacy... )"
        mom "( I'll just leave his clothes outside the door. )"
        pause
        show mom 125 with fastdissolve
        mom "( I can't believe he stood up to those men... for me. )"
        mom "( He's grown so quickly lately... )"
        mom "( ... In more ways than one. )"
        mom "( Hmm... )"
        mom "( Maybe I'll go in and check up on him. )"
        mom "( ... Just to make sure he doesn't need any help. )"
        scene shower_closeup
        show moms 26 zorder 2
        with fade
        player_name "Shit... So that's what getting punched in the face feels like..."
        show moms 27 with dissolve
        pause
        show moms_b zorder 1 at Position(xpos=350,ypos=768) with dissolve
        pause
        hide moms_b
        show moms 28 at Position(xpos=487,ypos=768)
        with dissolve
        pause
        show moms 29 at Position(xpos=492,ypos=768)
        player_name "Man... Is my nose supposed to be this soft?"
        show moms 31 at Position(xpos=484,ypos=768) with vpunch
        player_name "{b}[mom_name]{/b}??"
        player_name "Why are you-"
        show moms 30
        mom "Shhh, It's okay, Sweetie."
        mom "Let me help you..."
        show moms 34
        mom "You deserve it, after what you did back there."
        show moms 37_36
        pause 4
        show moms 34
        mom "Oh my, have you been working out?"
        show moms 35
        player_name "Yeah."
        show moms 34
        mom "I guess I just haven't noticed..."
        mom "You really are a man now..."
        show moms 36
        show moms 76 with dissolve
        show moms 41_76
        pause
        show moms 42 with hpunch
        with dissolve
        mom "Here Sweetie, let me help you."
        show moms 72
        player_name "Whoa!! {b}[mom_name]{/b}, are you sure?"
        show moms 43
        mom "Yes, it's okay. Just let Mommy take care of you..."
        show moms 44
        mom "You were so brave today, Sweetheart!"
        show moms 45 with dissolve
        mom "I was so proud of you..."
        show moms 74
        player_name "... Ohh, that feels really good, {b}[mom_name]{/b}!"
        show moms 73_74
        pause 4
        show moms 73
        player_name "{b}[mom_name]{/b}, I'm gonna..."
        show moms 46
        mom "It's okay, Sweetie, just let it go!"
        show moms 47 at Position(xpos=498,ypos=768)
        player_name "!!!"
        show white zorder 4 with dissolve
        show moms 47 at Position(xpos=498,ypos=768)
        show playersex 33 zorder 3 at Position(xpos=521,ypos=508)
        hide white with dissolve
        pause
        show moms 48
        hide playersex
        with dissolve
        mom "Wow, you had a lot in you..."
        show moms 44 at Position(xpos=484,ypos=768) with dissolve
        mom "There..."
        show moms 34 at Position(xpos=447,ypos=768) with dissolve
        mom "Doesn't that feel better?"
        show moms 35 at Position(xpos=447,ypos=768)
        player_name "Oooh, you have no idea..."
        player_name "... Thanks, {b}[mom_name]{/b}!"
        show moms 34
        mom "Now let's get you cleaned up."
        scene shower2
        with fade
        show player 261f at left with dissolve
        show mom 35b with dissolve
        pause
        show player 8 with dissolve
        show mom 35c with dissolve
        pause
        show player 21 with dissolve
        show mom 34 with dissolve
        with dissolve
        player_name "[mom_name], was this just a one time thing?"
        show player 1
        show mom 34
        mom "..."
        show mom 35
        mom "Oh, Sweetie... I don't know."
        show mom 34
        mom "..."
        show mom 35
        mom "I suppose, we can do it again."
        show mom 36
        mom "But you can't tell {b}ANYBODY{/b} and we can't take things too far!"
        show mom 34
        mom "..."
        show mom 36
        mom "And we {b}ABSOLUTELY CANNOT{/b} let your {b}Sister{/b} find out!"
        mom "Do you {b}understand{/b}?"
        show mom 34
        show player 21
        player_name "I understand, {b}[mom_name]{/b}."
        show mom 35
        show player 1
        mom "Alright..."
        mom "I have to go clean up the mess downstairs..."
        show mom 36
        mom "You wait a minute or two before coming out of the bathroom."
        mom "I don't want {b}[sis]{/b} to suspect anything. Alright?"
        show mom 32
        show player 28
        player_name "O-okay, {b}[mom_name]{/b}."
        show mom 33
        show player 1
        mom "That's my boy."
        hide mom with dissolve
        pause
        show player 21f at Position(xpos=0.4, ypos=1.0) with dissolve
        player_name "... Wow!"
        player_name "That was totally worth a punch in the face!"
        hide player
        with dissolve
        show popup_momshower at truecenter with dissolve
        $ M_mom.trigger(T_mom_bad_guys_beatup)
        pause
        hide popup_momshower with dissolve
        $ gTimer.tick()
        jump hallway_dialogue
    $ callScreen(location_count)

label player_mailbox:
    $ location_count = "Mailbox"
    $ callScreen(location_count, False)

label player_mailbox_dialogue:
    $ location_count = "Mailbox"
    scene expression gTimer.image("player_mailbox{}")

    if erik.completed(erik_orcette) and orcette not in inventory.items and not erik.known(erik_orcette_2) and orcette_mail_lock:
        player_name "( Sweet! It looks like I'm the first one to get the mail! )"
        menu:
            player_name "The package is addressed to me. This must be Erik's toy."
            "Leave it alone.":
                pause
            "Open it.":


                show mailbox_item04_c at truecenter
                with dissolve
                pause
                player_name "( So this is what he's been waiting for... )"
                player_name "( The {b}Orcette{/b}. )"
                player_name "( I better put this back in the box. )"

        show unlock38 at truecenter with dissolve
        $ inventory.items.append(orcette)
        $ player_mail = []
        pause
        hide unlock38
        hide mailbox_item04_c
        with dissolve
        player_name "( Time to get this to {b}Erik{/b} before someone catches me carrying this thing around. )"

    elif m_pizza_pamphlet in player_mail:
        player_name "( This is probably junk mail.)"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza? I haven't been to that place in a while. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True

    elif m_newspaper in player_mail:
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The thief is still on the loose? You'd think they would've caught him by now... )"
        player_name "( I better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
    $ callScreen(location_count, False)

label bad_guys_driveby:
    $ location_count = "Home Front"
    scene location_home_driveby_cutscene1
    with fade
    show text "Hmm, why is that car driving so slow?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Wait a second..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_home_driveby_cutscene2
    with fade
    show text "It's that strange man who was over here making threats the other day!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "What's his problem..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_home_front_blur
    show player 11
    player_name "..."
    show player 10
    player_name "I know {b}[mom_name]{/b} said not to worry about this..."
    player_name "But that guy really freaks me out!"
    show player 11
    player_name "..."
    hide player with dissolve
    $ M_mom.trigger(T_mom_bad_guys_watching)
    $ callScreen(location_count)