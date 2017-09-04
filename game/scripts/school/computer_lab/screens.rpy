screen computer_lab:
    add "backgrounds/location_computer.jpg"

    imagebutton:
        focus_mask True
        pos (15,288)
        idle "objects/object_door_76.png"
        hover "objects/object_door_76b.png"
        action Hide("computer_lab"), Play("audio", sfxDoor()), Jump("stairs_dialogue")

    if is_here("june"):
        if is_here("erik"):
            imagebutton:
                focus_mask True
                pos (678,343)
                idle "objects/character_june_03.png"
                hover "objects/character_june_03b.png"
                action Hide("computer_lab"), Jump("june_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (675,395)
                idle "objects/character_june_01.png"
                hover "objects/character_june_01b.png"
                action Hide("computer_lab"), Jump("june_dialogue")