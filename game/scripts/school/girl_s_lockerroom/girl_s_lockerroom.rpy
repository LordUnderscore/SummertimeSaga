label girl_lockerroom_dialogue:
    $ location_count = "School Girl's Lockerroom"
    if not judith_sobbing:
        scene girl_lockerroom
        show player 106 at left with dissolve
        player_name "Woah! There's a big hole in the ground in here..."
        player_name "( No wonder they had to close this lockeroom! )"
        show player 90
        player_name "..."
        show player 10
        player_name "( I can still hear sobbing. )"
        player_name "( There's definitely {b}someone in here{/b}... )"
        $ judith_sobbing = True
        hide player 10 with dissolve
    $ callScreen(location_count)

label judith_toilet:
    if not judith_daylock:
        if not judith_sex_sequence_unlocked:
            scene toilet_stall
            $ left_hall_dialogue_count = 4
            show judith 11 zorder 1 at Position( xpos = 310, ypos = 768) with dissolve
            window hide
            pause
            show player 106f zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
            player_name "!!!"
            jud "{b}*Sobbing*{/b}"
            show player 108
            player_name "{b}Judith{/b}?!"
            show judith 13
            show player 109
            jud "...Hey, {b}[firstname]{/b}."
            show judith 12
            show player 108
            player_name "Are you okay?"
            show judith 13
            show player 109
            jud "I just wanted to stay away, from everyone."
            show judith 12
            show player 108
            player_name "What do you mean?"
            show judith 13
            show player 109
            jud "No one likes me... And everyone makes fun of my body..."
            jud "...so at least in here I won't be made fun of."
            show judith 12
            show player 108
            player_name "You can't let these people get to you that way!"
            show judith 13
            show player 109
            jud "They're right, though. I am ugly..."
            menu:
                "You're not ugly!":
                    show player 111
                    show judith 12
                    player_name "I don't think you're ugly at all!!"
                    show judith 15
                    show player 110
                    jud "...Really?"
                    show judith 14
                    show player 111
                    player_name "Yeah!"
                    player_name "I think you look good!"
                    show judith 15
                    show player 110
                    jud "That's...the nicest thing anyone has said to me..."
                    show judith 14
                    show player 111
                    player_name "Well, I'm just being honest... And I'm sure I'm not the only one!"
                    player_name "You just have to ignore all the negative stuff at school."
                    show judith 15
                    show player 110
                    jud "I guess you're right..."
                    show judith 14
                    show player 111
                    player_name "Anyway, we should get out of here and get back to class."
                    show judith 17
                    show player 106f
                    jud "Wait!!"
                    jud "Stay here a little longer... With {b}me{/b}..."
                    menu:
                        "Ok.":
                            show judith 16
                            show player 111
                            player_name "Oh... Okay."
                            show judith 17
                            show player 110
                            jud "Do you remember the other day when..."
                            jud "...We were both in the lockeroom? In front of {b}Annie{/b}?"
                            show judith 16
                            show player 111
                            player_name "Yeah?"
                            show judith 17
                            show player 110
                            jud "Well I... I liked the way you looked at me."
                            show judith 16
                            show player 106f
                            player_name "!!!"
                            show judith 17
                            jud "It wasn't just your eyes... Your body was also reacting."
                            show judith 16
                            player_name "..."
                            show judith 17
                            jud "Was it my {b}breasts{/b} that made you... So happy? {b}Down there{/b}?"
                            show judith 16
                            show player 111
                            player_name "I... I'm sorry!"
                            show judith 17
                            show player 106f
                            jud "Don't be sorry!!"
                            jud "...I really liked it and..."
                            jud "...I was wondering If I could, you know, see it again?"
                            menu:
                                "Sure.":
                                    show judith 16
                                    show player 111
                                    player_name "I guess so..."
                                    show judith 17
                                    show player 106f
                                    jud "Let me do it."
                                    hide player
                                    show judith 18 at Position(xpos = 447, ypos = 768)
                                    player_name "!!!"
                                    show judith 19
                                    window hide
                                    pause
                                    show judith 20
                                    window hide
                                    pause
                                    show judith 21
                                    window hide
                                    pause
                                    show judith 22
                                    window hide
                                    pause
                                    show judith 24
                                    jud "It's so... Nice..."
                                    jud "...And thick."
                                    show judith 23
                                    player_name "{b}*Gasp*{/b}"
                                    show judith 24
                                    jud "I just love how it feels in my hand..."
                                    show judith 25_23
                                    pause 4
                                    jud "..."
                                    show judith 23
                                    jud "Would you like to touch my breasts?"
                                    menu:
                                        "Yes.":
                                            $ judith_sex_sequence_unlocked = True
                                            player_name "Yeah! I'd love to..."
                                            show judith 33
                                            player_name "..."
                                            show judith 34
                                            player_name "Wow..."
                                            show judith 35
                                            jud "Go ahead!"
                                            jud "Touch them... But be gentle! They're really sensitive..."
                                            show judith 36_37_38
                                            pause 4
                                            show judith 39 with hpunch
                                            jud "*Moaning*"
                                            player_name "!!!"
                                            show judith 33
                                            jud "It's just too much. My body get's all fuzzy when you touch my nipples..."
                                            show judith 4f zorder 1 at Position( xpos = 310, ypos = 768)
                                            show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
                                            player_name "I didn't mean to hurt you."
                                            show player 13f
                                            show judith 5f
                                            jud "No, it's fine! It felt really good... I'm just sensitive..."
                                            show judith 4f
                                            show player 10f
                                            player_name "Maybe we should stop..."
                                            show player 13f
                                            show judith 5f
                                            jud "Yeah... Thanks for staying with me, I feel much better..."
                                            show judith 2f
                                            jud "...And if you want, we could do this again, some time..."
                                            show judith 4f
                                            show player 17f
                                            player_name "I'd like that!"
                                            show judith 5f
                                            show player 13f
                                            jud "I'll see you later then."
                                            hide player
                                            hide judith
                                            with dissolve
                                            jump left_hall_dialogue
                                        "We should stop.":

                                            show judith 24
                                            player_name "I think we should stop..."
                                            show judith 6f zorder 1 at Position( xpos = 310, ypos = 768)
                                            show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
                                            player_name "We can't be late for class and {b}Annie{/b} could see us in here..."
                                            show player 13f
                                            show judith 2f
                                            jud "I understand. Thanks for staying with me..."
                                            show judith 3f
                                            jud "...And if you want, we could do this again, some time..."
                                            show judith 4f
                                            show player 17f
                                            player_name "I'd like that!"
                                            show player 13f
                                            show judith 5f
                                            jud "I'll see you later then."
                                            hide player
                                            hide judith
                                            with dissolve
                                            jump left_hall_dialogue
                                "I can't.":

                                    show judith 16
                                    show player 108
                                    player_name "I can't do that right now, {b}Judith{/b}..."
                                    player_name "Also, we should really go... I don't want to be late and {b}Annie{/b} could see us in here..."
                                    show judith 13
                                    show player 109
                                    jud "Oh..."
                                    jud "You can go, then. I'll stay here a little bit longer I think..."
                                    show player 111
                                    show judith 14
                                    player_name "Alright, I'll see you later then."
                                    jump left_hall_dialogue
                        "We should leave.":

                            show judith 16
                            show player 108
                            player_name "We should really go... I don't want to be late and {b}Annie{/b} is already on my case..."
                            show judith 13
                            show player 109
                            jud "Oh..."
                            jud "You can go, then. I'll stay here a little bit longer I think..."
                            show judith 14
                            show player 111
                            player_name "Alright, I'll see you later then."
                            jump left_hall_dialogue
                "I know...":

                    show judith 12
                    show player 108
                    player_name "I know, but you have to learn to deal with it!"
                    show player 109
                    jud "..."
                    show judith 11
                    jud "{b}*Sobbing*{/b}"
                    show player 108
                    player_name "I'm sorry..."
                    show player 106f
                    jud "I just want to be alone right now."
                    show player 108
                    player_name "I'll see you later, then..."
                    jump left_hall_dialogue
        else:

            scene toilet_stall
            show judith 14 zorder 1 at Position( xpos = 310, ypos = 768)
            show player 111 zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
            player_name "Hey!"
            show judith 15
            show player 110
            jud "I was hoping you'd come see me..."
            jud "Did anyone see you come in here?"
            show judith 14
            show player 108
            player_name "I don't think so?"
            show judith 14
            show player 110
            jud "Oh, good..."
            jud "Emm... So? What do you feel like doing?"
            call screen judith_stage01
    else:

        scene toilet_stall
        show player 11 with dissolve
        player_name "..."
        show player 10
        player_name "( {b}Judith{/b} is not here. )"
        player_name "( She must have gone home, or she's still in class. )"
        show player 108f
        player_name "( I should try coming back {b}tomorrow{/b}. )"
        hide player 108f
        jump girl_lockerroom_dialogue

label judith_kiss:
    $ judith_daylock = True
    show player 108
    show judith 14
    player_name "Hmm... Have you ever kissed someone?"
    show judith 15
    show player 110
    jud "You mean, like a... Kiss, kiss?"
    show judith 14
    show player 17f
    player_name "Well, yeah!"
    show judith 13
    show player 110
    jud "Not really..."
    show judith 14
    show player 17f
    player_name "Let's try it!"
    show judith 4f
    show player 110
    jud "..."
    hide player
    show judith 31_32 at Position ( xpos = 380, ypos = 768)
    with dissolve
    pause 4
    show judith 5f zorder 1 at Position( xpos = 320, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 640, ypos = 768)
    with dissolve
    jud "That... Was good..."
    show judith 4f
    show player 17f
    player_name "Feels a bit strange I guess. Ha ha."
    show judith 5f
    show player 11f
    jud "Let's do something else!"
    show judith 4f
    show player 14f
    player_name "Okay..."
    call screen judith_stage02

label judith_handjob:
    show player 111
    show judith 16
    player_name "We could do like last time, I guess?"
    show judith 17
    show player 106f
    jud "Let me do it."
    hide player
    show judith 18 at Position(xpos = 465, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "It's so... Nice..."
    jud "...And thick."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "I just love how it feels in my hand..."
    show judith 25_23
    pause 4
    player_name "That feels sooo... good!"
    show judith 24
    jud "You want me to stop?"
    call screen judith_stage03

label judith_keepgoing:
    show judith 25_23
    pause 4
    player_name "That feels sooo... good!"
    show judith 24
    jud "You want me to stop?"
    call screen judith_stage03

label judith_playwithtits:
    show judith 33
    jud "..."
    show judith 35
    jud "You like feeling them?"
    show judith 34
    player_name "Yeah..."
    show judith 36
    player_name "Your breasts are so nice and soft..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "{b}*Moaning*{/b}"
    player_name "!!!"
    show judith 35
    jud "You want to try something else?"
    call screen judith_stage03

label judith_cum:
    show judith 25_23
    pause 4
    show judith 26
    pause .3
    show judith 27
    jud "..."
    show judith 28
    jud "Wow, that's a lot of cum!"
    show judith 29
    player_name "Sorry! I didn't mean to make a mess..."
    show judith 28
    jud "It's fine..."
    jud "I always wanted to know how that feels!"
    show judith 30
    player_name "Oh. Ha ha!"
    show judith 5f zorder 1 at Position( xpos = 300, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 623, ypos = 768)
    jud "We could do this again..."
    show player 17f
    show judith 4f
    player_name "I'd like that!"
    show player 13f
    show judith 5f
    jud "Me too..."
    show player 2f
    show judith 4f
    player_name "We should get out of here..."
    show player 1f
    show judith 5f
    jud "Okay!"
    $ gTimer.tick()
    if not gTimer.is_dark():
        jump left_hall_dialogue
    else:
        jump night_closed_school

label judith_pullpants:
    show judith 24
    jud "I'm not... Ready for that yet."
    show judith 23
    player_name "Oh... It's okay! We don't have to."
    show judith 24
    jud "Maybe another time..."
    jud "...When I feel a bit more comfortable."
    show judith 23
    player_name "I'm ok with that."
    show judith 24
    jud "Can we do something else?"
    call screen judith_stage03