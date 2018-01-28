screen dianes_front_yard:
    add gTimer.image("backgrounds/location_diane_front{}.jpg")

    imagebutton:
        focus_mask True
        pos (289,382)
        idle gTimer.image("objects/object_door_106{}.png")
        hover gTimer.image("objects/object_door_106b{}.png")
        action Hide("dianes_front_yard"), If(
                                             gTimer.is_dark(),
                                             Jump("diane_front_yard_night_locked"),
                                             If(
                                                not aunt.known(aunt_mouse_attack),
                                                Jump("dianelobby_locked"),
                                                [Function(playSound), Jump("dianelobby_dialogue")]
                                             )
        )

    imagebutton:
        focus_mask True
        pos (563,482)
        idle gTimer.image("objects/object_door_107{}.png")
        hover gTimer.image("objects/object_door_107b{}.png")
        action Hide("dianes_front_yard"), Jump("garden_dialogue")