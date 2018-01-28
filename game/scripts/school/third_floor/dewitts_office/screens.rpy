screen mrs_dewitts_office:
    add gTimer.image("backgrounds/location_school_office2{}.jpg")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover "boxes/auto_option_generic_02b.png"
        action Hide("mrs_dewitts_office"), Jump("third_floor_dialogue")