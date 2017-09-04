screen dianes_bedroom:
    add gTimer.image("backgrounds/location_diane_bedroom{}.jpg")

    if aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_06.png"
            hover "images/objects/object_bed_06b.png"
            action Hide("dianes_bedroom"), Jump("diane_bedroom_dialogue")

    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_07.png"
            hover "images/objects/object_bed_07b.png"
            action Hide("dianes_bedroom"), Jump("diane_bedroom_dialogue")

    if (not aunt.known(aunt_drunken_splur) or aunt.completed(aunt_drunken_splur)) and ( not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)):
        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/door19_option_01.png"
            hover "boxes/door19_option_01b.png"
            action Hide("dianes_bedroom"), Jump("dianelobby_dialogue")