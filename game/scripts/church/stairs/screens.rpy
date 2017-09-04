screen church_stairs:
    add "backgrounds/location_church_stairs.jpg"

    imagebutton:
        focus_mask True
        pos (775,503)
        idle "objects/object_door_72.png"
        hover "objects/object_door_72b.png"
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_dialogue")

    imagebutton:
        focus_mask True
        pos (18,235)
        idle "objects/object_door_73.png"
        hover "objects/object_door_73b.png"
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_angelicas_room_dialogue")

    imagebutton:
        focus_mask True
        pos (315,210)
        idle "objects/object_door_74.png"
        hover "objects/object_door_74b.png"
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_bell_dialogue")