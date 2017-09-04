screen poker_screen:
    $ b = 680
    $ c = 0
    for Card in player_hand:
        $ a = 308
        $ a = a + c*55
        add Card.hand_image xpos a ypos b
        $ c += 1
    $ b1 = 48
    $ c1 = 0
    for Card in bot_hand:
        $ a = 308
        $ a = a + c1*55

        add "buttons/poker_cards_small_back.png" xpos a ypos b1
        $ c1 += 1
    $ b6 = 48
    $ c6 = 0
    for Card in bot02_hand:
        $ a6 = 602
        $ a6 = a6 + c6*55

        add "buttons/poker_cards_small_back.png" xpos a6 ypos b6
        $ c6 += 1
    imagebutton:
        idle "buttons/poker_button_allin_01.png"
        hover "buttons/poker_button_allin_01b.png"
        action [SetVariable("bot_fold_chance", bot_fold_chance - 30), Jump("all_in")]
        xpos 700
        ypos 706
    imagebutton:
        idle "buttons/poker_button_call_01.png"
        hover "buttons/poker_button_call_01b.png"
        action Jump("poker_call")
        xpos 570
        ypos 706
    imagebutton:
        idle "buttons/poker_button_fold_01.png"
        hover "buttons/poker_button_fold_01b.png"
        action Jump("fold")
        xpos 440
        ypos 706
    imagebutton:
        idle "buttons/poker_button_leave_01.png"
        hover "buttons/poker_button_leave_01b.png"
        action Hide("poker_screen"), Jump("erik_basement")
        xpos 865
        ypos 690

    if len(table) >= 1:
        add table[0].image xpos 250 ypos 300
    else:
        add "buttons/poker_cards_large_back.png" pos 250,300
    if len(table) >= 2:
        add table[1].image pos 360,300
    else:
        add "buttons/poker_cards_large_back.png" pos 360,300
    if len(table) >= 3:
        add table[2].image pos 470,300
    else:
        add "buttons/poker_cards_large_back.png" pos 470,300
    if len(table) >= 4:
        add table[3].image pos 580,300
    else:
        add "buttons/poker_cards_large_back.png" pos 580,300
    if len(table) >= 5:
        add table[4].image pos 690,300
    else:
        add "buttons/poker_cards_large_back.png" pos 690,300

    $ b4 = 630
    $ c4 = 0

    for Cloth in player_cloth:
        if c4 == 3:
            $ b4 = 700
            $ c4 = 0
        $ a4 = 30
        $ a4 = a4 + c4*80
        if Cloth in player_cloth_active:
            add Cloth.image pos a4,b4
        else:
            add Cloth.passive_image pos a4,b4
        $ c4 += 1

    $ b5 = 30
    $ c5 = 0
    for Cloth in erik_cloth:
        if c5 == 3:
            $ b5 = 100
            $ c5 = 0
        $ a5 = 30
        $ a5 = a5 + c5*80
        if Cloth in erik_cloth_active:
            add Cloth.image pos a5,b5
        else:
            add Cloth.passive_image pos a5,b5
        $ c5 += 1

    $ b7 = 30
    $ c7 = 0
    if poker_bot02 == "mia":
        for Cloth in mia_cloth:
            if c7 == 3:
                $ b7 = 100
                $ c7 = 0
            $ a7 = 750
            $ a7 = a7 + c7*80
            if Cloth in mia_cloth_active:
                add Cloth.image pos a7,b7
            else:
                add Cloth.passive_image pos a7,b7
            $ c7 += 1
    elif poker_bot02 == "erik_mom":
        for Cloth in mrsj_cloth:
            if c7 == 3:
                $ b7 = 100
                $ c7 = 0
            $ a7 = 750
            $ a7 = a7 + c7*80
            if Cloth in mrsj_cloth_active:
                add Cloth.image pos a7,b7
            else:
                add Cloth.passive_image pos a7,b7
            $ c7 += 1

    if erik_status == "call":
        add "buttons/poker_text_call.png" pos 330,10
    elif erik_status == "fold":
        add "buttons/poker_text_fold.png" pos 330,10
    elif erik_status == "allin":
        add "buttons/poker_text_allin.png" pos 330,10

    if mrsj_status == "call":
        add "buttons/poker_text_call.png" pos 630,10
    elif mrsj_status == "fold":
        add "buttons/poker_text_fold.png" pos 630,10
    elif mrsj_status == "allin":
        add "buttons/poker_text_allin.png" pos 630,10

    if player_status == "call":
        add "buttons/poker_text_call.png" pos 330,640
    elif player_status == "fold":
        add "buttons/poker_text_fold.png" pos 330,640
    elif player_status == "allin":
        add "buttons/poker_text_allin.png" pos 330,640

screen unclick_overlay:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Return()