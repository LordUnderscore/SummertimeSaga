label lair_dialogue:
    $ location_count = "Lair"
    if getPlayingMusic("<loop 89.4>audio/music_specuw.ogg"):
        $ playMusic("<loop 89.4>audio/music_specuw.ogg", 1.0)
    if getPlayingSound("<loop 8>audio/ambience_cave.ogg"):
        $ playSound("<loop 8>audio/ambience_cave.ogg", 1.0)
    if M_aqua.get_state() == S_aqua_lair:
        scene location_lair_blur
        show player 25
        player_name "*cough* Oh man... I thought I was done for."
        show player 113
        pause
        show player 10
        player_name "Whoa, this place is spooky!"
        player_name "It's like something out of a comic book."
        show player 113
        player_name "... or one of Erik's computer games."
        show player 10
        player_name "..."
        show player 12
        player_name "... But that weird fish lady has to be here somewhere!"
        player_name "If she thinks she's keeping my lure, well, she's got another thing coming!"
        show player 16
        hide player with dissolve
        show popup_lair at truecenter with dissolve
        $ loc_lair_unlocked = True
        pause
        hide popup_lair with dissolve
        $ M_aqua.trigger(T_aqua_lair_found)
    $ callScreen(location_count)

label aqua_dialogue:
    scene location_lair_mount
    if gTimer.is_night():
        $ location_count = "Town Map"
        show player 10 with dissolve
        player_name "It's getting late..."
        player_name "I should find my way out of this underwater cavern before it gets too dark."
        hide player with dissolve
        $ callScreen(location_count)

    elif M_aqua.get_state() == S_aqua_found:
        show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
        pause
        show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
        show aqua 1
        aqua "(!!!)" with hpunch
        aqua "You!!"
        show player 15
        show aqua 2
        player_name "That's right! Me!"
        player_name "You said I had to come get it. Well here I am!"
        player_name "Now give me back the shiny!"
        show player 16
        show aqua 1
        aqua "Hahahaha! You funny human!"
        aqua "You come long way. You mussst be good ssswimmer, like Aqua!"
        show player 24
        show aqua 2
        player_name "*cough* I guess..."
        show player 30
        player_name "What is this place anyways?"
        show player 16
        show aqua 1
        aqua "Thisss Aqua's nessst!"
        show player 12
        show aqua 2
        player_name "You live here?"
        show player 11
        show aqua 1
        aqua "Yesss."
        show player 10
        show aqua 2
        player_name "By yourself?"
        show player 11
        show aqua 4
        aqua "Yesss."
        show player 10
        show aqua 3
        player_name "Are there more of you?"
        show player 11
        show aqua 4
        aqua "More... of me?"
        show player 10
        show aqua 3
        player_name "You know, other nests with other... Umm, Aquas?"
        show player 11
        show aqua 4
        aqua "Oooh, no."
        show aqua 5
        aqua "No othersss. Just Aqua. Lassst of kind."
        show player 10
        show aqua 3
        player_name "Aww, well that's kinda sad. Sounds lonely."
        show player 5
        show aqua 1
        aqua "Not lonely. Have fishies!"
        show aqua 2b
        aqua "Fishies you steals!"
        show player 15
        show aqua 1b
        player_name "I told you that wasn't me! It's Captain Terry."
        show player 16
        show aqua 4
        aqua "Caplan Terry? Hmm..."
        show aqua 5
        pause
        show aqua 4
        aqua "Maybe you tell truth..."
        show player 12
        show aqua 3
        player_name "I'm telling the truth, Aqua. I promise."
        show player 16
        show aqua 2b
        aqua "Well what Aqua do then? Fishies keep getting steals!"
        show aqua 4
        aqua "If fishies all gone, who Aqua talk to?"
        show player 11
        show aqua 5
        aqua "Aqua go crazy before find mate."
        show player 10
        show aqua 3
        player_name "Mate?"
        show player 11
        show aqua 4
        aqua "Yesss, Aqua waiting for Mate. Make baby Aquasss."
        show player 10
        show aqua 5
        player_name "Really? How long have you been waiting?"
        show aqua 4
        show player 11
        aqua "Aqua dunno. Looooong time. Nobody come. Nobody find Aqua."
        show player 10
        show aqua 5
        player_name "Hmm... Well I found you."
        show player 13
        show aqua 1
        aqua "Yesss! You find Aqua!"
        show aqua 2
        aqua "..."
        show aqua 9
        aqua "If you talk true and promissse not steals fishies. Me give you back Shiny."
        show player 14
        show aqua 8
        player_name "Yes! Thank you Aqua."
        show player 13
        show aqua 9
        aqua "You promissse?"
        show player 14
        show aqua 8
        player_name "I promise, I won't steal 'fishies.'"
        show player 13
        show aqua 9
        aqua "Ookaay."
        show aqua 10
        pause
        show aqua 2
        show player 471
        show popup_lure zorder 3 at truecenter with dissolve
        $ inventory.items.append(special_lure)
        pause
        hide popup_lure with dissolve
        player_name "Phew... Thank you Aqua!"
        show player 470
        show aqua 1
        aqua "Just remember not to steal Aqua's fishies..."
        hide player
        hide aqua
        with dissolve
        $ M_aqua.trigger(T_aqua_friended)
        $ callScreen(location_count)

    elif M_aqua.get_state() == S_aqua_mate:
        jump aqua_sex
    else:

        show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
        show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
        player_name "Hi, Aqua!"
        show player 1
        show aqua 1
        aqua "Yess..."
        show player 2
        show aqua 2
        player_name "I wanted to speak with you."
        show player 1
        show aqua 4
        aqua "What doesss human boy want?"

    menu aqua_dialogue_repeat:
        "The others.":
            show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "Aqua, what happened to the rest of your kind?"
            show player 11
            show aqua 4
            aqua "Hmm, Aqua not sssure. They just gone one day. Aqua lassst one."
            show aqua 5
            show player 10
            player_name "Aww, I'm sorry Aqua."
            show player 11
            show aqua 1
            aqua "You asssk more quessstions?"
            show aqua 2
            jump aqua_dialogue_repeat
        "How are you?":

            show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "Aqua, how are you?"
            show player 1
            show aqua 4
            aqua "How am I?"
            show player 2
            show aqua 3
            player_name "Yes, how are you feeling?"
            show player 1
            show aqua 5
            aqua "Hmm, Aqua okay. Lonely with so few fishies..."
            show aqua 4
            aqua "... but likes that human boy come visssit."
            show player 2
            show aqua 3
            player_name "I like talking with you too Aqua."
            show player 1
            show aqua 1
            aqua "Yesss, like talking."
            aqua "You asssk more quessstions?"
            show aqua 2
            jump aqua_dialogue_repeat

        "Mating." if M_aqua.get_state() == S_aqua_mating_proposal:
            show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "Aqua, what kind of mate are you looking for?"
            show player 11
            show aqua 4
            aqua "Man. Ssstrong man. Make Aqua ssstrong babies."
            show aqua 1
            aqua "you know man like this?"
            show player 34
            show aqua 3
            player_name "Hmm."

            menu:
                "Me?" if pStats.chr() < 7:
                    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
                    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
                    player_name "[chr_warn]How about me?"
                    show player 3
                    show aqua 4
                    aqua "[chr_warn]You ssstrong man?"
                    show player 29
                    show aqua 3
                    player_name "[chr_warn]Yes?"
                    show player 3
                    show aqua 5
                    aqua "..."
                    aqua "Hmm..."
                    pause
                    show aqua 4
                    aqua "[chr_warn]Aqua thinks... No. Bad idea."
                    show player 24
                    show aqua 3
                    player_name "[chr_warn]Bummer..."


                "I can help!" if pStats.chr() >= 7:
                    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
                    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
                    player_name "Maybe I could help?"
                    show player 1
                    show aqua 7
                    aqua "You?"
                    show player 2
                    show aqua 6
                    player_name "Well I mean, I did swim all the way down here to find you."
                    show player 1
                    show aqua 7
                    aqua "You did."
                    show player 2
                    show aqua 6
                    player_name "... And I fought a very mean squid along the way."
                    show player 1
                    show aqua 7 with hpunch
                    aqua "You fight Inky?!"
                    show player 2
                    show aqua 6
                    player_name "Inky? Yes. I fight Inky."
                    show aqua 7
                    aqua "Oooh, Inky ssstrong!"
                    show aqua 12
                    pause
                    show aqua 11
                    aqua "Maybe you do give Aqua ssstrong babies."
                    show player 14
                    show aqua 13
                    player_name "Really?!"
                    show player 1
                    show aqua 14
                    aqua "Yesss. But no mate yet. First you prove strength."
                    show player 10
                    show aqua 13
                    player_name "Prove my strength? How am I supposed to do that?"
                    show player 1
                    show aqua 7
                    aqua "You sssay Caplan Terry steals fishies, yesss?"
                    show player 12
                    show aqua 6
                    player_name "CAPTAIN Terry. Yes, he's the guy who's been fishing off the dock."
                    show player 11
                    show aqua 7
                    aqua "Hmm, you go make Caplan Terry ssstop."
                    show aqua 11
                    aqua "You do this and then you mate with Aqua."
                    show player 10
                    show aqua 13
                    player_name "Well I suppose I can give it a shot."
                    show player 11
                    show aqua 14
                    aqua "Good. You go then. Sssave fishies!"
                    $ M_aqua.trigger(T_aqua_mating_offer)

        "Mating." if M_aqua.get_state() == S_aqua_valor_test:
            show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "What do I need to do again, Aqua? To prove my strength?"
            show player 11
            show aqua 7
            aqua "You sssave fishies from Caplan Terry!"
            show player 10
            show aqua 6
            player_name "Oh, right. CAPTAIN Terry."
            show player 11
            show aqua 7
            aqua "That's what Aqua say! Caplan Terry!"
            show player 12
            show aqua 6
            player_name "CAPT- Nevermind. I guess I should go try and talk to him."
            show player 5
            show aqua 7
            aqua "Yesss. You go, sssave fishies!"

        "Mate." if M_aqua.get_state() in [S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end]:
            show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "I thought maybe you would like to... Get in the water again?"
            show player 26
            show aqua 3
            aqua "..."
            show aqua 1
            aqua "Oh! You want make babies?"
            show player 21
            show aqua 12
            player_name "I, err... Sure?"
            show player 26
            show aqua 11
            aqua "Hahaha! Funny Human. You Aqua's mate now."
            show aqua 14
            aqua "Aqua always ready for more ssseeds! Mate take her ssstrongly in water whenever he wants."
            jump aqua_sex
        "Nothing.":

            show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
            show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
            player_name "Nothing, I was just saying hi!"
            show player 1
            show aqua 4
            aqua "Human boy isss... Funny..."
            show aqua 1
            aqua "...I like human boy..."
            show player 21
            show aqua 2
            player_name "I err... Like you too!"
            show player 13
            aqua "..."
            show player 29
            player_name "Anwyay, I should get going."
            show player 3
            show aqua 1
            aqua "You come back, see Aqua sssoon."
            show player 17
            show aqua 2
            player_name "You bet!"
    hide player
    hide aqua
    with dissolve
    $ callScreen(location_count)

label aqua_sex:
    $ gTimer.tick()
    if M_aqua.get_state() == S_aqua_mate:
        scene location_lair_mount
        show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
        show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
        player_name "Aqua, I have some good news!"
        show player 1
        show aqua 1
        aqua "*Gasp* You learn to breathe underwater, like Aqua?!"
        show player 12
        show aqua 2
        player_name "What? ... No."
        show player 1
        show aqua 7
        aqua "Oh. Ookaay. What news then?"
        show player 2
        show aqua 6
        player_name "I convinced Captain Terry to stop fishing!"
        show player 1
        show aqua 7
        aqua "You mean fishies safe!?"
        aqua "No more Captain Terry!?"
        show player 17
        show aqua 6
        player_name "Hey, you said it right that time!"
        show player 1
        show aqua 7
        aqua "Huh?"
        show player 2
        show aqua 6
        player_name "You said 'Captain Terry' correctly that time."
        show player 1
        show aqua 7
        aqua "Yesss. Caplan Terry!"
        show player 90
        show aqua 6
        player_name "..."
        show aqua 6b
        aqua "..."

        show player 37
        player_name "... Just nevermind."
        show player 2
        player_name "Your fish should be safe now."
        show player 1
        show aqua 7
        aqua "Oh thank you! Thank you! Thank you!"
        show aqua 14
        aqua "You good human! Strong human!"
        show player 29
        show aqua 13
        player_name "You're welcome, Aqua..."
        show player 1
        show aqua 11
        aqua "..."
        show aqua 12
        aqua "Is... human ready to mate with Aqua?"
        show player 21
        show aqua 13
        player_name "R-right now?"
        show player 297
        show aqua 14
        aqua "Yesss. Aqua wait long enough. Mate take her ssstrongly in water!"
        show player 10
        show aqua 13
        player_name "In the water?"
        show player 11
        show aqua 14
        aqua "Yesss. Come!"

    scene location_lair_cutscene
    with fade
    show text "Aqua's touch was soft and gentle as she took my hand and started towards the luminescent pool." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I struggled to keep pace, fumbling with my clothes." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "But she didn't seem to notice, her excitement palpable as she lead her mate into the water." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    if M_aqua.get_state() == S_aqua_mate:
        scene location_lair_water with fade
        show aswim 1 at left
        show pswim 1 at right
        pause
        show aswim 2
        aqua "Ooh, mate has good body."
        show aswim 1
        show pswim 2
        player_name "Thanks Aqua..."
        show aswim 3
        show pswim 1
        pause
        show aswim 2
        aqua "Your eel isss sleeping."
        show aswim 1
        show pswim 2
        player_name "Huh?"
        show aswim 3
        pause
        show pswim 3
        pause
        show pswim 2
        player_name "Oh. Yeah..."
        show aswim 2
        show pswim 1
        aqua "Does mate like Aqua's body?"
        show aswim 1
        show pswim 2
        player_name "Yes... Umm, 'mate' likes Aqua's body very much."
        show aswim 2
        show pswim 1
        aqua "Good. Aqua's body belong to you now."
        aqua "Mate's eel can play inssside Aqua whenever it wants."
        show aswim 3
        pause
        show aswim 2
        aqua "It's warm inssside Aqua..."
        show aswim 3
        pause
        show aswim 2
        aqua "... and soft..."
        show aswim 3
        pause
        show aswim 2
        aqua "... and wet."
        show pswim 3
        pause
        show aswim 3
        show pswim 4
        pause
        show aswim 4
        show pswim 5
        pause
        show pswim 9
        pause
        show aswim 2
        show pswim 6
        aqua "Ooh, eel likes this, yes?!"
        show aswim 3
        show pswim 7
        player_name "Y-yes..."
        show aswim 4
        aqua "Mmm, good. Aqua wantsss it."
        show aswim 3
        show pswim 8
        player_name "..."
        show aswim 4
        aqua "Aqua wantsss it now!"
        hide pswim
        show aswim 5 with dissolve
        pause
        show aswim 6 at right with dissolve
        player_name "*Gulp*"
        aqua "Aaah, yessss. Come eel, you play inssside Aqua."
        aqua "Give Aqua ssstrong babies..."
        player_name "Oh wow!"
        aqua "Mmm..."

    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    aqua "{b}Aqua{/b} needs it inssside her!"
    aqua "Hurry my mate!"
    player_name "..."
    show aquas 2
    aqua "Hissss."
    aqua "Your eel sssooo big!"
    aqua "Take me ssstrong!"
    $ M_aqua.set('sex speed', .175)
    show aquas 3_4_5_6_7
    with fade
    aqua "Ooohh!."
    pause
    aqua "So ssstrong!"
    pause
    aqua "and deep!"
    $ M_aqua.set('sex speed', .125)
    aqua "Aaahh!"
    pause
    aqua "Mmm, my mate."
    aqua "Faster!"
    $ M_aqua.set('sex speed', .075)
    pause
    label aqua_sex_loop:
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                show aquas 3_4_5_6_7
                pause 5
                if animcounter == 1:
                    aqua "Ahhhh!!!{p=1}{nw}"
                if animcounter == 3:
                    aqua "Take me!!!{p=1}{nw}"
                    player_name "Uhhh...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                show aquas 3
                pause
                show aquas 4
                pause
                show aquas 5
                pause
                show aquas 6
                pause
                show aquas 7
                pause
                if animcounter == 1:
                    aqua "Ahhhh!!!"
                if animcounter == 3:
                    aqua "Take me!!!"
                    player_name "Uhhh..."
                $ animcounter += 1

        call screen aqua_sex_options

    label aqua_sex_cum:
        player_name "This is unbelievable!"
        player_name "{b}Aqua{/b}, I'm gonna..."
        aqua "Yesss... YESSS MY MATE!"
        aqua "Give {b}Aqua{/b} your ssseeeeeeds!"
        aqua "HISSSSS!!!"
        show aquas 8 with flash
        player_name "UHHH!!"
        aqua "AAAAHHH!!!!"
        pause
        show aquas 9
        player_name "Wow!"
        player_name "That was incredible!"
        aqua "Yesss..."
        aqua "... {b}Aqua{/b} can feel strong babies swimming inssside her!"
        pause
        scene black with fade

    if M_aqua.get_state() == S_aqua_mate:
        scene location_lair_mount
        show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
        show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
        player_name "So you enjoyed that?"
        show player 1
        show aqua 12
        aqua "Yesss. Aqua enjoy much! Ssstill feel tingle dancing in legs!"
        show player 2
        show aqua 11
        player_name "You were incredible! I've never felt anything like that before."
        show player 1
        show aqua 14
        aqua "Yesss, this Aqua's first time too."
        show aqua 12
        aqua "... But Aqua wants more."
        show aqua 14
        aqua "Mate comes back, give Aqua more ssseed. Yes?"
        show player 2
        show aqua 13
        player_name "Absolutely, I'll come back really soon!"
        show player 1
        show aqua 14
        aqua "Mate promissse?"
        show player 2
        show aqua 13
        player_name "Oh, I promise!"
        show player 1
        show aqua 12
        aqua "Good. Aqua want much more!"
        show aqua 14
        aqua "Come back sssoon, Human."
        show aqua 11
        aqua "Aqua wait here until tingle ssstop dancing..."
        $ M_aqua.trigger(T_aqua_mated)
    hide player
    hide aqua
    with dissolve
    $ callScreen(location_count)

label seasucc_dialogue:
    scene lair_seasucc
    if M_aqua.get_state() == S_aqua_seasucc_intro:
        show aqua 19
        show seasucc_bg_01
        show seasucc_bg_02
        show seasucc 1
        show player 10 at left
        with dissolve
        player_name "Hey, {b}Aqua{/b}?"
        show player 5
        show aqua 20
        aqua "Yesss..."
        show aqua 19
        show player 10
        player_name "Umm, what's this strange looking thing?"
        show player 5
        show aqua 20
        aqua "Is not thing. Is {b}SsseaSucc{/b}!"
        show aqua 19
        show player 12
        player_name "Hmm, and what does this {b}SeaSucc{/b} do?"
        show player 5
        show aqua 20
        aqua "It is usssed for giving pleasssures."
        show aqua 19
        show player 12
        player_name "It gives you pleasure?"
        show player 5
        show aqua 20
        aqua "Yesss. It gives all friends pleasssure."
        show aqua 19
        show player 10
        player_name "So {b}SeaSucc{/b} would give me pleasure, too?"
        show player 5
        show aqua 20
        aqua "Yesss, if you make friends."
        show aqua 19
        show player 10
        player_name "How do I make friends with a chair?"
        show player 5
        show aqua 20
        aqua "You must feed it ssspecial food, {b}Falicum Mussshroom{/b}. {b}Falicum{/b}."
        show aqua 19
        show player 12
        player_name "Feed it? Weird..."
        player_name "But I've never heard of a {b}Falicum Mushroom{/b} before."
        show player 10
        player_name "Where can I find some?"
        show player 5
        show aqua 20
        aqua "It grows on land. {b}Deep in foressst{/b}. Dangerous for {b}Aqua{/b}."
        show aqua 19
        show player 12
        player_name "Hmm, in the {b}forest{/b}, huh?"
        show player 14
        player_name "I could go try and find some."
        show player 13
        show aqua 20
        aqua "Yesss. You go get {b}Falicum{/b}. Make friends with {b}SeaSucc{/b}."
        aqua "Then we enjoy pleasssure."
        $ M_aqua.trigger(T_aqua_seasucc)

    elif M_aqua.get_state() == S_aqua_seasucc_mushroom and mushroom not in inventory.items:
        show aqua 19
        show seasucc_bg_01
        show seasucc_bg_02 zorder 1
        show seasucc 1 zorder 2
        show player 12 zorder 3 at left
        with dissolve
        player_name "What did you say {b}SeaSucc{/b}, needed?"
        show player 5
        show aqua 20
        aqua "You must feed it ssspecial food, {b}Falicum Mussshroom{/b}. {b}Falicum{/b}."
        show aqua 19
        show player 10
        player_name "Where can I find some?"
        show player 5
        show aqua 20
        aqua "It grows on land. {b}Deep in foressst{/b}. Dangerous for {b}Aqua{/b}."
        show aqua 19
        show player 14
        player_name "Alright! I'll take a look."

    elif M_aqua.get_state() == S_aqua_seasucc_mushroom and mushroom in inventory.items:
        show aqua 19
        show seasucc_bg_01
        show seasucc_bg_02 zorder 1
        show seasucc 1 zorder 2
        show player 14 zorder 3 at left
        with dissolve
        player_name "{b}Aqua{/b}!"
        player_name "I think I found something."
        show player 239_240 with dissolve
        player_name "..."
        show player 500 with dissolve
        player_name "See?"
        show player 499
        show aqua 20
        aqua "{b}Falicum{/b}! Yesss."
        show aqua 19
        show player 500
        player_name "Is this what {b}SeaSucc{/b} needs?"
        show player 499
        show aqua 20
        aqua "Yesss. Feed {b}SeaSucc{/b}. Make friends!"
        aqua "Siittt... And feed {b}Falicum{/b}."
        show aqua 19
        show player 10 with dissolve
        player_name "Alright..."
        hide player
        show player seasucc 1 zorder 3 with dissolve
        pause
        show aqua 21
        show player seasucc 5 zorder 0
        show player_pants seasucc 2 zorder 0
        with dissolve
        pause
        show player seasucc 6 with dissolve
        pause
        show player seasucc 9 with dissolve
        player_name "Here you go {b}SeaSucc{/b}."
        show seasucc 2 with dissolve
        show player seasucc 8
        player_name "..."
        show seasucc 3
        show player seasucc 10
        with dissolve
        player_name "!!!" with hpunch
        show seasucc 4
        show player seasucc 5
        with dissolve
        show aqua 22
        aqua "Mmm, {b}SeaSucc{/b} likes {b}Falicum{/b}."
        show aqua 21
        show seasucc 1
        show player seasucc 7
        with dissolve
        player_name "You must of been really hungry!"
        show player seasucc 3 with dissolve
        show aqua 22
        aqua "You try {b}SeaSucc{/b} now. Yesss?"
        show aqua 21
        show player seasucc 7 with dissolve
        player_name "Uhh..."
        show player seasucc 5 with dissolve
        show aqua 22
        aqua "No worry. Ssshow {b}SeaSucc{/b} big eel."
        show aqua 21
        show player seasucc 6 with dissolve
        player_name "..."
        show player seasucc 7
        player_name "Alright..."
        hide player_pants
        show player seasucc 11 with dissolve
        pause
        show player seasucc 3
        show player_boner seasucc 2b
        with dissolve
        show aqua 25
        aqua "Ahh, good morning big eel. "
        show aqua 21
        show seasucc 5
        show player seasucc 7
        with dissolve
        player_name "Are you sure this is-"
        show aqua 24
        show player seasucc 5
        show seasucc 6
        with dissolve
        pause
        show seasucc 7 with dissolve
        player_name "!!!"
        hide player_boner
        show seasucc 8
        with dissolve
        pause
        show seasucc 8b
        pause
        show seasucc 8c
        pause
        show seasucc 8d
        pause
        show seasucc 8e
        show player seasucc 12
        player_name "Whoa!"
        $ M_aqua.set('sex speed', 0.175)
        show seasucc 8_8b_8c_8d_8e_8f_8g_8h_8i
        pause
        pause
        show player seasucc 13
        player_name "This thing feels... amazing!!"
        show player seasucc 14
        show aqua 23
        aqua "Yesss. Good pleasssure! {b}SeaSucc{/b} good!"
        show aqua 24
        pause
        label seasucc_loop:
            show screen sex_anim_buttons
            pause
            if anim_toggle == True:
                $ animcounter = 0
                while animcounter < 4:
                    hide screen sex_anim_buttons
                    show seasucc 8_8b_8c_8d_8e_8f_8g_8h_8i
                    pause 4
                    if animcounter == 0:
                        show player seasucc 13
                        if randomizer() <= 50:
                            player_name "Ohh...{p=1}{nw}"
                        else:
                            player_name "Uhh!{p=1}{nw}"
                        show player seasucc 14
                    if animcounter == 2 and randomizer() <= 50:
                        show aqua 23
                        aqua "Sssuck {b}SsseaSucc{/b}!{p=2}{nw}"
                        show aqua 24
                    if animcounter == 3 and randomizer() <= 50:
                        show player seasucc 13
                        pause 2
                        show player seasucc 14
                    pause 3
                    $ animcounter += 1
            else:

                $ animcounter = 0
                while animcounter < 4:
                    hide screen sex_anim_buttons
                    show seasucc 8
                    pause
                    show seasucc 8b
                    pause
                    show seasucc 8c
                    pause
                    show seasucc 8d
                    pause
                    show seasucc 8e
                    pause
                    show seasucc 8f
                    pause
                    show seasucc 8g
                    pause
                    show seasucc 8h
                    pause
                    show seasucc 8i
                    pause
                    if animcounter == 0:
                        show player seasucc 13
                        if randomizer() <= 50:
                            player_name "Ohh..."
                        else:
                            player_name "Uhh!"
                        show player seasucc 14
                    if animcounter == 2 and randomizer() <= 50:
                        show aqua 23
                        aqua "Sssuck {b}SsseaSucc{/b}!"
                        show aqua 24
                    if animcounter == 3 and randomizer() <= 50:
                        show player seasucc 13
                        pause 2
                        show player seasucc 14
                    $ animcounter += 1
            call screen seasucc_options

        label seasucc_cum:
            show player seasucc 13
            show aqua 23
            aqua "Give {b}SsseaSucc{/b} ssseeds."
            aqua "Cum for {b}SeaSucc{/b}!!!"
            show aqua 24
            pause
            hide player
            show seasucc 9 zorder 0
            with flash
            pause
            show seasucc 3
            show player seasucc 14 zorder 0
            show player_boner seasucc 15 zorder 0
            with dissolve
            pause
            show seasucc 4 with dissolve
            pause
            show seasucc 1 with dissolve
            show player seasucc 3
            show aqua 25
            if M_aqua.get_state() == S_aqua_seasucc_mushroom:
                aqua "Now that {b}SeaSucc{/b} tassste mate's ssseed, it remembers."
                aqua "You friends now!"
                aqua "It give pleasssure always."
                show popup_seasucc at truecenter with dissolve
                pause
                hide popup_seasucc with dissolve
            else:
                aqua "{b}SeaSucc{/b} likesss mate's ssseed!"
            $ gTimer.tick()
            $ M_aqua.trigger(T_aqua_seasucc_fuck)
    else:

        show aqua 20
        show seasucc_bg_01
        show seasucc_bg_02 zorder 1
        show seasucc 1 zorder 2
        show player 13 zorder 3 at left
        with dissolve
        aqua "Back for moresss?"
        show aqua 19
        menu:
            "Yes.":
                show player 4 with dissolve
                player_name "..."
                show player 26 with dissolve
                player_name "Yeah."
                show player 13
                show aqua 20
                aqua "{b}SeaSucc{/b} isss good!"
                aqua "Siittt... And feed {b}SeaSucc{/b}."
                show aqua 19
                hide player
                show player seasucc 1 zorder 3 with dissolve
                pause
                show aqua 21
                show player seasucc 5 zorder 0
                show player_pants seasucc 2 zorder 0
                with dissolve
                pause
                show aqua 22
                aqua "Ssshow {b}SeaSucc{/b} big eel."
                show aqua 21
                hide player_pants
                show player seasucc 11 with dissolve
                pause
                show player seasucc 3
                show player_boner seasucc 2b
                with dissolve
                show aqua 25
                aqua "Ahh, good morning big eel. "
                show aqua 21
                show seasucc 5
                with dissolve
                show aqua 24
                show player seasucc 5
                show seasucc 6
                with dissolve
                pause
                show seasucc 7 with dissolve
                player_name "!!!"
                hide player_boner
                show seasucc 8
                with dissolve
                pause
                show seasucc 8b
                pause
                show seasucc 8c
                pause
                show seasucc 8d
                pause
                show seasucc 8e
                show player seasucc 12
                player_name "Whoa!"
                $ M_aqua.set('sex speed', 0.175)
                show seasucc 8_8b_8c_8d_8e_8f_8g_8h_8i
                pause
                pause
                show player seasucc 13
                player_name "This thing feels... amazing!!"
                show player seasucc 14
                show aqua 23
                aqua "Yesss. Good pleasssure! {b}SeaSucc{/b} good!"
                show aqua 24
                jump seasucc_loop
            "No.":

                show player 14
                player_name "Not right now. Maybe later."
    hide aqua
    hide player
    hide player_boner
    hide seasucc
    hide seasucc_bg_01
    hide seasucc_bg_02
    with dissolve
    $ callScreen(location_count)

label aqua_lure_steal:
    scene location_pier_dock_cutscene
    with fade
    show text "When that line snapped, my heart sank. I thought my lure was lost..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...But suddenly, something breached the surface of the water!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...Or should I say, someone..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene minigame06b
    show player 472 at Position(xpos=0.715,ypos=.9425)
    show aqua 16 at Position (xpos=0.4175,ypos=1.0)
    aqua "Shiiiny..."
    show player 473
    show aqua 15
    player_name "!!!"
    player_name "Wh-What are you?!"
    show player 472
    show aqua 18
    aqua "Me? Me Aqua. What you?"
    show player 473
    show aqua 17
    player_name "Huh?"
    show player 472
    show aqua 18
    aqua "Me Aqua. You human steals all Aqua's fishies?!"
    show player 473
    show aqua 17
    player_name "Fishies?"
    show player 472
    show aqua 16b
    aqua "Yesss, fishies! You use shiny to sssteal my fishies!"
    show player 473
    show aqua 15b
    player_name "What? No, I just got the umm... 'Shiny?'"
    player_name "Captain Terry just gave it to me."
    show player 472
    show aqua 16b
    aqua "Caplan Terry?"
    show player 473
    show aqua 15b
    player_name "Yeah, CAPTAIN Terry."
    show player 472
    show aqua 16
    aqua "Hmm... Not sssure you tell truth."
    show aqua 16b
    aqua "Don't matter, shiny mine now!"
    show player 474
    show aqua 17
    player_name "Wait! Please, I worked really hard to get that!"
    show player 475
    show aqua 16b
    aqua "Too bad. You want? {b}You come get{/b}!!!"
    hide aqua with dissolve
    show player 474
    player_name "Hey!!"

    show player 476
    player_name "Crap!"
    player_name "..."
    show popup_lure2 at truecenter with dissolve
    $ inventory.items.remove(special_lure)
    pause
    hide popup_lure2 with dissolve
    $ M_aqua.trigger(T_aqua_lure_steal)

    label follow_aqua:
        player_name "!!!"
        player_name "(Damn! I'll have to go after her if I want that lure back.)"
        player_name "(... It could be dangerous though.)"
        player_name "(I better make sure I'm ready first.)"
        menu:
            "Dive!":
                player_name "Screw it! I worked too hard for that lure."
                player_name "I can't just let her take it!"
                show player 477
                $ playSound()
                jump aqua_chase
            "Not yet.":

                show player 476b
                player_name "(I... I can't just dive in after her.)"
                player_name "(There's no telling what's down there.)"
                player_name "(Maybe later...)"
    $ callScreen(location_count)

label aqua_chase:
    scene location_lair_dive
    with fade
    show text "I went straight after her..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... diving headfirst into the dark blue water." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I was determined to get my lure back!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_lair_ocean_look
    player_name "(She has to be around here somewhere.)"
    player_name "..."
    player_name "(Grr... Where did she go?!)"

    scene location_lair_ocean_prefight
    player_name "(!!!)" with hpunch
    player_name "(What the- !!)"
    player_name "(A giant squid!?!)"
    $ M_aqua.trigger(T_aqua_dive)

    scene versus_squid with vpunch
    $ renpy.pause(1.0, hard = True)

    if cheat_mode:
        menu:
            "Skip Mini-Game (Cheat)":
                jump squid_attack
            "Play Mini-Game":

                $ pass

    $ time_count = 5
    $ timer_range = 5

    label squid_fight_pre:
        $ renpy.random.shuffle(arrow_list)
        $ renpy.random.shuffle(keyboard_list)
        $ task_list = []
        $ move_list = []

        $ move_list_number = 8

        $ a = 0
        while (a < move_list_number):
            if renpy.variant("pc"):
                $ b = renpy.random.randint(0, 1)
                if b == 0:
                    $ move_list += [renpy.random.choice(arrow_list)]
                else:

                    $ move_list += [renpy.random.choice(keyboard_list)]
            else:

                $ move_list += [renpy.random.choice(arrow_list)]
            $ a += 1
        $ renpy.random.shuffle(move_list)
        $ arrow_index = 0
    call screen squid_fight

label squid_attack:
    $ M_aqua.trigger(T_aqua_squid_defeated)
    $ location_count = "Lair Entrance"
    scene location_lair_ocean_afterfight
    $ renpy.pause(1.0, hard = True)
    scene location_lair_ocean
    player_name "( Ah hah! She must be in that cave. )"
    player_name "( I'll need to find her quickly. )"
    player_name "( ...before I run out of air! )"
    player_name "( ...before I run out of air! )"
    $ callScreen(location_count, False)

label squid_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ gTimer.tick()
    scene location_lair_fail_squid
    with fade
    show text "The fight just wasn't going my way..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "The beast was too strong and the water was stifling." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I waited for my opening and made a mad dash to the surface" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene minigame06b with fade
    show player 478 at Position (xpos=0.644,ypos=1.0) with dissolve
    player_name "*cough*"
    player_name "I couldn't do it."
    show player 479 at Position (xpos=0.663,ypos=1.0) with dissolve
    player_name "..."
    player_name "I need to make sure I'm better prepared next time."
    $ callScreen(location_count)

label maze_pre:
    if cheat_mode:
        scene location_lair_ocean with None
        menu:
            "Skip Mini-Game (Cheat)":
                $ maze_choices = ["Middle", "Middle", "Left", "Left", "Middle", "Right", "Middle"]
                jump maze_finish
            "Play Mini-Game":

                $ pass

    $ time_count = 5
    $ timer_range = 5

    $ maze_choices = []
    call screen lair_maze

label maze_finish:
    if maze_choices == ["Middle", "Middle", "Left", "Left", "Middle", "Right", "Middle"]:
        $ M_aqua.trigger(T_aqua_maze_conquered)
        jump maze_pass
    else:

        jump maze_fail

label maze_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ gTimer.tick()
    $ location_count = "Pier"
    scene location_lair_fail_maze
    with fade
    show text "I was completely lost and running out of air." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "There was no choice but to retreat back to the surface." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Hopefully I'll do better next time..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    $ callScreen(location_count)

label maze_pass:
    scene location_lair_emerge
    with fade
    show text "The cave was a labyrinth of twists and turns." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I pushed forward stubbornly until I felt my lungs about to burst..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...This can't be the end! This can't be-" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Wait, is that, light!?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    jump lair_dialogue