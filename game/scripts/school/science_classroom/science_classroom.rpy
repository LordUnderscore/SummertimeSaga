default science_classroom_first_visit = True

label science_classroom_dialogue:
    $ location_count = "Science Classroom"
    if science_classroom_first_visit == True:
        scene science_classroom_c with None
        show okita 1 at right
        show player 5 at left
        with dissolve
        show okita 2
        okita "Well, well..."
        okita "Someone finally decided to put their brain to good use, once again."
        show okita 1
        show player 10
        player_name "Hi, {b}Ms. Okita{/b}."
        player_name "I didn't mean to be away this long. I was-"
        show okita 2
        show player 5
        okita "Your personal life is irrelevent to me."
        okita "What I care about is attendance, and results."
        show okita 1
        show player 24
        player_name "Yes, {b}Ms. Okita{/b}."
        show player 10
        player_name "I'll be studying twice as hard!"
        show okita 2
        show player 5
        okita "One more thing..."
        okita "Where's your {b}lab coat{/b}, {b}[firstname]{/b}?"
        show okita 1
        show player 35
        player_name "Oh, right..."
        show player 29
        player_name "I'm not sure where it is, {b}Ms. Okita{/b}."
        show okita 2
        show player 3
        okita "You can't conduct experiments in my class without it!"
        okita "Find your {b}lab coat{/b}, and we can begin our studies."
        show okita 1
        show player 10
        player_name "Yes, {b}Ms. Okita{/b}..."
        hide okita
        hide player
        with dissolve
        $ science_classroom_first_visit = False

    elif M_mia.get_state() == S_mia_return_favor:
        scene school_science_c02
        show player 13 at left
        show mia 10 at right
        with dissolve
        mia "{b}[firstname]{/b}!"
        show mia 7
        show player 14
        player_name "Hi, {b}Mia{/b}."
        show player 12
        player_name "How's your...leg?"
        show player 13
        show mia 9
        mia "Oh, it's fine... Just a little sore, ha ha."
        show mia 10
        mia "It's much better already, and I removed the bandage!"
        show mia 7
        show player 17
        player_name "Cool! How does it look?"
        show player 13
        show mia 10
        mia "I wanted to show you, actually... And give you something as a thank you for helping me."
        show mia 7
        show player 10
        player_name "Here?"
        show player 11
        show mia 9
        mia "Not here, silly!"
        show mia 7
        show player 17
        player_name "Oh, ha ha."
        show player 13
        show mia 10
        mia "{b}Come to my room tonight{/b} and I'll show you."
        show mia 7
        show player 14
        player_name "Okay, I'll come by!"
        show player 13
        show mia 10
        mia "Great! See you then!"
        hide player
        hide mia
        with dissolve
        $ M_mia.trigger(T_mia_night_invite)

    elif M_mia.get_state() == S_mia_strip_aftermath:
        scene school_science_c02
        show player 5 at left
        show mia 12 at right
        with dissolve
        mia "Hey, {b}[firstname]{/b}..."
        show mia 8
        show player 10
        player_name "{b}Mia{/b}!"
        player_name "Sorry about the other night."
        show player 12
        player_name "Is everything okay at home?"
        show player 5
        show mia 12
        mia "Actually, I wanted to talk about that."
        show mia 8
        show player 11
        player_name "..."
        show mia 12
        mia "I'm now forbidden to spend time with friends...and especially you."
        mia "My mom says I have to be home after school and not speak to you..."
        show mia 8
        show player 10
        player_name "...But {b}Mia{/b} I-"
        show player 11
        show mia 12
        mia "We can't talk, sorry..."
        hide mia with dissolve
        show player 24
        player_name "I didn't mean to get you in trouble..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_grounded)
    $ callScreen(location_count)

label okita_button_dialogue:
    scene science_classroom_c with None
    show okita 1 at right
    show player 5 at left
    with dissolve
    show player 10
    player_name "Hi, {b}Ms. Okita{/b}."
    show okita 2
    show player 5
    okita "What seems to be the problem, {b}[firstname]{/b}?"
    show okita 1
    show player 11
    menu:
        "Nothing.":
            show player 29
            player_name "No problem here, {b}Ms. Okita{/b}."
            player_name "Just preparing for the upcoming lab experiments."
            show okita 2
            show player 3
            okita "Good."
            okita "If my numbers are right, your study output has to increase by 400 percent in the coming weeks."
            show player 22
            okita "Otherwise, you WILL fall behind, and I WILL fail you."
            show okita 1
            show player 23
            player_name "!!!" with hpunch
            show player 10
            player_name "Understood, {b}Ms. Okita{/b}."
    hide okita
    hide player
    with dissolve
    $ callScreen(location_count)