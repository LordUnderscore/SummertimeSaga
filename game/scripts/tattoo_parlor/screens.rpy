screen tattoo_parlor:
    add gTimer.image("backgrounds/location_tattoo{}.jpg")

    imagebutton:
        focus_mask True
        pos (419,357)
        idle gTimer.image("objects/object_door_89{}.png")
        hover gTimer.image("objects/object_door_89b{}.png")
        action Hide("tattoo_parlor"), If(gTimer.is_dark, Function(playSound), NullAction()), Jump("tattoo_parlor_interior_dialogue")

    imagebutton:
        focus_mask True
        pos (643,138)
        idle gTimer.image("objects/object_stairs_04{}.png")
        hover gTimer.image("objects/object_stairs_04b{}.png")
        action Show("popup_unfinished")

screen tattoo_parlor_interior:
    add gTimer.image("backgrounds/location_tattoo_indoor{}.jpg")

    imagebutton:
        focus_mask True
        pos (9,280)
        idle gTimer.image("objects/object_door_90{}.png")
        hover gTimer.image("objects/object_door_90b{}.png")
        action Hide("tattoo_parlor_interior"), Jump("tattoo_parlor_dialogue")

    if is_here("grace"):
        imagebutton:
            focus_mask True
            pos (905,342)
            idle "objects/character_grace_01.png"
            hover "objects/character_grace_01b.png"
            action Hide("tattoo_parlor_interior"), Jump("grace_dialogue")