screen church_graveyard:
    add gTimer.image("backgrounds/location_church_graveyard{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (248,507)
            idle "images/objects/object_tomb_01.png"
            hover "images/objects/object_tomb_01b.png"
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        if not gTimer.is_dark():
            pos (627,223)
        else:
            pos (626,223)
        idle gTimer.image("images/objects/object_tomb_02{}.png")
        hover gTimer.image("images/objects/object_tomb_02b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("church_graveyard"), Jump("garden_dialogue")