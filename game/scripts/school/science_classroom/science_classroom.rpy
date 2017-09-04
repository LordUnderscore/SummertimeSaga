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