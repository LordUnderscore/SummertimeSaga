screen church_graveyard:
    if (datetime.date.today().month == 10 and datetime.date.today().day > 25) and (datetime.date.today().month == 11 and datetime.date.today().day < 2):
        add gTimer.image("backgrounds/location_church_graveyard_halloween{}.jpg")
    else:
        add gTimer.image("backgrounds/location_church_graveyard{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (248,507)
            idle "objects/object_tomb_01.png"
            hover "objects/object_tomb_01b.png"
            action Show("popup_unfinished")

        if M_aqua.is_set("tomb search"):
            imagebutton:
                focus_mask True
                pos (82,519)
                idle "objects/object_tomb_03.png"
                hover "objects/object_tomb_03b.png"
                action Hide("church_graveyard"), Jump("right_tombstone")

    imagebutton:
        focus_mask True
        if not gTimer.is_dark():
            pos (627,223)
        else:
            pos (626,223)
        if not M_player.is_set("pet cat") and not gTimer.is_dark():
            idle "objects/object_tomb_04.png"
            hover "objects/object_tomb_04b.png"
            action Hide("church_graveyard"), Jump("stray_cat")
        else:
            idle gTimer.image("objects/object_tomb_02{}.png")
            hover gTimer.image("objects/object_tomb_02b{}.png")
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("church_graveyard"), Jump("garden_dialogue")

screen cat_name_input:
    add "boxes/popup_name_cat.png" pos 250,250
    add Input (size=24, color="#5d9aff", default="", changed=stray_cat_name, length=12, xpos= 347, ypos = 347)
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover "buttons/menu_skip_01b.png" action Return pos 362,447