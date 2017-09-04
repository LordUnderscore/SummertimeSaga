screen church_cloister_bell:
    add "backgrounds/location_church_bell.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/door11_option_01.png"
        hover "boxes/door11_option_01b.png"
        action Hide("church_cloister_bell"), Jump("church_stairs_dialogue")