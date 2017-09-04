screen dealership:
    add "backgrounds/location_dealership_indoor.jpg"

    imagebutton:
        focus_mask True
        pos (321,441)
        idle "objects/character_josephine_01.png"
        hover "objects/character_josephine_01b.png"
        action Hide("dealership"), Jump("josephine_button_dialogue")