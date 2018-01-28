screen mrs_okitas_office:
    add gTimer.image("backgrounds/location_school_office4{}.jpg")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover "boxes/auto_option_generic_02b.png"
        action Hide("mrs_okitas_office"), Jump("third_floor_dialogue")