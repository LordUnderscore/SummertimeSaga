screen hospital_2nd_floor:
    add gTimer.image("backgrounds/location_hospital_second{}.jpg")

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover "objects/object_elevator_01b.png"
        action Hide("hospital_2nd_floor"), Jump("elevator_dialogue")

    imagebutton:
        focus_mask True
        pos (50,168)
        idle "objects/object_door_77.png"
        hover "objects/object_door_77b.png"
        action Hide("hospital_2nd_floor"), Jump("hospital_second_floor_room_dialogue")

    imagebutton:
        focus_mask True
        pos (260,405)
        idle "objects/object_phone_01.png"
        hover "objects/object_phone_01b.png"
        action Hide("hospital_2nd_floor"), Jump("hospital_second_floor_phone_dialogue")

    imagebutton:
        focus_mask True
        pos (843,168)
        idle "objects/object_door_78.png"
        hover "objects/object_door_78b.png"
        action Hide("hospital_2nd_floor"), Jump("hospital_storage_room_dialogue")