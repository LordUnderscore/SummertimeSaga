label mrsj_room:
    $ location_count = "Mrs Johnson's Room"
    if erik.in_progress(erik_breastfeeding):
        jump erik_breastfeeding
    elif erik.in_progress(erik_sex_ed):
        jump mrsj_sex_ed
    elif mrsj.started(mrsj_sex_ed) and kamasutra in inventory.items and birth_control_pills in inventory.items:
        jump mrsj_sex_ed_2
    $ callScreen(location_count)

label mrsj_ball:
    scene expression gTimer.image("mrsj_ball{}")
    show popup_unfinished at truecenter with dissolve
    $ renpy.pause()
    hide popup_unfinished with dissolve
    $ callScreen(location_count)

label mrsj_private_yoga:
    $ gTimer.tick()
    $ location_count = "Erik's House Entrance"
    $ mrsj_filled = True
    $ M_erimom.set('sex speed', .4)
    show player 435 at left
    show erikmom 53 at Position(xpos=734,ypos=650)
    player_name "Could I see your private yoga lessons?"
    show erikmom 54
    show player 434
    erimom "Well, I have a few special positions I always wanted to try."
    erimom "I just never had anyone to do them with... unless you think you could help me?"
    show erikmom 53
    show player 435
    player_name "Sure, {b}Mrs. Jonhson{/b}, I'd love to help!"
    show erikmom 54
    show player 434
    erimom "You think you have enough energy to keep up?"
    show erikmom 53
    show player 435
    player_name "I can try!"
    show erikmom 54
    show player 434
    erimom "Okay. Start by taking off your clothes..."
    show erikmom 53
    show player 8 with fastdissolve
    pause
    show player 8b with fastdissolve
    pause
    show player 431b with fastdissolve
    pause
    show player 431 with vpunch
    show erikmom 54
    erimom "Wow!"
    erimom "I don't think I've ever seen something this excited for yoga!"
    erimom "Why don't you lay down on the bed and get comfortable with me?"
    scene erik_upstairs_night_c2
    show erikmomsex 33 at topright
    with fade
    erimom "You like this view?"
    show erikmomsex 34
    player_name "It's really nice..."
    show erikmomsex 33
    erimom "Keep your eyes on me, I want to show you a neat little trick."
    show erikmomsex 35 with fastdissolve
    pause 0.05
    show erikmomsex 36 at Position(yoffset=70) with fastdissolve
    pause 0.2
    show erikmomsex 36_37
    player_name "Woah..."
    pause
    $ anim_toggle = True
    $ xray = False

    label mrsj_private_yoga_pos1_repeat:
        hide screen erimom_private_pos1_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show erikmomsex 36_37
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show erikmomsex 36 at Position(yoffset=70)
                pause
                show erikmomsex 37 at Position(yoffset=60)
                pause
                $ animcounter += 1

        show screen erimom_private_pos1_sex_options
        pause
        jump mrsj_private_yoga_pos1_repeat

        label erimom_private_pos1_switch:
            hide screen erimom_private_pos1_sex_options
            $ M_erimom.set('sex speed', .3)
            show erikmomsex 37 at Position(yoffset=60)
            pause 0.2
            show erikmomsex 38 with fastdissolve
            pause 0.2
            show erikmomsex 39 at Position(yoffset=87) with fastdissolve
            erimom "Let's move on to my next pose..."
            erimom "... something to help me stretch?"
            scene erik_upstairs_night_c3
            show erikmomsex 40 at Position(xpos=580,ypos=710)
            with fade
            erimom "This position is more fun..."
            erimom "... you just try and stay still, let me do the work..."
            show erikmomsex 40
            erimom "You're so BIG, {b}[firstname]{/b}..."
            show erikmomsex 41 with fastdissolve
            pause 0.5
            show erikmomsex 42 at Position(xoffset=-14) with fastdissolve
            pause 0.5
            show erikmomsex 43 at Position(xoffset=-20) with fastdissolve
            pause 0.5
            show erikmomsex 44 at Position(xoffset=-30) with fastdissolve
            erimom "Aaah... so deep..."
            player_name "{b}Mrs. Johnson{/b}, you feel so good..."
            erimom "I'm gonna start moving now, try to hold it in for more than a few minutes, {b}[firstname]{/b}."
            show erikmomsex 45 at Position(xoffset=-23)
            pause 0.2
            show erikmomsex 46 at Position(xoffset=-19)
            pause 0.2
            show erikmomsex 42_43_44_45_46
            pause
            erimom "Yes!! Keep going..."
            pause
            $ anim_toggle = True

            label mrsj_private_yoga_pos2_repeat:
                hide screen erimom_private_pos2_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show erikmomsex 42_43_44_45_46 at Position(xpos=580,ypos=710)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show erikmomsex 42 at Position(xoffset=-14)
                        pause
                        show erikmomsex 43 at Position(xoffset=-20)
                        pause
                        show erikmomsex 44 at Position(xoffset=-30)
                        pause
                        show erikmomsex 45 at Position(xoffset=-23)
                        pause 
                        show erikmomsex 46 at Position(xoffset=-19)
                        pause
                        $ animcounter += 1

                show screen erimom_private_pos2_sex_options
                pause
                jump mrsj_private_yoga_pos2_repeat

                label erimom_private_pos2_cum:
                    hide screen erimom_private_pos2_sex_options
                    show erikmomsex 42_43_44_45_46
                    erimom "Hold me tight, {b}[firstname]{/b}..."
                    erimom "... cum inside me!"
                    player_name "Are you sure?"
                    erimom "Yes, I need to feel your energy!"
                    show erikmomsex 47 at Position(xoffset=-34) with vpunch
                    erimom "AHH!!!"
                    show white zorder 4
                    pause 0.3
                    hide white with dissolve
                    erimom "Yes..."
                    erimom "I love the feeling of all that energy flowing, dripping..."
                    player_name "Isn't doing it inside dangerous?"
                    show erikmomsex 48 at Position(xoffset=-13) with dissolve
                    erimom "I'm on the pill, you don't have to worry about that, Honey..."
                    scene erik_upstairs_night_c2
                    show erikmom 56 at right
                    show player 426 at left
                    with fade
                    erimom "You... You did great, {b}[firstname]{/b}."
                    show player 429
                    show erikmom 55
                    player_name "Are you okay, {b}Mrs. Johnson{/b}?"
                    show player 426
                    show erikmom 56
                    erimom "I'm fine, just a little tired..."
                    erimom "I hope I won't be too sore to do yoga tomorrow."
                    show player 427
                    show erikmom 55
                    player_name "Is... {b}Erik{/b} okay with us spending time together?"
                    show player 428
                    show erikmom 56
                    erimom "Oh, he's not thinking about this right now..."
                    show player 426
                    erimom "He's far too busy spending time with his new girlfriend."
                    erimom "I think you can learn a lot if you keep coming to my lessons..."
                    erimom "... but I think I need a nap right now."
                    erimom "Feel free to come back, I'll be waiting here in the evenings."
                    show player 429
                    show erikmom 55
                    player_name "Sure, {b}Mrs. Jonhson{/b}!"
    $ callScreen(location_count)

label mrsj_3some:
    $ gTimer.tick()
    $ location_count = "Erik's House Entrance"
    $ mrsj_filled = True
    show erikmom 39 at right
    show player 21 at left
    show erik 1f zorder 1 at Position(xpos=300)
    player_name "{b}Erik{/b} and I were wondering if you could teach us things?"
    show player 13
    show erik 4f
    eri "Yeah, we'd like to try... having sex."
    show erikmom 40
    show erik 1f
    erimom "I was hoping two would come visit me for some lessons."
    show erikmom 39
    show player 21
    player_name "Really?"
    show player 13
    show erik 4f
    eri "What do you want us to do, Mom?"
    show erikmom 40b
    show erik 1f
    erimom "Well, I was reading this wonderful book you brought me..."
    show erikmom 40
    erimom "... and I think I have just the right thing for us!"
    erimom "How about I show you two a few positions?"
    show erikmom 39
    show player 21
    player_name "Se-sex positions?"
    show player 13
    show erikmom 40
    erimom "Why don't you take off your clothes and join me in bed?"
    erimom "You can follow my instructions..."
    show erik 55f at Position(xoffset=-8)
    show player 8 at Position(xoffset=-27)
    with fastdissolve
    erimom "... and let me do the rest."
    scene erik_upstairs_night_c3
    show erikmomsex 20 at topright
    with fade
    erimom "Let's start with this one!"
    erimom "I'll be on top of you Pumpkin, while I use my mouth on {b}[firstname]{/b}..."
    erimom "... try not to cum too fast!"
    erimom "I want to try a few positions."
    eri "Okay, Mom..."
    show erikmomsex 21_22_23_24_25 with fastdissolve
    pause
    eri "Mom..."
    eri "It feels so good... inside you..."
    $ anim_toggle = True
    $ xray = False
    $ M_erimom.set('sex speed', .4)

    label mrsj_3some_pos1_repeat:
        hide screen mrsj_3some_pos1_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show erikmomsex 21_22_23_24_25 at topright
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show erikmomsex 21
                pause
                show erikmomsex 22
                pause
                show erikmomsex 23
                pause
                show erikmomsex 24
                pause
                show erikmomsex 25
                pause
                $ animcounter += 1

        show screen mrsj_3some_pos1_sex_options
        pause
        jump mrsj_3some_pos1_repeat

        label mrsj_3some_pos1_switch:
            hide screen mrsj_3some_pos1_sex_options
            $ M_erimom.set('sex speed', .3)
            show erikmomsex 26
            erimom "How about we try something different..."
            erimom "... I'd like you boys to take me on my back."
            show erikmomsex 27 at Position(xanchor=0,xpos=200,ypos=100) with fade
            erimom "Yes, {b}[firstname]{/b}, just like that..."
            erimom "... I want to feel both of you at the same time."
            show erikmomsex 28 at Position(yoffset=42) with fastdissolve
            erimom "Ahh... Yes!"
            show erikmomsex 28_29_30
            erimom "Faster!!"
            $ anim_toggle = True

            label mrsj_3some_pos2_repeat:
                hide screen mrsj_3some_pos2_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show erikmomsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show erikmomsex 28 at Position(yoffset=42)
                        pause
                        show erikmomsex 29 at Position(yoffset=36)
                        pause
                        show erikmomsex 30 at Position(xoffset=-4,yoffset=41)
                        pause
                        $ animcounter += 1

                show screen mrsj_3some_pos2_sex_options
                pause
                jump mrsj_3some_pos2_repeat

                label mrsj_3some_pos2_cum:
                    hide screen mrsj_3some_pos2_sex_options
                    show erikmomsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
                    pause
                    show erikmomsex 31 at Position(xoffset=60,yoffset=42) with hpunch
                    erimom "AHHH!!!"
                    show white zorder 4
                    pause 0.3
                    hide white with dissolve
                    pause
                    show erikmomsex 32 with fastdissolve
                    erimom "You've made a real mess with all that cum!"
                    player_name "I came inside... Is that okay?"
                    erimom "Well, It's a good thing I started taking the pill..."
                    player_name "Sorry, {b}Mrs. Johnson{/b}."
                    erimom "It's okay, Honey. I love the feeling of cum dripping out of my..."
                    erimom "... Erm, I think we should take a break."
                    scene erik_upstairs_night_c2
                    show erikmom 56 at right
                    show player 426 zorder 2 at left
                    show erik 59f zorder 1 at Position(xpos=300)
                    with fade
                    erimom "My goodness..."
                    show erik 60f
                    show erikmom 55
                    eri "Are you okay, Mom?"
                    show erik 59f
                    show erikmom 56
                    erimom "Just a little tired, Pumpkin..."
                    erimom "... but you both did amazingly well."
                    erimom "I think I need a nap after all this!"
                    erimom "You boys feel free to come back another day..."
                    show erikmom 55
                    show erik 60f
                    eri "Come on, we should leave and let my mom rest."
                    show erik 59f
                    scene erik_inside_b
                    show erik 4 at right
                    show player 1 at left
                    with fade
                    eri "That was amazing!!"
                    show erik 1
                    show player 17
                    player_name "Yeah, your mom is awesome..."
                    show erik 4
                    show player 1
                    eri "I never thought it would feel this good..."
                    show erik 1
                    show player 14
                    player_name "I think she really liked it too!"
                    show erik 4
                    show player 1
                    eri "You need to come by again so we can have more fun..."
                    show erik 1
                    show player 14
                    player_name "I'll try to come by soon, I promise!"
                    show erik 4
                    show player 1
                    eri "I'll go play some games in my room, talk to you later."
                    show erik 1
                    show player 14
                    player_name "Cool, I'll see you then!"
                    hide erik
                    hide player
                    with dissolve
    $ callScreen(location_count)

label erimom_private_pos1_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos1_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos2_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos2_repeat

label erimom_private_pos2_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos2_repeat

label mrsj_3some_pos1_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos1_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos2_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_3some_pos2_repeat

label mrsj_3some_pos2_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_3some_pos2_repeat