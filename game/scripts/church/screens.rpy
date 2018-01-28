screen church:
    if gTimer.is_weekend() and gTimer.is_morning():
        if is_here("helen") and is_here("harold"):
            add "backgrounds/location_church_full01.jpg"

        elif is_here("helen"):
            add "backgrounds/location_church_full02.jpg"

        else:
            add "backgrounds/location_church_full03.jpg"

    else:
        add gTimer.image("backgrounds/location_church{}.jpg")

    if is_here("angelica"):
        imagebutton:
            focus_mask True
            pos (810,380)
            idle "objects/character_angelica_01.png"
            hover "objects/character_angelica_01b.png"
            action Hide("church"), Jump("angelica_dialogue")

    imagebutton:
        focus_mask True
        pos (281,367)
        idle gTimer.image("objects/object_door_47{}.png")
        hover gTimer.image("objects/object_door_47b{}.png")
        action Hide("church"), Jump("confessional_left")

    imagebutton:
        focus_mask True
        pos (440,368)
        idle gTimer.image("objects/object_door_48{}.png")
        hover gTimer.image("objects/object_door_48b{}.png")
        action Hide("church"), Play("audio", sfxDoor()), Jump("confessional_right")

    imagebutton:
        focus_mask True
        pos (287,169)
        idle gTimer.image("objects/object_door_71{}.png")
        hover gTimer.image("objects/object_door_71b{}.png")
        action Hide("church"), Function(playSound), Play("audio", sfxDoor()), Jump("church_stairs_dialogue")