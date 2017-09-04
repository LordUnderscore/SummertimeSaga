screen cafeteria:
    add "backgrounds/location_cafetaria.jpg"

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover "boxes/door07_option_01b.png"
        action Hide("cafeteria"), Jump("stairs_dialogue")