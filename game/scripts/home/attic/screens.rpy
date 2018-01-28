screen attic:
    add gTimer.image("backgrounds/location_home_attic{}.jpg")

    imagebutton:
        focus_mask True
        pos (214,640)
        idle gTimer.image("objects/object_door_41{}.png")
        hover gTimer.image("objects/object_door_41b{}.png")
        action Hide("attic"), Jump("hallway_dialogue")

    if not fishing_rod_taken:
        imagebutton:
            focus_mask True
            pos (220,365)
            idle gTimer.image("objects/object_rod_01{}.png")
            hover gTimer.image("objects/object_rod_01b{}.png")
            action Function(inventory.get_item, item = fishing_rod), SetVariable("fishing_rod_taken", True), Hide("attic"), Jump("fishing_rod")

    if not ring_taken:
        imagebutton:
            focus_mask True
            pos (262,198)
            idle gTimer.image("objects/object_ring_01{}.png")
            hover gTimer.image("objects/object_ring_01b{}.png")
            action Function(inventory.get_item, item = ring), SetVariable("ring_taken", True), Hide("attic"), Jump("ring")

    imagebutton:
        focus_mask True
        pos (287,500)
        idle gTimer.image("objects/object_safe_01{}.png")
        hover gTimer.image("objects/object_safe_01b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (450,390)
        idle gTimer.image("objects/object_dress_01{}.png")
        hover gTimer.image("objects/object_dress_01b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (807,398)
        idle gTimer.image("objects/object_globe_01{}.png")
        hover gTimer.image("objects/object_globe_01b{}.png")
        action Hide("attic"), With(fade), Jump("globe")

    imagebutton:
        focus_mask True
        pos (703,602)
        idle gTimer.image("objects/object_picture_01{}.png")
        hover gTimer.image("objects/object_picture_01b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (888,289)
        idle gTimer.image("objects/object_painting_01{}.png")
        hover gTimer.image("objects/object_painting_01b{}.png")
        action Hide("attic"), With(fade), Jump("painting")

    imagebutton:
        focus_mask True
        pos (178,548)
        idle gTimer.image("objects/object_discs_01{}.png")
        hover gTimer.image("objects/object_discs_01b{}.png")
        action Show("popup_unfinished")

    if not cheerleader_outfit_taken:
        imagebutton:
            focus_mask True
            pos (345,375)
            idle gTimer.image("objects/object_outfit_01{}.png")
            hover gTimer.image("objects/object_outfit_01b{}.png")
            action Function(inventory.get_item, item = cheerleader_outfit), SetVariable("cheerleader_outfit_taken", True), Hide("attic"), Jump("cheerleader_outfit")