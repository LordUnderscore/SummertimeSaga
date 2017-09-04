default caught = False
default mom_had_sex = False
default saw_mom_masturbate = False
default mom_sex_position = "missionary"
default mom_room_first_visit = True

label mom_masturbating:
    $ location_count = "Living Room"
    show mom_peek_sequence 2_3 zorder 3
    player_name "WHA-!!"
    player_name "{b}Mom{/b}?!?"
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
    scene home_livingroom_c
    show player 107 at left
    with fade
    player_name "( This is... I'm feeling... )"
    player_name "( ...so aroused by this. )"
    if not caught:
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
        sis "What's {b}Mom{/b} doing in there anyway?"
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
        sis "...You fantasize about {b}Mom{/b}... And your older {b}Sister{/b}?"
        show player 83f at right
        show sis 11f at left
        player_name "Please, don't tell {b}Mom{/b} I was watching her..."
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
        hide home_livingroom_c
    $ caught = True
    $ mom_dialogue_advance = True
    $ saw_mom_masturbate = True
    $ callScreen(location_count)

label mom_bedroom:
    $ location_count = "Mom's Bedroom"
    if gTimer.is_dark():
        scene mom_peek_sequence_1_night
        player_name "( {b}Mom's{/b} sleeping. )"
        player_name "( I can't make any noise. )"
    elif mom_room_first_visit:
        scene mom_bedroom
        show player 35 at left
        with dissolve
        player_name "( Where would mom keep her panties? )"
        hide player
        with dissolve
        $ mom_room_first_visit = False

    elif not gTimer.is_dark() and mom_count < 8:
        if saw_mom_masturbate == True and mom_masturbating == True:
            scene mom_bedroom
            show player 1
            player_name "( That's where {b}Mom{/b} was masturbating. )"
            player_name "( I can’t stop thinking about the way she was laying on her bed... )"
            show player 11
            player_name "( I Wonder what her bed feels like... )"
            player_name "( ...and the way it smells... )"
            show player 13
            player_name "( ...I should try laying in it. )"
            hide player
            with dissolve
        else:

            scene mom_peek_sequence_1
            player_name "( {b}Mom's{/b} not in her room. )"
            player_name "( She's probably in the shower or something... )"
    $ callScreen(location_count)

label mom_drawer:
    if not gTimer.is_dark():
        scene mom_drawer with None
        if not moms_panties_taken:
            show expression "objects/object_panties_02.png" at Position(xpos=260, ypos=690)
        player_name "( {b}Mom's{/b} lingerie... )"
        hide expression "objects/object_panties_02.png"
        hide mom_drawer
        hide mom_drawer_night
        if not moms_panties_taken:
            $ callScreen("Mom's Drawer", False)
    else:

        scene mom_drawer_night with None
        hide expression "objects/object_panties_02.png"
        hide mom_drawer
        hide mom_drawer_night
    $ callScreen(location_count)

label mom_drawer_continue:
    if not gTimer.is_dark():
        scene mom_drawer with None
        if not moms_panties_taken:
            show expression "objects/object_panties_02.png" at Position(xpos=260, ypos=690)
    else:

        scene mom_drawer_night with None
    player_name "( It smells good! )"
    player_name "( ...And it's so {b}soft{/b}... )"
    $ moms_panties_taken = True
    hide mom_drawer
    hide mom_drawer_night
    $ callScreen(location_count)

label mom_bed:
    if not gTimer.is_dark():
        scene mom_bedroom
        show player 106 with dissolve
        player_name "( Should I lay in her bed? )"
        menu:
            "Play with panties." if moms_panties_taken:
                $ moms_panties_taken = False
                if not caught:
                    scene location_mombed01
                    with dissolve
                    player_name "( {b}Mom’s panties{/b} are so soft... )"
                    show location_mombed 2_3
                    player_name "( It feels... )"
                    player_name "( ...SO good... )"
                    player_name "( ...I’m... )"
                    scene location_mombed06
                    player_name "( ...I’m cumming! )"
                    scene white with dissolve
                    scene location_mombed07
                    with dissolve
                    player_name "( Better clean up before I get caught... )"

                elif played_with_mom_panties == 0:
                    $ played_with_mom_panties = 1
                    scene location_mombed01
                    with dissolve
                    player_name "( These feel so soft against my skin... )"
                    show location_mombed 2_3
                    pause 5
                    scene location_mombed04
                    mom "!!!" with hpunch
                    scene location_mombed05
                    mom "Oh my..."
                    player_name "{b}Mom{/b}!!"
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
                    player_name "Hi, {b}Mom{/b}..."
                    show mom 13
                    show player 24
                    mom "Listen, I just want you to know that it's okay..."
                    mom "What happened was... normal!"
                    mom "And I know that young men your age have {b}needs{/b}..."
                    show player 5
                    show mom 14
                    player_name "..."
                    show mom 13
                    mom "You have a lot of affection for your {b}Mom{/b}, and you don't have a girlfriend..."
                    mom "...but you can't do that in my room! ...And you're ruining my lingerie..."
                    show mom 14
                    show player 24
                    player_name "Sorry, {b}Mom{/b}."
                    show mom 13
                    show player 5
                    mom "It's okay, Sweetie..."
                    show player 11
                    mom "...Can't you find something else? Like {b}internet porn{/b}?"
                    mom "Do you have that on your computer, or something?"
                    show mom 14
                    show player 21
                    player_name "{b}Mom{/b}!! Please, stop..."
                    show mom 13
                    show player 13
                    mom "Anyway... I want you to know that I {b}love you{/b}..."
                    mom "...And that I'm not mad about it!"
                    mom "I just want you to be happy..."
                    show mom 14
                    show player 21
                    player_name "I'll be fine, {b}Mom{/b}..."
                    $ gTimer.tick()
                    jump home_livingroom_dialogue
                else:

                    scene location_mombed01
                    with dissolve
                    player_name "( These feel so soft against my skin... )"
                    show location_mombed 2_3
                    pause 5
                    scene location_mombed04
                    mom "!!!" with hpunch
                    scene location_mombed05
                    mom "Oh my..."
                    player_name "{b}Mom{/b}!!"
                    scene mom_bedroom_closeup
                    show player 152 at left with dissolve
                    show mom 16 at right with dissolve
                    mom "{b}Again{/b}!"
                    show mom 20
                    mom "..."
                    show player 150 zorder 1
                    show mom 25 zorder 0 at Position(xpos = 610, ypos = 768) with dissolve
                    mom "Didn't I tell you not to do it in here?"
                    mom "Why didn't you listen?"
                    menu:
                        "Sorry.":
                            show mom 26
                            show player 151
                            player_name "I'm sorry, {b}Mom{/b}..."
                            player_name "...It won't happen again, I promise!"
                            show mom 27
                            show player 152
                            mom "Oh, Sweetie..."
                            show mom 25
                            mom "...Just try and do it elsewhere from now on."
                            mom "Can you do that for me, please?"
                            show mom 26
                            show player 151
                            player_name "Yes, {b}Mom{/b}..."
                        "I can't help it!":

                            show mom 26
                            show player 151
                            player_name "I don't know... It just {b}feels good{/b}..."
                            show mom 25
                            show player 152
                            mom "I know Sweetie... But it's in my room... And with my clothes!"
                            mom "Why can't you find something else to release your... {b}Energy{/b} with?"
                            mom "There're no girls at school that you like?"
                            menu:
                                "I'm trying.":
                                    show mom 26
                                    show player 151
                                    player_name "I'm trying, {b}Mom{/b}..."
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
                                    player_name "I will, {b}Mom{/b}..."
                                    show mom 25
                                    show player 152
                                    mom "As long as you're trying..."
                                    hide player
                                    show mom 28
                                    with dissolve
                                    mom "Come here..."
                                    show mom 29
                                    player_name "..."
                                    show mom 28
                                    mom "I love you so much, Sweetie..."
                                    show mom 29
                                    player_name "I love you too, {b}Mom{/b}!"
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
                                    mom "Or that girl next door? What's her name..."
                                    show mom 26
                                    show player 151
                                    player_name "{b}Mia{/b}..."
                                    show mom 25
                                    show player 152
                                    mom "Yeah! What about her?"
                                    show mom 26
                                    show player 151
                                    player_name "I dunno... Maybe..."
                                    show mom 25
                                    show player 152
                                    mom "Well, you have to make an effort, Sweetie!"
                                    show mom 26
                                    show player 151
                                    player_name "I will, {b}Mom{/b}..."
                                    show mom 25
                                    show player 152
                                    mom "As long as you're trying..."
                                    hide player
                                    show mom 28
                                    with dissolve
                                    mom "Come here..."
                                    show mom 29
                                    player_name "..."
                                    show mom 28
                                    mom "I love you so much, Sweetie..."
                                    show mom 29
                                    player_name "I love you too, {b}Mom{/b}!"
                                "I like you.":

                                    show mom 30
                                    show player 149
                                    player_name "I like you..."
                                    show player 152
                                    mom "..."
                                    show mom 25
                                    show player 150
                                    mom "But Sweetie... I'm your {b}Mom{/b}!"
                                    show mom 30
                                    show player 149
                                    player_name "I know! But all I can think about is you..."
                                    show player 151
                                    player_name "...And I don't like the girls at school..."
                                    show player 152
                                    mom "..."
                                    show mom 25
                                    mom "I don't really know what to say..."
                                    mom "I didn't know you felt this way!"
                                    show mom 27
                                    show player 150
                                    mom "Maybe I... sheltered you too much..."
                                    mom "Maybe it's my fault."
                                    show mom 26
                                    show player 149
                                    player_name "It's not your fault, {b}Mom{/b}..."
                                    show mom 30
                                    show player 151
                                    player_name "I just don't want anyone else!"
                                    show mom 20 at right with dissolve
                                    show player 150
                                    player_name "..."
                                    show mom 17
                                    mom "{b}*Sigh*{/b}"
                                    show mom 18
                                    mom "I'm going to do this {b}only once{/b}..."
                                    show mom 17
                                    mom "But you'll have to promise me that you'll meet new girls at school!"
                                    show mom 19
                                    show player 149
                                    player_name "What do you mean?"
                                    show player 154
                                    show mom 21
                                    window hide
                                    pause
                                    show mom 22
                                    window hide
                                    pause
                                    show mom 23 with hpunch
                                    window hide
                                    pause
                                    player_name "!!!"
                                    show mom 31
                                    mom "Finish what you started. Get it out of your system."
                                    show mom 23
                                    show player 149
                                    player_name "...{b}Mom{/b}?!!"
                                    show mom 31
                                    show player 150
                                    mom "Just {b}do it{/b}. It's okay..."
                                    show mom 23
                                    show player 155_156
                                    pause 4
                                    show mom 24
                                    mom "Oh!!!"
                                    $ animcounter = 0
                                    while (animcounter < 2):
                                        $ animcounter += 1
                                        show player 157
                                        window hide
                                        pause .4
                                        show player 158
                                        window hide
                                        pause .4
                                        show player 158
                                        window hide
                                        pause .2
                                    show player 161
                                    mom "..."
                                    show mom 22
                                    window hide
                                    pause
                                    show mom 21
                                    window hide
                                    pause
                                    show mom 16
                                    mom "You have to make an effort to meet other girls now... {b}Promise{/b}?"
                                    show mom 15
                                    show player 160
                                    player_name "Yeah..."
                                    show mom 17
                                    show player 161
                                    mom "This was just a {b}one time thing{/b}... To help you through this..."
                                    hide player
                                    show mom 28 with dissolve
                                    mom "Come here..."
                                    show mom 29
                                    player_name "..."
                                    show mom 28
                                    mom "I love you so much, Sweetie..."
                                    show mom 29
                                    player_name "I love you too, {b}Mom{/b}!"
                                    hide mom 29
                                    hide ui
                                    hide mom_bedroom_closeup
                                    $ mom_revealing_tommorow = True
                $ gTimer.tick()
                hide player
            "Another time.":

                show player 34
                player_name "( What if she walks in... )"
                player_name "Hmm..."
                player_name "( Maybe another time. )"
                hide player 34 with dissolve

    elif mom_count >= 10 and mom_revealing and mom_cuddling_unlocked:
        if mom_had_sex:
            $ animcounter = 0
            scene mom_bedroom_closeup
            if mom_count >= 9:
                show player 109 at right
                show mom 83 at left
                with dissolve
                mom "..."
                show mom 81
                mom "{b}[firstname]{/b}?"
                mom "Is everything okay?"
                show player 111
                player_name "Hey, {b}Mom{/b}."
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

                player_name "Thanks, {b}Mom{/b}."
                show moms_bed_overlay zorder 3 at Position(xpos=438)
                show moms 79 zorder 2 at Position(xpos=365)
                with dissolve
                player_name "I couldn't sleep... I was so horny thinking about you..."
                player_name "...And I wanted to be in you again."
                show moms 80
                mom "It's perfectly normal, Sweetie."
                $ mom_day_tick = False
                label mom_endgame_options:
                    menu:
                        "Cuddle":
                            $ mom_day_tick = True
                            show moms 79
                            player_name "Can we cuddle a little bit?"
                            show moms 80
                            mom "Of course."
                            show moms 83 with dissolve
                            player_name "You smell really good, {b}Mom{/b}..."
                            show moms 84
                            mom "Thanks, Sweetie."
                            label endgame_cuddle_options:
                                show moms 81_82 with dissolve
                                pause 4
                                show moms 81
                                menu:
                                    "Keep going":
                                        jump endgame_cuddle_options
                                    "Back":

                                        jump mom_endgame_options
                        "Kiss":

                            $ mom_day_tick = True
                            show moms 83
                            player_name "Can we kiss?"
                            show moms 84
                            mom "You don't even have to ask, Sweetie."
                            mom "Come here..."
                            label endgame_kiss_options:
                                show moms 85_86 with dissolve
                                pause 4
                                show moms 81 with dissolve
                                menu:
                                    "Keep going":
                                        jump endgame_kiss_options
                                    "Back":

                                        jump mom_endgame_options
                        "Breastfeed":

                            $ mom_day_tick = True
                            show moms 83
                            player_name "Can I... suck on your breasts?"
                            show moms 87 with dissolve
                            mom "Just... be gentle."
                            label endgame_breastfeed_options:
                                show moms 88_89 at Position(xpos=329) with dissolve
                                pause 4
                                show moms 89 at Position(xpos=327)
                                menu:
                                    "Keep going":
                                        jump endgame_breastfeed_options
                                    "Back":

                                        jump mom_endgame_options
                        "Rub":

                            $ mom_day_tick = True
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
                            label endgame_rub_options:
                                show moms 93_94 at Position(xpos=329)
                                pause 4
                                show moms 94 at Position(xpos=327)
                                menu:
                                    "Keep going":
                                        jump endgame_rub_options
                                    "Back":

                                        jump mom_endgame_options
                        "Fuck":

                            $ mom_day_tick = True
                            $ anim_toggle = False
                            $ xray = False
                            show moms 95 with dissolve
                            mom "Let me help you Sweetie..."
                            mom "...Now, slide it inside me... deep."
                            show moms 96 with dissolve
                            mom "Just like that... Yes, Sweetie..."
                            show moms 98 at Position(xpos=327) with dissolve
                            show screen xray_scr
                            pause
                            if anim_toggle:
                                hide screen xray_scr
                                show moms 97_98 at Position(xpos=329)
                                mom "Oh, yes!"
                                mom "Yes, Sweetie..."
                                mom "Keep going..."
                                mom "Deeper... Faster!!"
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
                                            show moms 97 at Position(xpos=329)
                                            pause
                                            show moms 98 at Position(xpos=327)
                                            pause
                                            show moms 97 at Position(xpos=329)
                                            pause
                                            show moms 98 at Position(xpos=327)
                                            pause
                                            show moms 97 at Position(xpos=329)
                                            pause
                                            show moms 98 at Position(xpos=327)
                                            pause
                                        show moms 97 at Position(xpos=329)
                                        jump mom_fuck_options
                                    "Cum":

                                        mom "AAHH!!!"
                                        show white zorder 4
                                        show moms 99 at Position(xpos=327) with vpunch
                                        hide white with dissolve
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
                                        scene location_momsidebed_night
                                        show player 110 at right
                                        show mom 81 at left
                                        with fade
                                        mom "{b}Mommy{/b} is tired now... Are you going to be okay?"
                                        show player 111
                                        show mom 82
                                        player_name "Yeah, I'm feeling much better... I think I'll be able to sleep, now."
                                        show player 110
                                        show mom 81
                                        mom "That's good. Sweet dreams my handsome boy."
                                        show mom 82
                                        show player 111
                                        player_name "Good night, {b}Mom{/b}."
                                        $ gTimer.tick()
                                        $ mom_door_lock = True
                                        jump home_livingroom_dialogue
                        "Leave":

                            if mom_day_tick:
                                $ gTimer.tick()
                            show moms 80 at Position(xpos=365) with dissolve
                            mom "I think that's enough for tonight, Sweetie."
                            mom "You should get back to your bed, alright?"
                            show moms 79
                            player_name "Okay, {b}Mom{/b}..."
                            player_name "Thanks for letting me lay here."
                            player_name "I should be able to get some sleep now."
                            show moms 80
                            mom "Good night, Sweetie."
                            hide moms_bed_overlay
                            $ mom_door_lock = True
                            jump home_livingroom_dialogue
        else:

            scene mom_bedroom_closeup_sex
            show player 109 at right
            show mom 83 at left
            with dissolve
            mom "..."
            show mom 81
            mom "{b}[firstname]{/b}?"
            mom "Is everything okay?"
            show mom 82
            show player 111
            player_name "Yes, {b}Mom{/b}."
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
            player_name "Yes, {b}Mom{/b}."
            scene mom_cuddle
            with fade
            show moms 77
            with fade
            player_name "Thanks, {b}Mom{/b}."
            show moms_bed_overlay zorder 3 at Position(xpos=438)
            show moms 79 zorder 2 at Position(xpos=365)
            with dissolve
            player_name "I like being close like this..."
            player_name "...And your bed is always so warm."
            show moms 80
            mom "I know Sweetie, but you can't be in here all the time..."
            show moms 79
            player_name "I know..."
            menu:
                "Cuddle":
                    $ gTimer.tick()
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
                    player_name "You smell really good, {b}Mom{/b}..."
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
                            "Ask for a kiss":

                                show moms 83
                                player_name "{b}Mom{/b}..."
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
                                player_name "I could feel you shaking, {b}Mom{/b}."
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

                                        "Breastfeed" if mom_count > 8 or mom_count == 8 and mom_dialogue_advance:
                                            if pStats.chr() >= 6:
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
                                            else:
                                                jump mom_denied_dialogue
                                            label breastfeed_options:
                                                menu:
                                                    "Keep going":
                                                        show moms 88_89 at Position(xpos=329) with dissolve
                                                        pause 4
                                                        show moms 88 at Position(xpos=329)
                                                        jump breastfeed_options
                                                    "Rub":

                                                        if pStats.chr() >= 8 and mom_count >= 8:
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
                                                        else:
                                                            jump mom_denied_dialogue
                                                        label rub_options:
                                                            menu:
                                                                "Keep going":
                                                                    show moms 93_94 at Position(xpos=329) with dissolve
                                                                    pause 4
                                                                    show moms 93 at Position(xpos=329)
                                                                    jump rub_options
                                                                "Fuck":

                                                                    if mom_count >= 12:
                                                                        $ mom_day_tick = True
                                                                        $ anim_toggle = False
                                                                        $ xray = False
                                                                        show moms 95 with dissolve
                                                                        mom "Let me help you Sweetie..."
                                                                        mom "...Now, slide it inside me... deep."
                                                                        show moms 96 with dissolve
                                                                        mom "Just like that... Yes, Sweetie..."
                                                                        show moms 98 at Position(xpos=327) with dissolve
                                                                        show screen xray_scr
                                                                        pause
                                                                        if anim_toggle:
                                                                            hide screen xray_scr
                                                                            show moms 97_98 at Position(xpos=329)
                                                                            mom "Oh, yes!"
                                                                            mom "Yes, Sweetie..."
                                                                            mom "Keep going..."
                                                                            mom "Deeper... Faster!!"
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
                                                                        label mom_fuck_options_first:
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
                                                                                        show moms 97 at Position(xpos=329)
                                                                                        pause
                                                                                        show moms 98 at Position(xpos=327)
                                                                                        pause
                                                                                        show moms 97 at Position(xpos=329)
                                                                                        pause
                                                                                        show moms 98 at Position(xpos=327)
                                                                                        pause
                                                                                        show moms 97 at Position(xpos=329)
                                                                                        pause
                                                                                        show moms 98 at Position(xpos=327)
                                                                                        pause
                                                                                    show moms 97 at Position(xpos=329)
                                                                                    jump mom_fuck_options_first
                                                                                "Cum":

                                                                                    mom "AAHH!!!"
                                                                                    show white zorder 4
                                                                                    show moms 99 at Position(xpos=327) with vpunch
                                                                                    hide white with dissolve
                                                                                    mom "YES, baby..."
                                                                                    $ xray = False
                                                                                    show moms 98 at Position(xpos=327) with dissolve
                                                                                    mom "{b}*Huffing*{/b}"
                                                                                    mom "Stay inside me a bit longer..."
                                                                                    mom "I like feeling your cum inside me."
                                                                                    show moms 100 with fade
                                                                                    mom "You came so much..."
                                                                                    player_name "Was it... wrong?"
                                                                                    mom "It's okay... {b}Mommy{/b} will be fine."
                                                                                    scene mom_bedroom_closeup
                                                                                    show player 110 at right
                                                                                    show mom 81 at left
                                                                                    with fade
                                                                                    mom "{b}Mommy{/b} is tired now... Are you going to be okay?"
                                                                                    show player 111
                                                                                    show mom 82
                                                                                    player_name "Yeah, I'm feeling much better... I think I'll be able to sleep, now."
                                                                                    show player 110
                                                                                    show mom 81
                                                                                    mom "That's good... Sweet dreams my handsome boy."
                                                                                    show mom 82
                                                                                    show player 111
                                                                                    player_name "Good night, {b}Mom{/b}."
                                                                                    hide moms_bed_overlay
                                                                                    $ mom_door_lock = True
                                                                                    $ mom_had_sex = True
                                                                                    jump home_livingroom_dialogue
                                                                    else:

                                                                        jump mom_denied_dialogue
                                                                "Leave":

                                                                    jump leave_block
                                                    "Leave":

                                                        jump leave_block
                                        "Leave":

                                            jump leave_block
                            "Leave":

                                jump leave_block
                "Leave":

                    jump leave_block
    else:

        scene mom_bedroom_night
        show player 106 with dissolve
        player_name "( Should I sneak into her bed? )"
        show player 34
        player_name "Hmm..."
        player_name "( I shouldn't bother her when she's sleeping... )"
        hide player 34 with dissolve
    $ callScreen(location_count)

label leave_block:
    scene mom_cuddle
    show moms 80 at Position(xpos=365)
    show moms_bed_overlay zorder 3 at Position(xpos=438)
    with dissolve
    mom "I think that's enough for tonight, Sweetie."
    mom "You should get back to your bed, okay?"
    show moms 79
    player_name "Okay, {b}Mom{/b}..."
    player_name "Thanks for letting me lay here with you."
    player_name "I should be able to get some sleep now."
    show moms 80
    mom "Good night, Sweetie."
    hide moms_bed_overlay
    $ mom_door_lock = True
    jump home_livingroom_dialogue

label mom_denied_dialogue:

    if pStats.chr() < 8:
        show moms 80 at Position(xpos=365) with hpunch
        mom "[chr_warn]I don't think we should be doing this Sweetie..."
        mom "[chr_warn]I want you to feel better but... This is going a bit too far."
        show moms 79
        player_name "[chr_warn]I didn't mean to-"
        show moms 80
        mom "[chr_warn]It's okay! I enjoy cuddling with my boy..."
        mom "[chr_warn]But you have to go sleep in your room now."
        show moms 79
        player_name "[chr_warn]Okay, {b}Mom{/b}."
    else:

        show moms 80 at Position(xpos=365) with hpunch
        mom "I don't think we should be doing this, Sweetie..."
        mom "I want you to feel better, but... This is going a bit TOO far."
        show moms 79
        player_name "I didn't mean to-"
        show moms 80
        mom "It's okay! I enjoy cuddling with my boy..."
        mom "But you have to go sleep in your room now."
        show moms 79
        player_name "Okay, {b}Mom{/b}."
    hide moms 79
    hide moms_bed_overlay
    $ mom_door_lock = True
    jump home_livingroom_dialogue

label mom_room_laundry:
    scene mom_bedroom
    show player 276 with dissolve
    player_name "I should take this down to the {b}basement{/b}."
    hide player with dissolve
    hide mom_bedroom
    $ fetched_laundry = True
    $ callScreen(location_count)

label mom_dialogue_button_room:
    scene mom_bedroom_closeup2
    show mom 55 at left
    show player 110 at right
    with dissolve
    mom "Hi, Sweetie..."
    mom "Were you looking for me?"
    show mom 54
    show player 111
    player_name "Yeah..."
    show player 110
    show mom 55
    mom "Is there something you wanted from me?"
    show mom 54
    jump mombedmenu_beforekiss
    label mombedmenu_afterkiss:
        mom "Now, is there anything else you wanted?"
        show mom 54
        menu mombedmenu_beforekiss:
            "Kiss.":
                show player 111 at right
                show mom 54 at left
                player_name "Can I have a kiss?"
                show player 110
                show mom 55
                mom "Of course, Sweetie! Come here."
                scene mom_bedroom
                show mom 79
                with fade
                mom "Mmmm..."
                show mom 80_79
                pause 3
                show mom 75 at Position(xpos=750)
                show player 227 at Position(xpos=200)
                with fastdissolve
                mom "You're getting better at this!"
                scene mom_bedroom_closeup2
                show mom 55 at left
                show player 110 at right
                with fade
                jump mombedmenu_afterkiss

            "Shower." if henchmen_count == 2:
                show player 111
                player_name "Hey, {b}Mom{/b}!"
                player_name "Want to take a shower with me?"
                show player 110
                show mom 55
                mom "It is getting pretty hot in the house..."
                mom "Sure! A shower sounds lovely right now."
                mom "You go ahead, Sweetie. I'll be there in a minute."
                scene shower_closeup
                show moms 27
                with dissolve
                pause
                show moms 28 at Position(xpos=487,ypos=768) with dissolve
                pause
                show moms 34 with dissolve
                mom "Sorry to keep you waiting, Sweetie..."
                jump mom_shower_question
            "Have sex.":

                show mom 54
                show player 111
                player_name "I feel like... Doing it with you again."
                show player 110
                show mom 55
                mom "That's okay!"
                mom "I was hoping you'd want to..."
                show player 111
                show mom 54
                player_name "Really?"
                show player 110
                show mom 58
                mom "Of course! You're my man, after all."
                show mom 57
                player_name "!!!"
                show mom 58
                mom "Take your clothes off, Sweetie."
                show mom 57
                show player 8f
                pause
                show player 261
                pause
                show player 263
                pause
                show mom 103
                mom "Now, lay on top of {b}Mommy{/b}..."
                show player 262 at right
                show mom 102 at left
                player_name "Don't have to tell me twice..."
                hide player
                show mom 104 at left
                with dissolve
                pause
                hide mom
                hide player
                with dissolve
                scene mom_bedroom_closeup_sex
                jump mom_sex

            "Laundry." if mom_basement_sex:
                show mom 54
                show player 111
                player_name "I was wondering if you wanted some help in the basement."
                show player 110
                show mom 55
                mom "In the basement? What for?"
                show player 111
                show mom 54
                player_name "Maybe I can help you with laundry... Like we did last time?"
                show player 110
                show mom 55
                mom "Oh, I see... I know exactly what you want!"
                mom "Give {b}Mommy{/b} a minute to get ready."
                mom "I'll meet you down there..."
                hide mom
                hide player
                with dissolve
                jump basement_mom_sex
            "Nevermind.":

                show mom 54
                show player 111
                player_name "Nothing, {b}Mom{/b}."
                player_name "Just wanted to say hi."
                show player 110
                show mom 55
                mom "Oh, okay..."
                mom "Well, come back if you'd like... {b}Mommy{/b} is a bit bored..."
                mom "We can have fun whenever you'd like."
                hide player
                hide mom
                with dissolve
    $ mom_dialogue_daily = True
    hide player dissolve
    hide mom dissolve
    $ callScreen(location_count)

label mom_sex:
    $ mom_sex_position = "missionary"
    $ cum = False
    $ anim_toggle = False
    $ xray = False
    show moms 106 at left
    with fade
    mom "Now, start nice and slow, Sweetie."
    show moms 103 with dissolve
    pause
    show moms 104 with dissolve
    mom "Aahh..."
    label missionary_loop:
        hide screen mom_sex_options
        show moms 104 at left
        show screen xray_scr
        pause
        if anim_toggle:
            hide moms 104
            hide screen xray_scr
            hide screen mom_sex_options
            if xray:
                show moms_xray 65_66_67_66 at Position(ypos = 1034)
            else:
                show moms 103_104_105_104 at Position(xpos = 450)
            pause 5
            hide moms_xray 65_66_67_66
            hide moms 103_104_105_104
            show moms 104 at left
        else:

            hide screen xray_scr
            hide screen mom_sex_options
            show moms 103 at left
            pause
            show moms 104
            pause
            show moms 105
            pause
            show moms 104
            pause
            show moms 103
            pause
            show moms 104
            pause
            show moms 105
            pause
            show moms 104
            pause
            show moms 103
            pause
            show moms 104
            pause
            show moms 105
            pause
            show moms 104
        show screen mom_sex_options
        pause
        jump missionary_loop

    label mom_missionary_cum:
        hide screen xray_scr
        hide screen mom_sex_options
        show moms 103
        player_name "{b}Mom{/b}, I'm gonna..."
        mom "Let it out, Sweetie!"
        show moms 105 with hpunch
        player_name "{b}Mom{/b}!!!"
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
        jump after_sex

    label mom_missionary_cum_outside:
        hide screen xray_scr
        hide screen mom_sex_options
        show moms 103
        player_name "{b}Mom{/b}, I'm gonna..."
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
        player_name "Yes, {b}Mom{/b}. Sorry about the mess..."
        jump after_sex

    label suck_tits:
        hide screen mom_sex_options
        show moms 67 at left
        show screen xray_scr
        pause
        if anim_toggle:
            hide moms 67
            hide screen xray_scr
            hide screen mom_sex_options
            show moms 68_67 at left
            pause 4
            mom "Yes, Sweetie...."
            pause 4
            mom "Keep sucking on them."
            pause 4
            hide moms 68_67
            show moms 67 at left
        else:

            hide screen xray_scr
            hide screen mom_sex_options
            show moms 68 at left
            pause
            show moms 67
            pause
            mom "Yes, Sweetie...."
            show moms 68
            pause
            show moms 67
            pause
            mom "Keep sucking on them."
            show moms 68
            pause
            show moms 67
            pause
            show moms 68
        show screen mom_sex_options
        pause
        jump suck_tits

    label cowgirl_loop:
        hide screen mom_sex_options
        show moms 65 at left
        show screen xray_scr
        pause
        if anim_toggle:
            hide moms 65
            hide screen xray_scr
            hide screen mom_sex_options
            if xray:
                show moms_xray 58_59_57 at Position(ypos = 849)
            else:
                show moms 65_66_64 at Position(xpos = 476)
            pause 5
            hide moms_xray 58_59_57
            hide moms 65_66_64
            show moms 65 at left
        else:

            hide screen xray_scr
            hide screen mom_sex_options
            show moms 65 at left
            pause
            show moms 66
            pause
            show moms 64
            pause
            show moms 65
            pause
            show moms 66
            pause
            show moms 64
            pause
            show moms 65
            pause
            show moms 66
            pause
            show moms 64
            pause
            show moms 65
            pause
            show moms 66
            pause
            show moms 64
        show screen mom_sex_options
        pause
        jump cowgirl_loop

    label mom_cowgirl_cum:
        hide screen xray_scr
        hide screen mom_sex_options
        show moms 69 at left with vpunch
        player_name "{b}Mom{/b}!!!"
        mom "Ahh!!!"
        show white with dissolve
        $ cum = True
        hide white with dissolve
        pause
        mom "Oh..."
        show moms 70 with dissolve
        mom "You should warn me when you're about to do it, Sweetie."
        player_name "Sorry, {b}Mom{/b}."
        player_name "I just couldn't help it..."
        player_name "It felt too good..."
        mom "It's okay. Let's clean you up..."
        jump after_sex

    label mom_cowgirl_cum_outside:
        hide screen xray_scr
        hide screen mom_sex_options
        scene mom_bedroom_closeup_sex
        show moms 64 at left
        player_name "{b}Mom{/b}, I'm gonna..."
        show moms 109 with dissolve
        show white with dissolve
        show playersex 72 at Position(xpos=478, ypos=418)
        hide white with dissolve
        pause
        show playersex 73 at Position(xpos=524, ypos=478) with dissolve
        mom "Thanks for the warning, Sweetie."
        mom "Let's get ourselves cleaned up..."
        jump after_sex

    label after_sex:
        scene mom_bedroom
        show player 227 at Position(xpos=200)
        show mom 73 at Position(xpos=650)
        with fade
        mom "Sweetie..."
        mom "I want you to tell me if you don't want to do this anymore, okay?"
        show player 228
        show mom 76
        player_name "No, it's fine, {b}Mom{/b}."
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
        player_name "I love you {b}Mom{/b}!"
        show player 227
        show mom 75
        mom "I love you too, Sweetie..."
        hide mom
        hide player
        with dissolve
        $ ui_lock_count = 0
        $ gTimer.tick()
        $ mom_dialogue_advance = True
    $ callScreen(location_count)