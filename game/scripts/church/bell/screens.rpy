screen church_cloister_bell:
    add gTimer.image("backgrounds/location_church_bell{}.jpg")

    if M_aqua.is_set("bell search"):
        imagebutton:
            focus_mask True
            pos (322,51)
            idle gTimer.image("objects/object_bell_01{}.png")
            hover gTimer.image("objects/object_bell_01b{}.png")
            action Hide("church_cloister_bell"), Jump("church_bell")

    imagebutton:
        focus_mask True
        pos (0,305)
        idle gTimer.image("objects/object_door_96{}.png")
        hover gTimer.image("objects/object_door_96b{}.png")
        action Hide("church_cloister_bell"), Jump("church_stairs_dialogue")