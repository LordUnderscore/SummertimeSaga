screen mall_second_floor:
    add "backgrounds/location_mall_upstairs.jpg"

    imagebutton:
        focus_mask True
        pos (358,236)
        idle "objects/object_door_21.png"
        hover "objects/object_door_21b.png"
        action Hide("mall_second_floor"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("pink_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (45,164)
        idle "objects/object_door_103.png"
        hover "objects/object_door_103b.png"
        action Hide("mall_second_floor"), Function(playSound), Jump("cupid_dialogue")

    imagebutton:
        focus_mask True
        pos (-2,527)
        idle "objects/object_stairs_07.png"
        hover "objects/object_stairs_07b.png"
        action Hide("mall_second_floor"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("mall_dialogue")]
        )