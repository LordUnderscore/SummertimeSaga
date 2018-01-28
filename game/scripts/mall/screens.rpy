screen mall:
    add "backgrounds/location_mall.jpg"

    imagebutton:
        focus_mask True
        pos (612,364)
        idle "objects/object_stairs_06.png"
        hover "objects/object_stairs_06b.png"
        action Hide("mall"), Jump("mall_second_floor")

    imagebutton:
        focus_mask True
        pos (761,234)
        idle "objects/object_door_22.png"
        hover "objects/object_door_22b.png"
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("consumr")]
        )

    imagebutton:
        focus_mask True
        pos (42,156)
        idle "objects/object_door_23.png"
        hover "objects/object_door_23b.png"
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("movie_theatre_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (541,321)
        idle "objects/object_door_53.png"
        hover "objects/object_door_53b.png"
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("comic_store_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (285,317)
        idle "objects/object_door_52.png"
        hover "objects/object_door_52b.png"
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("mall_toilets")]
        )

    if gTimer.is_weekend():
        imagebutton:
            focus_mask True
            pos (354,308)
            idle "objects/object_podium_01.png"
            hover "objects/object_podium_01b.png"
            action Hide("mall"), Jump("rump_dialogue")