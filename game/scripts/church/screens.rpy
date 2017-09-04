screen church:
    add "backgrounds/location_church.jpg"

    if angelica_count == 0:
        imagebutton:
            focus_mask True
            pos (810,380)
            idle "objects/character_angelica_01.png"
            hover "objects/character_angelica_01b.png"
            action Hide("church"), Jump("angelica_dialogue")

    imagebutton:
        focus_mask True
        pos (281,367)
        idle "objects/object_door_47.png"
        hover "objects/object_door_47b.png"
        action Hide("church"), Jump("confessional_left")

    imagebutton:
        focus_mask True
        pos (440,368)
        idle "objects/object_door_48.png"
        hover "objects/object_door_48b.png"
        action Hide("church"), Play("audio", sfxDoor()), Jump("confessional_right")

    imagebutton:
        focus_mask True
        pos (287,169)
        idle "objects/object_door_71.png"
        hover "objects/object_door_71b.png"
        action Hide("church"), Play("audio", sfxDoor()), Jump("church_stairs_dialogue")