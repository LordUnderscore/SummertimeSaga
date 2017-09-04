default mia_mail = []
default mias_house_kicked = 0

label mias_house_dialogue:
    $ location_count = "Mia's House"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_morning() and not gTimer.is_weekend():
        scene miahouse
        show player 12 with dissolve
        player_name "( There's no one here... )"
        show player 35
        player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
        hide player 35 with dissolve

    if mias_house_kicked == 1:
        scene miahouse
        show mia 12 at right with dissolve
        show player 11 at left
        mia "{b}[firstname]{/b}!!!"
        show mia 8
        show player 10
        player_name "Hey!"
        show player 12
        player_name "...I was just kicked out of your house!"
        show mia 12
        show player 90
        mia "I know!! I heard them from upstairs..."
        mia "...I'm so sorry!"
        show player 11
        mia "I didn't think my parents would be home..."
        show mia 8
        show player 12
        player_name "They seem really strict!"
        show mia 12
        show player 90
        mia "Yeah... My mom's been really bad lately."
        show mia 8
        show player 10
        player_name "Sooo... I guess we won't be studying after all."
        show mia 10
        show player 5
        mia "Actually, there's {b}another way{/b} I was think could work..."
        show player 11
        mia "...But we have to be super careful!"
        show mia 7
        show player 10
        player_name "How?"
        show mia 9
        show player 11
        mia "At {b}night{/b}!"
        show mia 10
        mia "I'll leave the front door unlocked for you..."
        show mia 9
        mia "You can just {b}sneak upstairs{/b} into my room. Just don't make any noise!"
        show mia 7
        show player 5
        player_name "..."
        show player 10
        player_name "That sounds really... Risky..."
        show mia 9
        show player 5
        mia "Don't worry! They sit in front of the TV all night, until they fall asleep..."
        show mia 7
        show player 21
        player_name "Okay. I'll try and come by, then."
        show mia 10
        show player 13
        mia "That's great, {b}[firstname]{/b}!!!"
        show mia 9
        mia "See you soon!"
        $ mias_house_kicked = 2

    elif gTimer.is_evening():
        scene miahouse_night
        show player 2 with dissolve
        player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
        hide player 2 with dissolve
        hide miahouse_night
    $ callScreen(location_count)

label mias_entrance:
    $ location_count = "Mia's House Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if mias_house_kicked == 0:
        scene mia_house_c
        show helen 2 zorder 1 at right
        show player 1 at left
        with dissolve
        helen "And you are?"
        show helen 1
        show player 14
        player_name "I'm {b}[firstname]{/b}!"
        player_name "I'm a friend from school..."
        show helen 2
        show player 1
        helen "A friend?"
        show player 11
        helen "Our daughter doesn't bring guests home."
        helen "She also didn't mention anything about your visit..."
        helen "Have you two met at church?"
        show helen 1
        show player 10
        player_name "No?"
        show helen 2
        show player 11
        helen "Are you a church goer, {b}[firstname]{/b}?"
        show helen 1
        show player 10
        player_name "Uhh... Not really, Ma'am."
        show helen 2
        show player 11
        helen "Of course not."
        show helen 1
        show player 1
        show harold 2 zorder 0 at Position (xpos = 670, ypos = 768) with dissolve
        harold "Hey, dear!"
        harold "Is this one of {b}Mia's{/b} friends?"
        show harold 1
        show helen 3
        show player 5
        helen "It's a young man who's about to leave."
        hide helen
        hide harold
        hide player
        with dissolve
        show unlock30 at truecenter with dissolve
        $ loc_church_unlocked = True
        pause
        hide unlock30
        pause .4
        show unlock32 at truecenter with dissolve
        $ loc_police_unlocked = True
        pause
        hide unlock32
        $ mias_house_kicked = 1
        jump mias_house_dialogue
    $ callScreen(location_count)

label mia_button_dialogue_house:
    if homework_count < 1:
        scene location_mia_closeup
        show player 14 at left with dissolve
        show mia 1 at right with dissolve
        player_name "Hey {b}Mia{/b}!"
        show mia 4 at right
        show player 1 at left
        mia "Hey {b}[firstname]{/b}!"
        mia "What're you doing here?"
        show mia 1 at right
        show player 29 at left
        player_name "Umm... I wanted to ask you something!"
        menu:
            "About that homework.":
                show player 21 at left
                player_name "Do you still need help studying for the exams?"
                show mia 3 at right
                show player 13 at left
                mia "Of course! I've been looking for {b}someone to study with{/b}..."
                show mia 6 at right
                show player 11 at left
                mia "...But have you caugh up with class yet?"
                show mia 2 at right
                show player 10 at left
                player_name "Oh! Right! {b}Mrs. Bissette{/b} assigned me some homework to catch up..."
                show mia 6 at right
                show player 13 at left
                mia "You probably should finish that, first!"
                show mia 4 at right
                mia "Then you can come over to my house... and we'll study in my room!"
                show mia 1 at right
                show player 14 at left
                player_name "Ye... yeah?"
                show mia 3 at right
                show player 1 at left
                mia "Sure! It'll be fun!"
                show mia 1 at right
                show player 17 at left
                player_name "Alright... I'll let you know when I'm done with them!"
                show mia 4 at right
                show player 1 at left
                mia "See you soon!"
                hide player 1 at left with dissolve
                hide mia 4 at right with dissolve
            "I forgot...":

                show mia 1 at right
                show player 4 at left
                player_name "Hmm... Yeah, but I forgot!"
                show mia 3 at right
                show player 11 at left
                mia "Haha! You're funny~"
                show mia 1 at right
                show player 17 at left
                player_name "Sorry! I can't remember what I wanted to say!"
                show player 14 at left
                player_name "I should get going."
                show mia 4 at right
                show player 1 at left
                mia "Have a good night!"
                hide player 1 at left with dissolve
                hide mia 4 at right with dissolve
    $ callScreen(location_count)

label mia_button_dilaogue_indoors:
    scene location_mia_house_closeup
    show mia 12 at right
    show player 13 at left with dissolve
    mia "Hey..."
    show mia 8
    show player 21
    player_name "Hi, {b}Mia{/b}!"
    show mia 12
    show player 5
    mia "I can't really speak right now..."
    mia "...But you {b}know what to do{/b}, if you want to meet up..."
    show player 10
    show mia 8
    player_name "Okay... See you later then..."
    hide player
    hide mia
    with dissolve
    jump mias_house_dialogue

label mia_button_dialogue_bedroom:
    $ location_count = "Mia's Bedroom"
    scene location_mia_bedroom_closeup
    show mia 10 at right
    show player 13 at left with dissolve
    mia "I'm so happy you came!"
    show mia 7
    show player 21
    player_name "Hi, {b}Mia{/b}!"
    show player 29
    player_name "Feels kind of strange, sneaking into someone's house at night..."
    show mia 9
    show player 13
    mia "It's fine! We're not gonna get in trouble..."
    show mia 10
    show player 11
    mia "...We just have to {b}stay quiet{/b}!"
    show mia 7
    show player 17
    player_name "If you say so. Haha."
    show mia 12
    show player 1
    label mia_talk:
        mia "So... You want to hang out?"
        menu:
            "Chat":
                show mia 7
                show player 2
                player_name "Sure!"
                show player 10
                player_name "Umm... You don't have to answer this, but..."
                show mia 8
                player_name "Don't you find it odd that your parents won't let you have friends over?"
                show player 5
                mia "..."
                show mia 12
                mia "It's just... the way it is, with my mom."
                show mia 8
                show player 12
                player_name "And you don't mind??"
                show player 11
                show mia 12
                mia "She's just being protective!"
                mia "I know she just loves me a lot, and wants the best for me..."
                show mia 8
                show player 12
                player_name "But you have to meet with friends secretly..."
                show mia 12
                show player 5
                mia "I know... But she wouldn't understand."
                show mia 8
                show player 24
                player_name "I see..."
                show player 21
                player_name "As long as you're happy?"
                show mia 9
                show player 13
                mia "Yup!"
                jump mia_talk
            "Study":

                if gTimer.is_night():
                    show player 10
                    player_name "I should get going: It's getting late."
                else:
                    show mia 7
                    show player 21
                    player_name "I guess we should be studying?"
                    show mia 9
                    show player 13
                    mia "Of course!"
                    show mia 10
                    mia "Let's do that, then."
                    show player 11
                    mia "Let me get all the textbooks and set up {b}on my bed{/b}?"
                    show mia 7
                    show player 21
                    player_name "Uh... Okay!"
                    jump mia_study
            "I have to go.":

                show mia 8
                show player 10
                player_name "I'd love to... But it's getting late..."
                show mia 12
                show player 5
                mia "Oh, okay..."
                mia "...Will you come back soon?"
                show player 14
                show mia 8
                player_name "Yeah. I'll see what I can do!"
                show mia 12
                show player 1
                mia "Good night..."
    $ callScreen(location_count)

label mia_study:
    scene mia_bedroom_closeup
    $ gTimer.tick()
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "So... I don't really know how to say this..."
    show mia 18
    show player 143
    mia "...And I'm so shy in front of people, especially boys..."
    mia "...but, I didn't really want to study."
    show player 145
    show mia 19
    player_name "Huh?"
    show mia 18
    show player 143
    mia "I couldn't come up with a better excuse to hang out..."
    mia "... And I kind of like you!"
    show player 145
    show mia 14
    player_name "Why didn't you just tell me before?"
    show mia 18
    show player 143
    mia "Well, I wanted to spend time together, but my mom would never allow it, so..."
    show mia 13
    show player 145
    player_name "It's okay. I understand!"
    show player 142
    player_name "It's nice of you to invite me. I like this..."
    show mia 16
    show player 141
    mia "What about you?"
    show mia 13
    show player 145
    player_name "Huh?"
    show mia 18
    show player 143
    menu:
        mia "Do you... Also like me?"
        "Yes.":
            show mia 19
            show player 145
            player_name "I do..."
            show mia 15
            show player 141
            mia "Really??"
            show mia 16
            show player 143
            mia "So... What do you like about me?"
            show mia 19
            show player 145
            player_name "I think you're really nice... You know..."
            player_name "...Like when you talk to me at school and stuff!"
            show mia 18
            show player 141
            mia "That's sweet!"
            show mia 19
            show player 142
            player_name "I also think that... you're really pretty!"
            show player 141
            mia "..."
            show mia 18
            mia "Really?"
            menu:
                "Close your eyes.":
                    show player 142
                    show mia 19
                    player_name "Close your eyes..."
                    show mia 18
                    show player 141
                    mia "Why?"
                    show mia 19
                    show player 142
                    player_name "...Just do it."
                    show mia 17
                    show player 147
                    mia "Hmm..."
                    show mia 18
                    mia "..."
                    show player 148
                    show mia 20 at Position (xpos = 647, ypos = 574) with hpunch
                    mia "{b}!!!{/b}"
                    show mia 18 zorder 1 at Position (xpos = 680, ypos = 574)
                    show player 143
                    mia "...I can't do that... Yet!"
                    show mia 14
                    show player 146
                    player_name "...Sorry, I thought-"
                    show mia 22
                    show player 144
                    mia "No, It's fine! I'm sorry... I just can't, right now..."
                    mia "...If my mom saw us, we'd be dead."
                    mia "It may be better if we did this another time..."
                    show mia 14
                    show player 146
                    player_name "It's okay. I understand..."
                    scene mia_bedroom
                    show mia 7 at right
                    show player 21 at left
                    with dissolve
                    player_name "I'll see you later, then?"
                    show mia 10
                    show player 13
                    mia "Yeah..."
                    mia "Thanks for coming."
                    show mia 7
                    show player 21
                    player_name "Good night!"
        "No.":

            show mia 14
            show player 146
            player_name "I see you more like... a friend."
            show mia 22
            show player 144
            mia "Ohh... I see."
            show mia 14
            show player 145
            player_name "But, this the first time we've ever hung out!"
            player_name "Give it some time. Maybe we can get to know each other better!"
            show mia 22
            show player 144
            mia "Yeah, okay..."
            scene mia_bedroom
            show mia 8 at right
            show player 21 at left
            with dissolve
            player_name "I'll see you later, then?"
            show player 13
            show mia 12
            mia "Yeah..."
            mia "Thanks for coming."
            show mia 8
            show player 21
            player_name "Good night!"
    $ location_count = "Mia's House"
    $ callScreen(location_count)

label night_closed_mia:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
    hide player 2 with dissolve
    hide miahouse_night
    $ callScreen(location_count)

label closed_mia:
    scene miahouse
    show player 12 with dissolve
    if gTimer.is_morning() and not gTimer.is_weekend():
        player_name "( There's no one here... )"
        show player 35
        player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
    else:
        player_name "( {b}Mia{/b} is outside, I shouldn't go in there. )"
    $ callScreen(location_count)

label mias_bedroom_screen:
    $ location_count = "Mia's Bedroom"
    $ callScreen(location_count)

label mias_house_sneak:
    $ location_count = "Mia's House Entrance"
    scene black with dissolve
    with Pause(0.5)

    show mia_sneak01 with dissolve
    show text "The door is unlocked.\n I hope I don't get in trouble for this...\n Alright, I'm going in." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show mia_sneak02 with dissolve
    show text "Both her parents are watching TV, as Mia predicted.\n I just have to be quiet and make my way upstairs now...\n" at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve


    hide mia_sneak01
    hide mia_sneak02
    scene black
    with dissolve
    with Pause(0.5)
    $ callScreen(location_count)

label mia_mailbox:
    scene expression gTimer.image("mia_mailbox{}")
    if m_pizza_pamphlet in mia_mail:
        player_name "( This is probably junk mail. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza. I haven't been there in a while. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True
        call screen mia_mailbox
    elif m_newspaper in mia_mail:
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The theif is still out on the loose? You would've thought they would've caught him by now. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
        call screen mia_mailbox
    else:
        call screen mia_mailbox

label mias_house:
    $ location_count = "Mia's House"
    $ callScreen(location_count)