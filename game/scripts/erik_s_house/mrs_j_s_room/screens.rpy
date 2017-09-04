screen mrs_johnsons_room:
    add gTimer.image("backgrounds/location_erik_house_upstairs{}.jpg")

    imagebutton:
        focus_mask True
        pos (696,498)
        idle gTimer.image("objects/object_ball_01{}.png")
        hover gTimer.image("objects/object_ball_01b{}.png")
        action Hide("mrs_johnsons_room"), Jump("mrsj_ball")

    if is_here("mrsj"):
        if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            imagebutton:
                focus_mask True
                pos (826,300)
                idle "objects/character_erikmom_03.png"
                hover "objects/character_erikmom_03b.png"
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        elif gTimer.is_dark() and erik.over(erik_gf):
            imagebutton:
                focus_mask True
                pos (250,420)
                idle "objects/character_erikmom_04.png"
                hover "objects/character_erikmom_04b.png"
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (0,410)
                idle gTimer.image("objects/object_bed_04_day{}.png")
                hover gTimer.image("objects/object_bed_04b_day{}.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("mrs_johnsons_room"), Jump("erik_indoors")