screen library_front:
    add gTimer.image("backgrounds/location_library_front{}.jpg")

    imagebutton:
        focus_mask True
        pos (364,486)
        idle gTimer.image("objects/object_door_105{}.png")
        hover gTimer.image("objects/object_door_105b{}.png")
        action Hide("library_front"), Function(playSound), Jump("library_dialogue")