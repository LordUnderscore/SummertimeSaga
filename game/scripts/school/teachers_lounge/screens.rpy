screen teachers_lounge:
    add gTimer.image("backgrounds/location_school_lounge{}.jpg")

    imagebutton:
        focus_mask True
        pos (61,208)
        idle gTimer.image("objects/object_door_102{}.png")
        hover gTimer.image("objects/object_door_102b{}.png")
        action Hide("teachers_lounge"), Jump("stairs_dialogue")