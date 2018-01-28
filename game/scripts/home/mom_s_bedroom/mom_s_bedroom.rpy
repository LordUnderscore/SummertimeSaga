default caught = False
default mom_had_sex = False
default saw_mom_masturbate = False
default mom_sex_position = "missionary"
default mom_room_first_visit = True

label mom_bedroom_screen:
    $ location_count = "Mom's Bedroom"
    $ callScreen(location_count)

label mom_bedroom:
    $ location_count = "Mom's Bedroom"
    if gTimer.is_dark():
        scene mom_peek_sequence_1_night
        player_name "( {b}[mom_name]'s{/b} sleeping. )"
        player_name "( I shouldn't make any noise. )"

    elif M_mom.get_state() == S_mom_spy and not gTimer.is_dark():
        show mom_peek_sequence 2_3 zorder 3
        player_name "WHA-!!"
        player_name "{b}[mom_name]{/b}?!?"
        player_name "( ...She's naked on her bed... )"
        player_name "( ...And rubbing herself...moaning. )"
        mom "Oh... Yes..."
        mom "Just like that, Sweetie..."
        mom "Mmm..."
        mom "Yes... {b}[firstname]{/b}..."
        mom "Closer to {b}Mommy{/b}..."
        player_name "!!!"
        mom "Mmm..."
        mom "Keep going..."
        mom "Help {b}Mommy{/b}... She needs to cum..."
        mom "..."

        mom "...Ahhh!!" with hpunch
        $ location_count = "Living Room"
        scene home_livingroom_c
        show player 107 at left
        with fade
        player_name "( This is... I'm feeling... )"
        player_name "( ...so aroused by this. )"
        show sis 10 at right with dissolve
        sis "..."
        show sis 9 at right
        sis "{b}Caught you{/b}!"
        show player 23 at left with hpunch
        show sis 10 at right
        player_name "!!!"
        show player 29 at left
        player_name "I was just-"
        show player 11 at left
        show sis 9 at right
        sis "Don't play stupid with me."
        show player 5 at left
        show sis 10 at right
        sis "What's {b}[mom_name]{/b} doing in there anyway?"
        show player 10 at left
        player_name "Uhh... Nothing!"
        show player 5 at left
        show sis 12 at right
        sis "Oh, yeah?"
        show sis 16 at left
        show player 22f at right
        with dissolve
        sis "Let's see then..."
        sis "{b}Wow{/b}..."
        show player 5f at right
        sis "She sure seems to be enjoying herself..."
        show sis 17f at left
        sis "..."
        show player 80f at right with dissolve
        sis "...And so are you, apparently!"
        show player 81f at right with hpunch
        player_name "!!!"
        show sis 12f at left
        show player 78f at right
        sis "Little {b}Brother{/b} is not so, {b}little{/b}, anymore..."
        show player 80f at right
        sis "Is that why you've been watching me when I shower lately?"
        show player 82f at right
        sis "You've been having urges..."
        sis "...You fantasize about {b}[mom_name]{/b}... And your older {b}Sister{/b}?"
        show player 83f at right
        show sis 11f at left
        player_name "Please, don't tell {b}[mom_name]{/b} I was watching her..."
        show player 82f at right
        show sis 19f at left
        sis "Well, well... That all depends!"
        show player 83f at right
        show sis 18f at left
        player_name "What do you mean?"
        show sis 19f at left
        show player 80f at right
        sis "If you behave and do as I say, when I say."
        show player 83f at right
        show sis 18f at left
        player_name "Uhh... Like what?"
        show player 82f at right
        show sis 19f at left
        sis "We'll see."
        show sis 18f at left
        player_name "..."
        show sis 12f at left
        sis "See you around, little {b}Brother{/b}!"
        hide player
        hide sis
        with dissolve
        $ M_mom.trigger(T_mom_caught_spying)
        $ gTimer.tick()

    elif M_mom.get_state() == S_mom_panties_masturbation_again:
        scene location_mombedroom_blur
        show player 1 with dissolve
        player_name "( Alright, I'm in! )"
        player_name "( Now I just need to {b}grab a pair of her panties{/b} before getting into her bed. )"
        player_name "( Oh, sweet release... Here I come! )"
        hide player with dissolve

    elif M_mom.get_state() == S_mom_sleepover_wakeup:
        scene mom_bedroom
        show player 264 at left with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 266 with dissolve
        player_name "I can't believe I slept in {b}[mom_name]{/b}'s bed last night..."
        show player 267
        pause
        show player 268
        player_name "I better go before she notices my morning wood."
        show player 267
        mom "{b}*Yawn*{/b}"
        player_name "!!!"
        show player 261 with dissolve
        pause
        show player 8f with dissolve
        pause
        show mom 2 at right with dissolve
        show player 22 with dissolve
        mom "How was your night, Sweetie?"
        show mom 1
        show player 21
        player_name "G... Good."
        show xtra 21 at left
        show player 5
        show mom 3
        mom "That was the best sleep I've had in a while."
        show mom 2
        mom "It felt good having someone with me in bed."
        mom "I miss that feeling."
        show mom 1
        show player 21
        player_name "Yeah... It was nice."
        show player 5
        show mom 3
        mom "You're a little cutie!"
        show mom 2
        mom "Leaving already?"
        show mom 1
        show player 21
        player_name "Yeah, I better go."
        show player 5
        show mom 2
        mom "Try and be quiet when you leave my room."
        mom "I don't need your sister thinking the whole family needs to sleep together!"
        show mom 3
        mom "Ha Ha Ha."
        show mom 1
        show player 21
        player_name "Yeah."
        player_name "Love you, {b}[mom_name]{/b}."
        show player 13
        show mom 2
        mom "Love you too."
        mom "You're always welcome to sleep here remember."
        hide xtra
        hide player
        hide mom
        with dissolve
        $ M_mom.trigger(T_mom_sleepover_morning)
        $ location_count = "Living Room"

    elif M_mom.get_state() == S_mom_dinner_outfit:
        scene mom_bedroom with None
        show mom 144 at left
        show player 11f at right
        with dissolve
        mom "So? How does it look?"
        show mom 145
        show player 14f
        player_name "That outfit looks great! You look amazing, {b}[mom_name]{/b}!"
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
        player_name "Uh... No {b}[mom_name]{/b}. Your bu... um.. I mean... pants look great."
        show player 212f
        pause
        show player 11f
        mom "Are you staring at my butt?"
        show player 21f
        player_name "N-n-no, of course not, {b}[mom_name]{/b}!!"
        show player 1f
        show mom 148 with fastdissolve
        mom "Well, thank you for your honesty. It makes me happy to know my butt can still make a man stumble for words."
        mom "Haha."
        show mom 149
        show player 29f
        player_name "Heh..."
        hide mom
        hide player
        with dissolve
        scene home_livingroom_b
        show player 35
        with dissolve
        player_name "I better get that {b}fish{/b} she asked for... I should make sure of what kind it was again..."
        show player 34
        $ M_mom.trigger(T_mom_dinner_outfit_check)
        $ unlock_ui()
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
                player_name "Hey {b}[mom_name]{/b}, what was-"
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
                player_name "You look... beautiful, {b}[mom_name]{/b}."
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
                player_name "Thanks, {b}[mom_name]{/b}!"
                player_name "I should really get going."
                show mom 154
                show player 13f
                mom "Okay. See you soon."
                scene home_livingroom_b
                show player 21
                with fade
                player_name "{b}Wow{/b}!"
                player_name "( {b}[mom_name]{/b} is so... hot... )"
                hide player with dissolve
                jump home_livingroom_dialogue
            "Just leave.":

                jump home_livingroom_dialogue

    elif M_mom.get_state() == S_mom_midnight_swim_after:
        $ location_count = "Living Room"
        scene home_livingroom_n_b
        show player 25f with dissolve
        player_name "I should leave her alone..."
        show player 24f
        player_name "She seemed pretty upset..."
        hide player with dissolve

    elif not M_mom.is_set("fetch lotion") and not M_mom.is_set("sleep together"):
        scene mom_peek_sequence_1
        player_name "( {b}[mom_name]'s{/b} not in her room. )"
        player_name "( She's probably in the kitchen or something... )"
    $ callScreen(location_count)

label mom_drawer:
    $ callScreen("Mom's Drawer", False)

label mom_drawer_panties:
    scene mom_bedroom
    show player 490
    player_name "( Wow, they're so soft. )"
    show player 489
    pause
    show player 491
    pause
    show player 490
    player_name "( ... Hmm, smells like fresh linens. )"
    show player 489
    player_name "( ... )"
    show player 490
    player_name "( I bet her bed smells like her... )"
    player_name "( Maybe, I could lay on it for just a little bit? )"
    player_name "( She won't ever find out. )"
    hide player
    with dissolve
    $ M_mom.trigger(T_mom_steal_panties)
    $ M_mom.set("panties taken", True)
    $ lock_ui()
    $ callScreen(location_count)

label mom_bed:
    if M_mom.is_set("panties taken"):
        scene location_mombed01 with dissolve
        if M_mom.get_state() == S_mom_panties_masturbation:
            player_name "( These feel so soft against my skin... )"
            show location_mombed 2_3
            pause 5
            scene location_mombed04
            mom "!!!" with hpunch
            scene location_mombed05
            mom "Oh my..."
            player_name "{b}[mom_name]{/b}!!"
            scene mom_bedroom_closeup
            show mom 16 at right
            show player 152 at left
            with dissolve
            mom "I'm so sorry, Sweetie!!"
            show mom 17
            show player 150
            mom "I didn't know you were in here..."
            mom "I ehh..."
            show mom 16
            mom "I should leave!"
            show mom 15
            show player 149
            player_name "But-"
            show mom 16
            show player 150
            mom "No, it's fine... Just... finish whatever you need to do..."
            show mom 17
            show player 154
            mom "I'll come back later!"
            player_name "..."
            scene home_livingroom_b
            show mom 16
            with dissolve
            mom "( I can't believe what I just saw! )"
            mom "( I never thought I would see my {b}Son{/b} doing... THAT! )"
            show mom 20
            mom "( And in {b}my room{/b}! )"
            show mom 17
            mom "( I guess... I always saw him as my innocent little boy! )"
            show mom 16
            mom "( But... Was he doing {b}-it-{/b} with... My {b}underwear{/b}? )"
            show mom 19
            mom "..."
            show mom 18
            mom "( It's probably normal... )"
            mom "( He's having hormonal changes, of course! )"
            mom "( I never see him bring girls over... He must be having urges... )"
            show mom 17
            mom "( ...But I should really tell him to do it in his room from now on... )"
            show mom 16
            mom "( ...And not with my {b}underwear{/b}! )"
            scene mom_bedroom_closeup
            show player 151 at left
            with dissolve
            player_name "( Oh my god! )"
            player_name "( I'm {b}SO{/b} screwed... )"
            player_name "( Why did I even DO this! )"
            show player 153
            player_name "...Ugh..."
            player_name "( I'm so stupid... )"
            show player 151
            player_name "( ...And now things are gonna be really awkward... )"
            scene home_livingroom_b
            show mom 13 at right with dissolve
            show player 5 at left with dissolve
            mom "Hey, Sweetie!"
            show mom 14
            show player 21
            player_name "Hi, {b}[mom_name]{/b}..."
            show mom 13
            show player 24
            mom "Listen, I just want you to know that it's okay..."
            mom "What happened was... normal!"
            mom "And I know that young men your age have {b}urges{/b}..."
            show player 5
            show mom 14
            player_name "..."
            show mom 13
            mom "You just have a lot of affection for your {b}Mother{/b}, and you don't have a girlfriend..."
            mom "...but you can't do that in my room! ...And you're ruining my lingerie..."
            show mom 14
            show player 24
            player_name "I'm Sorry, {b}[mom_name]{/b}."
            show mom 13
            show player 5
            mom "It's okay, Sweetie..."
            show player 11
            mom "...Can't you find something else? Like {b}internet porn{/b}?"
            mom "Do you have that on your computer, or something?"
            show mom 14
            show player 21
            player_name "{b}[mom_name]{/b}!! Please, stop..."
            show mom 13
            show player 13
            mom "Anyway... I want you to know that I {b}love you{/b}..."
            mom "...And that I'm not mad about it!"
            mom "I just don't want you to develop some sort of complex or something..."
            show mom 14
            show player 21
            player_name "I'll be fine, {b}[mom_name]{/b}..."
            show mom 13
            show player 13
            mom "Alright, alright. Just promise not to do that in my room anymore."
            show player 21
            show mom 14
            player_name "I promise..."
            $ M_mom.trigger(T_mom_caught_masturbating)
            $ location_count = "Living Room"

        elif M_mom.is_set("sex available"):
            player_name "( These feel so soft against my skin... )"
            show location_mombed 2_3
            pause 5
            scene location_mombed04
            mom "!!!" with hpunch
            scene location_mombed05
            mom "Again!"
            player_name "{b}[mom_name]{/b}!!"
            scene mom_bedroom_closeup
            show player 150 zorder 1 at left
            show mom 16 at right with dissolve
            mom "Sweetie!"
            show mom 25b at Position(xpos = 810, ypos = 768) with dissolve
            mom "You're going to ruin all my nice panties!"
            show mom 26 zorder 0 at Position(xpos = 610) with dissolve
            show player 151
            player_name "Sorry, I just... I can't seem to stop."
            show player 150
            show mom 25
            mom "It's alright. You're a man and you have urges..."
            mom "Want me to give you another little show to help speed things up?"
            show mom 26
            show player 154
            player_name "!!!"
            show player 149
            player_name "Really?"
            player_name "Yeah!"
            show player 150 zorder 0
            show mom 25b zorder 1 at Position(xpos = 810) with dissolve
            mom "Alright, Sweetie."
            show mom 19 at right with dissolve
            pause
            show mom 21 with dissolve
            pause
            show mom 22b with dissolve
            pause
            show mom 23d with dissolve
            pause
            show mom 23e
            mom "How do I look?"
            show mom 23d
            show player 149
            player_name "Beautiful..."
            show player 150
            show mom 24b
            show player 155_156_156b_156 with dissolve
            pause
            pause
            player_name "Oh, {b}[mom_name]{/b}! You're so sexy!"
            show player 157_158_159 with flash
            show mom 24c
            mom "!!!{p=1.5}{nw}"
            show player 161 with dissolve
            show mom 24b
            mom "That almost made it all the way over here!"
            show mom 23d
            show player 160
            player_name "You're the best {b}[mom_name]{/b}..."
            show player 161
            show mom 23e
            mom "I better be for letting you do this!"
            mom "Now, come over here and give me a hug."
            show mom 23d
            hide player
            show mom 28
            with dissolve
            mom "Love you."
            show mom 29
            player_name "Love you, too."
        else:

            player_name "( These feel so soft against my skin... )"
            show location_mombed 2_3
            player_name "( Oh, this is just what I needed... )"
            pause 5
            scene location_mombed04
            mom "!!!" with hpunch
            scene location_mombed05
            mom "Oh my..."
            player_name "{b}[mom_name]{/b}!!"
            scene mom_bedroom_closeup
            show player 152 at left with dissolve
            show mom 16 at right with dissolve
            mom "{b}Again{/b}!!?"
            show mom 20
            pause
            mom "..."
            show player 150 zorder 1
            show mom 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
            pause 1
            show mom 25 at Position(xpos =0.58, ypos = 768) with dissolve
            mom "Sweetie, we talked about this."
            if M_mom.get_state() != S_mom_panties_masturbation_again:
                jump mom_jerk_repeat
            mom "You promised you wouldn't do this in my room!"
            menu:
                "Sorry.":
                    show mom 26
                    show player 151
                    player_name "I'm sorry, {b}[mom_name]{/b}..."
                    player_name "I don't know what came over me!"
                    player_name "...It won't happen again, I promise!"
                    show mom 27
                    show player 152
                    mom "Oh, Sweetie..."
                    show mom 25
                    mom "...Just please, try and do it elsewhere from now on."
                    mom "Can you do that for Mommy?"
                    show mom 26
                    show player 151
                    player_name "Yes, {b}[mom_name]{/b}..."
                "I can't help it!":

                    show mom 26
                    show player 151
                    player_name "I'm sorry, [mom_name]... It just {b}feels so good{/b}..."
                    show mom 27
                    show player 152
                    mom "I know Sweetie... But it's not right you doing it in my bed... And with my clothes!"
                    show mom 25
                    mom "Why can't you find another outlet to release your... {b}Energy{/b} with?"
                    mom "What about the girls at your school, don't you like any of them?"
                    menu:
                        "I'm trying.":
                            show mom 26
                            show player 151
                            player_name "I'm trying, {b}[mom_name]{/b}..."
                            player_name "...It's not easy to meet girls sometimes..."
                            show player 152
                            mom "..."
                            show mom 25
                            mom "Have you... asked any of them on dates?"
                            show mom 26
                            show player 149
                            player_name "What?"
                            player_name "I can't just... do it like that..."
                            show mom 25
                            show player 152
                            mom "Well, you have to make an effort, Sweetie!"
                            show mom 26
                            show player 151
                            player_name "I will, {b}[mom_name]{/b}..."
                            show mom 25
                            show player 152
                            mom "As long as you're trying..."
                            show mom 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
                            mom "Come here..."
                            hide player
                            show mom 28
                            with dissolve
                            player_name "..."
                            mom "I love you so much, Sweetie..."
                            show mom 29
                            player_name "I love you too, {b}[mom_name]{/b}!"
                        "Not really.":

                            show mom 26
                            show player 151
                            player_name "I dunno... Not really..."
                            player_name "...I just haven't found one that I like, I guess."
                            mom "..."
                            show mom 25
                            show player 152
                            mom "What about the girls in the neighborhood?"
                            show mom 27
                            show player 150
                            mom "Or the neighbor girl? What's her name..."
                            show mom 26
                            show player 151
                            player_name "{b}Mia{/b}..."
                            show mom 25
                            show player 152
                            mom "Yeah! What about {b}Mia{/b}?"
                            show mom 26
                            show player 151
                            player_name "I dunno... Maybe..."
                            show mom 25
                            show player 152
                            mom "Well, you have to make an effort, Sweetie!"
                            show mom 26
                            show player 151
                            player_name "I will, {b}[mom_name]{/b}..."
                            show mom 25
                            show player 152
                            mom "As long as you're trying..."
                            show mom 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
                            mom "Come here..."
                            hide player
                            show mom 28
                            with dissolve
                            player_name "..."
                            mom "I love you so much, Sweetie..."
                            show mom 29
                            player_name "I love you too, {b}[mom_name]{/b}!"
                        "I like you.":

                            label mom_jerk_repeat:
                            $ M_mom.set("sex speed", .15)
                            $ M_mom.set("no panties", False)
                            if where_is("mom") == "Basement":
                                $ M_mom.set("no panties", True)
                            show mom 30
                            show player 149
                            if M_mom.get_state() == S_mom_panties_masturbation_again:
                                player_name "I like you..."
                            else:
                                player_name "But I can't get you out of my head..."
                            show player 152
                            mom "..."
                            if M_mom.get_state() == S_mom_panties_masturbation_again:
                                show mom 25
                                show player 150
                                mom "But Sweetie... I'm your {b}[mom]{/b}!"
                                show mom 30
                                show player 149
                                player_name "I know! But all I can think about is you..."
                                show player 151
                                player_name "...And I don't like the girls at school..."
                                show player 152
                                mom "..."
                                show mom 25
                                mom "I..."
                                show mom 26
                                mom "..."
                                show player 150
                                show mom 25
                                mom "This is my fault..."
                                mom "... All that kissing..."
                                show mom 27
                                mom "Oh, god... and the thing in the Car."
                                show mom 27
                                mom "..."
                                mom "I'm a terrible Mother..."
                                show mom 26
                                show player 149
                                player_name "It's not your fault, {b}[mom_name]{/b}..."
                                show mom 30
                                show player 151
                                player_name "It's me! I just don't want anyone else!"
                                player_name "Maybe there's something wrong with me..."
                                show mom 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
                                pause.4
                                show mom 15 at Position(xpos=0.8, ypos=1.0) with dissolve
                                show player 150
                                player_name "..."
                                show mom 17
                                mom "{b}*Sigh*{/b}"
                                show mom 18
                                mom "Sweetie, there's nothing wrong with you."
                                mom "You're just confused... That's all."
                            if M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 17 at Position(xpos=0.8, ypos=1.0) with dissolve
                            mom "... Maybe you just need to get this out of your system?"
                            show mom 15
                            if M_mom.get_state() == S_mom_panties_masturbation_again:
                                show player 149
                                player_name "What do you mean?"
                                show mom 18
                                mom "I'm going to do this but {b}only once, alright{/b}?"
                                show mom 17
                                mom "And you have to promise me that you'll try harder to talk with girls at school!"
                                show mom 19
                                show player 149
                                player_name "What are you gonna do?"
                            show player 154
                            show mom 21
                            window hide
                            pause
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 22b
                            else:
                                show mom 22
                            window hide
                            pause
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 23b with hpunch
                            else:
                                show mom 23 with hpunch
                            window hide
                            pause
                            player_name "!!!"
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 23e
                            else:
                                show mom 31
                            mom "Go ahead, Sweetie. Finish what you started..."
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 23b
                            else:
                                show mom 23
                            show player 149
                            player_name "...You mean it's okay?!!"
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 23e
                            else:
                                show mom 31
                            show player 150
                            if M_mom.get_state() == S_mom_panties_masturbation_again:
                                mom "It's okay, {b}just this once{/b}!"
                            else:
                                mom "Just {b}do it{/b}. It's okay..."
                                show mom 23b
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show player 149
                                player_name "{b}[mom_name]{/b}..."
                                player_name "...You're not wearing panties?"
                                show player 150
                                show mom 23c
                                pause
                                show mom 23e
                                mom "What's that?"
                                mom "Oh! My panties?"
                                mom "I guess I just...forgot!"
                                show mom 23d
                                player_name "..."
                                show mom 23e
                                mom "Does it...help?"
                                show mom 23d
                                show player 149
                                player_name "I like it."
                            else:

                                show mom 23
                                show player 155 with dissolve
                                player_name "O-okay..."
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show player 155_156_156b_156
                            else:
                                show player medmo 155_156_156b
                            pause
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 24d
                            else:
                                show mom 24
                            player_name "Oh, [mom_name]..."
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 24b
                            else:
                                show mom 24f
                            mom "Oh my..."
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 24d
                            else:
                                show mom 24
                            pause
                            player_name "[mom_name]!!! I'm gonna-"
                            mom "..."
                            show player 157 with flash
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 24c
                            else:
                                show mom 24e
                            player_name "Hnngg!!"
                            pause .4
                            show player 158
                            pause .4
                            show player 159
                            pause 1
                            show player 157
                            pause .4
                            show player 158
                            pause .4
                            show player 159
                            pause 1
                            show player 157
                            pause .4
                            show player 158
                            pause .4
                            show player 159
                            pause .2
                            show player 160 with dissolve
                            player_name "huuuh, huuuh, huuuuh..."
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 24b
                            else:
                                show mom 24f
                            mom "Wow, that was alot!"
                            player_name "..."
                            show player 161
                            if M_mom.is_set("no panties") and M_mom.get_state() != S_mom_panties_masturbation_again:
                                show mom 22b
                            else:
                                show mom 22
                            window hide
                            pause
                            show mom 21
                            window hide
                            pause
                            if M_mom.get_state() == S_mom_panties_masturbation_again:
                                show mom 16
                                mom "You have to make an effort to meet other girls now... {b}Promise{/b}?"
                                show mom 15
                                show player 160
                                player_name "Yeah..."
                                show mom 17
                                show player 161
                                mom "This was just a {b}one time thing{/b}... To get it out of your system..."
                            show mom 17
                            mom "Come here..."
                            hide player
                            show mom 28 with dissolve
                            pause
                            show mom 29
                            player_name "..."
                            show mom 28
                            mom "I love you so much, Sweetie..."
                            show mom 29
                            player_name "I love you too, {b}[mom_name]{/b}!"
                            $ M_mom.trigger(T_mom_caught_masturbating)
        $ M_mom.set("panties taken", False)
        $ gTimer.tick()
        $ unlock_ui()
        hide mom
        hide player
        with dissolve

    elif M_mom.is_set("sleep together") and gTimer.is_dark():
        scene mom_bedroom_closeup_sex
        if M_mom.is_set("sex available"):
            show player 109 at right
            show mom 83 at left
            with dissolve
            mom "..."
            show mom 81
            mom "{b}[firstname]{/b}?"
            mom "Is everything okay?"
            show player 111
            player_name "Hey, {b}[mom_name]{/b}."
            show player 108
            player_name "I'm just having trouble sleeping..."
            player_name "All I can think about is being inside you."
            show player 109
            show mom 81
            mom "It's okay."
            mom "You have too much energy that needs... releasing."
            mom "Come inside, {b}Mommy{/b} knows exactly what to do."
            show mom 82
            show player 108
            player_name "You sure?"
            show mom 81
            show player 110
            mom "Oh, yes... {b}Mommy{/b} needs it, too."
            scene mom_cuddle
            show moms 77
            with fade

            player_name "Thanks, {b}[mom_name]{/b}."
            show moms_bed_overlay zorder 3 at Position(xpos=438)
            show moms 79 zorder 2 at Position(xpos=365)
            with dissolve
            player_name "I couldn't sleep... I was so horny thinking about you..."
            player_name "...And I wanted to be in you again."
            show moms 80
            mom "It's perfectly normal, Sweetie."
        else:

            show player 109 at right
            show mom 83 at left
            with dissolve
            mom "..."
            show mom 81
            mom "{b}[firstname]{/b}?"
            mom "Is everything okay?"
            show mom 82
            show player 111
            player_name "Yes, {b}[mom_name]{/b}."
            show player 108
            player_name "I'm just having trouble sleeping..."
            show player 109
            show mom 81
            mom "Oh..."
            mom "I understand Sweetie... It's been hard lately."
            mom "I've also had trouble sleeping with everything that happened..."
            show mom 83
            mom "...And not having someone by my side at night."
            show mom 82
            show player 108
            player_name "Do you mind?"
            show player 109
            show mom 83
            mom "{b}*Sigh*{/b}"
            show mom 81
            show player 110
            mom "Just for a little while... then you have to go back to your room, okay?"
            show mom 82
            show player 111
            player_name "Yes, {b}[mom_name]{/b}."
            scene mom_cuddle
            with fade
            show moms 77
            with fade
            player_name "Thanks, {b}[mom_name]{/b}."
            show moms_bed_overlay zorder 3 at Position(xpos=438)
            show moms 79 zorder 2 at Position(xpos=365)
            with dissolve
            player_name "I like being close like this..."
            player_name "...And your bed is always so warm."
            show moms 80
            mom "I know Sweetie, but you can't be in here all the time..."
            show moms 79
            player_name "I know..."
        $ gTimer.tick()
        label mom_sleep_options:
            menu:
                "Cuddle":
                    if M_mom.is_set("sex available"):
                        show moms 79
                        player_name "Can we cuddle a little bit?"
                        show moms 80
                        mom "Of course."
                        show moms 83 with dissolve
                        player_name "You smell really good, {b}[mom_name]{/b}..."
                        show moms 84
                        mom "Thanks, Sweetie."
                        show moms 81_82 with dissolve
                        pause 4
                        show moms 81
                    else:

                        show moms 79
                        player_name "Can we... cuddle a little bit?"
                        show moms 80
                        mom "Sure, Sweetie."
                        show moms 81_82 with dissolve
                        mom "!!!"
                        mom "( He's... caressing my hips... )"
                        mom "( And moving closer between my legs... )"
                        mom "( He's never been this affectionate... )"
                        show moms 83
                        player_name "You smell really good, {b}[mom_name]{/b}..."
                        show moms 82
                        mom "..."
                        show moms 84
                        mom "Thanks, Sweetie."
                        show moms 82
                    label cuddle_options:
                        menu:
                            "Keep going":
                                show moms 81_82
                                pause 4
                                show moms 81
                                jump cuddle_options
                            "Stop.":

                                show moms 79 with dissolve
                                jump mom_sleep_options
                "Ask for a kiss":

                    if M_mom.is_set("sex available"):
                        show moms 83
                        player_name "Can we kiss?"
                        show moms 84
                        mom "You don't even have to ask, Sweetie."
                        mom "Come here..."
                        show moms 85_86 with dissolve
                        pause 4
                        show moms 81 with dissolve
                    else:

                        show moms 83
                        player_name "{b}[mom_name]{/b}..."
                        show moms 84
                        mom "Yes?"
                        show moms 83
                        player_name "You think I could have a kiss?"
                        show moms 84
                        mom "A kiss?"
                        mom "On your cheek?"
                        show moms 83
                        player_name "No, like... A real kiss."
                        show moms 81
                        mom "..."
                        show moms 83
                        player_name "I've just never really done it with anyone other than you before..."
                        show moms 84
                        mom "Never?"
                        show moms 83
                        player_name "No..."
                        player_name "But I always wanted to try it more."
                        show moms 84
                        mom "I... I suppose I could teach you again."
                        mom "But just on the lips, okay?"
                        show moms 83
                        player_name "Okay..."
                        show moms 85_86 with hpunch
                        mom "!!!"
                        mom "( I can feel his tongue. )"
                        mom "( But I can't just, stop... )"
                        mom "( Wow, he's really into it... and not bad at it. )"
                        mom "( Ohh... )"
                        mom "( His hands are pressing againt my breasts... and... )"
                        mom "( His knee, rubbing on my... )"
                        mom "( I feel so... Hot, right now. )"
                        show moms 83 with dissolve
                        player_name "...How was I?"
                        show moms 84
                        mom "..."
                        mom "You were... quite, good."
                        show moms 83
                        player_name "I could feel you shaking, {b}[mom_name]{/b}."
                        show moms 84
                        mom "I... I must be getting too warm. That's all."
                        show moms 81 with dissolve
                    label kiss_options:
                        menu:
                            "Keep going":
                                show moms 85_86 with dissolve
                                pause 4
                                show moms 81 with dissolve
                                jump kiss_options
                            "Stop.":

                                show moms 79 with dissolve
                                jump mom_sleep_options
                "Breastfeed":

                    if M_mom.is_set("sex available"):
                        show moms 83
                        player_name "Can I... suck on your breasts?"
                        show moms 87 with dissolve
                        mom "Just... be gentle."
                        show moms 88_89 at Position(xpos=329) with dissolve
                        pause 4
                        show moms 89 at Position(xpos=327)
                    else:

                        show moms 83
                        player_name "Can I... kiss you elsewhere?"
                        show moms 84
                        mom "Elsewhere?"
                        show moms 83
                        player_name "I want to kiss your chest... and your breasts..."
                        show moms 84
                        mom "But, Sweetie..."
                        show moms 83
                        player_name "Just a little, I promise."
                        show moms 84
                        mom "..."
                        show moms 87 with dissolve
                        mom "Just... Be gentle."
                        show moms 88_89 at Position(xpos=329) with dissolve
                        mom "( He's moving lower... )"
                        mom "( ...And grabbing onto my legs? )"
                        mom "( Ahhh...!! )" with hpunch
                        mom "( Oh, my... )"
                        mom "( He's sucking on my nipples and licking my breasts! )"
                        mom "( I can't believe how... good this feels... )"
                        mom "( He's latched onto me so tight... I love the feeling... )"
                        show moms 88 at Position(xpos=329)
                    label breastfeed_options:
                        menu:
                            "Keep going":
                                show moms 88_89 at Position(xpos=329) with dissolve
                                pause 4
                                show moms 88 at Position(xpos=329)
                                jump breastfeed_options
                            "Stop.":

                                show moms 79 with dissolve
                                jump mom_sleep_options
                "Rub":

                    if M_mom.is_set("sex available"):
                        show moms 90 at Position(xpos=327) with dissolve
                        mom "Yes, Sweetie."
                        show moms 91 with dissolve
                        mom "Take it out, and place it between my legs..."
                        show moms 92 with dissolve
                        pause
                        show moms 93_94 at Position(xpos=329) with dissolve
                        mom "You're so nice and hard, now."
                        mom "I can feel it..."
                        mom "Keep moving your hips, Sweetie."
                        mom "It feels so good..."
                        mom "Ahhh.."
                        pause
                        show moms 93_94 at Position(xpos=329)
                        pause 4
                        show moms 94 at Position(xpos=327)
                    else:

                        show moms 90 at Position(xpos=327) with dissolve
                        mom "( What is he... )"
                        show moms 91 with dissolve
                        mom "..."
                        show moms 92 with dissolve
                        mom "( He took it out... )"
                        mom "( And I can feel it on my leg! )"
                        mom "( I should be stopping him but... )"
                        mom "( ...I can't resist the urge to feel it against me. )"
                        show moms 93_94 at Position(xpos=329) with hpunch
                        mom "( Ahhh...! )"
                        mom "( It's rubbing against my clit... )"
                        mom "( It's so hard! )"
                        mom "( OH!! )"
                        mom "( He's trusting his hips back and forth... )"
                        mom "( Against my pussy, as if he was trying to... )"
                        mom "( Ahhh... this feels so good! I might... cum... )"
                        mom "( This is too much!! )"
                        show moms 93 at Position(xpos=329)
                    label rub_options:
                        menu:
                            "Keep going":
                                show moms 93_94 at Position(xpos=329) with dissolve
                                pause 4
                                show moms 93 at Position(xpos=329)
                                jump rub_options
                            "Stop.":

                                show moms 79 with dissolve
                                jump mom_sleep_options

                "Fuck" if M_mom.is_set("sex available"):
                    $ anim_toggle = False
                    $ xray = False
                    show moms 95 with dissolve
                    if randomizer() <= 50:
                        mom "Let me help you Sweetie..."
                        mom "...Now, slide it inside me... deep."
                        show moms 96 with dissolve
                        mom "Just like that... Yes, Sweetie..."
                    else:
                        mom "I can't take all the teasing like that."
                        mom "I want you to bury that big cock in me."
                        mom "Don't go slow..."
                        mom "You've teased me enough."
                        show moms 96 with dissolve
                        pause
                    show moms 98 at Position(xpos=327) with dissolve
                    if randomizer() <= 50:
                        mom "AHH!"
                    else:
                        mom "Ohh..."
                    show screen xray_scr
                    pause
                    if anim_toggle:
                        hide screen xray_scr
                        show moms 97_98 at Position(xpos=329)
                        mom "Oh, yes!{p=1}{nw}"
                        mom "Yes, Sweetie...{p=1}{nw}"
                        mom "Keep going...{p=1}{nw}"
                        mom "Deeper... Faster!!{p=1}{nw}"
                    else:

                        hide screen xray_scr
                        show moms 97 at Position(xpos=329)
                        mom "Oh, yes!"
                        show moms 98 at Position(xpos=327)
                        mom "Yes, Sweetie..."
                        show moms 97 at Position(xpos=329)
                        mom "Keep going..."
                        show moms 98 at Position(xpos=327)
                        mom "Deeper... Faster!!"
                        show moms 97 at Position(xpos=329)
                    show moms 97 at Position(xpos=329)
                    label mom_fuck_options:
                        menu:
                            "Keep going":
                                show moms 98 at Position(xpos=327)
                                show screen xray_scr
                                pause
                                if anim_toggle:
                                    hide screen xray_scr
                                    show moms 97_98 at Position(xpos=329)
                                    pause 4
                                else:

                                    hide screen xray_scr
                                    $ animcounter = 0
                                    while (animcounter < 4):
                                        show moms 97 at Position(xpos=329)
                                        pause
                                        show moms 98 at Position(xpos=327)
                                        pause
                                        $ animcounter += 1
                                show moms 97 at Position(xpos=329)
                                jump mom_fuck_options
                            "Cum":

                                mom "AAHH!!!"
                                show white zorder 4
                                show moms 99 at Position(xpos=327) with vpunch
                                hide white with dissolve
                                if randomizer() <= 50:
                                    mom "YES baby..."
                                    $ xray = False
                                    show moms 98 at Position(xpos=327) with dissolve
                                    mom "{b}*Huffing*{/b}"
                                    mom "Stay inside me a bit longer..."
                                    mom "I like feeling your cum inside me."
                                    show moms 100 with fade
                                    mom "You came so much..."
                                    player_name "Was it... wrong?"
                                    mom "It's okay... {b}Mommy{/b} will be fine."
                                else:
                                    $ xray = False
                                    show moms 98 at Position(xpos=327) with dissolve
                                    mom "Oh, baby..."
                                    show moms 100 with fade
                                    mom "I didn't think you were going to stop..."
                                    mom "That was great..."

                                show moms 80 at Position(xpos=329) with fade
                                if randomizer() <= 50:
                                    mom "Please stay with me tonight."
                                else:
                                    mom "Are you sleeping here tonight?"
                                show moms 79
                                menu:
                                    "Stay.":
                                        player_name "Alright, {b}[mom_name]{/b}."
                                        show moms 80
                                        mom "Good boy."
                                        hide moms
                                        hide moms_bed_overlay
                                        scene black
                                        with fade
                                        jump mom_sleeping
                                    "Leave.":

                                        player_name "I can't. Maybe tomorrow."
                                        show moms 80
                                        mom "Aww... Well don't be shy."
                                        scene black
                                        hide moms
                                        hide moms_bed_overlay
                                        with fade
                                        pause
                                        scene mom_bedroom_closeup
                                        show player 111 at right
                                        show mom 82 at left
                                        with dissolve
                                        player_name "Goodnight, {b}[mom_name]{/b}."
                                        show player 110
                                        show mom 81
                                        mom "Goodnight, Sweetie."
                                        mom "I love you."
                                        show mom 82
                                        show player 111
                                        player_name "Love you too, {b}[mom_name]{/b}."
                                        hide player
                                        hide mom
                                        with dissolve
                                        $ location_count = "Living Room"
                "Sleep with {b}[mom_name]{/b}.":

                    show moms 79 with dissolve
                    player_name "Goodnight, {b}[mom_name]{/b}..."
                    show moms 80 with dissolve
                    mom "Goodnight, {b}[firstname]{/b}..."
                    hide moms
                    hide moms_bed_overlay
                    jump mom_sleeping

    elif gTimer.is_dark():
        scene mom_bedroom_night
        show player 106 with dissolve
        player_name "( Should I sneak into her bed? )"
        show player 34
        player_name "Hmm..."
        player_name "( I shouldn't bother her when she's sleeping... )"
        hide player with dissolve
    else:

        scene mom_bedroom
        show player 1 with dissolve
        player_name "( It felt so good, jerking off in her bed. )"
        player_name "( ... Just utterly enveloped in her scent. )"
        show player 5
        player_name "( But I promised her I wouldn't do that again. )"
        player_name "( I should really try my hardest to keep that promise. )"
        hide player with dissolve
    $ callScreen(location_count)

label mom_sleeping:
    scene location_mombedroom_blur_night_sleep with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    hide unlock11 with dissolve
    scene black with fade
    hide location_mombedroom_blur_night_sleep with fade

    $ Sleep()
    if M_mom.is_set("sex available"):
        if randomizer() <= 50:
            scene mom_bedroom
            show player 7 with dissolve
            player_name "{b}*Yawn*{/b}"
            show player 101 with dissolve
            player_name "Looks like {b}[mom_name]{/b} is already up."
            show player 8 with dissolve
            pause
            show player 14 with dissolve
            player_name "I better sneak out of here, so {b}[sis_name]{/b} doesn't see me."
        else:

            scene mom_bedroom_closeup2
            show mom 83 at left
            show player 7 at right
            with dissolve
            player_name "{b}*Yawn*{/b}"
            show player 8 with dissolve
            show mom 81
            mom "Morning, {b}[firstname]{/b}."
            show mom 82
            show player 22 with hpunch
            player_name "!!!"
            show player 108 with dissolve
            player_name "Morning! Did I wake you?"
            show player 109
            show mom 82
            mom "No, Sweetie."
            mom "I was too enjoying you next to me."
            show mom 81
            show player 111
            player_name "Yeah, it was nice sleeping with you. Your bed has softer pillows."
            show player 110
            show mom 81
            mom "Right."
            mom "I suppose I better get up too, then."
            mom "Thanks again for sleeping with me."
            show mom 82
            show player 111
            player_name "You're welcome. Love you, {b}[mom_name]{/b}."
            show player 110
            show mom 81
            mom "I love you too, Sweetie."
        hide mom
        hide player
        with dissolve
    jump mom_bedroom

label mom_room_laundry:
    scene mom_bedroom
    show player 276 with dissolve
    player_name "I should take this down to the {b}basement{/b}."
    hide player with dissolve
    $ M_mom.trigger(T_mom_got_laundry)
    $ callScreen(location_count)

label mom_sex:
    $ M_mom.set("sex speed", .4)
    $ M_mom.set("change angle", False)
    $ mom_sex_position = "missionary"
    $ cum = False
    $ anim_toggle = False
    $ xray = False
    $ first_time_cowgirl = True
    $ first_time_suck_tits = True
    show moms 106 at left
    with fade
    mom "Now, start nice and slow, Sweetie."
    show moms 103 with dissolve
    pause
    show moms 104 with dissolve
    mom "Aahh..."
    show moms 104 at left

    label missionary_loop:
        hide screen mom_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        scene mom_bedroom_closeup_sex
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                hide moms
                hide moms_xray
                if xray:
                    show moms_xray 65_66_67_66 at Position(ypos = 1034)
                else:
                    show moms 103_104_105_104 at Position(xpos = 450)
                pause 5
                if randomizer() <= 33:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, Sweetie!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                elif randomizer() <= 66:
                    if animcounter == 1:
                        mom "Oh...{p=1}{nw}"
                    if animcounter == 2:
                        mom "Give it to me, Sweetie.{p=2}{nw}"
                        player_name "You like that?{p=2}{nw}"
                        mom "Yesss....{p=1}{nw}"
                    if animcounter == 3:
                        mom "Ahh!{p=1}{nw}"
                else:
                    if animcounter == 2:
                        mom "Faster, Sweetie!{p=2}{nw}"
                        mom "{b}Mommy's{/b} almost there!{p=2}{nw}"
                        player_name "Oh, {b}[mom_name]{/b}! I can feel you clenching down on me!{p=2}{nw}"
                    if animcounter == 3:
                        mom "Ahh!!!{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                show moms 103 at left
                pause
                show moms 104
                pause
                show moms 105
                pause
                show moms 104
                pause
                $ animcounter += 1
                if randomizer() <= 33:
                    if animcounter == 1:
                        mom "Ahhhh!!!"
                    if animcounter == 3:
                        mom "Oh, Sweetie!!!"
                        player_name "Uhhh..."
                elif randomizer() <= 66:
                    if animcounter == 1:
                        mom "Oh..."
                    if animcounter == 2:
                        mom "Give it to me, Sweetie."
                        player_name "You like that?"
                        mom "Yesss...."
                    if animcounter == 3:
                        mom "Ahh!"
                else:
                    if animcounter == 2:
                        mom "Faster, Sweetie!"
                        mom "{b}Mommy's{/b} almost there!"
                        player_name "Oh, {b}[mom_name]{/b}! I can feel you clenching down on me!"
                    if animcounter == 3:
                        mom "Ahh!!!{p=1}{nw}"

        show screen mom_sex_options
        pause
        jump missionary_loop

    label mom_missionary_cum:
        hide screen xray_scr
        hide screen mom_sex_options
        hide moms_xray
        if randomizer() <= 50:
            show moms 103 at left
            player_name "{b}[mom_name]{/b}, I'm gonna..."
            mom "Let it out, Sweetie!"
            show moms 105 with hpunch
            player_name "{b}[mom_name]{/b}!!!"
            show white with dissolve
            $ cum = True
            hide white with dissolve
            mom "Ahhh!!!"
            hide screen xray_scr
            mom "Yes!"
            mom "Stay inside {b}Mommy{/b} for a while..."
            show moms 106 with fade
            $ xray = False
            mom "You let out so much..."
        else:
            show moms 105 at left with hpunch
            player_name "Oh, {b}[mom_name]{/b}!"
            show white with dissolve
            $ cum = True
            hide white with dissolve
            mom "Ahh!!!"
            hide screen xray_scr
            mom "Oh, Sweetie..."
            mom "That was intense..."
            player_name "That felt good."
            mom "Yeah..."
            mom "Oh, Sweetie. You are good."
            show moms 106 with fade
            $ xray = False
            mom "Your still so stiff..."
            mom "I bet you could go again!"
        jump after_sex

    label mom_missionary_cum_outside:
        hide screen xray_scr
        hide screen mom_sex_options    
        if randomizer() <= 50:
            show moms 103
            player_name "{b}[mom_name]{/b}, I'm gonna..."
            mom "Let it out, Sweetie!"
            hide screen xray_scr
            $ xray = False
            show moms 107 with dissolve
            show white with dissolve
            show playersex 70 at Position(xpos=568, ypos=348)
            hide white with dissolve
            pause
            show playersex 71 at Position(xpos=612, ypos=450)
            pause
            hide playersex
            show moms 108
            mom "Oh!!!"
            mom "Wow!"
            mom "Go get {b}Mommy{/b} some tissues so she can clean herself, will you?"
            player_name "Yes, {b}[mom_name]{/b}. Sorry about the mess..."
        else:
            show moms 103
            player_name "{b}[mom_name]{/b}, can I cum on top of you?"
            mom "Yes, Sweetie!"
            hide screen xray_scr
            $ xray = False
            show moms 107 with dissolve
            show white with dissolve
            show playersex 70 at Position(xpos=568, ypos=348)
            hide white with dissolve
            pause
            show playersex 71 at Position(xpos=612, ypos=450)
            pause
            hide playersex
            show moms 108
            mom "Oh!"
            mom "I didn't think it'd be that much!"
            mom "I'm going to have to change the sheets!"
            player_name "Sorry..."
            mom "Don't be. I like being showered in my man's cum."
        jump after_sex

    label suck_tits:
        hide screen mom_sex_options
        scene mom_bedroom_closeup_sex
        if first_time_suck_tits and randomizer() <= 50:
            $ first_time_suck_tits = False
            show moms 67 at left with dissolve
            player_name "I want to suck your tits."
            show moms 68
            mom "Be gentle."
            mom "They're sensitive."
        show moms 67 at left
        show screen xray_scr
        pause
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                hide screen xray_scr
                hide screen mom_sex_options
                show moms 68_67 at left
                if randomizer() <= 33:
                    if animcounter == 2:
                        mom "Yes, Sweetie....{p=1}{nw}"
                        mom "Keep sucking on them.{p=1}{nw}"
                if randomizer() <= 66:
                    if animcounter == 1:
                        mom "Mmmm...{p=1}{nw}"
                    if animcounter == 2:
                        mom "Oh!{p=1}{nw}"
                        mom "Gentle, Sweetie!{p=1}{nw}"
                else:
                    if animcounter == 3:
                        mom "Oh, baby...{p=1}{nw}"
                        mom "You like sucking {b}Mommy's{/b} titties?{p=2}{nw}"
                        player_name "Mmhmm..{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                hide screen xray_scr
                hide screen mom_sex_options
                show moms 68 at left
                pause
                show moms 67
                pause
                if randomizer() <= 33:
                    if animcounter == 2:
                        mom "Yes, Sweetie...."
                        mom "Keep sucking on them."
                if randomizer() <= 66:
                    if animcounter == 1:
                        mom "Mmmm..."
                    if animcounter == 2:
                        mom "Oh!"
                        mom "Gentle, Sweetie!"
                else:
                    if animcounter == 3:
                        mom "Oh, baby..."
                        mom "You like sucking {b}Mommy's{/b} titties?"
                        player_name "Mmhmm.."
                $ animcounter += 1

        show screen mom_sex_options
        pause
        jump suck_tits

    label cowgirl_loop:
        hide screen mom_sex_options
        if first_time_cowgirl:
            $ first_time_cowgirl = False
            show moms 62 at left with dissolve
            if randomizer() <= 50:
                mom "Lay back and let {b}Mommy{/b} take a turn."
            else:
                mom "You just like watching my tits bounce don't you, my naughty boy?"
        show screen xray_scr
        pause
        hide screen xray_scr
        scene mom_bedroom_closeup_sex
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                hide moms
                hide moms_xray
                if M_mom.get("change angle"):
                    scene bedroom_sex_05
                    show moms 170_171_172_173_174_175_176_177
                else:
                    scene mom_bedroom_closeup_sex
                    if xray:
                        show moms_xray 58_59_57 at Position(ypos = 849)
                    else:
                        show moms 65_66_64 at Position(xpos = 476)
                pause 5
                if randomizer() <= 50:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, Sweetie!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                else:
                    if animcounter == 2:
                        mom "You like this?{p=2}{nw}"
                        player_name "Yeah...{p=1}{nw}"
                        mom "I do too...{p=2}{nw}"
                        mom "I can really feel you deep inside me like this.{p=2}{nw}"
                    if animcounter == 3:
                        mom "Ahh!!!{p=1}{nw}"
                        mom "Oh, baby...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                if M_mom.get("change angle"):
                    scene bedroom_sex_05
                    show moms 170
                    pause
                    show moms 171
                    pause
                    show moms 172
                    pause
                    show moms 173
                    pause
                    show moms 174
                    pause
                    show moms 175
                    pause
                    show moms 176
                    pause
                    show moms 177
                    pause
                else:
                    scene mom_bedroom_closeup_sex
                    show moms 65 at left
                    pause
                    show moms 66
                    pause
                    show moms 64
                    pause
                $ animcounter += 1
                if randomizer() <= 50:
                    if animcounter == 2:
                        mom "Ahhhh!!!"

                    if animcounter == 3:
                        mom "Oh, Sweetie!!!"
                        player_name "Uhhh..."
                else:
                    if animcounter == 2:
                        mom "You like this?"
                        player_name "Yeah..."
                        mom "I do too..."
                        mom "I can really feel you deep inside me like this."
                    if animcounter == 3:
                        mom "Ahh!!!"
                        mom "Oh, baby..."

        show screen mom_sex_options
        pause
        jump cowgirl_loop

    label mom_cowgirl_cum:
        hide screen xray_scr
        hide screen mom_sex_options
        hide moms_xray
        scene mom_bedroom_closeup_sex
        show moms 69 at left with vpunch
        player_name "{b}[mom_name]{/b}!!!"
        mom "Ahh!!!"
        show white with dissolve
        $ cum = True
        hide white with dissolve
        pause
        mom "Oh..."
        show moms 70 with dissolve
        mom "You should warn me when you're about to do it, Sweetie."
        player_name "Sorry, {b}[mom_name]{/b}."
        player_name "I just couldn't help it..."
        player_name "It felt too good..."
        mom "It's okay. Let's clean you up..."
        jump after_sex

    label mom_cowgirl_cum_outside:
        hide screen xray_scr
        hide screen mom_sex_options
        scene mom_bedroom_closeup_sex
        show moms 64 at left
        if randomizer() <= 50:
            player_name "{b}[mom_name]{/b}, I'm gonna..."
            show moms 109 with dissolve
            show white with dissolve
            show playersex 72 at Position(xpos=478, ypos=418)
            hide white with dissolve
            pause
            show playersex 73 at Position(xpos=524, ypos=478) with dissolve
            mom "Thanks for the warning, Sweetie."
            mom "Let's get ourselves cleaned up..."
        else:
            player_name "{b}[mom_name]{/b}! I'm..."
            show moms 109 with dissolve
            show white with dissolve
            show playersex 72 at Position(xpos=478, ypos=418)
            hide white with dissolve
            pause
            show playersex 73 at Position(xpos=524, ypos=478) with dissolve
            mom "!!!"
            player_name "Where'd my cum land?"
            mom "Ha Ha Ha..."
            mom "I can feel it all over my tits, Sweetie."
            mom "I thought I could avoid getting all messy."
        jump after_sex

    label after_sex:
        scene mom_bedroom
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
            player_name "No, it's fine, {b}[mom_name]{/b}."
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
        show mom 80
        with dissolve
        pause
        show mom 79 with dissolve
        pause
        show mom 80 with dissolve
        pause
        show player 228 at Position(xpos=200)
        show mom 78
        with dissolve
        player_name "I love you, {b}[mom_name]{/b}!"
        show player 227
        show mom 75
        mom "I love you too, Sweetie..."
        hide mom
        hide player
        with dissolve
        $ unlock_ui()
        $ gTimer.tick()
        $ mom_dialogue_advance = True
    $ callScreen(location_count)

label missionary_mom_faster_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') - 0.1)
    jump missionary_loop

label missionary_mom_slower_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') + 0.1)
    jump missionary_loop

label cowgirl_mom_faster_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') - 0.1)
    jump cowgirl_loop

label cowgirl_mom_slower_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') + 0.1)
    jump cowgirl_loop