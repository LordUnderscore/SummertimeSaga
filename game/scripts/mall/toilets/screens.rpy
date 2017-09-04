screen mall_toilets:
    if rump_n_cunt in magic_numbers:
        add "backgrounds/location_mall_washroom_event.jpg"

    else:
        add "backgrounds/location_mall_washroom.jpg"

    imagebutton:
        focus_mask True
        pos (184,189)
        idle "objects/object_door_54.png"
        hover "objects/object_door_54b.png"
        action Hide("mall_toilets"), If(rump_n_cunt in magic_numbers, Jump("rump_toilets_stall"), Jump("mall_toilets_stall"))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_10.png"
        hover "boxes/auto_option_10b.png"
        action Hide("mall_toilets"), Jump("mall_dialogue")