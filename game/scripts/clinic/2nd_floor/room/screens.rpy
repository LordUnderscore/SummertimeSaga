screen hospital_2nd_floor_room:
    add gTimer.image("backgrounds/location_hospital_room{}.jpg")

    imagebutton:
        focus_mask True
        pos (69,274)
        idle "objects/object_door_79.png"
        hover "objects/object_door_79b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (433,428)
        idle "objects/object_bed_09.png"
        hover "objects/object_bed_09b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("hospital_2nd_floor_room"), Jump("hospital_second_floor_dialogue")