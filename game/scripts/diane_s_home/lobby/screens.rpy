screen dianes_lobby:
    add gTimer.image("backgrounds/location_diane_entrance{}.jpg")

    if aunt.over(aunt_mouse_attack) and (not aunt.known(aunt_drunken_splur) or aunt.completed(aunt_drunken_splur)):
        if ui_lock_count == 0:
            imagebutton:
                focus_mask True
                pos (700,431)
                idle "objects/object_door_56.png"
                hover "objects/object_door_56b.png"
                action Hide("dianes_lobby"), Play("audio", sfxDoor()), Jump("map_dialogue")

        imagebutton:
            focus_mask True
            pos (26,193)
            idle "objects/object_door_57.png"
            hover "objects/object_door_57b.png"
            action Hide("dianes_lobby"), Jump("kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (369,93)
        idle "objects/object_door_58.png"
        hover "objects/object_door_58b.png"
        action Hide("dianes_lobby"), Play("audio", sfxDoor()), Jump("dianebedroom_dialogue")