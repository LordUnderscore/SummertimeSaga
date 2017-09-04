screen dining_room:
    add gTimer.image("backgrounds/location_home_diningroom{}.jpg")

    if gTimer.is_morning() and sister.known(sis_breakfast) and not sister.over(sis_breakfast):
        imagebutton:
            focus_mask True
            pos (158,439)
            idle "images/objects/object_table_02_sis.png"
            hover "images/objects/object_table_02b_sis.png"
            action Hide("dining_room"), Jump("dining_room_table_sis")

    else:
        imagebutton:
            focus_mask True
            pos (158,484)
            idle gTimer.image("objects/object_table_02{}.png")
            hover gTimer.image("objects/object_table_02b{}.png")
            action Hide("dining_room"), Jump("dining_room_table_dialogue")

    imagebutton:
        focus_mask True
        pos (952,288)
        idle gTimer.image("objects/object_door_45{}.png")
        hover gTimer.image("objects/object_door_45b{}.png")
        action Hide("dining_room"), Jump("home_kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (27,293)
        idle gTimer.image("objects/object_door_46{}.png")
        hover gTimer.image("objects/object_door_46b{}.png")
        action Hide("dining_room"), Jump("backyard_dialogue")