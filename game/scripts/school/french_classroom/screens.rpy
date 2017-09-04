screen board_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("board_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/board_option_01.png"
        hover "boxes/board_option_01b.png"
        action If(
            not gTimer.is_dark(),
            [Hide("board_options"), Hide("french_classroom"), Jump("class_study01")],
            NullAction()
        )

screen french_classroom:
    add "backgrounds/location_classroom.jpg"

    imagebutton:
        focus_mask True
        pos (384,276)
        idle "objects/object_door_07.png"
        hover "objects/object_door_07b.png"
        action Hide("french_classroom"), Play("audio", sfxDoor()), Jump("school_dialogue")

    imagebutton:
        focus_mask True
        pos (833,316)
        idle "objects/object_board_01.png"
        hover "objects/object_board_01b.png"
        action Show("board_options")

    imagebutton:
        focus_mask True
        pos (747,342)
        idle "objects/character_bissette_01.png"
        hover "objects/character_bissette_01b.png"
        action Hide("french_classroom"), Jump("teacher_button_dialogue")