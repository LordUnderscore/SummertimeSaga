screen harolds_house_office:
    add gTimer.image("backgrounds/location_mia_house_office{}.jpg")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("harolds_house_office"), Jump("mias_upstairs")