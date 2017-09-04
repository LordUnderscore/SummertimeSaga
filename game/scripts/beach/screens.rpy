screen beach:
    add gTimer.image("backgrounds/location_beach{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (666,569)
            idle "objects/object_island_01.png"
            hover "objects/object_island_01b.png"
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (187,495)
        idle gTimer.image("objects/object_stall_01{}.png")
        hover gTimer.image("objects/object_stall_01b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (444,318)
        idle gTimer.image("objects/object_tower_01{}.png")
        hover gTimer.image("objects/object_tower_01b{}.png")
        action Show("popup_unfinished")