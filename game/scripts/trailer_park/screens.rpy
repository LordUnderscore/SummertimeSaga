screen trailer_park:
    add gTimer.image("backgrounds/location_trailer_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (787,320)
        idle gTimer.image("objects/object_door_85{}.png")
        hover gTimer.image("objects/object_door_85b{}.png")
        action Hide("trailer_park"), If(gTimer.is_dark, Function(playSound), NullAction()), Jump("trailer_interior_dialogue")

screen trailer_interior:
    add gTimer.image("backgrounds/location_trailer_interior{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,0)
        idle gTimer.image("objects/object_door_86{}.png")
        hover gTimer.image("objects/object_door_86b{}.png")
        action Hide("trailer_interior"), Jump("trailer_park_dialogue")

    imagebutton:
        focus_mask True
        pos (411,312)
        idle gTimer.image("objects/object_door_87{}.png")
        hover gTimer.image("objects/object_door_87b{}.png")
        action Hide("trailer_interior"), Function(playSound), Jump("trailer_bedroom_dialogue")

    if is_here("crystal"):
        imagebutton:
            focus_mask True
            pos (690,288)
            idle "objects/character_crystal_01.png"
            hover "objects/character_crystal_01b.png"
            action Hide("trailer_interior"), Jump("roxmom_dialogue")

screen trailer_bedroom:
    add gTimer.image("backgrounds/location_trailer_bedroom{}.jpg")

    imagebutton:
        focus_mask True
        pos (819,136)
        idle gTimer.image("objects/object_door_88{}.png")
        hover gTimer.image("objects/object_door_88b{}.png")
        action Hide("trailer_bedroom"), Jump("trailer_interior_dialogue")

    imagebutton:
        focus_mask True
        pos (0,558)
        idle gTimer.image("objects/object_bed_10{}.png")
        hover gTimer.image("objects/object_bed_10b{}.png")
        action Show("popup_unfinished")