screen boys_lockerroom:

    if not gTimer.is_dark():
        if roxxy.started(roxxy_shower):
            add "backgrounds/location_locker_room_empty.jpg"
        else:
            add "backgrounds/location_locker_room.jpg"
    else:
        add "backgrounds/location_locker_room_night.jpg"

    if roxxy.started(roxxy_shower):
        if not gTimer.is_dark():
            imagebutton:
                focus_mask True
                pos (25,274)
                idle "images/objects/object_door_17_girls.png"
                hover "images/objects/object_door_17b_girls.png"
                action Hide("boys_lockerroom"), Jump("roxxy_shower_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (25,274)
            idle gTimer.image("objects/object_door_17{}.png")
            hover gTimer.image("objects/object_door_17b{}.png")
            if not gTimer.is_dark():
                action If(
                    shower_door_count == 0,
                    [Hide("boys_lockerroom"), Jump("door17_locked_dialogue")],
                    [Hide("boys_lockerroom"), Jump("lockershowers_dialogue")]
                )
            else:
                action Hide("boys_lockerroom"), Jump("denied_access_locker")

    if gTimer.is_evening() and quest11 in quest_list and not webcam_planted:
        imagebutton:
            focus_mask True
            pos (520,160)
            idle "objects/object_airvent_01.png"
            hover "objects/object_airvent_01b.png"
            action Hide("boys_lockerroom"), Jump("airvent_webcam_quest")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover "boxes/auto_option_02b.png"
        action Hide("boys_lockerroom"), Jump("left_hall_dialogue")

screen boys_locker_shower:
    add "backgrounds/location_lockershowers.jpg"

    if gTimer.gameDay() >= 1:
        imagebutton:
            focus_mask True
            pos (530,300)
            idle "objects/character_latinas_01.png"
            hover "objects/character_latinas_01b.png"
            action Hide("boys_locker_shower"), Jump("latinas_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover "boxes/auto_option_02b.png"
        action Hide("boys_locker_shower"), Jump("locker_room_dialogue")