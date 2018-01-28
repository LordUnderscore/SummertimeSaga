screen school_right_hallway:

    add gTimer.image("backgrounds/location_school_second{}.jpg")

    imagebutton:
        focus_mask True
        pos (134,327)
        idle gTimer.image("objects/object_sign_03{}.png")
        hover gTimer.image("objects/object_sign_03b{}.png")
        action [Hide("school_right_hallway"),
                If(
                    quest09_1 or quest09_2,
                    Jump("quest09_1"),
                    Jump("school_dialogue")
                )
        ]

    imagebutton:
        focus_mask True
        pos (16,420)
        idle gTimer.image("objects/object_door_11{}.png")
        hover gTimer.image("objects/object_door_11b{}.png")
        action Hide("school_right_hallway"), Jump("third_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (610,366)
        idle "objects/object_door_12.png"
        hover "objects/object_door_12b.png"
        action Hide("school_right_hallway"), Function(playSound), Jump("cafeteria_dialogue")

    imagebutton:
        focus_mask True
        pos (471,332)
        idle gTimer.image("objects/object_door_75{}.png")
        hover gTimer.image("objects/object_door_75b{}.png")
        action Hide("school_right_hallway"), Function(playSound), Play("audio", sfxDoor()), Jump("computer_lab_dialogue")

    imagebutton:
        focus_mask True
        pos (864,408)
        idle gTimer.image("objects/object_door_97{}.png")
        hover gTimer.image("objects/object_door_97b{}.png")
        action Hide("school_right_hallway"), Function(playSound), Play("audio", sfxDoor()), Jump("teach_lounge_dialogue")

    if quest09 not in quest_list or quest09 in completed_quests:
        imagebutton:
            focus_mask True
            pos (320,370)
            idle "objects/character_annie_01.png"
            hover "objects/character_annie_01b.png"
            action Hide("school_right_hallway"), Jump("annie_button_dialogue")