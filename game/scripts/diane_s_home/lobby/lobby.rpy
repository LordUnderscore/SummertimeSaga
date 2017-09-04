label dianelobby_dialogue:
    $ location_count = "Diane's Lobby"
    if aunt.started(aunt_mouse_attack):
        scene dianeentrance with None
        show player 22 with dissolve
        dia "HELP!"
        dia "QUICK! HELP ME!"
        show player 23
        player_name "{b}Aunt Diane{/b}?!"
        player_name "I'M COMING!"
        show player 22
        dia "EEEEEEEKKKKKKK!"
        hide player with dissolve
    $ callScreen(location_count)

label dianelobby_locked:
    scene dianekitchen with None
    show aunt 3 at right
    show player 11 at left
    with dissolve
    dia "Where are you going? The garden is outside, not in there, handsome."
    hide aunt
    hide player
    with dissolve
    $ callScreen(location_count)