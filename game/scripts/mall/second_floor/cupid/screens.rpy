screen cupid:
    add "backgrounds/location_mall_cupid.jpg"

    imagebutton:
        focus_mask True
        pos (685,232)
        idle "objects/object_door_104.png"
        hover "objects/object_door_104b.png"
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_choose_gift, S_mom_show_necklace],
                                Jump("mom_cupid_outing_block"),
                                [Function(playSound), Jump("cupid_dressroom")]
        )

    imagebutton:
        focus_mask True
        pos (167,328)
        idle "objects/character_kass_01.png"
        hover "objects/character_kass_01b.png"
        action Hide("cupid"), Jump("kass_dialogue")

    if is_here("mom"):
        imagebutton:
            focus_mask True
            pos (580,320)
            idle "objects/character_mom_08.png"
            hover "objects/character_mom_08b.png"
            action Hide("cupid"), Jump("mom_cupid_outing")

    imagebutton:
        focus_mask True
        pos (463,280)
        idle "objects/object_jewelery_01.png"
        hover "objects/object_jewelery_01b.png"
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_show_necklace, S_mom_dressing_room],
                                Jump("mom_cupid_outing_block"),
                                Jump("necklace_display")
        )

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_choose_gift, S_mom_show_necklace, S_mom_dressing_room],
                                Jump("mom_cupid_outing_block"),
                                Jump("mall_second_floor")
        )

screen cupid_necklace_display:
    add "backgrounds/location_mall_cupid_closeup_stall.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("cupid_dressroom"), Jump("cupid_dialogue")

screen cupid_dressroom:
    add "backgrounds/location_mall_cupid_closeup_stall.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("cupid_dressroom"), Jump("cupid_dialogue")