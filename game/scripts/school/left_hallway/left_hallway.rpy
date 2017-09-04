default left_hall_cult_seen = False

label left_hall_dialogue:
    $ location_count = "School Left Hallway"
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not gTimer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if not gTimer.is_dark():
        if left_hall_dialogue_count == 0 and not left_hall_dialogue_advancement:
            scene lefthall
            show player 2 at left with dissolve
            show judith 6 at right with dissolve
            player_name "Hey, {b}Judith{/b}..."
            show player 11 at left
            player_name "..."
            show player 10 at left
            player_name "Is everything all right?"
            show player 5 at left
            show judith 3 at right
            jud "Oh, hey, {b}[firstname]{/b}..."
            jud "I'm just not feeling too well; I might just go home."
            show player 10 at left
            show judith 1 at right
            player_name "You're not coming to the Athletics class?"
            show player 5 at left
            show judith 2 at right
            jud "Well..."
            show judith 6 at right
            jud "...I just..."
            show judith 3 at right
            jud "... I can't go in the guy's Locker Room."
            show player 10 at left
            show judith 1 at right
            player_name "Oh yeah, I heard about it... That sucks."
            show player 5 at left
            show judith 2 at right
            jud "I don't really feel comfortable about it, like the other girls."
            show judith 6 at right
            show player 34 at left
            player_name "Well..."
            show player 35 at left
            show judith 1 at right
            player_name "The class is starting soon, so there's probably not that many people left in there anyway?"
            show player 1 at left
            show judith 5 at right
            jud "Yeah, I guess you're right..."
            show player 2 at left
            show judith 4 at right
            player_name "I can go in with you, to make sure you're okay..."
            show player 33 at left
            player_name "...And I won't look!"
            show player 13 at left
            show judith 5 at right
            jud "Okay... I'll follow you, then."
            hide player 13 at left with dissolve
            hide judith 5 at left with dissolve
            $ left_hall_dialogue_advancement = True

        elif left_hall_dialogue_count == 2 and not left_hall_dialogue_advancement:
            scene lefthall
            show judith 10 at left with dissolve
            show latinas 19 at right with dissolve
            lopez "Just look at those nasty-ass saggy tits!"
            show latinas 18 at right
            show judith 7 at left
            jud "..."
            show latinas 20 at right
            show judith 8 at left
            martinez "She's probably too poor to afford a bra..."
            show latinas 18 at right
            show judith 7 at left
            jud "It's not like that!!"
            show latinas 22 at right
            show judith 10 at left
            lopez "You think you're gonna get the boys attention showing your tits around like that?"
            show latinas 18 at right
            show judith 7 at left
            jud "My breasts are sensitive!! It hurts when I wear a bra..."
            jud "I'm just more comfortable like this!!"
            show latinas 22 at right
            show judith 10 at left
            lopez "Haha!"
            show latinas 21 at right
            show judith 9 at left
            martinez "Yo, you better not hang around here no more..."
            martinez "PUTA! Did you just hear? This is our turf, so get out!"
            show latinas 18 at right
            show player 12 at Position( xpos = 290, ypos = 768)
            hide judith 9
            show judith 9 at left
            with dissolve
            player_name "What's going on here?!"
            show player 114
            jud "{b}*Sobbing*{/b}"
            hide combo 7 at left
            show player 90 at Position( xpos = 290, ypos = 768)
            show judith 9 at left
            show latinas 20 at right
            martinez "You defending this ugly bitch now??"
            show latinas 19 at right
            lopez "Keep walking white boy!"
            show latinas 18 at right
            show player 113
            player_name "Are you okay {b}Judith{/b}?"
            show latinas 20 at right
            hide judith
            $ judith_in_toilet = True
            show player 90 at left
            with dissolve
            martinez "What's the matter, white boy, you not gonna run after your bitch?"
            show latinas 18 at right
            show player 12 at left
            player_name "You didn't have to do this..."
            show latinas 20 at right
            martinez "We'll do whatever the fuck we want!"
            show latinas 22 at right
            lopez "Haha! See ya!"
            hide player 12 at right with dissolve
            hide latinas 22 at right with dissolve
            $ left_hall_dialogue_advancement = True

        elif left_hall_dialogue_count == 3 and not girl_lockerroom_unlocked:
            scene lefthall
            show player 11 with dissolve
            player_name "..."
            show player 10
            player_name "...Where's {b}Judith{/b}?"
            player_name "( She usually hangs out in this hallway. )"
            show player 34
            player_name "Hmm..."
            show player 35
            player_name "( I can {b}hear{/b} something... )"
            show player 10
            player_name "( Is that someone... Sobbing? )"
            show player 12
            player_name "( It's like a crying voice coming from the {b}girls locker room{/b}... )"
            hide player 12 with dissolve
            $ girl_lockerroom_unlocked = True
    else:

        if quest11 in quest_list and quest11 not in completed_quests and not left_hall_cult_seen:
            scene cult_event 5
            with dissolve
            window hide
            $ renpy.pause()
            scene cult_event 6
            with Dissolve(0.3)
            $ renpy.pause()
            scene expression "backgrounds/location_lefthall_night.jpg"
            with Dissolve(0.3)
            scene lefthall_night
            show player 11 at left with dissolve
            show erik 1 at right with dissolve
            player_name "..."
            show player 12
            player_name "They went in the utility closet?"
            show player 90
            show erik 5
            eri "Why would they go in there?"
            show player 35
            show erik 1
            player_name "The better question is: How could they all fit in there?"
            player_name "It must lead somewhere else..."
            show player 34
            show erik 5
            eri "Can we leave now?"
            show player 12
            show erik 1
            player_name "Let's just stick to our original plan, and look around."
            show player 1
            show erik 3
            eri "Okay..."
            hide player 1 with dissolve
            hide erik 3 with dissolve
            $ left_hall_cult_seen = True
    $ callScreen(location_count)

label judith_button_dialogue:
    if left_hall_dialogue_count == 1 and not left_hall_dialogue_advancement:
        scene location_lefthall_closeup
        show player 1 at left with dissolve
        show judith 5 at right with dissolve
        jud "Hey {b}[firstname]{/b}!"
        show player 2 at left
        show judith 4 at right
        player_name "Hey {b}Judith{/b}, how's it going?"
        show player 1 at left
        show judith 5 at right
        jud "Oh, I'm great!"
        show judith 2 at right
        jud "I... I just wanted to thank you."
        show judith 4 at right
        show player 21 at left
        player_name "Oh. For what?"
        show judith 3 at right
        show player 13 at left
        jud "In the locker room... You made me feel... safe."
        show judith 4 at right
        show player 11 at left
        player_name "Oh..."
        show judith 5 at right
        jud "And, you know... you stood up to {b}Annie{/b}. I think that was very brave."
        show judith 4 at right
        show player 29 at left
        player_name "It's fine, {b}Judith{/b}. I was just trying to do the right thing."
        player_name "I should be the sorry one... for showing you my... you know..."
        show judith 5 at right
        show player 11 at left
        jud "Oh that's fine!! I enjoyed-"
        show judith 3 at right
        jud "I mean... I didn't mind, at all."
        show judith 5 at right
        jud "We just got to... know each other a little better!"
        show judith 4 at right
        show player 21 at left
        player_name "Haha. Yeah. I suppose so..."
        show judith 5 at right
        show player 1 at left
        jud "I have to go! I'll see you in class then!"
        show player 14 at left
        show judith 4 at right
        player_name "See you later!"
        hide player 14 at left with dissolve
        hide judith 4 at left with dissolve
        $ left_hall_dialogue_advancement = True
    $ callScreen(location_count)

label door64_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "(This is the wrong class. )"
    $ callScreen(location_count)

label door64_locked2_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( I should go in the {b}Field{/b} for my {b}Athletics{/b} class. )"
    $ callScreen(location_count)

label door14_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "( The utility closet is locked. )"
    $ callScreen(location_count)

label door14b_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( I should go in the {b}Fieldd{/b} for my {b}Athletics{/b} class. )"
    $ callScreen(location_count)

label door16_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "( The girl's Locker Room is under repairs. I can't go in there. )"
    $ callScreen(location_count)

label door16b_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( I should go in the {b}Field{/b} for my {b}Athletics{/b} class. )"
    $ callScreen(location_count)

label door16c_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( I need to shower in the {b}Locker Room{/b} first. )"
    $ callScreen(location_count)

label denied_access_lefthall:
    scene lefthall_night
    show erik 1f at Position (xpos = 550, ypos = 768)
    show player 34 at Position (xpos = 370, ypos = 768)
    player_name "Hmm..."
    show player 113
    player_name "( We should find {b}another way{/b}. )"
    hide player 113
    hide erik 1f
    $ callScreen(location_count)

label denied_access_utility:
    scene lefthall_night
    show player 1 at left
    show erik 1 at right
    with dissolve
    player_name "( It's locked... )"
    player_name "( Let's just stick to our original plan, and look around. )"
    hide player 1 with dissolve
    hide erik 1 with dissolve
    $ callScreen(location_count)

label denied_locker_room_dialogue:
    scene lefthall
    show player 10 at left
    player_name "( I better avoid the {b}Locker Room{/b} for today. {b}Dexter{/b} might come looking for me in there. )"
    $ callScreen(location_count)