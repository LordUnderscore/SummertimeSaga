label hospital_storage_room_dialogue:
    if M_roz.is_set("fun time"):
        jump roz_storage_sex

    elif hospital_access_card not in inventory.items:
        scene hospital_lock
        player_name "Damn, it's locked!"
        player_name "It looks like I need an {b}access card{/b} to unlock this door..."
        if not Roz.known(roz_storage):
            $ Roz.add_event(roz_storage)
        $ callScreen(location_count)
    $ location_count = "Hospital Storage Room"
    $ roz_trick.finish()
    $ roz_storage.finish()
    $ callScreen(location_count)

label hospital_storage_cabinet_dialogue:
    $ location_count = "Hospital Storage Cabinet"
    if mrsj.started(mrsj_sex_ed) and birth_control_pills not in inventory.items:
        scene hospital_cabinet_filled
        player_name "Hmm..."
        player_name "There's quite a few kinds of pills here."
        player_name "Maybe that green box?"
    $ callScreen(location_count, False)

label roz_storage_sex:
    $ M_roz.set("fun time", False)
    $ gTimer.tick()
    scene location_hospital_sex with fade
    if M_roz.get_state() == S_roz_end:
        show player 11f at Position(xpos=.7,ypos=1.0)
        pause
        show roz 4 at left with dissolve
        show player 13f
        pause
        show roz 5
        roz "Surprised to see you back so soon. I musta left an impression."
        show player 14f
        show roz 4
        player_name "Y-yeah. You were really good!"
        show player 13f
        show roz 5
        roz "Hah, well you don't get to be my age without learning a few tricks, Kiddo."
        show roz 8
        pause
        show roz 9
        roz "Well then..."
        hide roz
        hide player
        show roz 16 at right with dissolve
        show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
        pause
        show roz 17
        pause
        show roz 18
        pause
        show player 80
        pause
        show roz 19
        roz "Why don't you get that monster out and so we can get started."
        show player 83
        player_name "Yes Ma'am!"
        hide player with dissolve
        show roz 18
        show player 480 at Position(xpos=.35,ypos=1.0)
        pause
        show roz 19
        roz "Kid, you really got a great one."
        show roz 18
        show player 482
        pause
        show roz 19
        roz "Don't you be forgettin' to finish inside now..."
        show roz 18
        show player 481
        player_name "Y-yes Ma'am!"
        show player 483 at Position (xpos=.36,ypos=1.0)
        show roz 19
        roz "That's a good boy..."
    else:

        show player 12 at center with dissolve
        player_name "I'm pretty sure Roz said the box would be here."
        show player 11 zorder 2
        player_name "But I don't see it. Maybe she moved it and forgot?"
        show roz 5 zorder 1 at left with dissolve

        roz "Need some help?"
        show player 23f at Position(xpos=.7,ypos=1.0)
        show roz 4
        player_name "Whoa!"
        show player 22f
        player_name "..."
        show player 10f
        player_name "Oh, he-hey Roz. You scared me!"
        show player 11f
        show roz 5
        roz "Ahh, don't be ridiculous! I just came to give you a hand."
        show player 10f
        show roz 4
        player_name "Uhh yeah, okay. Umm, are you sure the box is in here? I can't seem to find it."
        show player 11f
        show roz 5
        roz "No? That's odd."
        roz "I suppose it's possible I brought the box down already and it just slipped my mind."
        roz "This old noggin ain't as sharp as it used to be."
        show roz 4
        player_name "..."
        show player 10f
        player_name "O-Okay. No problem, I'll just run down stairs and-"
        show player 22f
        show roz 6

        player_name "!!!" with hpunch
        show roz 7
        roz "What's the hurry?"
        roz "Seems to me we have a few moments of privacy here..."
        roz "And I think there's something else you can do for me."
        show player 38f
        show roz 6
        player_name "Oh uh, s-sure. What did you have in mind?"
        show player 3f
        show roz 7
        roz "Here's the thing, {b}[firstname]{/b}."
        roz "It's been a looooong time since this old bird got some action. You know what I mean?"
        show player 10f
        show roz 6
        player_name "Umm, a-action?"
        show player 11f
        show roz 7
        roz "That's right. Action."
        show roz 10
        pause


        show roz 8
        pause
        show player 23f
        player_name "!!!" with hpunch
        show player 42f
        player_name "Whoa! Roz, What are you doing?"
        show roz 9
        roz "Eh? What's it look like I'm doin'?"
        roz "Get those clothes off and lets see what your packin' down there."
        show player 10f
        show roz 8
        player_name "Wait you want me to--B-but I can't do that!"
        show player 11f
        show roz 9
        roz "Huh? You want those {b}records{/b} or not?"
        show player 10f
        show roz 8
        player_name "Well yeah, I really need them but-"
        show player 11f
        show roz 9
        roz "Well then what are ya babblin' about? You help me and I help you. Got it?"
        show player 24f
        show roz 8
        player_name "I... I got it."
        show roz 9
        roz "Good!"
        hide roz
        hide player
        show roz 16 at right with dissolve
        show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
        pause
        show roz 17
        pause
        show roz 18
        pause
        show player 78
        pause
        show roz 19
        roz "Heh, I still got it."
        show player 80
        show roz 18
        pause
        show roz 19
        roz "What's the hold up?"
        show player 83
        player_name "Oh man..."
        hide player with dissolve
        show roz 18
        show player 480 at Position(xpos=.35,ypos=1.0)
        pause
        show roz 19
        roz "Phew wee! What a monster!"
        show roz 18
        show player 482
        pause
        show roz 19
        roz "I knew this was a good idea!"
        show roz 18
        pause
        show roz 19
        roz "Now get over here and give ole' Roz what she's been missin'."
        show roz 18
        show player 481
        player_name "O-Okay!"
        show player 483 at Position (xpos=.36,ypos=1.0)
        show roz 19
        roz "That's a good boy..."

    scene location_hospital_sex
    $ M_roz.set('sex speed', .175)
    show rozs 1_2_3_4_5_6_7 at right
    with fade
    roz "That's it Kid, nice and deep."
    pause
    roz "Oh Yeeaah..."
    pause
    roz "Don't you worry about pullin' out neither."
    roz "None of the plumbing works anymore and I like the feel of it inside."
    $ M_roz.set('sex speed', .125)
    show rozs 1_2_3_4_5_6_7
    roz "That's it, just like that."
    pause
    roz "C'mon Kid, harder!"
    $ M_roz.set('sex speed', .075)
    $ anim_toggle = True
    show rozs 1_2_3_4_5_6_7
    pause

    label roz_sex_loop:
        hide screen roz_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                show rozs 1_2_3_4_5_6_7 at right
                pause 5
                if animcounter == 1:
                    roz "Ahhhh!!!{p=1}{nw}"
                if animcounter == 3:
                    roz "Oh!!!{p=1}{nw}"
                    player_name "Uhhh...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                show rozs 1 at right
                pause
                show rozs 2
                pause
                show rozs 3
                pause
                show rozs 4
                pause
                show rozs 5
                pause
                show rozs 6
                pause
                show rozs 7
                pause
                if animcounter == 1:
                    roz "Ahhhh!!!"
                if animcounter == 3:
                    roz "Oh!!!"
                    player_name "Uhhh..."
                $ animcounter += 1

        show screen roz_sex_options
        pause
        jump roz_sex_loop

    label roz_faster_sex:
        $ M_roz.set('sex speed', M_roz.get('sex speed') - 0.05)
        jump roz_sex_loop

    label roz_slower_sex:
        $ M_roz.set('sex speed', M_roz.get('sex speed') + 0.05)
        jump roz_sex_loop

    label roz_sex_cum:
        hide screen roz_sex_options
        player_name "Roz, I can't hold out... M-much longer."
        roz "Finish inside me!"
        pause
        roz "Oh goodness!!!"
        show rozs 8_9 with flash
        player_name "UHHH!!"
        roz "AAAAHHH!!!!"
        pause
        hide rozs
        show player 482 zorder 2 at Position(xpos=.36,ypos=1.0)
        show roz 18 zorder 1 at right
        show rozs 144 zorder 3 at Position(xpos=.5158,ypos=.895)
        show players 143 zorder 4 at Position(xpos=.435,ypos=.8625)
        pause
        show roz 19
        roz "*wheeze* ... Whew."
        roz "Dear me... *cough* That was really good, [firstname]!"
        show roz 18
        show player 481
        player_name "Y-yeah..."
        show player 482
        show roz 19
        roz "Just give me a moment... to catch my breath."
        scene black with fade

    scene location_hospital_sex with fade
    if M_roz.get_state() == S_roz_end:
        show player 1f at Position(xpos=.7,ypos=1.0) with dissolve
        show roz 13 at left with dissolve
        pause
        show roz 15
        roz "You done good today, Kiddo."
        roz "Seeing lots of improvement."
        show player 29f
        show roz 14
        player_name "Really? Heh, thanks. I guess..."
        show player 3f
        show roz 15
        roz "My pleasure, {b}[firstname]{/b}."
        roz "You come back and see ole' Roz again real soon. Ya hear?"
        show player 29f
        show roz 14
        player_name "S-sure thing."
        hide roz
        hide player
        with dissolve
    else:

        show player 5f at Position(xpos=.7,ypos=1.0)
        show roz 4 at left
        pause
        show roz 12
        roz "Here's the records."
        show player 12f
        show roz 11
        player_name "You've had them the whole time?!"
        show player 462
        show roz 5
        roz "Of course, I told ya I knew where they were."
        show roz 4
        player_name "..."
        show roz 5
        roz "I'm not sure what name you're looking for..."
        roz "But if they're in the {b}cemetery{/b}, then they'll be in these {b}records{/b}."
        show roz 13
        pause
        show player 463
        show roz 14
        player_name "...Thanks, I guess."
        show player 462
        show roz 15
        roz "My pleasure, Kiddo."
        roz "Do come back and see me again. Ya know, if you need anything else."
        show roz 14
        pause
        show roz 15
        roz "Like maybe a second round? Heh!"
        show roz 14
        hide roz with dissolve
        pause
        show player 37f
        player_name "(I... Can't believe I just had sex with Roz.)"
        player_name "(She's old enough to be my grandmother...)"
        show player 24f
        player_name "(At least I got the {b}Obituary Records{/b}.)"
        player_name "(I sure hope that Boatsmith is in there somewhere.)"
        hide player with dissolve
        $ inventory.items.append(obituary_records)
        $ M_roz.trigger(T_roz_fuckery)
    $ callScreen(location_count)