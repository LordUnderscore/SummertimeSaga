default police_lobby_first_visit = True
default police_office_first_visit = True
default police_basement_first_visit = True
default police_earl_first_visit = True

label police_lobby_dialogue:
    $ location_count = "Police Lobby"
    if police_lobby_first_visit == True:
        scene police_lobby_b with None
        show player 11
        with dissolve
        player_name "( The Police station... Man, I'm sure glad I never had to come here before. )"
        hide player with dissolve
        $ police_lobby_first_visit = False
    $ callScreen(location_count)

label police_board:
    scene police_board
    with dissolve
    player_name "( This looks like the info board... )"
    pause
    $ callScreen(location_count)

label police_office_dialogue:
    $ location_count = "Police Office"
    if police_office_first_visit == True:
        scene police_office_b
        show yumi 2f at left
        show harold 1 at right
        with dissolve
        yum "Thank you so much for this opportunity, sir!"
        yum "I've been looking forward to this moment every since I entered the academy."
        show harold 2
        show yumi 1f
        harold "That's great, {b}Yumi{/b}."
        harold "It feels good to have a new partner."
        show yumi 2f
        show harold 1
        yum "I have to get back to cell duty."
        show yumi 1f
        show harold 2
        harold "Oh. Alright then. See you later."
        show harold 1
        hide yumi with dissolve
        pause
        show player 1 at left with dissolve
        show harold 2
        harold "Hey! What are you doing here?"
        harold "Aren't you one of {b}Mia's{/b} classmates?"
        show harold 1
        show player 14
        player_name "Hi, I just had some questions."
        show player 1
        menu:
            "Where's {b}Mia{/b}?":
                show player 14 at left
                show harold 1 at right
                player_name "I was just wondering: do you know where {b}Mia{/b} is?"
                show player 11
                show harold 2
                harold "I'm sorry, I can't help you right now; we're busy with a new case..."
                harold "But, she should be at school or at home."
                show harold 1
                show player 14
                player_name "Okay. Thanks, Sir!"
                hide player
                hide harold
                hide ui
                with dissolve
                $ police_office_first_visit = False
    $ callScreen(location_count)

label police_basement_dialogue:
    $ location_count = "Police Basement"
    if police_basement_first_visit == True:
        scene police_basement_b
        pause .4
        scene police_c_3
        show player 1
        with dissolve
        player_name "( This must be the \"drunk tank\" people talk about... )"
        hide player with dissolve
        $ police_basement_first_visit = False
    $ callScreen(location_count)

label police_cell_dialogue:
    scene police_cell
    show xtra 13 zorder 1 at left
    show player 10f zorder 2
    with dissolve
    player_name "I wouldn't want to end up in there. Sheesh!"
    hide player with dissolve
    $ callScreen(location_count)

label police_cell_larry_dialogue:
    scene police_cell
    if not erik.known(erik_father_forgive):
        show larry 15 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 5f at right with dissolve
        larry "Hey! You!"
        show larry 14
        show player 11f
        player_name "!!!"
        show player 12f
        player_name "Umm...Yeah?"
        player_name "What do you want?"
        show player 16f
        show larry 15
        larry "Listen, I'm not mad at you for what you did."
        larry "It's actually nice knowing there is someone keeping watch out for my family."
        show larry 14
        show player 5f
        player_name "..."
        show larry 15
        larry "I know what I was doing was bad, okay?."
        larry "I just... I need you to give {b}Erik{/b} a message from me."
        show larry 14
        show player 10f
        player_name "I'm not sure he would want that..."
        show player 5f
        show larry 15
        larry "I need you to tell him that I'm sorry!"
        larry "I'm sorry for everything..."
        show larry 14
        show player 12f
        player_name "I don't know if I should."
        show player 5f
        show larry 15
        larry "Please!"
        larry "I...I can help you!"
        show larry 14
        show player 10f
        player_name "Huh?"
        show player 11f
        show larry 15
        larry "I stashed a bag full of stolen things I took."
        larry "I'll tell you where they are if you tell my son that everything I did was to help him."
        larry "I was trying to get back on top, you know?"
        larry "I just...did it the wrong way, and I'm sorry for that..."
        show larry 14
        show player 34f
        player_name "..."
        show larry 15
        show player 5f
        larry "You can return the stolen goods to the police, or keep them! I don't care."
        larry "Can you just tell {b}Erik{/b} I'm sorry...and that I love him."
        larry "Hopefully, he can forgive me one day and...perhaps we can see each other again?"
        show larry 14
        show player 35f
        player_name "Hmm..."
        show player 12f
        player_name "I suppose I could. I'll see what I can do."
        show player 5f
        show larry 15
        larry "Thanks, kid!"
        $ erik.add_event(erik_father_forgive)

    elif erik.started(erik_father_forgive):
        show larry 14 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 12f at right with dissolve
        player_name "What did you want me to do again for you?"
        show player 5f
        show larry 15
        larry "Talk to {b}Erik{/b} and tell him I love him and that I'm sorry..."
        larry "If you do, I'll tell you where I hid all the goods I stole."
        show larry 14
        show player 10f
        player_name "I'll see what I can do."

    elif erik.completed(erik_father_forgive) and not erik.known(erik_father_treasure):
        show larry 15 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 5f at right with dissolve
        larry "Hey! It's you again!"
        larry "Did you get a chance to speak to {b}Erik{/b} like I asked?"
        show larry 14
        show player 12f
        player_name "Yeah. I did."
        show player 5f
        show larry 15
        larry "And what...what did he say?!"
        show larry 14
        show player 12f
        player_name "He'll think about it."
        show player 10f
        player_name "You need to give him some time, I guess..."
        show player 5f
        show larry 15
        larry "Thanks, kid."
        larry "You did the right thing..."
        larry "...Alright."
        larry "About those stolen goods I stashed."
        larry "They're {b}behind a bush in the park, next to a white tree{/b}."
        show larry 14
        show player 34f
        player_name "Hmm..."
        show player 12f
        player_name "Okay, I'll go have a look."
        show player 5f
        show larry 15
        larry "Listen! I'm going to try and turn my life around!"
        larry "You'll see!"
        larry "And...and maybe, someday you can even convince {b}Erik{/b} to come visit me?"
        show larry 14
        show player 12f
        player_name "We'll see."
        show player 5f
        show larry 15
        larry "Thanks..."
        $ erik.add_event(erik_father_treasure)

    elif erik.known(erik_father_treasure):
        show larry 14 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 12f at right with dissolve
        player_name "Where did you hide the stolen goods?"
        show player 5f
        show larry 15
        larry "They're {b}behind a bush in the park, next to a white tree{/b}."
        show larry 14
        show player 12f
        player_name "Okay, I'll go have a look."
    hide player
    hide larry
    hide cell_bars
    hide larry_hands
    with dissolve
    $ callScreen(location_count)

label police_harold_dialogue:
    scene police_c_2
    show player 1 at left
    show harold 2 at right
    with dissolve
    harold "Oh, hey, it's you again. Need something?"
    show harold 1
    show player 14
    player_name "Hi, I just had some questions."
    show player 1
    menu:
        "Where's Mia?":
            show player 14 at left
            show harold 1 at right
            player_name "I was just wondering: do you know where Mia is?"
            show player 11
            show harold 2
            harold "I'm sorry, I can't help you right now; we're busy with a new case..."
            harold "But, she should be at school or at home."
            show harold 1
            show player 14
            player_name "Okay. Thanks, Sir!"
            hide player
            hide harold
            with dissolve
    $ callScreen(location_count)

label police_earl_dialogue:
    scene police_c_1 with None
    if police_earl_first_visit == True:
        show earl 2 at right
        show player 11 at left
        with dissolve
        ear "What'chu doing in here?!"
        show earl 3
        ear "Is it another one of those \"Bring your kids to work\" days?"
        show earl 1
        show player 14
        player_name "Oh, no, I'm just passing by, Sir."
        player_name "I wanted to speak with {b}Harold{/b}."
        show earl 2
        show player 1
        ear "Wait a minute... Don't you go to school with my daughter?"
        show earl 3
        show player 14
        player_name "Oh, right! You're {b}Rhonda's{/b} dad!"
        show earl 2
        show player 1
        ear "Shiiiiiiiiiiieeeeeet!"
        show player 11
        ear "You better watch yourself around my baby girl, or I'll have to put surveillance on {b}you{/b}."
        show earl 4
        ear "Got it?!"
        show earl 1
        show player 29 at Position(xpos=8)
        player_name "Uhh... of course, Sir!"
        player_name "I would never-"
        show earl 2
        show player 13 at left
        ear "Relax, I'm just messing with ya! Move along now."
        $ police_earl_first_visit = False
    else:
        show earl 2 at right
        show player 1 at left
        with dissolve
        ear "Hey, what's up?"
        show player 14
        show earl 3
        player_name "Just passing by, Sir."
        show earl 2
        show player 1
        ear "Alright then."
    hide earl
    hide player
    with dissolve
    $ callScreen(location_count)

label police_yumi_dialogue:
    scene police_c_3 with None
    show yumi 2 at right
    show player 1 at left
    with dissolve
    yum "Hello, are you a visitor or are you here to post bail?"
    show yumi 1
    menu:
        "Just visiting.":
            show player 14 at left
            show yumi 1 at right
            player_name "I'm just here to visit someone."
            show yumi 2
            show player 1
            yum "Sure. Make sure you leave your backpack in the bin, and stay behind the line."
            yum "There's no touching allowed."
            hide player
            hide yumi
            with dissolve
    $ callScreen(location_count)