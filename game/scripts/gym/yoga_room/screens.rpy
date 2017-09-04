screen yoga_room:
    add gTimer.image("backgrounds/location_yoga{}.jpg")

    if is_here("mrsj"):
        imagebutton:
            focus_mask True
            pos (660,340)
            idle "objects/character_erikmom_01.png"
            hover "objects/character_erikmom_01b.png"
            action Hide("yoga_room"), Jump("mrsj_yoga_button_dialogue")

    if is_here("anna"):
        imagebutton:
            focus_mask True
            pos (660,340)
            idle "objects/character_anna_02.png"
            hover "objects/character_anna_02b.png"
            action Hide("yoga_room"), Jump("anna_yoga_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_05.png"
        hover "boxes/auto_option_05b.png"
        action Hide("yoga_room"), Jump("training_dialogue")