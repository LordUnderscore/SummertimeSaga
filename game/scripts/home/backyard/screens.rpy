screen backyard:
    add gTimer.image("backgrounds/location_home_backyard{}.jpg")

    imagebutton:
        focus_mask True
        pos (544,365)
        idle gTimer.image("images/objects/object_door_65{}.png")
        hover gTimer.image("images/objects/object_door_65b{}.png")
        action Hide("backyard"), Jump("dining_room_dialogue")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (52,537)
            idle "images/objects/object_chair_02.png"
            hover "images/objects/object_chair_02b.png"
            action Show("popup_unfinished")