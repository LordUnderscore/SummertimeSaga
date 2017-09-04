screen police_office:
    add "backgrounds/location_police_office.jpg"

    imagebutton:
        focus_mask True
        pos (670,384)
        idle "images/objects/character_harold_01.png"
        hover "images/objects/character_harold_01b.png"
        action Hide("police_office"), Jump("police_harold_dialogue")

    imagebutton:
        focus_mask True
        pos (280,350)
        idle "images/objects/character_earl_01.png"
        hover "images/objects/character_earl_01b.png"
        action Hide("police_office"), Jump("police_earl_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_13.png"
        hover "boxes/auto_option_13b.png"
        action Hide("police_office"), Jump("police_lobby_dialogue")