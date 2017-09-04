screen school_left_hallway:
    add gTimer.image("backgrounds/location_lefthall{}.jpg")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (757,297)
            idle "objects/object_door_14.png"
            hover "objects/object_door_14b.png"
            action If(
                wearing_jersey_count == 1,
                [Hide("school_left_hallway"), Play("audio", sfxDoor(True)), Jump("door14_locked_dialogue")],
                [Hide("school_left_hallway"), Jump("door14b_locked_dialogue")]
            )

        if roxxy_shower_lock:
            imagebutton:
                focus_mask True
                pos (661,281)
                idle "objects/object_door_15.png"
                hover "objects/object_door_15b.png"
                action Hide("school_left_hallway"), Function(playSound), Jump("denied_locker_room_dialogue")
        else:
            imagebutton:
                focus_mask True
                pos (661,281)
                idle "objects/object_door_15.png"
                hover "objects/object_door_15b.png"
                action Hide("school_left_hallway"), Function(playSound), Jump("locker_room_dialogue")

        imagebutton:
            focus_mask True
            pos (872,172)
            idle "objects/object_door_64.png"
            hover "objects/object_door_64b.png"
            action If(
                classroom_door_count == 0,
                [Hide("school_left_hallway"), Jump("door64_locked_dialogue")],
                If(classroom_door_count == 1,
                   [Hide("school_left_hallway"), Jump("door64_locked2_dialogue")],
                   [Hide("school_left_hallway"), Function(playSound), Play("audio", sfxDoor()), Jump("art_classroom_dialogue")]
                )
            )

        imagebutton:
            focus_mask True
            pos (195,281)
            idle "objects/object_door_16.png"
            hover "objects/object_door_16b.png"
            action If(
                player.known(intense_gymercise) and not roxxy.completed(roxxy_shower),
                [Hide("school_left_hallway"), Jump("door16c_locked_dialogue")],
                If(
                    wearing_jersey_count == 1,
                    If(
                        girl_lockerroom_unlocked,
                        [Hide("school_left_hallway"), Function(playSound),Jump("girl_lockerroom_dialogue")],
                        [Hide("school_left_hallway"), Jump("door16_locked_dialogue")]
                    ),
                    [Hide("school_left_hallway"), Jump("door16b_locked_dialogue")]
                )
            )

        if left_hall_dialogue_count > 0:
            if not judith_in_toilet:
                imagebutton:
                    focus_mask True
                    pos (490,370)
                    idle "objects/character_judith_01.png"
                    hover "objects/character_judith_01b.png"
                    action Hide("school_left_hallway"), Jump("judith_button_dialogue")
    else:
        imagebutton:
            focus_mask True
            pos (757,297)
            idle "objects/object_door_14_night.png"
            hover "objects/object_door_14b_night.png"
            action Hide("school_left_hallway"), Jump("denied_access_utility")

        imagebutton:
            focus_mask True
            pos (661,281)
            idle "objects/object_door_15_night.png"
            hover "objects/object_door_15b_night.png"
            action Hide("school_left_hallway"), Function(playSound), Jump("locker_room_dialogue")

        imagebutton:
            focus_mask True
            pos (872,172)
            idle "objects/object_door_64_night.png"
            hover "objects/object_door_64b_night.png"
            action Hide("school_left_hallway"), Play("audio", sfxDoor(True)), Jump("denied_access_lefthall")

        imagebutton:
            focus_mask True
            pos (195,281)
            idle "objects/object_door_16_night.png"
            hover "objects/object_door_16b_night.png"
            action Hide("school_left_hallway"), Jump("denied_access_lefthall")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover "boxes/door07_option_01b.png"
        action Hide("school_left_hallway"), Jump("school_dialogue")