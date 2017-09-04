screen eriks_room:
    add gTimer.image("backgrounds/location_erik_house_bedroom{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,556)
        idle "objects/object_bed_08.png"
        hover "objects/object_bed_08b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (559,361)
        idle gTimer.image("objects/object_desk_08{}.png")
        hover gTimer.image("objects/object_desk_08b{}.png")
        action Show("popup_unfinished")

    if is_here("erik"):
        if erik.started(erik_card_hunt):
            imagebutton:
                focus_mask True
                pos (229,498)
                idle gTimer.image("objects/character_erik_02{}.png")
                hover gTimer.image("objects/character_erik_02b{}.png")
                action Hide("eriks_room"), Jump("erik_button_dialogue")

        elif is_here("june"):
            imagebutton:
                focus_mask True
                pos (0,309)
                idle "objects/object_bed_08_june.png"
                hover "objects/object_bed_08b_june.png"
                action Hide("eriks_room"), Jump("erik_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (559,358)
                idle gTimer.image("objects/object_desk_08_erik{}.png")
                hover gTimer.image("objects/object_desk_08b_erik{}.png")
                action Hide("eriks_room"), Jump("erik_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("eriks_room"), Jump("erik_indoors")