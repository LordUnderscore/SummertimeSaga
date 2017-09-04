screen mall:
    add "backgrounds/location_mall.jpg"

    imagebutton:
        focus_mask True
        pos (600,281)
        idle "objects/object_door_21.png"
        hover "objects/object_door_21b.png"
        action Hide("mall"), Function(playSound), Jump("pink_dialogue")

    imagebutton:
        focus_mask True
        pos (761,234)
        idle "objects/object_door_22.png"
        hover "objects/object_door_22b.png"
        action Hide("mall"), Hide("ui"), Function(playSound), Jump("consumr")

    imagebutton:
        focus_mask True
        pos (42,156)
        idle "objects/object_door_23.png"
        hover "objects/object_door_23b.png"
        action Hide("mall"), Function(playSound), Jump("movie_theatre_dialogue")

    imagebutton:
        focus_mask True
        pos (541,321)
        idle "objects/object_door_53.png"
        hover "objects/object_door_53b.png"
        action Hide("mall"), Function(playSound), Jump("comic_store_dialogue")

    imagebutton:
        focus_mask True
        pos (285,317)
        idle "objects/object_door_52.png"
        hover "objects/object_door_52b.png"
        action Hide("mall"), Function(playSound), Jump("mall_toilets")

    if gTimer.is_weekend():
        imagebutton:
            focus_mask True
            pos (354,308)
            idle "objects/object_podium_01.png"
            hover "objects/object_podium_01b.png"
            action Hide("mall"), Jump("rump_dialogue")