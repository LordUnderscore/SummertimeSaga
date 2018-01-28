default condom_taken = False
default sis_panties_bought = False
default sis_quest_first = True
default sis_confession_first = True
default sis_deal_first = True
default sis_final_cum = "Outside"
default sis_final_cum_inside_first = True

label sis_bedroom_dialogue:
    $ location_count = "Sis' Bedroom"




    scene expression gTimer.image("sisbedroom{}")
    if not gTimer.is_dark():
        if sis_bedroom_count == 0:
            scene sisbedroom
            show player 34 at left with dissolve
            player_name "( Hmmm... )"
            show player 35 at left
            player_name "( She's not in her room... )"
            show player 18 at left
            player_name "( Maybe I can look around a bit! )"
            hide player 18 at left with dissolve

        elif sister.started(sis_hallway02) and sister.over(sis_telescope02):
            scene sisbedroom_closeup
            show sis 22 at right
            show player 11 at left with dissolve
            sis "Leave me alone, already! Why don't you just pester {b}[mom_name]{/b} for some of her panties, pervert!"
            sis "She has so many in {b}her drawer{/b}, and leaves her clothes scattered throughout {b}her room{/b}!!"
            jump hallway_dialogue

        elif sis_bedroom_count == 1 and not sis_panties_trade and look_for_panties:
            $ unlock_ui()
            scene sisbedroom
            show player 22 at left
            show sis 7b at right
            with dissolve
            sis "What the {b}FUCK{/b} are you doing in here?!!" with hpunch
            show sis 8b at right
            show player 23 at left
            player_name "It's not what you-"
            show player 22
            show sis 7b
            sis "Were you going through my things?!"
            show sis 8b
            show player 23
            player_name "Wait!"
            show sis 7b
            show player 22
            sis "Are you trying to {b}steal{/b} my stuff??"
            show player 23
            show sis 8b
            player_name "Let me explain!!"
            show player 22
            show sis 9c at Position(xpos=937)
            sis "Oh, you better have a {b}really{/b} good fucking explanation!"
            sis "Unless you want {b}[mom_name]{/b} to know about you stealing from me."
            show player 23
            show sis 6b
            player_name "No!"
            show player 10
            show sis 10b
            player_name "Well... It's not like that..."
            player_name "Okay, look, I desperately need to do someone a favor."
            player_name "And that favor is... to get them a pair of {b}panties{/b}..."
            show player 5
            show sis 9c
            sis "What the fuck?!"
            show sis 10b
            show player 21
            player_name "I know, It sounds a little weird..."
            show sis 7b at right
            show player 11
            with hpunch
            sis "A {b}LITTLE{/b}?!"
            sis "What kind of sick perverted people have you been hanging around?"
            show sis 9c at Position(xpos=937)
            sis "Please, don't tell me it's that {b}Erik{/b} creep."
            show player 12
            show sis 10b
            player_name "Of course not!"
            show player 10
            player_name "Listen, {b}Sis{/b}! I really need this!"
            show sis 11b
            player_name "I'll give you whatever you want for them!"
            show player 5
            sis "Hmmm..."
            show sis 12b
            show player 11
            sis "Alright! If you need them so badly, I'll let you {b}buy{/b} them off of me."
            show sis 11b
            show player 10
            player_name "What?"
            show sis 12b
            show player 11
            sis "That's right."
            sis "I know you've been working for {b}Aunt Diane{/b} lately..."
            sis "...you must have {b}some{/b} cash on you!"
            show sis 11b
            show player 10
            player_name "But-"
            show sis 9c
            show player 11
            sis "{b}LOOK{/b}! I'm {b}not{/b} going to just throw away all my underwear, okay?!"
            sis "I'll need to buy new ones, so the {b}only{/b} way you're getting any of mine..."
            show sis 12b
            show player 5
            sis "is with {b}money{/b}."
            show sis 18b at right
            show player 10
            player_name "How much do you want?"
            show sis 19b
            show player 11
            sis "{b}$100{/b} should cover it."
            show sis 18b
            show player 29
            player_name "That's a lot of money..."
            show sis 9c at Position(xpos=937)
            show player 11 at left
            sis "So? You taking them or not?!"
            show sis 6b
            $ bedtable01_count = 1
            if inventory.money >= panties.cost:
                menu:
                    "Here's $100.":
                        show player 12 at left
                        show sis 18b at right
                        player_name "Okay! Fine!"
                        $ inventory.money -= 100
                        $ inventory.items.append(panties)
                        $ sis_panty01.finish()
                        $ completed_quests.append(quest07)
                        $ sis_panties_bought = True
                        play audio coins2
                        show player 41 at Position (xpos=38) with fastdissolve
                        pause
                        show sis 80b at Position(xpos=945)
                        show player 1 at left
                        sis "Alright, you can keep them..." with fastdissolve
                        show sis 81b
                        show player 11
                        sis "Now, get out of my room, pervert!"
                        show sis 14b
                        show unlock17 at truecenter
                        pause
                        hide unlock17 with dissolve
                        $ sis_bedroom_count = 2
                        $ sis_panties_trade = True
                        jump hallway_dialogue
                    "I don't need it.":

                        show sis 10b at Position(xpos=937)
                        show player 35 at left
                        player_name "Actually, I don't need any right now..."
                        show sis 9c
                        show player 39 at Position (xpos=38)
                        sis "Then give them back, and get out of my room, you pervert!"
                        jump hallway_dialogue
            else:

                menu:
                    "I don't have enough.":
                        show player 24 at left
                        show sis 10b at Position(xpos=937)
                        player_name "I don't have that much money on me..."
                        show sis 9c
                        show player 5
                        sis "Too bad. Get out of my room, you pervert!"
                        jump hallway_dialogue

        elif sis_bedroom_count == 2 and not sis_dialogue_advance and not sis_diary_unlocked:
            scene sisbedroom_closeup
            show sis 20 at right
            show player 24 at left with dissolve
            sis "Well, well."
            sis "What would my perverted little {b}Brother{/b} want, this time?"
            sis "More panties? Perhaps?"
            menu:
                "Yeah, more panties.":
                    show sis 21
                    show player 111f
                    player_name "Yeah, more panties, actually."
                    show player 106
                    show sis 22
                    sis "Just come back later..."
                    show sis 23
                    show player 108f
                    player_name "But-"
                    show sis 22
                    show player 109f
                    sis "I'm busy right now, can't you see??"
                    show sis 23
                    show player 108f
                    player_name "Alright..."
                    show sis 22
                    show player 109f
                    sis "And close the door on the way out!"
                    show sis 20
                    show player 106
                    sis "I wouldn't want a pervert spying on me."
                    show sis 21
                    show player 109f
                    player_name "..."
                    show player 108f
                    player_name "Okay..."
                    jump hallway_dialogue

                "Mom needs you." if sister.over(sis_shower_cuddle01):
                    show sis 21
                    show player 108f
                    player_name "Umm... Actually, {b}[mom_name]{/b} needs to..."
                    show player 111f
                    player_name "...Talk to you about something!"
                    show sis 22
                    show player 106
                    sis "What about?"
                    menu:
                        "She needs help.":
                            show sis 23
                            show player 111f
                            player_name "She needs help with something downstairs..."
                            show player 110f
                            sis "..."
                            show sis 22
                            show player 106
                            sis "What does she need help with anyway?"
                            show player 108f
                            show sis 23
                            player_name "I'm not sure."
                            player_name "She just... asked me to tell you!"
                            show sis 22
                            show player 109f
                            sis "Ugh!"
                            show sis 24
                            sis "Fine. I'm going..."
                            show sisbed zorder 1 at right
                            show player 5 zorder 2
                            show sis 9 zorder 2 with dissolve
                            sis "Just don't touch anything, and leave my room..."
                            hide sis 9 with fade
                            show player 106
                            player_name "..."
                            show player 113
                            player_name "Okay..."
                            hide player
                            hide sisbed
                            $ diary_scene = True
                            $ sis_dialogue_advance = True
                            $ sis_diary_unlocked = True
                "Nothing.":

                    show player 108f
                    show sis 21
                    player_name "Nevermind... It's nothing."
                    show sis 20
                    show player 109f
                    sis "Can you please close the door on the way out?"
                    show player 106
                    sis "I wouldn't want a pervert spying on me."
                    show sis 21
                    show player 109f
                    player_name "..."
                    show player 108f
                    player_name "Okay..."
                    jump hallway_dialogue

        elif sister.started(sis_final):
            scene sis_webcam2
            show sis 151 at Position(xpos=407,ypos=748)
            with fade
            sis "Heyyy, guys!"
            show sis 155
            sis "I'm so glad you've been enjoying my new cam shows."
            show sis 151
            sis "My new toys have been so popular, I've been getting tons of new subscribers!"
            show sis 150
            sis "..."
            show sis 152
            sis "What?! You guys think I could do better? But, how?!"
            sis "Role play?"
            show sis 154
            sis "You mean like... outfits and costumes?"
            show sis 152
            sis "But what kind of theme, though?"
            sis "Cheerleaders and bondage?!"
            show sis 154
            sis "It's kind of specific... but I guess that's what's popular right now."
            show sis 153
            sis "Hmm..."
            show sis 151
            sis "What else would make you guys... open up your wallets?"
            show sis 152
            sis "More hardcore? You guys mean sex?"
            sis "And raw too?!"
            show sis 154
            sis "I guess it does look more natural..."
            show sis 152
            sis "Well, you guys are out of luck. I don't have a boyfriend."
            show sis 151
            sis "Unfortunately, all I have right now are my toys! Haha!"
            show sis 150
            sis "..."
            show sis 152
            sis "You guys really think I could double my income with this kind of stuff?"
            show sis 153
            sis "Hmm..."
            show sis 155
            sis "All right! Thanks for the suggestions, guys!!"
            show sis 159 at left
            show sis 159 at Position(ypos=748)
            sis "I'll see what i can do..."
            show sis 160 at Position(ypos=771) with fastdissolve

            sis "Shit... They want to see actual sex, now."
            sis "I don't know if any of my ex-boyfriends would want to do this. They're all jerks, regardless."
            sis "Though, there's always my little brother."
            sis "Ugh... I don't know if that's a good idea."
            sis "It's kind of gross thinking about it, but he does have a nice cock, I suppose."
            sis "I bet he'd even do it for free, the little pervert."
            sis "If I promise him something good, he might get me all my costumes too!"
            sis "It's so tempting! They'd pay a lot of money to see that stuff."
            sis "I'll have to think this over..."
            scene hallway
            show player 11
            with fade
            player_name "..."
            show player 35
            player_name "( I can't believe she's going this far, just to please her subscribers... )"
            show player 4 at Position(xpos=518)
            player_name "( She must love the attention she's getting... and the money. )"
            hide player with dissolve
            $ sis_final.finish()
            $ unlock_ui()
            jump hallway_dialogue
        else:

            $ callScreen(location_count)
    elif gTimer.is_dark() and not in_sis_room:
        scene sisbedroom_clear
        player_name "( {b}[sis_name]{/b}'s sleeping. )"
        player_name "( I have to be real quiet or she might hear me... )"
        player_name "( ...Don't want to wake her up, or I'm dead! )"
    $ in_sis_room = False
    $ callScreen(location_count)

label sneak_in_sis_bed:
    $ gTimer.tick()
    scene sisbedroom_bed with None
    show sissex 46 at right
    with dissolve
    player_name "( Maybe if I'm real careful... )"
    player_name "( ...I can sneak in without her noticing... )"
    show sissex 47 with dissolve
    player_name "( I just have to to slip under the sheets slowly like this... )"
    hide sissex
    show sissex 48 zorder 1 at Position(xpos=644)
    show sis_bedcover zorder 2 at right
    with dissolve
    player_name "( Okay, this is scarier than I expected... )"
    player_name "( I really want to hold her though... )"
    player_name "( ... maybe she won't notice just a light touch? )"
    menu:
        "Leave.":
            player_name "( On second thought, maybe I should do it some other time. )"
            hide sissex
            hide sis_bedcover
            jump hallway_dialogue

        "Cuddle." if sister.known(sis_shower_cuddle01) and not sister.known(sis_shower_cuddle02):
            $ sis_shower_cuddle01.finish()
            show sissex 49 at Position(xpos=682) with fastdissolve
            pause
            show sissex 50 with fastdissolve
            pause
            show sissex 52
            sis "{b}[firstname]{/b}?"
            show sissex 53
            sis "What the {b}FUCK{/b} are you doing??!!" with hpunch
            show sissex 91
            player_name "Don't yell! You're gonna wake up {b}[mom_name]{/b}..."
            show sissex 53
            sis "You think I {b}CARE{/b}??! What's wrong with you?!"
            show sissex 91
            player_name "I..."
            player_name "I'm sorry!!"
            show sissex 53
            sis "Shut up and {b}GET OUT{/b}!!" with hpunch
            hide sissex
            hide sis_bedcover
            jump hallway_dialogue

        "Cuddle." if sister.known(sis_shower_cuddle02):
            $ sis_shower_cuddle02.finish()
            show sissex 49 at Position(xpos=682) with fastdissolve
            player_name "( Woah... Her skin is so soft... )"
            player_name "( ...And she doesn't seem to notice my hand touching her leg. )"
            player_name "( I'll caress it just a bit... )"
            show sissex 84
            pause .4
            show sissex 49_84 at Position(xpos = 682)
            pause 8
            show sissex 84
            player_name "( If she doesn't notice this, maybe I could go further... )"
            menu:
                "Leave.":
                    player_name "( I want do more... )"
                    player_name "( But I should probably leave before I wake her up. )"
                    player_name "( I'll try again some other night... )"
                    hide sissex
                    hide sis_bedcover
                    jump hallway_dialogue

                "Squeeze boobs." if not sister.known(sis_shower_cuddle03):
                    show sissex 54 with fastdissolve
                    pause
                    show sissex 55
                    pause
                    show sissex 50 with fastdissolve
                    pause
                    show sissex 52
                    sis "{b}[firstname]{/b}?"
                    show sissex 53
                    sis "What the {b}FUCK{/b} are you doing??!!" with hpunch
                    show sissex 91
                    player_name "Don't yell! You're gonna wake up {b}[mom_name]{/b}..."
                    show sissex 53
                    sis "You think I {b}CARE{/b}??! What's wrong with you?!"
                    show sissex 91
                    player_name "I..."
                    player_name "I'm sorry!!"
                    show sissex 53
                    sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                    hide sissex
                    hide sis_bedcover
                    jump hallway_dialogue

                "Squeeze boobs." if sister.known(sis_shower_cuddle03):
                    $ sis_shower_cuddle03.finish()
                    if not sister.known(sis_couch03):
                        $ sister.add_event(sis_couch03)
                    show sissex 54 with fastdissolve
                    pause
                    show sissex 55
                    pause
                    player_name "( Woah, they're huge... )"
                    player_name "( I can barely fit them in my hand... )"
                    show sissex 54_55
                    pause 8
                    show sissex 56 with fastdissolve
                    player_name "!!!"
                    player_name "( Oh crap! Did she wake up?! )"
                    show sissex 57 with fastdissolve
                    pause
                    show sissex 58 with fastdissolve
                    player_name "( She... )"
                    player_name "( She lifted her shirt up... )"
                    player_name "( Is she trying to tell me something? )"
                    player_name "( Maybe she wants me to feel her breasts again... )"
                    show sissex 59 with fastdissolve
                    pause
                    show sissex 60_59
                    pause 8
                    show sissex 60
                    player_name "( They're so {b}warm{/b}... )"
                    show sissex 59
                    player_name "( ...so {b}soft{/b}... )"
                    show sissex 60
                    player_name "( This is awesome... )"
                    show sissex 61 with fastdissolve
                    player_name "!!!"
                    player_name "( Oh, crap! )"
                    show sissex 62 with fastdissolve
                    player_name "( I'm getting hard... )"
                    player_name "( Shit! It's pressing right against her pussy... )"
                    player_name "( Wait... )"
                    player_name "( She didn't react at all? )"
                    player_name "( Maybe I can rub it against her... )"
                    menu:
                        "Leave.":
                            player_name "( No... It's too risky. )"
                            player_name "( I'll try some other time. )"
                            hide sissex
                            hide sis_bedcover
                            jump hallway_dialogue

                        "Rub pussy." if not sister.known(sis_shower_cuddle04):
                            show sissex 63 at Position(xpos=684) with fastdissolve
                            pause
                            show sissex 62 at Position(xpos=682)
                            pause
                            show sissex 63 at Position(xpos=684)
                            pause
                            show sissex 64 at Position(xpos=682) with fastdissolve
                            pause
                            show sissex 65
                            pause
                            show sissex 66
                            sis "{b}[firstname]{/b}?"
                            show sissex 67
                            sis "What the {b}FUCK{/b} are you doing??!!" with hpunch
                            show sissex 65b
                            player_name "Don't yell! You're gonna wake up {b}[mom_name]{/b}..."
                            show sissex 67
                            sis "You think I {b}CARE{/b}??! What's wrong with you?!"
                            show sissex 65b
                            player_name "I..."
                            player_name "I'm sorry!!"
                            show sissex 67
                            sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                            hide sissex
                            hide sis_bedcover
                            jump hallway_dialogue

                        "Rub pussy." if sister.known(sis_shower_cuddle04):
                            if not sister.known(sis_final):
                                $ sister.add_event(sis_final)
                            $ sis_shower_cuddle04.finish()
                            show sissex 63 at Position(xpos=684) with fastdissolve
                            pause
                            show sissex 62_64 at Position(xpos=682)
                            pause 8
                            show sissex 62 at Position(xpos=682)
                            player_name "( Her breathing is getting faster... )"
                            player_name "( This feeling... She's actually getting wet... )"
                            show sissex 63 at Position(xpos=684)
                            player_name "( It's {b}SO{/b} good! I want more... )"
                            show sissex 68 at Position(xpos=682) with fastdissolve
                            player_name "( Let's see if I can lower her panties... )"
                            show sissex 69 with fastdissolve
                            pause
                            show sissex 70 at Position(xpos=652) with fastdissolve
                            pause
                            show sissex 71 at Position(xpos=682) with fastdissolve
                            player_name "( Man... )"
                            show sissex 72 with fastdissolve
                            player_name "( I can't believe I'm about to do this... )"
                            menu:
                                "Leave.":
                                    player_name "( No... I can't, not yet. )"
                                    player_name "( I should get out of here before she flips out. )"
                                    hide sissex
                                    hide sis_bedcover
                                    jump hallway_dialogue

                                "Put it inside." if not sister.known(sis_shower_cuddle05) or pStats.dex() < 7:
                                    if pStats.dex() < 7:
                                        $ stat_warn = dex_warn
                                    else:
                                        $ stat_warn = ""
                                    show sissex 76 at Position(xpos=674) with fastdissolve
                                    pause
                                    show sissex 75 at Position(xpos=682)
                                    sis "[stat_warn]Do you {b}REALLY{/b} think I'm gonna let you go that far?!" with hpunch
                                    show sissex 74
                                    sis "[stat_warn]You're lucky I didn't stop you earlier, you fucking pervert!!"
                                    show sissex 73b
                                    player_name "You... you knew I was here?"
                                    show sissex 74
                                    sis "[stat_warn]Of course, you idiot! I just wanted to see how {b}desperate{/b} you were for me."
                                    show sissex 75
                                    sis "[stat_warn]Now pull up your pants and go finish what you started in your {b}OWN{/b} room!!"
                                    show sissex 73b
                                    player_name "I..."
                                    player_name "I'm sorry!!"
                                    show sissex 75
                                    sis "Yeah right, {b}GET OUT{/b}!!" with hpunch
                                    hide sissex
                                    hide sis_bedcover
                                    jump hallway_dialogue

                                "Put it inside." if sister.known(sis_shower_cuddle05) and pStats.dex() >= 7:
                                    $ sis_shower_cuddle05.finish()
                                    show sissex 76 at Position(xpos=674) with fastdissolve
                                    pause
                                    show sissex 75 at Position(xpos=682)
                                    sis "Do you {b}REALLY{/b} think I'm gonna let you go that far?!" with hpunch
                                    show sissex 74
                                    sis "You're lucky I didn't stop you earlier, you fucking pervert!!"
                                    show sissex 73b
                                    player_name "You... you knew I was here?"
                                    show sissex 74
                                    sis "Of course, you idiot! You were too slow and stupid to notice..."
                                    show sissex 73
                                    menu:
                                        "Rabbit fuck.":
                                            show sissex 77 at Position(xpos=713)
                                            sis "Ahh!!!" with vpunch
                                            show sissex 79b at Position(xpos=720) with fastdissolve
                                            sis "What are you DOING?!!"
                                            show sissex 78 at Position(xpos=713) with fastdissolve
                                            player_name "I want you, {b}[sis_name]{/b}!!!"
                                            $ anim_toggle = False
                                            $ xray = False
                                            show screen sex_xray_anim_buttons
                                            pause
                                            if anim_toggle:
                                                hide sissex 78
                                                hide screen sex_xray_anim_buttons
                                                show sissex 79_78 at Position(xpos = 720)
                                                pause 8
                                                hide sissex 79_78
                                            else:

                                                hide screen sex_xray_anim_buttons
                                                $ animcounter = 0
                                                while animcounter < 4:
                                                    show sissex 79 at Position(xpos = 720)
                                                    pause
                                                    show sissex 78 at Position(xpos = 713)
                                                    pause
                                                    $ animcounter += 1
                                            show sissex 79b at Position(xpos=720)
                                            sis "FUCK!!!"
                                            show sissex 77 at Position(xpos=713)
                                            sis "Don't go so FAST!!"
                                            show sissex 79b at Position(xpos=720)
                                            sis "Oh god..."
                                            show sissex 77 at Position(xpos=713)
                                            sis "It's..."
                                            show sissex 79 at Position(xpos=720)
                                            sis "... It's {b}SO FUCKING GOOD{/b}!!" with vpunch
                                            if anim_toggle:
                                                hide sissex 79
                                                show sissex 78_79 at Position(xpos = 713)
                                                pause 4
                                                hide sissex 78_79
                                            else:

                                                $ animcounter = 0
                                                while animcounter < 2:
                                                    show sissex 78 at Position(xpos = 713)
                                                    pause
                                                    show sissex 79 at Position(xpos = 720)
                                                    pause
                                                    $ animcounter += 1
                                            show sissex 77 at Position(xpos=713)
                                            sis "Don't you {b}DARE{/b} cum inside me..."
                                            show sissex 79b at Position(xpos=720)
                                            sis "... I swear, I'll {b}KILL YOU{/b}!!"
                                            label sisbedroom_sex_loop:
                                                menu:
                                                    "Keep going.":
                                                        show sissex 79b at Position(xpos = 720)
                                                        show screen sex_xray_anim_buttons
                                                        pause
                                                        if anim_toggle:
                                                            hide sissex 79b
                                                            hide screen sex_xray_anim_buttons
                                                            show sissex 78_79 at Position(xpos = 713)
                                                            pause 8
                                                            hide sissex 78_79
                                                            show sissex 79b at Position(xpos = 720)
                                                        else:

                                                            hide screen sex_xray_anim_buttons
                                                            $ animcounter = 0
                                                            while animcounter < 4:
                                                                show sissex 78 at Position(xpos = 713)
                                                                pause
                                                                show sissex 79 at Position(xpos = 720)
                                                                pause
                                                                $ animcounter += 1
                                                        jump sisbedroom_sex_loop

                                                    "Cum inside." if pStats.str() < 7:
                                                        show sissex 78 at Position(xpos=713)
                                                        pause
                                                        show sissex 79 at Position(xpos=720)
                                                        pause
                                                        show sissex 89b at Position(xpos=674) with hpunch
                                                        pause
                                                        show white zorder 3
                                                        show sissex 89c
                                                        hide white with dissolve
                                                        pause
                                                        show sissex 88 at Position(xpos=674)
                                                        sis "[str_warn]What the {b}FUCK{/b}??" with vpunch
                                                        sis "[str_warn]Were you about to cum INSIDE ME??"
                                                        show sissex 89
                                                        player_name "Don't yell! You're gonna wake up {b}[mom_name]{/b}..."
                                                        show sissex 87
                                                        sis "[str_warn]What's wrong with you?!"
                                                        show sissex 88
                                                        sis "[str_warn]You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!!"
                                                        show sissex 89
                                                        player_name "I..."
                                                        player_name "I'm sorry!!"
                                                        show sissex 88
                                                        sis "Yeah. Suure you are! {b}GET OUT{/b}!!"
                                                        hide sissex
                                                        hide sis_bedcover
                                                        jump hallway_dialogue

                                                    "Cum inside." if pStats.str() >= 7:
                                                        show sissex 78 at Position(xpos=713)
                                                        pause
                                                        show sissex 79 at Position(xpos=720)
                                                        sis "Oh god..."
                                                        show sissex 78 at Position(xpos=713)
                                                        sis "... I can't take much more..."
                                                        show sissex 80a at Position(xpos=738)
                                                        sis "{b}Ahhhh!!!!{/b}" with vpunch
                                                        show white zorder 3
                                                        show sissex 80b
                                                        hide white with dissolve
                                                        pause
                                                        show white zorder 3
                                                        show sissex 80c
                                                        hide white with dissolve
                                                        pause
                                                        $ xray=False
                                                        show sissex 81b at Position(xpos=674) with fastdissolve
                                                        sis "{b}*Panting*{/b}"
                                                        show sissex 81 at Position(xpos=674)
                                                        sis "Did you just cum inside me??"
                                                        show sissex 90
                                                        player_name "I... I'm not sure..."
                                                        show sissex 82
                                                        sis "Don't lie! I felt it, it just kept shooting deep inside me!"
                                                        show sissex 90
                                                        player_name "It was a reflex!"
                                                        player_name "I... I couldn't stop..."
                                                        show sissex 82
                                                        sis "What's wrong with you?!" with hpunch
                                                        sis "You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!!"
                                                        show sissex 90
                                                        player_name "I..."
                                                        player_name "I'm sorry!!"
                                                        show sissex 82
                                                        sis "Just..."
                                                        sis "Just {b}GET OUT{/b}!!" with hpunch
                                                        hide sissex
                                                        hide sis_bedcover
                                                        jump hallway_dialogue
                                                    "Cum outside.":

                                                        show sissex 78 at Position(xpos=713)
                                                        pause
                                                        show sissex 79 at Position(xpos=720)
                                                        pause
                                                        show sissex 85b at Position(xpos=674)
                                                        pause
                                                        show white zorder 3
                                                        show sissex 85 at Position(xpos=674)
                                                        hide white with dissolve
                                                        pause
                                                        show sissex 86 with fastdissolve
                                                        player_name "Ahh..."
                                                        show sissex 88
                                                        sis "Are you SATISFIED now?! You little shit..." with hpunch
                                                        show sissex 87
                                                        sis "You're lucky I was feeling horny..."
                                                        sis "... and that you have a nice... dick."
                                                        show sissex 89
                                                        player_name "I enjoyed it too-"
                                                        show sissex 87
                                                        sis "I don't care!!"
                                                        show sissex 88
                                                        sis "Hurry up and {b}GET OUT{/b}!!"
                                                        hide sissex
                                                        hide sis_bedcover
                                                        jump hallway_dialogue

label sis_button_dialogue:
    if sis_panties_trade:
        if not sis_panties_bought:
            scene sisbedroom with None
            show sis 9 at right
            show sis 9 at Position(xpos=937)
            show player 11 at left
            with dissolve
            sis "If you're here for the {b}panties{/b}, I told you, {b}$100{/b} or nothing."
            show sis 6
            if inventory.money >= panties.cost:
                menu:
                    "Here's $100.":
                        show player 12 at left
                        show sis 18 at right
                        player_name "Okay, fine."
                        $ inventory.money -= 100
                        $ inventory.items.append(panties)
                        $ sis_panty01.finish()
                        $ completed_quests.append(quest07)
                        $ sis_panties_bought = True
                        play audio coins2
                        show player 41 at Position (xpos=38) with fastdissolve
                        pause
                        show sis 80 at Position(xpos=945)
                        show player 1 at left
                        sis "Alright, you can keep them..." with fastdissolve
                        show sis 81
                        show player 11
                        sis "Now, get out of my room, pervert!"
                        show sis 14
                        show unlock17 at truecenter
                        pause
                        hide unlock17 with dissolve
                        hide player
                        hide sis
                        jump hallway_dialogue
                    "I don't need it.":

                        show sis 10 at Position(xpos=937)
                        show player 35 at left
                        player_name "Actually, I don't need any right now..."
                        show sis 9
                        show player 39 at Position (xpos=38)
                        sis "Then give them back, and get out of my room, you pervert!"
                        hide player
                        hide sis
                        jump hallway_dialogue
            else:

                menu:
                    "I don't have enough.":
                        show player 24 at left
                        show sis 10 at Position(xpos=937)
                        player_name "I don't have that much money on me..."
                        show sis 9
                        show player 5
                        sis "Too bad! Get out of my room, you pervert!"
                        hide player
                        hide sis
                        jump hallway_dialogue
        else:

            scene sisbedroom with None
            show player 11 at left
            show sis 19 at right
            with dissolve




            if not sister.over(sis_panty02):
                sis "Well, well..."
                sis "What would my perverted little brother want this time?"
                sis "More {b}panties{/b}, perhaps?"
            elif not sister.over(sis_panty03):
                sis "Well, well..."
                sis "What would my perverted little brother want this time?"
                sis "Let me guess, more {b}panties{/b}?"
            elif not sister.over(sis_panty04):
                sis "Well, well..."
                sis "What would my perverted little brother want this time?"
                show player 1
                sis "Don't tell me: it's more {b}panties{/b}."
            else:
                sis "Well, well..."
                sis "What would my perverted little brother want this time?"
            show sis 18
            menu sis_bedroom_menu:
                "Talk.":
                    if not sister.over(sis_shower_cuddle02):
                        show player 2
                        player_name "I was just wondering how you're doing."
                        show player 13
                        show sis 10 at Position(xpos = 937)
                        sis "..."
                        show sis 9
                        sis "You usually don't ask me those things..."
                        sis "Why do you care all of a sudden?"
                        show player 2
                        show sis 9b
                        player_name "Well, you're my {b}big sister{/b} and sometimes I feel like we should be closer."
                        show player 11
                        show sis 7 at right
                        sis "Listen, you idiot."
                        sis "I'm fine, and we're NOT friends."
                        show sis 8
                        show player 5
                        player_name "..."
                        show sis 9 at Position(xpos = 937)
                        sis "Is there anything else you wanted to talk about, or can I just kick you out of my room?"
                    else:
                        show player 14
                        player_name "I wanted to say that I'm enjoying cuddling with you at night..."
                        show player 18
                        player_name "...I'm just glad you're starting to like me more."
                        show player 13
                        show sis 10 at Position(xpos = 937)
                        sis "..."
                        show player 11
                        show sis 9
                        sis "Really?"
                        show sis 7 at right
                        sis "You think I'm doing it because I like you?!"
                        show sis 9 at Position(xpos = 937)
                        sis "Man, you're so pathetic."
                        show player 5
                        show sis 6
                        player_name "..."
                        show sis 12
                        sis "Just don't get too greedy. You're lucky I let you in my room to begin with."
                        show sis 9
                        sis "Is there anything else you wanted to talk about, or can I just kick you out of my room?"

                "I love you." if sister.over(sis_final2):
                    if sis_confession_first:
                        show player 2 at left
                        player_name "Hey, {b}[sis_name]{/b}..."
                        show player 29
                        player_name "I... I wanted to tell you something..."
                        show player 1
                        show sis 10 at Position(xpos = 937)
                        sis "Uhh... okay?"
                        show player 2
                        player_name "Well..."
                        show player 3
                        show sis 9
                        sis "Spit it out! I don't have all day!"
                        show player 21
                        show sis 9b
                        player_name "I think I love you."
                        show sis 10
                        sis "?!?" with hpunch
                        show player 5
                        show sis 7 at right
                        sis "Eww! What the fuck!?"
                        sis "What's wrong with you??"
                        show player 22
                        show sis 8
                        player_name "!!!"
                        show player 5
                        show sis 9 at Position(xpos = 937)
                        sis "Why are you talking like that?"
                        show player 25
                        show sis 6
                        player_name "I don't know... It's just a feeling I had!!"
                        show player 22
                        show sis 7 at right
                        sis "I'm your Sister! Not some girlfriend from school, you IDIOT!!"
                        show player 6
                        show sis 8
                        player_name "I'm sorry!!"
                        show player 5
                        show sis 9 at Position(xpos = 937)
                        sis "Just because I let you fuck me on my cam shows, doesn't mean that I have feelings for you! Got it?!"
                        show player 25
                        show sis 6
                        player_name "Yes... I understand..."
                        show player 5
                        show sis 7 at right
                        sis "Good! Now, {b}GET OUT OF MY ROOM{/b}!!" with hpunch
                        show player 22
                        show sis 8
                        player_name "!!!"
                        hide player
                        show sis 9 at Position(xpos = 937)
                        with fade
                        sis "Gosh... Have I gone too far?"
                        sis "I knew he liked me but... I can't believe my little brother is starting to have feelings for me now."
                        sis "He has been pretty helpful... I'm making tons of money with my cam show because of him..."
                        sis "Ugh!! He's probably just horny."
                        $ sis_confession_first = False
                        hide sis
                        hide sisbedroom
                        jump hallway_dialogue
                    else:

                        show player 14 at left
                        player_name "Hey {b}[sis_name]{/b}..."
                        player_name "Just letting you know that I like you a lot."
                        show player 1
                        show sis 9 at Position(xpos = 937)
                        sis "Again??"
                        show player 17
                        show sis 9b
                        player_name "I think that, I love you."
                        show sis 10
                        sis "?!?" with hpunch
                        show player 25
                        show sis 9
                        sis "You have to stop with that!!"
                        sis "What's wrong with you??"
                        show player 22
                        show sis 6
                        player_name "!!!"
                        show sis 7 at right
                        sis "I'm your Sister! Not some girlfriend from school, you IDIOT!!"
                        show player 6
                        show sis 8
                        player_name "I'm sorry!!"
                        show player 5
                        show sis 9 at Position(xpos = 937)
                        sis "Just because I let you fuck me on my cam shows, doesn't mean that I have feelings for you! Got it?!"
                        show sis 6
                        show player 24
                        player_name "Yes... I understand..."
                        show sis 7 at right
                        sis "Good! Now, {b}GET OUT OF MY ROOM{/b}!!"
                        show player 22
                        show sis 8
                        player_name "!!!"
                        hide player
                        show sis 9 at Position(xpos = 937)
                        with fade
                        sis "Ugh!! He's probably just horny."
                        hide sis
                        hide sisbedroom
                        jump hallway_dialogue

                "Trade for panties." if not sister.completed(sis_panty04):
                    if not sister.over(sis_panty02):
                        menu:

                            "Not yet." if not sister.known(sis_panty02) or sister.completed(sis_panty02):
                                show player 12 at left
                                show sis 10 at Position(xpos=937)
                                player_name "I'm fine for now."
                                show sis 9
                                show player 11
                                sis "So... What are you doing here, then?"
                                show sis 10
                                show player 10
                                player_name "I uhh... I'm just-"
                                show sis 7 at right
                                show player 11
                                sis "I'm busy right now, can't you see!?"
                                show sis 8
                                show player 12
                                player_name "Alright..."
                                show sis 9 at Position(xpos=937)
                                show player 11
                                sis "And close the door on the way out!"
                                sis "I wouldn't want a pervert spying on me."
                                show sis 6
                                player_name "..."
                                show player 10
                                player_name "Okay..."
                                hide player
                                hide sis
                                jump hallway_dialogue

                            "Yeah, more panties." if sister.started(sis_panty02):
                                if sis_quest_first:
                                    show player 21 at left
                                    show sis 11 at Position(xpos=937)
                                    player_name "Yeah, more panties, actually."
                                    show sis 10
                                    player_name "Except this time... I need {b}used panties{/b}..."
                                    show player 11
                                    show sis 7 at right
                                    sis "USED?!" with hpunch
                                    show sis 8
                                    show player 10
                                    player_name "I know... That's what he said, though..."
                                    show sis 9 at Position(xpos=937)
                                    show player 11
                                    sis "Just give him a pair from my drawer!"
                                    show sis 10
                                    show player 10
                                    player_name "I can't! He said I need to make {b}SURE{/b} they've been {b}worn{/b}..."
                                    show sis 55 at right
                                    show player 11
                                    sis "You mean I have to give you {b}THESE{/b}??"
                                    show sis 6 at Position(xpos=937)
                                    show player 21
                                    player_name "Yeah... I guess so..."
                                    show sis 11
                                    show player 11
                                    sis "Hmmm..."
                                    show sis 9
                                    show player 13
                                    sis "Fine! I'll do it!"
                                    show sis 12
                                    show player 11
                                    sis "But you'll have to {b}buy{/b} me something."
                                    show sis 18 at right
                                    player_name "..."
                                    show sis 19
                                    sis "You heard me."
                                    sis "You have to buy me some {b}girl toys{/b}."
                                    show sis 10 at Position(xpos=937)
                                    show player 12
                                    player_name "What?"
                                    show sis 9
                                    show player 11
                                    sis "Stop acting so innocent! You know what I'm talking about!"
                                    sis "{b}Sex{/b} toys!!"
                                    show sis 61 at right with fastdissolve
                                    sis "Like one of these!"
                                    show sis 18 with fastdissolve
                                    player_name "!!!"
                                    show player 14
                                    player_name "I guess I could..."
                                    show player 10
                                    player_name "But... aren't those expensive? And where do I get them, anyway?"
                                    show sis 9 at Position(xpos=937)
                                    show player 11
                                    sis "I know you have the cash for it..."
                                    show sis 12
                                    sis "And you can buy them at {b}Pink{/b}, in the {b}Mall{/b}."
                                    show sis 82
                                    show player 12
                                    player_name "Which one do you want?"
                                    show sis 12
                                    show player 11
                                    sis "I want the {b}Electro Clit{/b}. It's the purple one."
                                    show sis 10
                                    show player 10
                                    player_name "I don't know if I can do it... people might see me going in that store..."
                                    show sis 7 at right
                                    show player 11
                                    sis "{b}LOOK{/b}! I'm doing you a favor, okay?!"
                                    show sis 9 at Position(xpos=937)
                                    sis "If you're not going to trade for them, then go away!!"
                                    show player 21
                                    show sis 82
                                    player_name "Well... I guess I have to..."
                                    show sis 19 at right
                                    show player 11
                                    sis "Come back to me when you have that {b}toy{/b}."
                                    hide player
                                    hide sis
                                    $ sis_quest_first = False
                                    jump hallway_dialogue
                                else:

                                    scene sisbedroom
                                    show sis 17 at right
                                    show sis 9 at Position(xpos=937)
                                    show player 11 at left
                                    with dissolve
                                    sis "Well? Did you find the {b}toy{/b}?"
                                    show sis 6
                                    menu:
                                        "Here's the toy." if electroclit in inventory.items:
                                            show player 239_240
                                            pause
                                            show sis 18 zorder 2 at right
                                            show player 287 zorder 1 at left
                                            player_name "Here's your toy..." with fastdissolve
                                            show sis 62
                                            show player 13
                                            sis "Thanks!" with fastdissolve
                                            $ inventory.items.remove(electroclit)
                                            show sis 11 at Position(xpos=937)
                                            show player 14
                                            with fastdissolve
                                            player_name "What about the panties?"
                                            show sis 9
                                            show player 11
                                            sis "Leave my room so I can change."
                                            show sis 10
                                            show player 10
                                            player_name "But... I was told to make SURE they're used."
                                            show sis 9
                                            show player 11
                                            sis "So? They are!"
                                            show sis 10
                                            show player 10
                                            player_name "I'm sorry, but... I was told to be present when you take them off..."
                                            show sis 9
                                            show player 11
                                            sis "Wow... You really ARE a pervert!"
                                            sis "Fine..."
                                            sis "But cover your eyes! I'm not letting you watch me!"
                                            show sis 6
                                            show player 296
                                            player_name "..."

                                            show sis 50 at Position(xpos=1017) with fastdissolve
                                            pause
                                            show sis 52 with fastdissolve
                                            pause
                                            show sis 53 at right with fastdissolve

                                            sis "Here! Take them!"
                                            show player 291 at Position(xpos=38)
                                            show sis 56
                                            with fastdissolve
                                            pause
                                            show player 292
                                            player_name "Thanks..."
                                            show player 290
                                            show sis 59
                                            sis "Now, get out of my room, pervert!" with hpunch
                                            show sis 58
                                            show unlock17 zorder 3 at truecenter
                                            pause
                                            hide unlock17 with dissolve
                                            hide player
                                            hide sis
                                            $ inventory.items.append(panties)
                                            $ sis_panty02.finish()
                                            $ sis_quest_first = True
                                            jump hallway_dialogue

                                        "I don't have it." if electroclit not in inventory.items:
                                            show player 24 at left
                                            show sis 10 at Position(xpos=937)
                                            player_name "I don't have the toy yet..."
                                            show sis 9
                                            show player 5
                                            sis "Too bad. Get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue
                                        "I don't need it.":

                                            show sis 10 at Position(xpos=937)
                                            show player 35 at left
                                            player_name "Actually, I don't need any {b}panties{/b} right now..."
                                            show sis 9
                                            show player 11
                                            sis "Then get out of my room, pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue

                    elif not sister.over(sis_panty03):
                        menu:

                            "Not yet." if not sister.known(sis_panty03) or sister.completed(sis_panty03):
                                show player 12 at left
                                show sis 10 at Position(xpos=937)
                                player_name "I'm fine for now."
                                show sis 9
                                show player 11
                                sis "So... What are you doing here, then?"
                                show sis 10
                                show player 10
                                player_name "I uhh... I'm just-"
                                show sis 7 at right
                                show player 11
                                sis "I'm busy right now, can't you see!?"
                                show sis 8
                                show player 12
                                player_name "Alright..."
                                show sis 9 at Position(xpos=937)
                                show player 11
                                sis "And close the door on the way out!"
                                sis "I wouldn't want a pervert spying on me."
                                show sis 6
                                player_name "..."
                                show player 10
                                player_name "Okay..."
                                hide player
                                hide sis
                                jump hallway_dialogue

                            "Yeah, more panties." if sister.started(sis_panty03):
                                if sis_quest_first:
                                    show player 21 at left
                                    show sis 11 at Position(xpos=937)
                                    player_name "Yeah, more panties, actually."
                                    show sis 10
                                    player_name "But this time... I need... {b}wet panties{/b}..."
                                    show sis 7 at right
                                    show player 11
                                    sis "First used, now {b}wet{/b} ones?!"
                                    show sis 9 at Position(xpos=937)
                                    sis "Just who the fuck is this creep?"
                                    show sis 6
                                    show player 10
                                    player_name "Look, it doesn't matter: He said I need to make sure they're wet..."
                                    show sis 9
                                    show player 11
                                    sis "You've got to be kidding me!!"
                                    sis "You mean I have to make them {b}WET{/b}??"
                                    show sis 6
                                    show player 21
                                    player_name "Yeah... I guess so..."
                                    show sis 9
                                    show player 11
                                    sis "You're starting to get pushy with those demands..."
                                    sis "...but I'll do it."
                                    sis "You'll have to buy me more {b}girl toys{/b}, though."
                                    show sis 82
                                    show player 14
                                    player_name "Sure..."
                                    player_name "I guess I could..."
                                    player_name "Which one do you want this time?"
                                    show player 11
                                    show sis 12
                                    sis "I want the {b}UltraVibrator 2000{/b}."
                                    show sis 10
                                    show player 12
                                    player_name "Damn... I really don't like going into that store..."
                                    show sis 7 at right
                                    show player 11
                                    sis "{b}LOOK{/b}! You're asking me for {b}WET{/b} panties, okay?!" with hpunch
                                    sis "If you're not going to trade for them, then go away!!"
                                    show sis 18 at right
                                    show player 21
                                    player_name "Well... I guess I have to..."
                                    show sis 19
                                    show player 11
                                    sis "Come back to me when you have that {b}toy{/b}."
                                    hide player
                                    hide sis
                                    $ sis_quest_first = False
                                    jump hallway_dialogue
                                else:

                                    scene sisbedroom
                                    show sis 17 at right
                                    show sis 9 at Position(xpos=937)
                                    show player 11 at left
                                    with dissolve
                                    sis "Well? Did you find the {b}toy{/b}?"
                                    show sis 6
                                    menu:
                                        "Here's the toy." if ultravibrato in inventory.items:
                                            show player 239_240
                                            pause
                                            show sis 18 zorder 2 at right
                                            show player 288 zorder 1 at left
                                            player_name "Here's your toy..." with fastdissolve
                                            show sis 63
                                            show player 13
                                            sis "Thanks!" with fastdissolve
                                            $ inventory.items.remove(ultravibrato)
                                            show sis 11 at Position(xpos=937)
                                            show player 14
                                            player_name "What about the panties?" with fastdissolve
                                            show sis 9
                                            show player 11
                                            sis "Right... You wanted {b}wet{/b} panties, huh?"
                                            show sis 10
                                            show player 10
                                            player_name "Yeah... It has to be fresh..."
                                            show sis 9
                                            show player 5
                                            sis "Man, you really are sick and perverted."
                                            show sis 10
                                            show player 10
                                            player_name "I'm sorry, I was told to make sure..."
                                            show sis 9
                                            show player 11
                                            sis "I guess my little brother has to be a witness, then."
                                            sis "Stay right there so I can get this done."
                                            show sis 10
                                            show player 21
                                            player_name "What are you gonna do?"
                                            show sis 7 at right
                                            show player 11
                                            sis "What do you think?!"
                                            sis "I'm getting those panties WET, you IDIOT!!"
                                            show sis 9 at Position(xpos=937)
                                            sis "So cover your eyes, I can't do it with you watching me."
                                            show player 10
                                            player_name "Okay..."
                                            scene sisbedroom_c_2
                                            pause 0.001
                                            show player 296 zorder 1 at left
                                            show sis 66 zorder 0 at Position(xpos=546)
                                            with dissolve
                                            pause
                                            show sis 68 with fastdissolve
                                            pause
                                            show sis 69_68
                                            pause 5
                                            show sis 67
                                            sis "Ahhh..." with fastdissolve
                                            show sis 66
                                            player_name "!!!"
                                            show sis 67
                                            sis "There, that should do it..."
                                            scene sisbedroom
                                            show player 296 at left
                                            show sis 51 at right
                                            with dissolve
                                            pause
                                            show sis 52 with fastdissolve
                                            pause
                                            show sis 54 at right with fastdissolve
                                            sis "Here. Take them!"
                                            show player 291 at Position(xpos=38)
                                            show sis 56
                                            with fastdissolve
                                            pause
                                            show sis 57
                                            sis "I bet you enjoyed this little session, you sicko."
                                            show player 292
                                            show sis 56
                                            player_name "I just-"
                                            show player 290
                                            show sis 59
                                            sis "Get out of my room, you pervert!" with hpunch
                                            show sis 58
                                            show unlock31 zorder 3 at truecenter
                                            pause
                                            hide unlock31 with dissolve
                                            hide player
                                            hide sis
                                            $ inventory.items.append(panties)
                                            $ sis_panty03.finish()
                                            $ sis_quest_first = True
                                            jump hallway_dialogue

                                        "I don't have it." if ultravibrato not in inventory.items:
                                            show player 24 at left
                                            show sis 10 at Position(xpos=937)
                                            player_name "I don't have the toy yet..."
                                            show sis 9
                                            show player 5
                                            sis "Too bad. Get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue
                                        "I don't need it.":

                                            show sis 10 at Position(xpos=937)
                                            show player 35 at left
                                            player_name "Actually, I don't need any {b}panties{/b} right now..."
                                            show sis 9
                                            show player 11
                                            sis "Then get out of my room, pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue

                    elif not sister.over(sis_panty04):
                        menu:

                            "Not yet." if not sister.known(sis_panty04) or sister.completed(sis_panty04):
                                show player 12 at left
                                show sis 10 at Position(xpos=937)
                                player_name "I'm fine for now."
                                show sis 9
                                show player 11
                                sis "So... What are you doing here, then?"
                                show sis 10
                                show player 10
                                player_name "I uhh... I'm just-"
                                show sis 7 at right
                                show player 11
                                sis "I'm busy right now, can't you see!?"
                                show sis 8
                                show player 12
                                player_name "Alright..."
                                show sis 9 at Position(xpos=937)
                                show player 11
                                sis "And close the door on the way out!"
                                sis "I wouldn't want a pervert spying on me."
                                show sis 6
                                player_name "..."
                                show player 10
                                player_name "Okay..."
                                hide player
                                hide sis
                                jump hallway_dialogue

                            "Yeah, more panties." if sister.started(sis_panty04):
                                if sis_quest_first:
                                    show player 21 at left
                                    show sis 11 at Position(xpos=937)
                                    player_name "Yeah, one last time, actually."
                                    show sis 10
                                    player_name "But this time... I need you to {b}squirt on them{/b}..."
                                    show player 11
                                    sis "?!"
                                    show player 10
                                    player_name "I know!!... That's what he said, though..."
                                    show sis 9
                                    show player 1
                                    sis "Squirt?"
                                    show sis 6
                                    show player 10
                                    player_name "I know! He said I need to make {b}SURE{/b} they're {b}soaked in squirt{/b}..."
                                    show sis 7 at right
                                    show player 11
                                    sis "You mean I have to {b}SQUIRT{/b} onto them??" with hpunch
                                    show sis 8
                                    show player 21
                                    player_name "Yeah, I guess so... they have to be really wet with that stuff!"
                                    show sis 9 at Position(xpos=937)
                                    show player 11
                                    sis "You're starting to make this quite hard..."
                                    show sis 12
                                    show player 13
                                    sis "...But I think I've got an idea..."
                                    show player 11
                                    sis "You'll have to buy me a specific {b}toy{/b}, though."
                                    show sis 82
                                    show player 21
                                    player_name "Yeah, no problem..."
                                    player_name "Which one?"
                                    show player 11
                                    show sis 19 at right
                                    sis "I'll need the {b}Dual Sybian{/b}."
                                    show sis 18
                                    player_name "..."
                                    show player 10
                                    show sis 10 at Position(xpos=937)
                                    player_name "The what?"
                                    show player 11
                                    show sis 9
                                    sis "It looks kind of like a saddle, you can't miss it."
                                    show player 12
                                    show sis 10
                                    player_name "Uhh, how much does it cost?"
                                    show player 11
                                    show sis 7 at right
                                    sis "{b}LOOK{/b}, you're asking me to squirt, okay?!" with hpunch
                                    sis "If you're not going to get that {b}toy{/b}, you can forget about it!!"
                                    show sis 8
                                    show player 10
                                    show sis 18
                                    player_name "Okay, okay!!"
                                    show player 11
                                    show sis 19
                                    sis "Come back to me when you get it."
                                    hide player
                                    hide sis
                                    $ sis_quest_first = False
                                    jump hallway_dialogue
                                else:

                                    scene sisbedroom
                                    show sis 17 at right
                                    show sis 9 at Position(xpos=937)
                                    show player 11 at left
                                    with dissolve
                                    sis "Well? Did you find the {b}toy{/b}?"
                                    show sis 6
                                    menu:
                                        "Here's the toy." if sybian in inventory.items:
                                            show player 239_240
                                            pause
                                            show sis 18 zorder 2 at right
                                            show player 289 zorder 1 at Position(xpos=12)
                                            player_name "Yeah, I got it." with fastdissolve
                                            player_name "Man... this thing is heavy!!"
                                            show player 13 at left
                                            show sis 64
                                            sis "Thanks!" with fastdissolve
                                            $ inventory.items.remove(sybian)
                                            show player 21
                                            show sis 10 at Position(xpos=937)
                                            player_name "So... how are we going about getting your squirt on the panties?" with fastdissolve
                                            show player 1
                                            show sis 9
                                            sis "Right... You wanted my {b}squirt{/b} on these panties..."
                                            show player 21
                                            show sis 10
                                            player_name "Yeah. It has to be really wet..."
                                            show player 11
                                            show sis 12
                                            sis "I've never squirted before... But now that you got me a Dual Sybian..."
                                            show player 21
                                            show sis 82
                                            player_name "You can do it?"
                                            show player 11
                                            show sis 19 at right
                                            sis "Maybe... but I may need some help."
                                            show sis 18
                                            player_name "..."
                                            show player 10
                                            player_name "What do you-"
                                            show player 11
                                            show sis 60
                                            with fastdissolve
                                            sis "Shut up and take this remote."
                                            show sis 18
                                            show player 293
                                            with fastdissolve
                                            pause
                                            show player 295
                                            show sis 64
                                            with fastdissolve
                                            sis "This thing needs a {b}test run{/b}."
                                            sis "Don't bother closing your eyes..."
                                            sis "You gotta see the remote, after all."
                                            scene sisbedroom_c_2b
                                            pause 0.001
                                            show sis 70 at Position(xpos=686)
                                            with dissolve
                                            pause
                                            show sis 50 at right with fastdissolve
                                            pause
                                            show sis 52 with fastdissolve
                                            pause
                                            show sis 71 at Position (xpos=824,ypos=701) with fade
                                            pause
                                            show sis 72 at Position (xpos=845,ypos=723) with dissolve
                                            pause
                                            player_name "What am I supposed to do?"
                                            show sis 75
                                            sis "I need you to turn it on, you idiot!" with hpunch
                                            show sis 72
                                            player_name "Okay! Okay!"
                                            $ sybian_stage = 0
                                            $ sis_sybian_speed = 0.8
                                            hide player
                                            show screen sybianscr
                                            with fastdissolve
                                            pause
                                            label sybian_stage1:
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                sis "Oh!.." with vpunch
                                                show sis 83 at Position (xpos=845,ypos=723)
                                                sis "That's... interesting..."
                                                show sis 74_83 at Position (xpos=843,ypos=723)
                                                pause 5
                                                show sis 75 at Position (xpos=845,ypos=723)
                                                sis "You gotta make it go faster, you IDIOT!!"
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                show screen sybianscr
                                                with fastdissolve
                                                pause

                                            label sybian_stage2:
                                                show sis 83 at Position (xpos=845,ypos=723)
                                                sis "Oh, My, God!!" with vpunch
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                sis "This thing is fucking amazing!!"
                                                show sis 74_83 at Position (xpos=843,ypos=723)
                                                pause 5
                                                show sis 75 at Position (xpos=845,ypos=723)
                                                sis "Faster, make it go FASTER!!"
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                show screen sybianscr
                                                with fastdissolve
                                                pause

                                            label sybian_stage3:
                                                show sis 83 at Position (xpos=845,ypos=723)
                                                sis "Ahhhh!!!" with vpunch
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                sis "OH GOD..."
                                                show sis 83 at Position (xpos=845,ypos=723)
                                                sis "...I THINK..."
                                                show sis 74 at Position (xpos=843,ypos=723)
                                                sis "...I'M..."
                                                show sis 83 at Position (xpos=845,ypos=723)
                                                sis "...I'M CUMMING!!!"
                                                show sis 76 at Position (xpos=842,ypos=701)
                                                sis "Ahhh!!!" with vpunch
                                            scene sisbedroom
                                            pause 0.001
                                            show player 13 at left
                                            show sis 57 at right
                                            with dissolve
                                            sis "Wow..."
                                            sis "I didn't know I could do that."
                                            show sis 54 at right
                                            show player 11
                                            sis "I bet you enjoyed taking part, you nasty boy." with fastdissolve
                                            sis "Here you go."
                                            show player 314 at Position(xpos=38)
                                            show sis 56
                                            player_name "I uhh-" with fastdissolve
                                            show player 313
                                            show sis 56
                                            with fastdissolve
                                            pause
                                            show player 314
                                            player_name "Thanks..."
                                            show sis 57
                                            show player 313
                                            sis "No..."
                                            sis "Thank YOU, for the help..."
                                            sis "Now, get out of my room, you pervert."
                                            show sis 56
                                            show unlock31 zorder 3 at truecenter
                                            pause
                                            hide unlock31 with dissolve
                                            hide player
                                            hide sis
                                            $ inventory.items.append(panties)
                                            $ sis_panty04.finish()
                                            $ sis_quest_first = True
                                            jump hallway_dialogue

                                        "I don't have it." if sybian not in inventory.items:
                                            show player 24 at left
                                            show sis 10 at Position(xpos=937)
                                            player_name "I don't have the toy yet..."
                                            show sis 9
                                            show player 5
                                            sis "Too bad. Get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue
                                        "I don't need it.":

                                            show sis 10 at Position(xpos=937)
                                            show player 35 at left
                                            player_name "Actually, I don't need any {b}panties{/b} right now..."
                                            show sis 9
                                            show player 11
                                            sis "Then get out of my room, pervert!"
                                            hide player
                                            hide sis
                                            jump hallway_dialogue

                "Make a deal." if sister.over(sis_breakfast):
                    if sis_deal_first:
                        show player 1 at left
                        show sis 7 at right
                        show sis 12 at Position(xpos=937)
                        with dissolve
                        sis "So?"
                        sis "Have you thought about our little {b}deal{/b}?"
                        show player 14
                        show sis 11
                        player_name "Well, I don't mind lending you some money, but when do I get it back?"
                        show player 1
                        show sis 9
                        sis "Oh yeah, about that... I really do need all the money I can get."
                        show player 11
                        show sis 12
                        sis "So what if, you know... I could repay you in a {b}different way{/b}?"
                        sis "Maybe do {b}something{/b} for you..."
                        show sis 11
                        show player 21
                        player_name "Like what?"
                        show player 11
                        show sis 19 at right
                        sis "I don't know, maybe something you'd like?"
                        sis "Something that you've always wanted?"
                        show sis 6 at Position(xpos=937)
                        show player 10
                        player_name "Uhh... I don't know..."
                        show player 11
                        show sis 9
                        sis "Gosh, You're so stupid!"
                        show sis 7 at right
                        sis "I'm trying to {b}TELL YOU{/b} something!" with hpunch
                        show player 10
                        show sis 6 at Position(xpos=937)
                        player_name "I don't get it! What are you offering?!"
                        show player 11
                        show sis 12
                        sis "You always stare at my {b}breasts{/b} like a pervert!"
                        sis "I can let you {b}see{/b} them... maybe even let you {b}touch{/b} them..."
                        show player 21
                        show sis 18 at right
                        player_name "Re- Really?"
                        player_name "Well, how much money do you need?"
                        show sis 19
                        show player 11
                        sis "I'll do it for {b}$500{/b}."
                        show player 12
                        show sis 8
                        player_name "That's a lot of money..."
                        show player 11
                        show sis 7
                        sis "Excuse me?!"
                        sis "They're worth WAY more than that!!"
                        show sis 9 at Position(xpos=937)
                        sis "So, deal or no deal?"
                        show player 11
                        show sis 6
                        menu:
                            "Alright." if inventory.money >= 500:
                                $ sis_deal_first = False
                                $ sister.add_event(sis_shower_cuddle02)
                                show player 12 at left
                                show sis 82 at Position(xpos=937)
                                player_name "Fine."
                                show player 41 at Position(xpos=38) with fastdissolve
                                pause
                                show player 11 at left
                                show sis 80 at Position(xpos=945)
                                sis "Hold on: I'm counting it first." with fastdissolve
                                show sis 14
                                sis "Hmm..."
                                $ inventory.money -= 500
                                play audio coins2
                                show player 1
                                show sis 12 at Position(xpos=937)
                                sis "Fine. It's all here." with fastdissolve
                                show sis 10
                                show player 21
                                player_name "So... how do we do this?"
                                show player 11
                                show sis 7 at right
                                sis "You're not touching ANYTHING, unless I tell you otherwise. Understood?!"
                                show player 21
                                show sis 8
                                player_name "Okay..."
                                show sis 161 at Position(xpos = 943) with fastdissolve
                                pause
                                show sis 162 with fastdissolve
                                pause
                                show sis 91 at right with fastdissolve
                                show player 1
                                sis "You can touch it with ONE hand..."
                                hide player
                                show sis 92
                                with fastdissolve
                                pause
                                show sis 94 with fastdissolve
                                pause
                                show sis 93_94
                                pause 8
                                show sis 95_94
                                pause 8
                                show sis 95
                                sis "Why are you squeezing my nipple like that?"
                                show sis 94
                                sis "Can't you just touch it normally?"
                                show sis 95
                                pause
                                show sis 96
                                sis "Hahh..."
                                label sis_titsplay_menu:
                                    menu:
                                        "Continue.":
                                            show sis 93_94
                                            pause 8
                                            show sis 95_94
                                            pause 8
                                            show sis 95
                                            pause
                                            show sis 96
                                            sis "Hahh..."
                                            jump sis_titsplay_menu

                                        "Suck on it." if pStats.dex() < 5:
                                            show sis 97 at Position(xpos=1008) with fastdissolve
                                            pause
                                            show sis 98
                                            sis "[dex_warn]What the FUCK?!" with hpunch
                                            show sis 102
                                            show player 5 at left
                                            with dissolve
                                            sis "[dex_warn]I never said you could {b}SUCK{/b} on them, you idiot!"
                                            show sis 103
                                            show player 10
                                            player_name "I'm sorry!"
                                            player_name "I thought it was okay!"
                                            show sis 102
                                            show player 5
                                            sis "I told you, just with your HAND!!!"
                                            sis "Get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            with dissolve
                                            jump hallway_dialogue

                                        "Suck on it." if pStats.dex() >= 5:
                                            show sis 99 at Position(xpos=1008) with hpunch
                                            sis "Ahhh!!"
                                            show sis 100
                                            sis "What are you DOING?!"
                                            label sis_titssuck_menu:
                                                show sis 99_100_101
                                                pause 8
                                                show sis 101
                                            menu:
                                                "Keep going.":
                                                    jump sis_titssuck_menu
                                                "Stop.":

                                                    show sis 98 at Position(xpos=1008)
                                                    sis "What the FUCK?!" with hpunch
                                                    show sis 102
                                                    show player 5 at left
                                                    with dissolve
                                                    sis "I never said you could SUCK on them! You idiot!!"
                                                    show player 10
                                                    show sis 103
                                                    player_name "I'm sorry!"
                                                    player_name "I thought you liked it!"
                                                    show sis 102
                                                    show player 5
                                                    sis "I- I didn't, Okay?! I was just pretending!!"
                                                    sis "I let you go WAY too far this time..."
                                                    sis "Get out of my room, you pervert!"
                                                    hide player
                                                    hide sis
                                                    with dissolve
                                                    jump hallway_dialogue
                                        "Stop.":

                                            show sis 91 at right
                                            show player 1 at left
                                            with fastdissolve
                                            sis "Satisfied?"
                                            show sis 89
                                            show player 21
                                            player_name "Yeah... Thanks."
                                            show player 1
                                            show sis 90
                                            sis "No... Thank YOU, {b}[firstname]{/b}!"
                                            sis "Come back any time. If you want more... You know the deal."
                                            show player 21
                                            show sis 89
                                            player_name "Okay."
                                            show player 11
                                            show sis 91
                                            sis "Now get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            with dissolve
                                            jump hallway_dialogue

                            "Not yet" if inventory.money >= 500:
                                show player 12
                                show sis 10
                                player_name "Actually, never mind."
                                player_name "I need to think it over some more."
                                show player 11
                                show sis 7 at right
                                sis "Get out of my room then, you pervert!"
                                hide player
                                hide sis
                                with dissolve
                                jump hallway_dialogue

                            "I don't have enough." if inventory.money < 500:
                                show player 10
                                show sis 10 at Position(xpos=937)
                                player_name "I don't have that much money right now..."
                                show player 11
                                show sis 9
                                sis "You're broke?! That's just sad..."
                                show player 14
                                show sis 10
                                player_name "I should have more soon, though."
                                show player 5
                                show sis 9
                                sis "Ugh... Come back to me when you have the money then."
                                sis "Get out of my room, you pervert!"
                                hide player
                                hide sis
                                with dissolve
                                jump hallway_dialogue
                    else:

                        show player 1 at left
                        show sis 7 at right
                        show sis 12 at Position(xpos=937)
                        with dissolve
                        sis "So?"
                        sis "You want to make a little {b}deal{/b}?"
                        show sis 11
                        show player 21
                        player_name "Yeah..."
                        player_name "How much money do you need again?"
                        show sis 19 at right
                        show player 11
                        sis "I'll do it for {b}$500{/b}."
                        show player 12
                        show sis 8
                        player_name "That's a lot of money, {b}[sis_name]{/b}..."
                        show player 11
                        show sis 7
                        sis "Excuse me?!"
                        sis "They're worth WAY more than that!!"
                        show sis 9 at Position(xpos=937)
                        sis "So: Deal or no deal?"
                        show player 11
                        show sis 6
                        menu:
                            "Alright." if inventory.money >= 500:
                                show player 12 at left
                                show sis 82 at Position(xpos=937)
                                player_name "Alright..."
                                show player 41 at Position(xpos=38) with fastdissolve
                                pause
                                show player 11 at left
                                show sis 80 at Position(xpos=945)
                                sis "Hold on: I'm counting it first." with fastdissolve
                                show sis 14
                                sis "Hmm..."
                                $ inventory.money -= 500
                                play audio coins2
                                show player 1
                                show sis 12 at Position(xpos=937)
                                sis "Fine. It's all here." with fastdissolve
                                show sis 10
                                show player 21
                                player_name "So... Just like last time?"
                                show player 11
                                show sis 7 at right
                                sis "Yeah, NO touching without my permission!"
                                show player 21
                                show sis 8
                                player_name "Okay..."
                                show sis 161 at Position(xpos = 943) with fastdissolve
                                pause
                                show sis 162 with fastdissolve
                                pause
                                show sis 91 at right with fastdissolve
                                show player 1
                                sis "You can touch it with ONE hand..."
                                hide player
                                show sis 92
                                with fastdissolve
                                pause
                                show sis 94 with fastdissolve
                                pause
                                show sis 93_94
                                pause 8
                                show sis 95_94
                                pause 8
                                show sis 95
                                sis "Why are you squeezing my nipple like that?"
                                show sis 94
                                sis "Can't you just touch it normally?"
                                show sis 95
                                pause
                                show sis 96
                                sis "Hahh..."
                                label sis_titsplay_menu_rep:
                                    menu:
                                        "Continue.":
                                            show sis 93_94
                                            pause 8
                                            show sis 95_94
                                            pause 8
                                            show sis 95
                                            pause
                                            show sis 96
                                            sis "Hahh..."
                                            jump sis_titsplay_menu_rep

                                        "Suck on it." if pStats.dex() < 5:
                                            show sis 97 at Position(xpos=1008) with fastdissolve
                                            pause
                                            show sis 98
                                            sis "[dex_warn]What the FUCK?!" with hpunch
                                            show sis 102
                                            show player 5 at left
                                            with dissolve
                                            sis "[dex_warn]I never said you could {b}SUCK{/b} on them, you idiot!"
                                            show sis 103
                                            show player 10
                                            player_name "I'm sorry!"
                                            player_name "I thought it was okay!"
                                            show sis 102
                                            show player 5
                                            sis "I told you, just with your HAND!!!"
                                            sis "Get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            with dissolve
                                            jump hallway_dialogue

                                        "Suck on it." if pStats.dex() >= 5:
                                            show sis 99 at Position(xpos=1008) with hpunch
                                            sis "Ahhh!!"
                                            show sis 100
                                            sis "What are you DOING?!"
                                            label sis_titssuck_menu_rep:
                                                show sis 99_100_101
                                                pause 8
                                                show sis 101
                                            menu:
                                                "Keep going.":
                                                    jump sis_titssuck_menu_rep
                                                "Stop.":

                                                    show sis 98 at Position(xpos=1008)
                                                    sis "What the FUCK?!" with hpunch
                                                    show sis 102
                                                    show player 5 at left
                                                    with fastdissolve
                                                    sis "I never said you could {b}SUCK{/b} on them, you idiot!!"
                                                    show player 10
                                                    show sis 103
                                                    player_name "I'm sorry!"
                                                    player_name "I thought you liked it!"
                                                    show sis 102
                                                    show player 5
                                                    sis "I- I didn't, Okay?! I was just pretending!!"
                                                    sis "I let you go WAY too far this time..."
                                                    sis "Get out of my room, you pervert!"
                                                    hide player
                                                    hide sis
                                                    with dissolve
                                                    jump hallway_dialogue
                                        "Stop.":

                                            show sis 91 at right
                                            show player 1 at left
                                            with fastdissolve
                                            sis "Satisfied?"
                                            show sis 89
                                            show player 21
                                            player_name "Yeah... Thanks."
                                            show player 1
                                            show sis 90
                                            sis "No... Thank YOU, {b}[firstname]{/b}!"
                                            sis "Come back any time. If you want more... You know the deal."
                                            show player 21
                                            show sis 89
                                            player_name "Okay."
                                            show player 11
                                            show sis 91
                                            sis "Now get out of my room, you pervert!"
                                            hide player
                                            hide sis
                                            with dissolve
                                            jump hallway_dialogue

                            "Not yet" if inventory.money >= 500:
                                show player 12
                                show sis 10
                                player_name "Actually, never mind."
                                player_name "I need to think it over some more."
                                show player 11
                                show sis 7 at right
                                sis "Get out of my room then, you pervert!"
                                hide player
                                hide sis
                                with dissolve
                                jump hallway_dialogue

                            "I don't have enough." if inventory.money < 500:
                                show player 10
                                show sis 10 at Position(xpos=937)
                                player_name "I don't have that much money right now..."
                                show player 11
                                show sis 9
                                sis "You're broke?! That's just sad..."
                                show player 14
                                show sis 10
                                player_name "I should have more soon, though."
                                show player 5
                                show sis 9
                                sis "Ugh... Come back to me when you have the money, then."
                                sis "Get out of my room, you pervert!"
                                hide player
                                hide sis
                                with dissolve
                                jump hallway_dialogue

                "Cam show." if sister.known(sis_final2):
                    if sister.completed(sis_final2):
                        $ gTimer.tick()
                        $ anim_toggle = False
                        $ xray = False
                        show player 2
                        show sis 11 at Position(xpos=937)
                        player_name "Do you need me... for another {b}cam show{/b}?"
                        show player 1
                        show sis 12
                        sis "Someone is feeling {b}horny{/b}."
                        sis "You want to feel your {b}big sister's{/b} pussy, huh?"
                        show player 13
                        show sis 11
                        player_name "..."
                        show player 21
                        player_name "Well, if you need my help, I guess..."
                        show player 1
                        show sis 19 at right
                        sis "Alright, wait right there, you little pervert."
                        sis "Let me get my {b}props{/b}, and then I'll explain what to do."
                        scene black with fade
                        if sis_final_cum == "Inside" and sis_final_cum_inside_first:
                            scene sisbedroom
                            show sis 166 zorder 1 at right
                            show player 1 at left
                            show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                            with fade
                            sis "Ugh... this thing is so tight!"
                            show player 21
                            show sis 167
                            player_name "I think it looks good..."
                            show player 11
                            show sis 166
                            sis "Stop with your cheap flattery."
                            show sis 167
                            player_name "..."
                            show sis 109
                            sis "So... you know how I told you that cumming inside was a bad thing?"
                            sis "It turns out, my fans LOVE {b}creampies{/b}. I got an absolute TON of new subscribers because of it."
                            show sis 108
                            show player 21
                            player_name "Wait... What?"
                            show player 1
                            show sis 166
                            sis "What I'm saying is you can keep doing it, you moron! I don't mind!"
                            show player 21
                            show sis 167
                            player_name "Ohh..."
                            show sis 166
                            show player 11
                            sis "Now, just sit on my bed, and don't say anything while I set up the cam show..."
                            sis "I don't want anyone to find out that you're my brother!"
                            show sis 109
                            sis "We have to keep up this boyfriend facade while we're on camera."
                            show sis 108
                            show player 21
                            player_name "Okay..."
                            $ sis_final_cum_inside_first = False

                        elif sis_final_cum == "Outside":
                            scene sisbedroom
                            show sis 166 zorder 1 at right
                            show player 1 at left
                            show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                            with fade
                            sis "Ugh... this thing is so tight!"
                            show player 21
                            show sis 167
                            player_name "I think it looks good..."
                            show player 11
                            show sis 166
                            sis "Stop with your cheap flattery."
                            show sis 166
                            show player 11
                            sis "Now, just sit on my bed and don't say anything while I set up the cam show..."
                            sis "I'd like to keep us being siblings a secret."
                            show sis 109
                            sis "They need to think you're my boyfriend."
                            show sis 108
                            show player 21
                            player_name "Okay..."

                        scene sis_webcam2
                        show sis 151 zorder 2 at Position(xpos=407,ypos=748)
                        show sis_cheer1 zorder 3 at Position(xpos=439,ypos=724)
                        show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
                        show xtra 20 zorder 4 at left
                        with fade
                        sis "Alright, we're live!"
                        show sis 155
                        sis "Heyyy guys!"
                        show sis 151
                        sis "Sorry to keep you waiting! I had to go fetch my boyfriend!"
                        sis "He's been veeery bad and now I have to teach him a lesson!"
                        sis "Let's get started, shall we?"
                        hide sis
                        hide sis_cheer1
                        show sissex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
                        show playersex 116b
                        with fastdissolve
                        sis "Just gotta do a few things..."
                        hide sissex
                        show sissex 104 zorder 1 at Position(xpos=122,ypos=540)
                        show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
                        with fastdissolve
                        sis "Let me remove this skirt first..."
                        show sissex 105 at Position(xpos=144,ypos=544) with fastdissolve
                        pause
                        show sissex 106 at Position(xpos=170,ypos=542) with fastdissolve
                        sis "Now, let's use these to make sure he doesn't go anywhere, while I fuck his brains out..."
                        show sissex 106b
                        show playersex 120
                        player_name "You're not really going to-"
                        show sissex 107 zorder 2 at Position(xpos=300,ypos=542)
                        show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
                        with fastdissolve
                        pause
                        show playersex 125
                        show sissex 109 at Position(xpos=357,ypos=620)
                        with fastdissolve
                        sis "What do you say guys? Should we find out what's hiding under his shorts?"
                        show sissex 108
                        player_name "..."
                        show sissex 111 at Position(xpos=375,ypos=634) with fastdissolve
                        sis "Oh, wow..."
                        show sissex 112 at Position(xpos=374,ypos=674)
                        show playersex 127
                        sis "Will you look at that nice, thick, long cock..." with vpunch
                        show sissex 113 with fastdissolve
                        sis "Let's make it nice and hard."
                        show sissex 115b with fastdissolve
                        pause
                        show sissex 114b_115b
                        pause 8
                        show sissex 114
                        sis "I wonder if it'll fit inside me..."
                        show sissex 115b
                        player_name "!!!"
                        show playersex 126
                        player_name "Wait... You're on the pill, right?"
                        show sissex 110b at Position(xpos=423,ypos=674)
                        show playersex 127b
                        sis "Shhh!!!" with hpunch
                        sis "You don't have to worry about that!!"
                        sis "Just do what you did last time and we'll be fine!"
                        show sissex 114 at Position(xpos=374,ypos=674)
                        show playersex 127
                        with fastdissolve
                        sis "Sorry about that, guys!"
                        show sissex 115
                        sis "My boyfriend is just... shy."
                        show sissex 114
                        sis "Now, let's give you what you've all been waiting for..."
                        show sissex 116 at right with dissolve
                        pause
                        show sissex 119b at Position(xpos=933,ypos=674) with fastdissolve
                        sis "Oh, YESS!!"
                        show sissex 117b at Position(xpos=910,ypos=674) with fastdissolve
                        sis "It's so... {b}deep{/b}!!"
                        $ M_sis.set('sex speed', .3)
                        show sissex 117_118_119_120_121 at Position(xpos = 910,ypos = 674)
                        pause 8
                        show sissex 117b at Position(xpos=910,ypos=674)
                        sis "His cock is SO much better than any of my toys..."
                        show sissex 118b at Position(xpos=912,ypos=674)
                        sis "It's really stretching me out..."
                        show sissex 119 at Position(xpos=933,ypos=674)
                        pause
                        show sissex 120 at Position(xpos=939,ypos=674)
                        pause
                        show sissex 121 at Position(xpos=924,ypos=674)
                        pause

                        label sis_cheerleader_fuck_looprep:
                            $ sis_cheerleader_sex2_menu = False
                            hide screen sis_cheerleader_sex_options
                            show screen xray_scr
                            pause
                            hide screen xray_scr
                            if anim_toggle:
                                $ animcounter = 0
                                while animcounter < 4:
                                    show sissex 117_118_119_120_121 zorder 2 at Position(xpos = 910, ypos = 674)
                                    pause 5
                                    if animcounter == 1:
                                        sis "Ahhhh!!!{p=1}{nw}"
                                    if animcounter == 3:
                                        sis "Oh!!!{p=1}{nw}"
                                        player_name "Uhhh...{p=1}{nw}"
                                    pause 3
                                    $ animcounter += 1
                            else:

                                $ animcounter = 0
                                while animcounter < 4:
                                    show sissex 117 at Position(xpos=910, ypos=674)
                                    pause
                                    show sissex 118 at Position(xpos=912, ypos=674)
                                    pause
                                    show sissex 119 at Position(xpos=933, ypos=674)
                                    pause
                                    show sissex 120 at Position(xpos=939, ypos=674)
                                    pause
                                    show sissex 121 at Position(xpos=924, ypos=674)
                                    pause
                                    if animcounter == 1:
                                        sis "Ahhhh!!!"
                                    if animcounter == 3:
                                        sis "Oh!!!"
                                        player_name "Uhhh..."
                                    $ animcounter += 1

                            show screen sis_cheerleader_sex_options
                            pause
                            jump sis_cheerleader_fuck_looprep

                            label sis_cheerleader_fuck_cum_outside:
                                hide screen sis_cheerleader_sex_options
                                if anim_toggle:
                                    sis "( I can feel his dick... )"
                                    sis "( ... it's throbbing like crazy... )"
                                    sis "( ... is he about to cum?! )"
                                else:
                                    show sissex 117 at Position(xpos=910,ypos=674)
                                    sis "( I can feel his dick... )"
                                    show sissex 118 at Position(xpos=912,ypos=674)
                                    sis "( ... it's throbbing like crazy... )"
                                    show sissex 119 at Position(xpos=933,ypos=674)
                                    sis "( ... is he about to cum?! )"
                                    show sissex 120 at Position(xpos=939,ypos=674)
                                pause
                                show sissex 130b
                                $ xray = False
                                with vpunch
                                sis "Ahh!!"
                                show sissex 130
                                show white zorder 5
                                show playersexc 129 zorder 4 at Position(xpos=560,ypos=377)
                                hide white with dissolve
                                pause
                                show playersexc 130 at Position(xpos=609,ypos=423) with fastdissolve
                                pause
                                show sissex 130b
                                sis "Wow..."
                                sis "Can you guys see my gaping pussy?"
                                sis "And all that hot cum running down my back..."
                                sis "I hope you guys liked it!"
                                if sister.completed(sis_final2):
                                    jump sis_cheerleader_fuck_afterrep
                                else:
                                    jump sis_cheerleader_fuck_after_initial

                            label sis_cheerleader_break_free_fail:
                                hide screen sis_cheerleader_sex_options
                                if anim_toggle:
                                    player_name "[str_warn]( Hey, these cuffs don't feel that sturdy... )"
                                    player_name "[str_warn]( Come on... )"
                                    player_name "[str_warn]( Damn it, I can't break free. )"
                                    player_name "[str_warn]( I'm not strong enough... )"
                                else:
                                    show sissex 117 at Position(xpos=910,ypos=674)
                                    player_name "[str_warn]( Hey, these cuffs don't feel that sturdy... )"
                                    show sissex 118 at Position(xpos=912,ypos=674)
                                    player_name "[str_warn]( Come on... )"
                                    show sissex 119 at Position(xpos=933,ypos=674)
                                    player_name "[str_warn]( Damn it, I can't break free. )"
                                    show sissex 120 at Position(xpos=939,ypos=674)
                                    player_name "[str_warn]( I'm not strong enough... )"
                                    show sissex 121 at Position(xpos=924,ypos=674)
                                show screen sis_cheerleader_sex_options
                                pause
                                jump sis_cheerleader_fuck_looprep

                            label sis_cheerleader_break_free_pass:
                                $ sis_cheerleader_sex2_menu = True
                                hide screen sis_cheerleader_sex_options
                                if anim_toggle:
                                    player_name "( Hey, these cuffs don't feel that sturdy... )"
                                    player_name "( Okay, here goes... )"
                                else:
                                    show sissex 117 at Position(xpos=910,ypos=674)
                                    player_name "( Hey, these cuffs don't feel that sturdy... )"
                                    show sissex 118 at Position(xpos=912,ypos=674)
                                    player_name "( Okay, here goes... )"
                                show sissex 119b at Position(xpos=933,ypos=674)
                                sis "Hey, what are you-"
                                show sissex 122 at Position(xpos=1022,ypos=768)
                                hide playersex
                                sis "!!!" with hpunch
                                show sissex 123 at Position(xpos=985,ypos=768)
                                sis "Ahh!!" with vpunch
                                show sissex 124
                                sis "What are you... DOING?!"
                                show sissex 125
                                pause
                                show sissex 126
                                pause
                                show sissex 127
                                pause
                                show sissex 123
                                sis "You're... going too... fast!"
                                show sissex 124
                                pause
                                show sissex 125
                                pause
                                show sissex 126
                                sis "This feels... AMAZING!!"
                                show sissex 127
                                pause

                                label sis_cheerleader_fuck_looprep2:
                                    hide screen sis_cheerleader_sex_options
                                    show screen xray_scr
                                    pause
                                    hide screen xray_scr
                                    if anim_toggle:
                                        $ animcounter = 0
                                        while animcounter < 4:
                                            show sissex 123_124_125_126_127 at Position(xpos = 985, ypos = 768)
                                            pause 5
                                            if animcounter == 1:
                                                sis "Ahhhh!!!{p=1}{nw}"
                                            if animcounter == 3:
                                                sis "Oh!!!{p=1}{nw}"
                                                player_name "Uhhh...{p=1}{nw}"
                                            pause 3
                                            $ animcounter += 1
                                    else:

                                        $ animcounter = 0
                                        while animcounter < 4:
                                            show sissex 123
                                            pause
                                            show sissex 124
                                            pause
                                            show sissex 125
                                            pause
                                            show sissex 126
                                            pause
                                            show sissex 127
                                            pause
                                            if animcounter == 1:
                                                sis "Ahhhh!!!{p=1}{nw}"
                                            if animcounter == 3:
                                                sis "Oh!!!{p=1}{nw}"
                                                player_name "Uhhh...{p=1}{nw}"
                                            $ animcounter += 1

                                    show screen sis_cheerleader_sex_options
                                    pause
                                    jump sis_cheerleader_fuck_looprep2


                                    label sis_cheerleader_fuck_cum_inside_unhappy:
                                        hide screen sis_cheerleader_sex_options
                                        if anim_toggle:
                                            sis "( Oh my god, I can feel him tensing up... )"
                                            sis "( ... Is he about to cum {b}inside me{/b}?! )"
                                            pause
                                            sis "( Shit, I can't get him off me!!! )"
                                        else:
                                            show sissex 123
                                            sis "( Oh my god, I can feel him tensing up... )"
                                            show sissex 124
                                            sis "( ... Is he about to cum {b}inside me{/b}?! )"
                                            show sissex 125
                                            pause
                                            show sissex 126
                                            sis "( Shit, I can't get him off me!!! )"
                                            show sissex 127
                                            pause
                                        show sissex 129
                                        sis "AAHHHH!!!!" with vpunch
                                        show white zorder 5
                                        show sissex 129c
                                        hide white with dissolve
                                        pause
                                        show sissex 128 with fastdissolve
                                        sis "Oh god..."
                                        show sissex 129b_128
                                        pause 2.9
                                        show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
                                        show sissex 131 zorder 2 at Position(xpos=985,ypos=674)
                                        with dissolve
                                        $ xray = False
                                        sis "What the... {b}FUCK{/b}?!"
                                        sis "I told you {b}NOT{/b} to cum inside me, you {b}IDIOT{/b}!!!" with hpunch
                                        jump sis_cheerleader_fuck_after

                                    label sis_cheerleader_fuck_cum_inside_happy:
                                        hide screen sis_cheerleader_sex_options
                                        if anim_toggle:
                                            sis "( Oh my god, I can feel him tensing up... )"
                                            sis "( ... Is he about to cum {b}inside me{/b}?! )"
                                            pause
                                            sis "( Shit, I can't get him off me!!! )"
                                        else:
                                            show sissex 123
                                            sis "( Oh my god, I can feel him tensing up... )"
                                            show sissex 124
                                            sis "( ... Is he about to cum {b}inside me{/b}?! )"
                                            show sissex 125
                                            pause
                                            show sissex 126
                                            sis "( Shit, I can't get him off me!!! )"
                                            show sissex 127
                                            pause
                                        show sissex 129
                                        sis "AAHHHH!!!!" with vpunch
                                        show white zorder 5
                                        show sissex 129c
                                        hide white with dissolve
                                        sis "YESS, DEEPER!!"
                                        show sissex 128 with fastdissolve
                                        pause
                                        show white zorder 5
                                        show sissex 129b
                                        hide white with fastdissolve
                                        pause
                                        show sissex 128 with fastdissolve
                                        sis "Keep cumming!"
                                        show white zorder 5
                                        show sissex 129b
                                        hide white with fastdissolve
                                        pause
                                        show sissex 128 with fastdissolve
                                        sis "I want more..."
                                        show white zorder 5
                                        show sissex 129b
                                        hide white with fastdissolve
                                        pause
                                        show sissex 128 with fastdissolve
                                        pause
                                        show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
                                        show sissex 132 zorder 2 at Position(xpos=985,ypos=674)
                                        with dissolve
                                        $ xray = False
                                        sis "Look at all that cum dripping out of my pussy..."
                                        sis "...I might get {b}knocked up{/b}, at this rate..."
                                        label sis_cheerleader_fuck_afterrep:
                                            scene sisbedroom
                                            show sis 109 at right
                                            show player 13 at left
                                            show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                                            with fade
                                            sis "Well done!"
                                            show sis 108
                                            show player 21
                                            player_name "We did okay?"
                                            show player 13
                                            show sis 109
                                            sis "Yeah, they're loving our {b}little act{/b}."
                                            sis "I... have to give you credit."
                                            sis "I didn't expect you to be able to keep up so well."
                                            sis "You're pretty good."
                                            show sis 108
                                            show player 14
                                            player_name "Really?"
                                            show sis 109
                                            show player 13
                                            sis "I'm still gonna need you for more cam shows."
                                            show player 21
                                            show sis 167
                                            player_name "Thanks, I really enjo-"
                                            show sis 164
                                            show player 11
                                            sis "STOP it!!" with hpunch
                                            show sis 165
                                            sis "..."
                                            show sis 166
                                            sis "{b}*Sigh*{/b}"
                                            show sis 109
                                            sis "Yeah, me too, I guess..."
                                            show player 13
                                            show sis 108
                                            sis "..."
                                            show sis 166
                                            show player 11
                                            sis "But, don't start getting ideas! I'm doing this because it's getting me loads of money..."
                                            sis "Oh, and do me a favor: try not to spend TOO much time with {b}[mom_name]{/b}..."
                                            sis "I know what you two are up to, I need you {b}fresh{/b} and {b}rested{/b}."
                                            sis "My subscribers now expect this kind of stream {b}regularly{/b}."
                                            show sis 164
                                            sis "So NO jerking off, and NO sex!!"
                                            show sis 165
                                            show player 12
                                            player_name "Okay! Okay! I get it..."
                                            show sis 109
                                            show player 13
                                            sis "Good."
                                            show sis 164
                                            show player 11
                                            sis "Good, now {b}GET OUT OF MY ROOM{/b}!!" with hpunch
                                            hide player
                                            hide sis
                                            hide sis_cheer2
                                            jump hallway_dialogue

                    elif handcuffs not in inventory.items or cheerleader_outfit not in inventory.items:
                        show player 1
                        show sis 12 at Position(xpos=937)
                        sis "So?"
                        sis "Do you have all the stuff I asked you for?"
                        show player 2
                        show sis 11
                        player_name "Not yet..."
                        show player 22
                        show sis 7 at right
                        sis "Then go find them and {b}GET OUT{/b}!!"
                        jump hallway_dialogue

                    elif handcuffs in inventory.items or cheerleader_outfit in inventory.items:
                        $ gTimer.tick()
                        $ inventory.items.remove(handcuffs)
                        $ inventory.items.remove(cheerleader_outfit)
                        $ sis_final2.finish()
                        $ sister.add_event(sis_shower_cuddle05)
                        show player 1 at left
                        show sis 12 at Position(xpos=937)
                        sis "So..."
                        sis "Do you have all the stuff I asked you for?"
                        show sis 82
                        show player 21
                        player_name "Yeah, yeah..."
                        show player 239_240
                        pause
                        show player 285 with fastdissolve
                        player_name "Here it is."
                        show player 1
                        show sis 158 at right
                        with fastdissolve
                        sis "Excellent."
                        show sis 12 at Position(xpos=937)
                        show player 11
                        sis "Maybe you're not as stupid as I thought after all."
                        show sis 10
                        show player 12
                        player_name "Can I go now?"
                        show sis 7 at right
                        show player 11
                        sis "Wait!!"
                        show sis 9 at Position(xpos=937)
                        sis "We're not done yet."
                        show sis 12
                        sis "Don't you want to know what my end of the deal is?"
                        show sis 10
                        show player 12
                        player_name "Right... let me guess: Another insult or something..."
                        show sis 9
                        show player 16
                        sis "{b}*Sigh*{/b}."
                        show player 11
                        sis "I was hoping to find someone else to do this with... but you'll have to do."
                        show sis 9b
                        player_name "..."
                        show sis 19 at right
                        sis "I need you to fuck me."
                        show sis 18
                        player_name "!!!" with vpunch
                        show player 10
                        player_name "What? I don-"
                        show sis 7
                        show player 11
                        sis "DON'T GET ANY IDEAS!"
                        show sis 9 at Position(xpos=937)
                        sis "I'm only doing this because I need to boost my channel!"
                        show sis 10
                        show player 10
                        player_name "I don't think I want-"
                        show sis 7 at right
                        show player 11
                        sis "You're COMPLAINING?!!" with hpunch
                        show sis 8
                        player_name "!!!"
                        show player 10
                        player_name "No! It's just that, sometimes, I feel like you're just using me for money..."
                        show sis 9 at Position(xpos=937)
                        show player 11
                        sis "Oh, please! Stop pretending."
                        sis "I know you've been enjoying this little game of ours..."
                        sis "And now, you finally get to do what you wanted to for so long..."
                        show sis 12
                        sis "You get to fuck me."
                        sis "Don't lie to me! I know you've been fantasizing about this moment for a long while now."
                        sis "So this is your chance, pervert."
                        show sis 82
                        show player 4
                        player_name "..."
                        show player 14
                        player_name "Okay! I'm in!"
                        player_name "But, what do I have to do for your cam show?"
                        show sis 12
                        show player 1
                        sis "Let me get dressed in this outfit, first."
                        sis "Then I'll explain what we're going to do..."
                        show sis 9
                        show player 11
                        sis "...and you better do EXACTLY as I say! Got it?!"
                        show sis 82
                        show player 21
                        player_name "Yes, {b}[sis_name]{/b}..."
                        scene black with fade
                        scene sisbedroom
                        show sis 166 zorder 1 at right
                        show player 11 at left
                        show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                        with fade
                        sis "You really couldn't find me a more fitting outfit?!"
                        show sis 167
                        show player 10
                        player_name "Well, it's yours from high school... I figured it would still fit you."
                        show sis 164
                        show player 11
                        sis "Yeah, it fit five years ago, you moron!"
                        sis "Can't you see that my tits got BIGGER?!"
                        show sis 167
                        show player 10
                        player_name "I'm sorry..."
                        show sis 166
                        show player 11
                        sis "Oh, forget it! Just sit on my bed and don't say anything while I set up for the cam show..."
                        sis "I don't want anyone to find out that you're my brother!"
                        show sis 109
                        sis "As far as they know, you're just my stupid boyfriend."
                        show sis 108
                        show player 21
                        player_name "Okay..."
                        scene sis_webcam2
                        show sis 151 zorder 2 at Position(xpos=407,ypos=748)
                        show sis_cheer1 zorder 3 at Position(xpos=439,ypos=724)
                        show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
                        show xtra 20 zorder 4 at left
                        with fade
                        sis "Alright, we're live!"
                        show sis 155
                        sis "Heyyy guys!"
                        show sis 151
                        sis "Sorry about the wait! I know you've all been waiting patiently to see me..."
                        sis "... but I have something special on the menu for you today!"
                        sis "I'm a diiirty little high school slut, wearing only my cheerleader outfit, with no panties..."
                        sis "I also have my horny boyfriend, waiting to fuck me with his huuuge cock..."

                        sis "Let's get started, shall we?"
                        hide sis
                        hide sis_cheer1
                        show sissex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
                        show playersex 116b
                        with fastdissolve
                        sis "Just gotta do a few things..."
                        hide sissex
                        show sissex 104 zorder 1 at Position(xpos=122,ypos=540)
                        show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
                        with fastdissolve
                        sis "Let me remove this skirt, first..."
                        show sissex 105 at Position(xpos=144,ypos=544) with fastdissolve
                        pause
                        show sissex 106 at Position(xpos=170,ypos=542) with fastdissolve
                        sis "Now, let's use these to make sure he doesn't go anywhere, while I fuck his brains out..."
                        show sissex 106b
                        show playersex 120
                        player_name "You're not really going to-"
                        show sissex 107 zorder 2 at Position(xpos=300,ypos=542)
                        show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
                        with fastdissolve
                        pause
                        show playersex 125
                        show sissex 109 at Position(xpos=357,ypos=620)
                        with fastdissolve
                        sis "What do you say, guys? Should we find out what's hiding under his shorts?"
                        show sissex 108
                        player_name "..."
                        show sissex 111 at Position(xpos=375,ypos=634) with fastdissolve
                        sis "Oh, wow..."
                        show sissex 112 at Position(xpos=374,ypos=674)
                        show playersex 127
                        sis "Will you look at that nice, thick, long cock..." with vpunch
                        show sissex 113 with fastdissolve
                        sis "Let's make it nice and hard."
                        show sissex 115b with fastdissolve
                        pause
                        show sissex 114b_115b
                        pause 8
                        show sissex 114
                        sis "I wonder if it'll fit inside me..."
                        show sissex 115b
                        player_name "!!!"
                        show playersex 126
                        player_name "We're having sex right now?"
                        player_name "Shouldn't we, you know, use a cond-"
                        show sissex 110b at Position(xpos=423,ypos=674)
                        show playersex 127b
                        sis "Shhh!!!" with hpunch
                        sis "My fans want to see raw sex, okay??!"
                        sis "So I'll just make sure you cum outside, got it!?"
                        show sissex 114 at Position(xpos=374,ypos=674)
                        show playersex 127
                        with fastdissolve
                        sis "Sorry about that, guys!"
                        show sissex 115
                        sis "My boyfriend is just... shy."
                        show sissex 114
                        sis "Now, let's give you what you've all been waiting for..."
                        show sissex 116 at right with dissolve
                        pause
                        show sissex 119b at Position(xpos=933,ypos=674) with fastdissolve
                        sis "Oh, YESS!!"
                        show sissex 117b at Position(xpos=910,ypos=674) with fastdissolve
                        sis "It's so... {b}deep{/b}!!"
                        $ M_sis.set('sex speed', .3)
                        show sissex 117_118_119_120_121 at Position(xpos = 910,ypos = 674)
                        pause 8
                        show sissex 117b at Position(xpos=910,ypos=674)
                        sis "I love riding my boyfriend's cock!"
                        show sissex 118b at Position(xpos=912,ypos=674)
                        sis "It barely fits in my tight pussy...."
                        show sissex 119 at Position(xpos=933,ypos=674)
                        pause
                        show sissex 120 at Position(xpos=939,ypos=674)
                        pause
                        show sissex 121 at Position(xpos=924,ypos=674)
                        pause
                        $ anim_toggle = False
                        $ xray = False
                        jump sis_cheerleader_fuck_looprep

                        label sis_cheerleader_fuck_after_initial:
                        scene sisbedroom
                        show sis 109 at right
                        show player 13 at left
                        show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                        with fade
                        sis "Well done!"
                        show sis 108
                        show player 21
                        player_name "We did okay?"
                        show player 13
                        show sis 109
                        sis "I think so: my subscribers seem to love the new content."
                        sis "I have to say though..."
                        sis "I didn't expect my {b}little brother{/b} to be able to perform like that."
                        sis "You did pretty well, I guess."
                        show sis 108
                        show player 14
                        player_name "Really?"
                        show sis 109
                        show player 13
                        sis "Maybe I can use you again for more cam shows..."
                        show player 21
                        show sis 167
                        player_name "Thanks, I enjoyed-"
                        show sis 164
                        show player 11
                        sis "No, STOP that!!" with hpunch
                        show sis 166
                        sis "This was {b}strictly business{/b}, nothing else!"
                        sis "Don't start getting ideas. I'm doing this to earn good money..."
                        sis "Oh, and do me a favor, try not to spend TOO much time with {b}[mom_name]{/b}..."
                        sis "I know what you two are up to, but I need you {b}fresh{/b} and {b}rested{/b}."
                        sis "My subscribers are expecting more cam shows this week."
                        show sis 164
                        sis "So NO jerking off, and NO sex!!"
                        show sis 165
                        show player 12
                        player_name "Okay! Okay! I got it..."
                        show sis 109
                        show player 13
                        sis "Good!"
                        show sis 164
                        show player 11
                        sis "Now, {b}GET OUT OF MY ROOM{/b}!!" with hpunch
                        $ sis_final_cum = "Outside"
                        hide player
                        hide sis
                        hide sis_cheer2
                        jump hallway_dialogue

                        label sis_cheerleader_fuck_after:
                            scene sisbedroom
                            show sis 164 at right
                            show player 5 at left
                            show sis_cheer2 zorder 2 at Position(xpos=797,ypos=757)
                            with fade
                            sis "What the fuck was that?!"
                            show sis 165
                            show player 10
                            player_name "I didn't mean to!!"
                            show sis 164
                            show player 5
                            sis "I told you {b}NOT{/b} to cum inside, didn't I?!" with hpunch
                            show player 10
                            show sis 165
                            player_name "I'm sorry, {b}[sis_name]{/b}... I just couldn't stop myself! It felt {b}SO GOOD{/b}!"
                            show sis 166
                            show player 11
                            sis "Do you have any idea how much {b}trouble{/b} we can get into if I get {b}pregnant{/b}?!"
                            show sis 167
                            show player 5
                            player_name "..."
                            show player 10
                            player_name "I told you we should've used condoms..."
                            show sis 164
                            show player 11
                            sis "We CAN'T!! My subscribers want the REAL thing, okay?!"
                            show sis 166
                            sis "Just stick to my directions next time, you idiot!"
                            sis "*Sigh*"
                            show sis 109
                            show player 13
                            sis "That \"accident\" aside: you weren't too bad."
                            show sis 108
                            show player 21
                            player_name "We did okay?"
                            show player 13
                            show sis 109
                            sis "I think so, my subscribers seem to love the new content."
                            sis "I have to say though..."
                            sis "I didn't expect my {b}little brother{/b} to be able to perform like that."
                            sis "Yeah, you did pretty well, I guess."
                            show sis 108
                            show player 14
                            player_name "Really?"
                            show sis 109
                            show player 13
                            sis "Maybe I can use you again for more cam shows..."
                            show player 21
                            show sis 167
                            player_name "Thanks, I enjoyed-"
                            show sis 164
                            show player 11
                            sis "No! STOP that!" with hpunch
                            show sis 166
                            sis "This was {b}strictly business{/b}, nothing else!"
                            sis "Don't start getting ideas. I'm doing this to earn good money..."
                            sis "Oh, and do me a favor, and try not to spend TOO much time with {b}[mom_name]{/b}..."
                            sis "I know what you two are up to, I need you {b}fresh{/b} and {b}rested{/b}."
                            sis "My subscribers are expecting more cam shows this week."
                            show sis 164
                            sis "So NO jerking off, and NO sex!!"
                            show sis 165
                            show player 12
                            player_name "Okay! Okay! I got it..."
                            show sis 109
                            show player 13
                            sis "Good."
                            show sis 164
                            show player 11
                            sis "Now, {b}GET OUT OF MY ROOM{/b}!!" with hpunch
                            $ sis_final_cum = "Inside"
                            hide player
                            hide sis
                            hide sis_cheer2
                            jump hallway_dialogue

                "Need toys?" if sister.over(sis_shower_cuddle05) and not sister.completed(sis_webcam04):
                    if not sister.known(sis_webcam04):
                        show player 2
                        player_name "I was just wondering if you needed more of those toys..."
                        show player 1
                        show sis 9 at Position(xpos=937)
                        sis "Huh?"
                        show sis 12
                        sis "So... do you need more panties?"
                        show player 2
                        show sis 11
                        player_name "No, not really..."
                        show player 1
                        show sis 9
                        sis "Wait... Are you offering to buy me sex toys?!"
                        show player 2
                        show sis 9b
                        player_name "Well, they help you get more subscribers on your cam shows..."
                        show player 1
                        show sis 10
                        sis "..."
                        show sis 9
                        sis "Have you been watching me on your computer this whole time?"
                        show player 22
                        show sis 9b
                        player_name "!!!"
                        show sis 12
                        sis "Haha! You're such a pervert!"
                        show player 1
                        sis "Hmm... I guess there's one last toy I need to get..."
                        show player 14
                        show sis 11
                        player_name "Oh, yeah?"
                        show player 13
                        show sis 19 at right
                        sis "You can get me a {b}Bad Monster{/b}, if you'd like."
                        sis "I've always wanted one of my own."
                        show player 4
                        show sis 18
                        player_name "What is it?"
                        show player 1
                        show sis 19
                        sis "It's a {b}huge{/b}, {b}green{/b}, monster cock dildo..."
                        show player 23
                        show sis 18
                        player_name "!!!"
                        show sis 19
                        sis "Come back if you need anything, you little pervert."
                        $ sister.add_event(sis_webcam04)

                    elif badmonster not in inventory.items:
                        show player 2
                        player_name "What's the name of that toy you wanted?"
                        show player 1
                        show sis 9 at Position(xpos=937)
                        sis "The {b}Bad Monster{/b}..."
                        show sis 12
                        sis "...It's a {b}huge{/b}, {b}green{/b}, monster cock..."
                        show sis 11
                        show player 2
                        player_name "Right. Thanks. I'll try and find it."
                        show player 1
                        show sis 12
                        sis "Come back if you need anything, you little pervert."

                    elif badmonster in inventory.items:
                        show player 14
                        player_name "I found that toy you wanted!"
                        show player 13
                        show sis 19
                        sis "Excellent!"
                        show player 239_240
                        pause
                        show player 286
                        show sis 18
                        player_name "Here. I hope you like it."
                        show player 13
                        show sis 65
                        sis "Oh I'm sure I'll enjoy every inch of it..."
                        show player 21
                        show sis 11 at Position(xpos=937)
                        player_name "Are you... planning on using it during your cam shows?"
                        show player 13
                        show sis 19 at right
                        sis "I'm sure you're going to watch me anyway, so wait and find out!"
                        show player 11
                        show sis 11 at Position(xpos=937)
                        player_name "..."
                        show sis 12
                        sis "I'm sure you're looking forward to it, you pervert."
                        $ inventory.items.remove(badmonster)
                        $ sis_webcam04.finish()

                "Watch TV tonight." if sister.over(sis_final2) and not sis_watch_tv_tonight:
                    show sis 10 at Position(xpos = 937)
                    show player 14
                    player_name "Do you want to... Watch TV tonight?"
                    show sis 9
                    show player 1
                    sis "Watch... TV?"
                    show sis 12
                    show player 11
                    sis "Hah!"
                    sis "You mean, you want your older sister to play with you on the couch?"
                    show sis 82
                    show player 21
                    player_name "Yeah. Maybe do something like last time?"
                    show player 1
                    sis "Hmm..."
                    show sis 12
                    sis "I might come down, if I feel like it."
                    show sis 82
                    show player 17
                    player_name "Sweet!"
                    show sis 10
                    show player 21
                    player_name "I'll see you downstairs later, then."
                    show sis 9
                    show player 11
                    sis "Don't get too excited, pervert."
                    show sis 9b
                    player_name "..."
                    show sis 19 at right
                    show player 1
                    sis "Anything else you want?"
                    show sis 18
                    $ sis_watch_tv_tonight = True
                    jump sis_bedroom_menu

                "Watch the neighbors." if sister.over(sis_final2):
                    $ gTimer.tick()
                    show player 14 at left
                    show sis 10 at Position(xpos=937)
                    player_name "Hey, do you want to hang out in my room?"
                    show player 1
                    show sis 9
                    sis "And do what?"
                    show player 21
                    show sis 9b
                    player_name "I was thinking maybe we could watch the neighbors through my telescope..."
                    show player 11
                    show sis 9
                    sis "Why would I do that?"
                    show player 21
                    player_name "I don't know... Maybe we can see some interesting stuff?"
                    show sis 11
                    player_name "You know... like last time."
                    show player 11
                    show sis 12
                    sis "You mean you want to spy on people doing dirty things."
                    show player 5
                    show sis 9
                    sis "Don't play dumb! I know how your dirty little mind works!"
                    sis "And what if we get caught?"
                    show player 12
                    show sis 10
                    player_name "We hide?"
                    show player 11
                    show sis 9
                    sis "Haha! Yeah, right."
                    sis "I bet you'd like that."
                    sis "Knowning that they're also watching you..."
                    show player 21
                    show sis 82
                    player_name "Heh, maybe?"
                    show player 1
                    sis "Hmm..."
                    show player 11
                    show sis 12
                    sis "Alright, let's go."
                    show player 14
                    show sis 82
                    player_name "Wait, really?!"
                    show player 13
                    show sis 12
                    sis "Sure! I'm bored."
                    sis "Let's go quick, while {b}[mom_name]{/b} is downstairs..."

                    scene home_hallway_cutscene with fade
                    show text "We quickly snuck out into the hallway and into my room.\n[sis_name] looked really eager about it, pulling me by my shirt.\nI had never done fun things with her before; she always seemed to hate being around me.\nEver since that cam show, we've been getting closer." at Position (xpos= 512, ypos = 700) with dissolve
                    pause
                    scene telescope_window
                    show player 357 at Position(xpos=456,ypos=758)
                    show sis 137 at right
                    with dissolve
                    pause
                    show sis 138
                    sis "Well?!"
                    sis "Anything good?"
                    show sis 137
                    player_name "Hmm... Hold on, I see... {b}Mrs. Johnson{/b} on her bed..."
                    show windowmomday 4a with dissolve
                    player_name "What's {b}Erik{/b} doing in her room?"
                    sis "What are they doing?!"
                    player_name "He's on his knees in front of her..."
                    player_name "She's just talking to him."
                    show windowmomday 4b with fastdissolve
                    player_name "..."
                    player_name "She's taking off her panties in front of him!"
                    sis "What?!"
                    show windowmomday 4c
                    player_name "Woah!" with hpunch
                    sis "What is it?!"
                    player_name "I... I think he's licking her down there..."
                    scene telescope_window
                    show player 357 at Position(xpos=456,ypos=758)
                    show sis 138 at right
                    with dissolve
                    sis "What?!"
                    sis "Are you serious?"
                    show sis 137
                    player_name "Yeah... Like, between her legs!"
                    sis "..."
                    show sis 138
                    sis "Move over."
                    show player 361 at left
                    show sis 142 at Position(xpos=806,ypos=768)
                    with fastdissolve
                    sis "Let me see."
                    show sis 140
                    pause
                    sis "Wow, I can't believe she's making him eat her pussy like that."
                    sis "It's... really hot!"
                    show sis 145_146_147_148 at Position(xpos=285,ypos=229,xanchor=0,yanchor=0) with fastdissolve
                    show player 362
                    sis "She must be using him."
                    sis "Commanding him what to do..."
                    show sis 144 at Position(xpos=285,ypos=231,xanchor=0,yanchor=0)
                    show player 361
                    sis "I want that, too."
                    show sis 143
                    show player 360
                    player_name "Huh?"
                    show sis 144
                    show player 361
                    sis "I want to feel what she's feeling. Now."
                    sis "And you're going to do as I tell you."
                    show sis 143
                    player_name "..."
                    show sis 144
                    sis "Let's use your bed."
                    scene bedroom_sex2
                    show sissex 135 at right
                    show sissex_cunnilingus_player at right
                    with fade
                    sis "You're going to do exactly as I say."
                    sis "I don't want your dirty hands on me..."
                    sis "... so you'll only use your mouth."
                    show sissex 134
                    player_name "Uh... Okay... But how?"
                    show sissex 135
                    sis "Are you stupid?"
                    sis "Just use your tongue and put your lips around it..."
                    sis "... and remember to focus on my clit."
                    show sissex 134
                    player_name "Okay..."
                    show sissex 137b with fastdissolve
                    sis "And don't stop until I tell you to..."
                    show sissex 139_140_141_142
                    hide sissex_cunnilingus_player
                    with fastdissolve
                    pause
                    sis "There you go."
                    sis "Just like that..."
                    pause
                    sis "Squeeze my tits."
                    player_name "Hmh?"
                    sis "Just do it!!"
                    show sissex 139b_140b_141b_142b with fastdissolve
                    pause
                    sis "Ahh..."
                    pause
                    sis "Don't stop!"
                    show sissex 139b
                    $ anim_toggle = False
                    $ xray = False
                    menu sis_cunnilingus_loop:
                        "Keep going.":
                            show screen sex_xray_anim_buttons
                            pause
                            if anim_toggle == True:
                                hide screen sex_xray_anim_buttons
                                show sissex 139b_140b_141b_142b at right
                                pause 8
                                show sissex 139b at right
                            else:

                                hide screen sex_xray_anim_buttons
                                $ animcounter = 0
                                while animcounter < 2:
                                    show sissex 139b
                                    pause
                                    show sissex 140b
                                    pause
                                    show sissex 141b
                                    pause
                                    show sissex 142b
                                    pause
                                    $ animcounter += 1
                                show sissex 139b
                                pause
                                show sissex 140b
                                pause
                                show sissex 141b
                                pause
                                show sissex 142b
                            jump sis_cunnilingus_loop
                        "Make her cum.":

                            sis "I'm... CLOSE!!"
                            sis "OH MY-"
                            show sissex 143
                            sis "AAHH!!!!!" with hpunch
                            show sissex 135b
                            show sissex_cunnilingus_player at right
                            with dissolve
                            sis "Well done, little bother!"
                            sis "I guess we found a good use for you, after all."
                            show sissex 134b
                            player_name "You liked it?"
                            show sissex 135b
                            sis "Don't get too confident; there's room for improvement."
                            show sissex 134b
                            player_name "You mean we can do this again?"
                            show sissex 135b
                            sis "We'll see about that, you pervert..."
                            sis "I gotta clean myself up. See you later."
                            scene bedroom
                            show player 18
                            with fade
                            player_name "( Man, that was crazy! )"
                            show player 13
                            player_name "( I can't believe Sis was so into this... )"
                            show player 11
                            player_name "( ...though my tongue is really sore... )"
                            jump bedroom_dialogue

    hide player
    hide sis
    $ callScreen(location_count)

label diary_dialogue:
    scene sisbedroom
    label diary01:
        show sis_diary 01 at truecenter with dissolve
        player_name "( This must be... Her {b}diary{/b}... )"
        player_name "( Interesting... )"
        player_name "( Maybe I can read some of it. )"
        window hide
        call screen diary_next

    label diary02:
        show sis_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
        show sis_diary 02 at truecenter with Dissolve(0.2)
        player_name "( She should really think about moving out... )"
        player_name "(She's been staying home and doing nothing for so long... )"
        window hide
        call screen diary_next

    label diary03:
        show sis_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
        show sis_diary 03 at truecenter with Dissolve(0.2)
        player_name "Woa..."
        player_name "( I never knew my Sister was THAT {b}horny{/b}... )"
        window hide
        call screen diary_next

    label diary04:
        show sis_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
        show sis_diary 04 at truecenter with Dissolve(0.2)
        player_name "!!!"
        window hide
        call screen diary_next

    hide sis_diary
    show player 108f
    with dissolve
    player_name "( ...I can't believe she wrote all this stuff... )"
    show player 21
    player_name "( Would she really... Help me lose my virginity?? )"
    show player 108f
    player_name "( Or... She was just joking? )"
    show player 12
    player_name "( ...And what is this {b}Live Crush{/b} cam show about?? )"
    show player 109f
    player_name "..."
    show player 108f
    player_name "( So many things I didn't know my {b}Sister{/b} was into... )"
    show player 113
    player_name "( I should get out of here before she gets back. )"
    hide player
    $ callScreen(location_count)

label bedtable_night:
    scene sisbedroom_night
    player_name "( I should come back later, when she's not around. )"
    $ in_sis_room = True
    jump sis_bedroom_dialogue

label desk02_locked_dialogue:
    scene expression gTimer.image("sisbedroom{}")
    show player 35 at left
    player_name "( I don't have the {b}password{/b} for her computer... )"
    $ callScreen(location_count)

label bedside01_dialogue:
    scene bedside01
    player_name "WHAT THE-"
    player_name "..."
    player_name "( Are those... {b}sex toys{/b}?! )"
    player_name "..."
    player_name "( ...and her {b}panties{/b}! )"
    player_name "( Maybe if... I could just take one pair... )"
    player_name "( ...she won't notice. )"
    $ look_for_panties = True
    $ sis_bedroom_count = 1
    $ lock_ui()
    $ callScreen("Bedside01")

label bedside01_dialogue2:
    scene bedside01
    player_name "( Man... )"
    player_name "..."
    player_name "( This thing is always filled with nasty stuff! )"
    player_name "( I better ask her first if I can take those panties... )"
    $ callScreen(location_count)

label siscomp_day:
    scene sisbedroom
    show player 98 at left with dissolve
    player_name "( Hmm... Let's see if she left her computer on. )"
    player_name "( I wonder what I could find on here... )"
    if shower.occupied("sis"):
        show sis 8b at right with dissolve
        sis "..."
        show sis 7b at right with hpunch
        sis "Can I help you with {b}SOMETHING{/b}??!"
        show sis 8b at right
        show player 23 at left
        player_name "!!!"
        show player 29 at left
        show sis 10b at right
        player_name "Sorry!! I was just... trying to see if your internet is working!!"
        player_name "I can't seem to connect on my computer..."
        show player 3 at left
        show sis 9c at right
        sis "Don't fucking {b}touch{/b} my computer!!"
        show player 24 at left
        sis "Just ask me next time."
        show player 10 at left
        show sis 6b at right
        player_name "Of course!"
        show player 22 at left
        show sis 7b at right
        sis "Now, get out of {b}MY ROOM{/b}!!!"
        hide player 22 at left with dissolve
        hide sis 7b at right with dissolve
    else:

        show sis 8 at right with dissolve
        sis "..."
        show sis 7 at right with hpunch
        sis "Can I help you with {b}SOMETHING{/b}??!"
        show sis 8 at right
        show player 23 at left
        player_name "!!!"
        show player 29 at left
        show sis 10 at right
        player_name "Sorry!! I was just... trying to see if your internet is working!!"
        player_name "I can't seem to connect on my computer..."
        show player 3 at left
        show sis 9 at right
        sis "Don't fucking {b}touch{/b} my computer!!"
        show player 24 at left
        sis "Just ask me next time."
        show player 10 at left
        show sis 6 at right
        player_name "Of course!"
        show player 22 at left
        show sis 7 at right
        sis "Now, get out of {b}MY ROOM{/b}!!!"
        hide player 22 at left with dissolve
        hide sis 7 at right with dissolve
    $ location_count = "Hallway"
    $ shower.unoccupy()
    $ callScreen(location_count)

label condom:
    scene expression gTimer.image("sisbedroom{}")
    show expression "objects/closeup_condom.png" with dissolve
    player_name "A {b}condom{/b}?!"
    player_name "{b}Sis{/b} must be hiding them in her room..."
    player_name "She probably won't notice if I only take one..."
    hide expression "objects/closeup_condom.png" with dissolve
    show expression "boxes/popup_condom.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_condom.png" with dissolve
    $ callScreen(location_count)

label sis_cheerleader_faster_sex:
    $ M_sis.set('sex speed', M_sis.get('sex speed') - 0.1)
    if sis_cheerleader_sex2_menu:
        jump sis_cheerleader_fuck_looprep2
    else:
        jump sis_cheerleader_fuck_looprep

label sis_cheerleader_slower_sex:
    $ M_sis.set('sex speed', M_sis.get('sex speed') + 0.1)
    if sis_cheerleader_sex2_menu:
        jump sis_cheerleader_fuck_looprep2
    else:
        jump sis_cheerleader_fuck_looprep