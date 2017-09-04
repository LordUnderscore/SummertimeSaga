screen angelicas_room:
    add "backgrounds/location_church_nun.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/door11_option_01.png"
        hover "boxes/door11_option_01b.png"
        action Hide("angelicas_room"), Jump("church_stairs_dialogue")