screen warehouse:
    add gTimer.image("Backgrounds/location_warehouse{}.jpg")

    imagebutton:
        focus_mask True
        pos (341,486)
        idle gTimer.image("objects/object_door_108{}.png")
        hover gTimer.image("objects/object_door_108b{}.png")
        action Show("popup_unfinished")