screen art_classroom:
    add gTimer.image("backgrounds/location_school_art{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (431,277)
            idle "objects/object_door_60.png"
            hover "objects/object_door_60b.png"
            action Hide("art_classroom"), Play("audio", sfxDoor()), Jump("left_hall_dialogue")

        imagebutton:
            focus_mask True
            pos (833,277)
            idle "objects/object_painting_02.png"
            hover "objects/object_painting_02b.png"
            action Show("popup_unfinished")

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