default tv_channel = 0
default tv_pink_channel = 7
default tv_channel_pink = True
default tv_channel_1_seen = False
default tv_channel_2_seen = False
default tv_channel_3_seen = False
default tv_channel_4_seen = False
default tv_channel_5_seen = False
default tv_channel_6_seen = False
default tv_channel_7_seen = False
default tv_channel_8_seen = False

label home_livingroom_dialogue:
    python:
        sis_caught_spying = False
    $ location_count = "Living Room"
    if sister.in_progress(sis_couch01):
        scene home_entrance_night with None
        show player 11 with dissolve
        pause 0.0001
        player_name "( I'm not going back in there, she'll catch me for sure. )"
        player_name "( I should go to bed. )"
        hide player with dissolve
        hide home_entrance_night
        jump home_entrance

    elif sister.started(sis_couch03) and gTimer.is_evening():
        scene home_livingroom_n_b with None
        show player 12
        with dissolve
        player_name "( Is someone in here? )"
        show player 11
        player_name "..."
        jump home_livingroom_tv

    if mom_count == 6 and not mom_dialogue_advance and gTimer.is_afternoon() or mom_count == 6 and not mom_dialogue_advance and gTimer.is_morning() and shower != "mom":
        scene home_livingroom_b with None
        show player 34 with dissolve
        player_name "What was that?"
        show player 35
        player_name "( I {b}hear{/b} something... Or someone? )"
        show player 12
        player_name "( It's like a voice, coming from... {b}Mom's bedroom{/b}? )"
        show player 10
        player_name "( I should go see if everything's okay... )"
        hide player 10 with dissolve
        $ mom_masturbating = True
    $ callScreen(location_count)

label couch_dialogue:
    scene home_livingroom_n_c with None
    show player 11 at left
    with dissolve
    player_name "( Someone's definitely in here. )"
    scene home_livingroom_couch01
    show sissex 1 zorder 2
    with dissolve
    pause
    show sissex 4
    show player 298 zorder 1 at Position(xpos=450,ypos=308) with dissolve
    player_name "( Is that... lesbian porn? )"
    show sissex 1
    player_name "( Since when do we have that channel? )"
    show sissex 4
    show player 299 at Position(xpos=555,ypos=337) with dissolve
    player_name "( This is some pretty hardcore stuff. )"
    show sissex 3
    show player 300 at Position(xpos=566,ypos=331)
    player_name "!!!" with vpunch
    show sissex 2
    show player 302 at Position(xpos=593,ypos=387) with fastdissolve
    player_name "( Oh, crap! )"
    show sissex 3
    show player 301 at Position(xpos=602,ypos=386) with fastdissolve
    player_name "( {b}[sis]{/b} is here... )"
    show sissex 2
    player_name "( She is't wearing panties?! )"
    show sissex 4
    player_name "( It looks like she's playing with herself... )"
    player_name "( ...and she doesn't know I'm here. )"
    $ sis_couch01.finish()
    $ sister.add_event(sis_couch02)
    menu:
        "Leave.":
            player_name "( I better leave before she sees me. )"
            hide player with fastdissolve
            show unlock33 zorder 3 at truecenter
            pause
            hide unlock33 with dissolve
            hide sissex
            jump home_entrance
        "Keep watching.":

            show sissex 2_3_1_4
            pause 8
            show sissex 1
            player_name "( That's hot, but I shouldn't push my luck. )"
            hide player with fastdissolve
            show unlock33 zorder 3 at truecenter
            pause
            hide unlock33 with dissolve
            hide sissex
            jump home_entrance

label home_livingroom_tv_locked:
    scene expression gTimer.image("home_livingroom{}_b") with None
    show popup_tv_locked at truecenter with dissolve
    pause
    hide popup_tv_locked with dissolve
    $ callScreen(location_count)

label home_livingroom_tv:
    if masturbated_tv:
        if sister.known(sis_couch02) and played_with_mom_panties == 1:
            scene home_livingroom_n_b with None
            show player 11
            with dissolve
            player_name "( I'm not risking that again, tonight... )"
            player_name "( I should go to bed. )"
        else:

            scene home_livingroom_n_b with None
            show player 11
            with dissolve
            player_name "( I think that's enough for one night. )"
            player_name "( I should go to bed. )"
        hide player with dissolve
        hide home_livingroom_n
        jump home_livingroom_dialogue
    $ tv_channel = 0
    jump tv_channel_responses

label tv_channel_responses:
    if sister.started(sis_couch03) and gTimer.is_evening():
        scene home_livingroom_couch01 with None
        show playersex 82 at Position(xpos=497)
        with dissolve
        player_name "Let's see what's on TV..."

        scene home_livingroom_tv
        show home_tv_channel_08 at Position(xpos = 522, ypos = 521)
        player_name "( Someone left it on the Pink Channel? )"
        player_name "The password was..."
        pause .4
        show text "{color=#ff4bdf}L6bv12R{/color}" as username at Position(xpos = 433, ypos = 341)
        pause .4
        show text "{color=#ff4bdf}12345{/color}" as password at Position(xpos = 423, ypos = 411)
        pause 1
        hide username
        hide password
        show home_tv_channel_10 at Position(xpos = 522, ypos = 521)
        player_name "Woah!"
        player_name "( I've never seen someone use their feet like {b}that{/b}. )"
        player_name "( Actually, that's kind of hot. )"
        jump couch_footjob

    scene home_livingroom_tv

    $ pink_user = ""
    $ pink_pass = ""

    if tv_channel == -1:
        $ tv_channel = 7

    elif tv_channel == 8:
        $ tv_channel = 0

    if tv_channel == 0 and not tv_channel_1_seen:
        show home_tv_channel_01 at Position(xpos=522, ypos=521)
        player_name "Hmm... Let's see what's on TV."
        $ tv_channel_1_seen = True

    elif tv_channel == 1 and not tv_channel_2_seen:
        show home_tv_channel_02 at Position(xpos=522, ypos=521)
        player_name "( Local news. Boring! )"
        $ tv_channel_2_seen = True

    elif tv_channel == 2 and not tv_channel_3_seen:
        show home_tv_channel_03 at Position(xpos=522, ypos=521)
        player_name "( That's the kind of sport I could get into. )"
        $ tv_channel_3_seen = True

    elif tv_channel == 3 and not tv_channel_4_seen:
        show home_tv_channel_04 at Position(xpos=522, ypos=521)
        player_name "( Hey, it's Mayor Rump! )"
        $ tv_channel_4_seen = True

    elif tv_channel == 4 and not tv_channel_5_seen:
        show home_tv_channel_05 at Position(xpos=522, ypos=521)
        player_name "..."
        player_name "( These nature channels are so strange... )"
        $ tv_channel_5_seen = True

    elif tv_channel == 5 and not tv_channel_6_seen:
        show home_tv_channel_06 at Position(xpos=522, ypos=521)
        player_name "( Who watches this stuff? )"
        $ tv_channel_6_seen = True

    elif tv_channel == 6 and not tv_channel_7_seen:
        show home_tv_channel_07 at Position(xpos=522, ypos=521)
        player_name "( This channel's a dud. )"
        $ tv_channel_7_seen = True

    elif tv_channel == 7:
        if sis_watch_tv_tonight and gTimer.is_evening():
            $ tv_pink_channel = 8

        elif sister.over(sis_couch03):
            $ tv_pink_channel = renpy.random.randint(7,8)
        else:

            $ tv_pink_channel = 7

        if tv_pink_channel == 7 and not tv_channel_pink:
            show home_tv_channel_09 at Position(xpos=522, ypos=521)
            if gTimer.is_evening():
                if sister.completed(sis_couch02)and played_with_mom_panties == 1:
                    pause .4
                    hide home_tv_channel_09
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    player_name "( That's pretty hot. )"
                    show playersex 83 with fastdissolve
                    player_name "( Hmm... )"
                    player_name "( Everyone should be sleeping. )"
                    show playersex 84 with fastdissolve
                    player_name "( I'll just have to be quiet... )"
                    show playersex 85 with fastdissolve
                    pause .4
                    show playersex 86_85
                    pause 8
                    scene home_livingroom_couch02
                    show playersex 80 at Position(xpos=497)
                    player_name "!!!" with hpunch
                    player_name "( Oh, Shit! {b}Mom{/b}'s coming out of her room! )"
                    show playersex 81
                    pause
                    show mom 126 at Position (xpos=917,ypos=694)
                    show player 303 at left
                    hide playersex
                    with dissolve
                    pause
                    show mom 127 at Position (xpos=872,ypos=540) with fastdissolve
                    mom "Is someone in here?"
                    show mom 128 at Position (xpos=862,ypos=511) with fastdissolve
                    mom "Oh, my!"
                    show mom 129
                    player_name "( Shit-shit-shit! I left the TV on! )"
                    show player 305
                    show mom 132 at Position (xpos=680,ypos=768) with dissolve
                    mom "I wonder who..."
                    show player 304
                    mom "No, It can't be him. It must be his sister."
                    mom "They never used to do this sort of thing."
                    mom "Maybe I'm being too lenient..."
                    show player 305
                    show mom 133 at Position (xpos=812,ypos=767) with fastdissolve
                    mom "{b}*sigh*{/b}"
                    mom "They'll be fine. I'm going back to bed."
                    show mom 134 at Position (xpos=868,ypos=546) with fastdissolve
                    pause
                    scene home_livingroom_couch01
                    show player 305 at left
                    with dissolve
                    pause
                    show player 306
                    player_name "Man, that was close!"
                    player_name "( Too close... )"
                else:

                    player_name "( Woah! That's the one she was watching last time. )"
                    hide home_tv_channel_09
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    player_name "( That's pretty hot. )"
                    show playersex 83 with fastdissolve
                    player_name "( Hmm... )"
                    player_name "( Everyone should be sleeping. )"
                    show playersex 84 with fastdissolve
                    player_name "( I'll just have to be quiet. )"
                    show playersex 85 with fastdissolve
                    pause .4
                    show playersex 86_85
                    pause 8
                    player_name "( Almost there... )"
                    show playersex 86
                    show white
                    pause 0.001
                    show playersex 87
                    hide white
                    with dissolve
                    pause
                    show playersex 88 with fastdissolve
                    pause
                    show playersex 85b
                    player_name "( It looks like they have new porn videos every night. )"
                    player_name "( I should {b}come back another time{/b} to watch some... )"
                    show playersex 89
                    with dissolve
                    player_name "( Damn it. I made a mess. )"
                    player_name "( I better clean this up before someone walks in. )"
                    $ sis_couch02.finish()
                hide player
                hide home_livingroom_couch01
                $ masturbated_tv = True
                jump home_livingroom_dialogue

        elif tv_pink_channel == 8 and not tv_channel_pink:
            show home_tv_channel_10 at Position(xpos=522, ypos=521)
            if gTimer.is_evening():
                if sis_watch_tv_tonight:
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    pause
                    show playersex 83
                    player_name "( Hmm... )"
                    player_name "( I guess she decided not to come down. )"
                    show playersex 84 with fastdissolve
                    player_name "( Oh well, since I'm already here... )"
                    show playersex 85 with fastdissolve
                    pause
                    show playersex 86_85
                    pause 4
                    show playersex 86
                    show sis 77 at Position(xpos=559,ypos=333) with dissolve
                    pause
                    show playersex 85
                    show sis 78 at Position(xpos=878,ypos=510) with dissolve
                    pause
                    show sis 79
                    show playersex 90
                    sis "What, you really couldn't wait for me?" with hpunch
                    sis "You wouldn't want to miss out on your sister's feet, now would you?"
                    show sis 78
                    player_name "I... I didn't know if you'd come!"
                    hide sis
                    show playersex 92 at Position(xpos=533)
                    with dissolve
                    sis "Why are you hiding it?"
                    show playersex 94
                    sis "No one's around, idiot." with fastdissolve
                    show playersex 95
                    sis "Come on, let's see that horny cock of yours." with fastdissolve
                    show playersex 97 with fastdissolve
                    pause
                    show playersex 96_97
                    pause 4
                    show playersex 97
                    menu:
                        "Jump on her." if pStats.dex() < 7:
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 131 at Position(xpos=587)
                            sis "[dex_warn]What are you doing?!" with hpunch
                            show playersex 132
                            sis "[dex_warn]Who said you could touch me?!"
                            sis "[dex_warn]I think you got more than you deserved for today."
                            sis "[dex_warn]Go finish in your room, pervert.."
                            hide playersex
                            hide sis
                            $ masturbated_tv = True
                            $ sis_watch_tv_tonight = False
                            jump home_livingroom_dialogue

                        "Jump on her." if pStats.dex() >= 7:
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 133 at Position(xpos=578)
                            sis "What are you-" with hpunch
                            show playersex 134 at Position(xpos=553)
                            player_name "{b}[sis]{/b}!!!"
                            show playersex 135
                            player_name "I want you! Now!"
                            show playersex 136
                            sis "You pervert!!! Ahh!!!"
                            show playersex 137
                            pause
                            show playersex 134_135_136_137
                            pause 8
                            sis "Stop moving your hips like that... It's... Too deep!!"
                            show playersex 134
                            sis "We... We have to stop..."
                            show playersex 135
                            sis "We're too loud. {b}Mom{/b} will..."
                            show playersex 136
                            sis "... It's so good!!"
                            show playersex 137
                            menu sis_couch_sex_loop:
                                "Keep going.":
                                    show playersex 134_135_136_137
                                    pause 8
                                    show playersex 137
                                    jump sis_couch_sex_loop
                                "Cum inside.":

                                    show playersex 134
                                    sis "...Are you?!"
                                    show playersex 135
                                    player_name "I'm cumming!!"
                                    show playersex 136
                                    sis "Don't-"
                                    show playersex 138
                                    sis "{b}AHHH{/b}!!!" with hpunch
                                    show white
                                    hide white with dissolve
                                    pause
                                    show white
                                    hide white with fastdissolve
                                    pause
                                    show playersex 142 at Position(xpos=574)
                                    sis "What the {b}FUCK{/b}?!" with dissolve
                                    show playersex 141
                                    player_name "I'm sorry!! I couldn't hold it..."
                                    show playersex 142
                                    sis "Why do you keep cumming inside me, you {b}IDIOT{/b}!?"
                                    show playersex 141
                                    player_name "I don't know..."
                                    show playersex 140
                                    sis "Ugh..."
                                    sis "You know I need you fresh and rested for my cam shows!!"
                                    sis "And what if I get {b}pregnant{/b}?!"
                                    show playersex 139
                                    player_name "..."
                                    show playersex 141
                                    sis "I really shouldn't watch these pornos with you..."
                                    sis "I have to clean myself up now."
                                    sis "Thanks a lot, pervert."
                                    hide playersex
                                    hide sis
                                    $ masturbated_tv = True
                                    $ sis_watch_tv_tonight = False
                                    jump home_livingroom_dialogue
                        "Cum.":

                            pause .4
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 97
                            player_name "Stop! I'm-"
                            show white
                            pause 0.001
                            show playersex 98
                            hide white with dissolve
                            pause
                            show playersex 99 with dissolve
                            player_name "Ahh..."
                            show playersex 100 with fastdissolve
                            sis "Gross..."
                            show playersex 101
                            player_name "Sorry about the mess..."
                            show playersex 100
                            sis "Next time you need something, just ask!"
                            show playersex 103
                            sis "Now get me a tissue box, so I can clean this off, you pervert!" with hpunch
                            hide playersex
                            hide sis
                            $ masturbated_tv = True
                            $ sis_watch_tv_tonight = False
                            jump home_livingroom_dialogue
                else:

                    label couch_footjob:
                        pause .4
                        hide home_tv_channel_10
                        scene home_livingroom_couch01
                        show playersex 83 at Position(xpos=497)
                        player_name "( Hmm... )"
                        player_name "( The others should be asleep. )"
                        show playersex 84 with fastdissolve
                        player_name "( I'll just have to be quiet. )"
                        show playersex 85 with fastdissolve
                        pause .4
                        show playersex 86_85
                        pause 8
                        show playersex 86
                        show sis 77 at Position(xpos=559,ypos=333) with dissolve
                        pause
                        show playersex 85
                        show sis 78 at Position(xpos=878,ypos=510) with dissolve
                        pause
                        show sis 79
                        show playersex 90
                        sis "Well, well!" with hpunch
                        sis "Really?"
                        sis "You don't think I saw that?"
                        hide sis
                        show playersex 92 at Position(xpos=533)
                        with dissolve
                        sis "So, I was wondering..."
                        sis "How exactly were you able to access the Pink Channel?"
                        show playersex 91
                        player_name "It was already there when I turned the TV on!"
                        show playersex 92
                        sis "I think you're lying."
                        sis "I also think you went through someone else's emails, and found their Pink Channel subscription."
                        show playersex 91
                        player_name "I'm sorry... I didn't-"
                        show playersex 92
                        sis "Cut the crap!"
                        show playersex 93
                        sis "If you were so horny..."
                        show playersex 92
                        sis "... you could've just asked me for it."
                        show playersex 91
                        player_name "I..."
                        show playersex 92
                        sis "So..."
                        sis "You're into feet, huh?"
                        show playersex 91
                        player_name "I don't know what you mean."
                        show playersex 94
                        sis "I think..." with fastdissolve
                        show playersex 95
                        sis "... you know exactly what I mean." with fastdissolve
                        show playersex 108
                        sis "Just like this, right?" with fastdissolve
                        show playersex 97
                        pause .4
                        $ anim_toggle = False
                        label couch_footjob_loop:
                            show screen sex_anim_buttons
                            pause
                            if anim_toggle == True:
                                hide screen sex_anim_buttons
                                hide playersex 97
                                show playersex 96_97 at Position(xpos=533)
                                pause 8
                                hide playersex 96_97
                                show playersex 97 at Position(xpos=533)
                            else:

                                hide screen sex_anim_buttons
                                $ animcounter = 0
                                while (animcounter < 2):
                                    show playersex 96
                                    pause
                                    show playersex 97
                                    pause
                                    $ animcounter += 1
                                show playersex 96
                                pause
                                show playersex 97
                        menu:
                            "Keep Going.":
                                jump couch_footjob_loop
                            "Cum.":

                                pause .4
                                show playersex 108
                                sis "How is it?"
                                show playersex 109
                                sis "Does this feel good?"
                                show playersex 108
                                sis "You little pervert..."
                                show playersex 97
                                player_name "Stop! I'm-"
                                show white
                                pause 0.001
                                show playersex 98
                                hide white with dissolve
                                pause
                                show playersex 99 with dissolve
                                player_name "Ahh..."
                                show playersex 100 with fastdissolve
                                sis "Gross..."
                                show playersex 101
                                player_name "Sorry about the mess..."
                                show playersex 100
                                sis "Next time you need something, just ask!"
                                show playersex 103
                                sis "Now get me a tissue box, so I can clean this off, you pervert!" with hpunch
                                hide playersex
                                hide sis
                                $ sis_couch03.finish()
                                $ masturbated_tv = True
                                jump home_livingroom_dialogue

        elif not tv_channel_8_seen:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            player_name "Pink channel?"
            player_name "( That must be the channel my sister was watching. )"
            player_name "( I wonder where I could find her account password... )"
            player_name "( I bet they emailed it to her. )"
            $ tv_channel = 7
            $ tv_channel_8_seen = True
    hide home_tv_channel_01
    hide home_tv_channel_02
    hide home_tv_channel_03
    hide home_tv_channel_04
    hide home_tv_channel_05
    hide home_tv_channel_06
    hide home_tv_channel_07
    hide home_tv_channel_08
    hide home_tv_channel_09
    hide home_tv_channel_10
    call screen home_livingroom_tv

label tv_pink_channel_pass_check:
    if pink_user == "L6bv12R" and pink_pass == "12345":
        $ tv_channel_pink = False
        jump tv_channel_responses

    elif pink_user != "L6bv12R" or pink_pass != "12345":
        show home_tv_channel_08 at Position(xpos=522, ypos=522)
        show sis_wrong_pass at Position(xpos=520, ypos= 510) with dissolve
        pause 1
        hide sis_wrong_pass with dissolve
        jump tv_channel_responses

label door44_options:
    if mother.known(mom_dinner_outfit) and not mother.over(mom_dinner_outfit):
        scene mom_bedroom with None
        show mom 144 at left
        show player 11f at right
        with dissolve
        mom "So? How does it look?"
        show mom 145
        show player 14f
        player_name "That outfit looks great! You look amazing, {b}Mom{/b}!"
        show mom 146
        show player 13f
        mom "Awww... Thank you dear. How about from the back?"
        show mom 147 with fastdissolve
        show player 212f
        pause
        show player 21f
        player_name "Still great!"
        show player 1f
        mom "Umm... Do the pants make my butt look too big?"
        mom "They aren't too tight, are they?"
        show player 14f
        player_name "Uh... No {b}Mom{/b}. Your bu... um.. I mean... pants look great."
        show player 212f
        pause
        show player 11f
        mom "Are you staring at my butt?"
        show player 21f
        player_name "N-n-no, of course not, {b}Mom{/b}!!"
        show player 1f
        show mom 148 with fastdissolve
        mom "Well, thank you for your honesty. It makes me happy to know my butt can still make a man stumble for words."
        mom "Haha."
        show mom 149
        show player 29f at Position(xoffset=-8)
        player_name "Heh..."
        hide mom
        hide player
        with dissolve
        scene home_livingroom_b
        show player 35
        with dissolve
        player_name "I better get that {b}fish{/b} she asked for... I should make sure of what kind it was again..."
        show player 34
        $ ui_lock_count = 0
        $ mom_dinner_outfit.finish()
        $ mother.complete_events(mom_dinner_outfit)
        menu:
            "Ask {b}Mom{/b}.":
                scene mom_bedroom
                show mom 159 at left
                with fade
                pause
                show mom 160 with fastdissolve
                pause
                show mom 161b
                show player 14f at right with fastdissolve
                player_name "Hey {b}Mom{/b}, what was-"
                show player 11f
                player_name "!!!" with hpunch
                show mom 161
                mom "Sweetie! I'm still changing!"
                show player 21f
                show mom 152 with fastdissolve
                player_name "Oh, sorry!"
                show mom 153
                show player 13f
                mom "It's okay!"
                mom "We've seen each other naked before..."
                show mom 152
                show player 14f
                player_name "Soo... I just wanted to know what kind of fish to get for {b}Aunt Diane{/b} again."
                show mom 153
                show player 1f
                mom "It's a {b}sea trout{/b}, Sweetie."
                show mom 152
                show player 14f
                player_name "Okay, thanks! I'll be going now..."
                show mom 154
                show player 11f
                mom "Wait!"
                show mom 155
                show player 10f
                player_name "Huh?"
                show mom 156 with fastdissolve
                show player 11f
                mom "How do I look now?"
                show mom 157
                show player 21f
                player_name "Uhhh..."
                player_name "You look... beautiful, {b}Mom{/b}."
                show mom 158
                show player 13f
                mom "You're always so nice to me, Sweetie."
                mom "Come give me a hug!"
                show mom 162 at Position(xpos=102)
                hide player
                with fastdissolve
                pause
                show mom 163
                player_name "!!!" with hpunch
                show mom 155 at left
                show player 21f at right
                with fastdissolve
                player_name "Thanks, {b}Mom{/b}!"
                player_name "I should really get going."
                show mom 154
                show player 13f
                mom "Okay. See you soon."
                scene home_livingroom_b
                show player 21
                with fade
                player_name "{b}Wow{/b}!"
                player_name "( {b}Mom{/b} is so... hot... )"
                hide player with dissolve
                jump home_livingroom_dialogue
            "Just leave.":

                jump home_livingroom_dialogue

    elif not mom_cuddling_unlocked and gTimer.is_evening():
        scene home_livingroom_n_b with None
        show player 10 at left
        with dissolve
        player_name "( I really shouldn't disturb {b}Mom{/b} when she's sleeping. )"
        hide player
        with dissolve
        $ callScreen(location_count)

    elif not mom_door_lock and not gTimer.is_night():
        if mom_count == 10 and not mom_dialogue_advance or mom_count >= 11:
            $ location_count = "Mom's Bedroom"
            jump mom_bedroom

        elif mom_masturbating and not gTimer.is_dark():
            $ location_count = "Mom's Bedroom"
            jump mom_masturbating

        elif (gTimer.is_morning() and shower == "mom") or gTimer.is_dark():
            $ location_count = "Mom's Bedroom"
            jump mom_bedroom
        else:

            if gTimer.is_dark():
                jump door44_locked_night
            else:

                jump door44_locked_dialogue
    else:

        if gTimer.is_dark():
            jump door44_locked_night
        else:

            jump door44_locked_dialogue

label door44_locked_dialogue:
    if door20_locked_count == 0:
        scene home_livingroom_b
        show player 22 at left
        show mom 2 at right
        with dissolve
        mom "{b}[firstname]{/b}? Are you looking for something in my room?"
        show player 21 at left
        show mom 1 at right
        player_name "I was... Umm... Looking for my phone!"
        show player 18 at left
        player_name "But it's right here in my pocket actually!"
        show mom 3 at right
        show player 11 at left
        mom "Isn't {b}Erik{/b} waiting for you?"
        show mom 1 at right
        show player 17 at left
        player_name "Yeah, I'm on my way!"
        hide player 17 at left
        hide mom 1 at right
    else:

        scene home_livingroom_b
        show player 24 at left
        player_name "( Now's not a good time to snoop around {b}Mom's{/b} bedroom. )"
        hide player 17 at left
    $ callScreen(location_count)

label door44_locked_night:
    scene home_livingroom_n_b
    show player 24 at left
    player_name "( Now's not a good time to snoop around {b}Mom's{/b} bedroom. )"
    hide player 17 at left
    $ callScreen(location_count)