screen science_classroom:

    add "backgrounds/location_school_science.jpg"

    imagebutton:
        focus_mask True
        pos (407,272)
        idle "objects/object_door_59.png"
        hover "objects/object_door_59b.png"
        action Hide("science_classroom"), Play("audio", sfxDoor()), Jump("school_dialogue")

    imagebutton:
        focus_mask True
        pos (505,335)
        idle "objects/character_okita_01.png"
        hover "objects/character_okita_01b.png"
        action Hide("science_classroom"), Jump("okita_button_dialogue")

    if is_here("mia"):
        imagebutton:
            focus_mask True
            pos (718,390)
            idle "objects/character_mia_03.png"
            hover "objects/character_mia_03b.png"
            action Hide("science_classroom"), Jump("mia_button_dialogue")