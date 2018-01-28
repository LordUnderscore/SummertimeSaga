screen school_hall:
    add gTimer.image("backgrounds/location_school{}.jpg")

    imagebutton:
        focus_mask True
        pos (434,449)
        idle gTimer.image("objects/object_door_05{}.png")
        hover gTimer.image("objects/object_door_05b{}.png")
        if not gTimer.is_dark():
            action If(
                courtyard_door_count == 0,
                [Hide("school_hall"), Jump("door05_locked_dialogue")],
                [Hide("school_hall"), Function(playSound), Jump("gym_dialogue")]
            )
        else:
            action Hide("school_hall"), Jump("denied_access_mainhall")

    imagebutton:
        focus_mask True
        pos (615,407)
        idle gTimer.image("objects/object_door_62{}.png")
        hover gTimer.image("objects/object_door_62b{}.png")
        if not gTimer.is_dark():
            action If(
                classroom_door_count == 0,
                [Hide("school_hall"), Jump("door06_locked_dialogue")],
                If(
                    classroom_door_count == 1,
                    [Hide("school_hall"), Jump("door06_locked2_dialogue")],
                    [Hide("school_hall"), Function(playSound), Play("audio", sfxDoor()), Jump("music_classroom_dialogue")]
                )
            )
        else:
            action Hide("school_hall"), Play("audio", sfxDoor(True)), Jump("denied_access_mainhall")

    imagebutton:
        focus_mask True
        pos (362,411)
        idle gTimer.image("objects/object_door_63{}.png")
        hover gTimer.image("objects/object_door_63b{}.png")
        if not gTimer.is_dark():
            action If(
                classroom_door_count == 0,
                [Hide("school_hall"), Jump("door06_locked_dialogue")],
                If(
                    classroom_door_count == 1,
                    [Hide("school_hall"), Jump("door06_locked2_dialogue")],
                    [Hide("school_hall"), Function(playSound), Play("audio", sfxDoor()), Jump("science_classroom_dialogue")]
                )
            )
        else:
            action Hide("school_hall"), Play("audio", sfxDoor(True)), Jump("denied_access_mainhall")

    imagebutton:
        focus_mask True
        pos (857,125)
        idle gTimer.image("objects/object_door_06{}.png")
        hover gTimer.image("objects/object_door_06b{}.png")
        if not gTimer.is_dark():
            action If(
                player.known(intense_gymercise) and not roxxy.completed(roxxy_shower),
                [Hide("school_hall"), Jump("door05_locked4_dialogue")],
                If(
                    classroom_door_count == 0,
                    [Hide("school_hall"), Jump("door06_locked_dialogue")],
                    If(classroom_door_count == 1,
                       [Hide("school_hall"), Jump("door06_locked2_dialogue")],
                       [Hide("school_hall"), Function(playSound), Play("audio", sfxDoor()), Jump("classroom_dialogue")]
                    )
                )
            )
        else:
            action Hide("school_hall"), Play("audio", sfxDoor(True)), Jump("denied_access_mainhall")

    imagebutton:
        focus_mask True
        pos (222,225)
        idle gTimer.image("objects/object_sign_01{}.png")
        hover gTimer.image("objects/object_sign_01b{}.png")
        action If(
            left_hall_count == 0,
            [Hide("school_hall"), Jump("left_hall_dialogue")],
            If(
                left_hall_count == 1,
                [Hide("school_hall"), Jump("door05_locked2_dialogue")],
                If(
                    left_hall_count == 2,
                    [Hide("school_hall"), Jump("door05_locked3_dialogue")],
                    [Hide("school_hall"), Jump("left_hall_dialogue")]
                )
            )
        )

    imagebutton:
        focus_mask True
        pos (694,225)
        idle gTimer.image("objects/object_sign_02{}.png")
        hover gTimer.image("objects/object_sign_02b{}.png")
        if not gTimer.is_dark():
            action If(
                player.known(intense_gymercise) and not roxxy.completed(roxxy_shower),
                [Hide("school_hall"), Jump("door05_locked4_dialogue")],
                If(
                    stairs_count == 0,
                    [Hide("school_hall"), Jump("door05_locked_dialogue")],
                    If(
                        stairs_count == 1,
                        [Hide("school_hall"), Jump("door05_locked2_dialogue")],
                        If(
                            stairs_count == 2,
                            [Hide("school_hall"), Jump("door05_locked3_dialogue")],
                            [Hide("school_hall"), Jump("stairs_dialogue")]
                        )
                    )
                )
            )
        else:
            action Hide("school_hall"), Jump("denied_access_mainhall")

    if not gTimer.is_dark():
        if not player.known(intense_gymercise) or roxxy.over(roxxy_shower):
            imagebutton:
                focus_mask True
                pos (660,335)
                idle "objects/character_roxxy_01.png"
                hover "objects/character_roxxy_01b.png"
                action Hide("school_hall"), Jump("roxxy_button_dialogue")

    imagebutton:
        focus_mask True
        pos (36,235)
        idle gTimer.image("objects/object_locker_01{}.png")
        hover gTimer.image("objects/object_locker_01b{}.png")
        action Hide("school_hall"), Jump("school_locker")

screen school_locker:
    add "backgrounds/location_school_locker_mc.jpg"

    imagebutton:
        focus_mask True
        pos (562,57)
        idle "objects/object_paper_01.png"
        hover "objects/object_paper_01b.png"
        action Show("school_locker_list")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover "boxes/auto_option_generic_02b.png"
        action Hide("school_locker"), Jump("school_dialogue")

screen school_locker_list:
    default mark_list = []
    imagebutton:
        focus_mask True
        pos (0,0)
        idle "backgrounds/location_school_locker_list.jpg"
        action Hide("school_locker_list")

    python:
        import math

        i = 0
        while i < (math.floor(M_mia.get("progress count") / M_mia.get("progress mark"))):
            mark_list.append(i)
            i += 1

    $ i = 0
    for i in mark_list:
        add "buttons/locker_list_02.png" pos (453 + (35 * i)),247
        $ i += 1

    if M_mia.get("progress count") == (M_mia.get("progress mark") * 8) or M_helen.get_state() != S_helen_start:
        add "buttons/locker_list_01.png" pos 750,210