screen art_classroom:
    add gTimer.image("backgrounds/location_school_art{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (431,277)
            idle "objects/object_door_60.png"
            hover "objects/object_door_60b.png"
            action Hide("art_classroom"), Play("audio", sfxDoor()), Jump("left_hall_dialogue")

        if M_mia.get_state() in [S_mia_draw_tattoo, S_mia_show_tattoo]:
            imagebutton:
                focus_mask True
                pos (833,277)
                idle "objects/object_painting_02.png"
                hover "objects/object_painting_02b.png"
                action Hide("art_classroom"), Jump("easel_dialogue")

        imagebutton:
            focus_mask True
            pos (249,367)
            idle "objects/object_fruits_01.png"
            hover "objects/object_fruits_01b.png"
            action Show("popup_unfinished")

        imagebutton:
            focus_mask True
            pos (135,315)
            idle "objects/character_ross_01.png"
            hover "objects/character_ross_01b.png"
            action Hide("art_classroom"), Jump("ross_button_dialogue")

screen tattoos:
    imagebutton:
        focus_mask True
        pos (88,113)
        idle "buttons/tattoo_drawing_01.png"
        hover "buttons/tattoo_drawing_01b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_butterfly"), Return()

    imagebutton:
        focus_mask True
        pos (399,135)
        idle "buttons/tattoo_drawing_02.png"
        hover "buttons/tattoo_drawing_02b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_dolphin"), Return()

    imagebutton:
        focus_mask True
        pos (675,113)
        idle "buttons/tattoo_drawing_03.png"
        hover "buttons/tattoo_drawing_03b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_stars"), Return()

    imagebutton:
        focus_mask True
        pos (98,415)
        idle "buttons/tattoo_drawing_04.png"
        hover "buttons/tattoo_drawing_04b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_flowers"), Return()

    imagebutton:
        focus_mask True
        pos (411,411)
        idle "buttons/tattoo_drawing_05.png"
        hover "buttons/tattoo_drawing_05b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_skull"), Return()

    imagebutton:
        focus_mask True
        pos (702,447)
        idle "buttons/tattoo_drawing_06.png"
        hover "buttons/tattoo_drawing_06b.png"
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_cookie"), Return()