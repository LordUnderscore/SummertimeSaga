screen church_stairs:
    add gTimer.image("backgrounds/location_church_stairs{}.jpg")

    imagebutton:
        focus_mask True
        pos (775,503)
        idle gTimer.image("objects/object_door_72{}.png")
        hover gTimer.image("objects/object_door_72b{}.png")
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_dialogue")

    imagebutton:
        focus_mask True
        pos (18,235)
        idle gTimer.image("objects/object_door_73{}.png")
        hover gTimer.image("objects/object_door_73b{}.png")
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_angelicas_room_dialogue")

    imagebutton:
        focus_mask True
        pos (315,210)
        idle gTimer.image("objects/object_door_74{}.png")
        hover gTimer.image("objects/object_door_74b{}.png")
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_bell_dialogue")