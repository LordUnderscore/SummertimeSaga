screen police_office:
    add "backgrounds/location_police_office.jpg"

    imagebutton:
        focus_mask True
        pos (669,425)
        idle "objects/character_harold_01_empty.png"
        if M_mia.get_state() == S_mia_search_desk:
            hover "objects/character_harold_01b_empty.png"
            action Hide("police_office"), Jump("police_harolds_desk")

    if is_here("harold"):
        imagebutton:
            focus_mask True
            pos (670,384)
            idle "objects/character_harold_01.png"
            hover "objects/character_harold_01b.png"
            action Hide("police_office"), Jump("police_harold_dialogue")

    if is_here("earl"):
        imagebutton:
            focus_mask True
            pos (280,350)
            idle "objects/character_earl_01.png"
            hover "objects/character_earl_01b.png"
            action Hide("police_office"), Jump("police_earl_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_13.png"
        hover "boxes/auto_option_13b.png"
        action Hide("police_office"), Jump("police_lobby_dialogue")

screen harolds_desk:

    imagebutton:
        focus_mask True
        pos (896,628)
        idle PulseImage("objects/object_picture_02.png", "objects/object_picture_02b.png", delay = 0.5)
        hover "objects/object_picture_02b.png"
        action Hide("harolds_desk"), Return()