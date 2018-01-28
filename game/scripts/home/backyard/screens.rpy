screen backyard:
    add gTimer.image("backgrounds/location_home_backyard{}.jpg")

    imagebutton:
        focus_mask True
        pos (544,365)
        idle gTimer.image("objects/object_door_65{}.png")
        hover gTimer.image("objects/object_door_65b{}.png")
        action Hide("backyard"), Jump("dining_room_dialogue")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (52,537)
            idle "objects/object_chair_02.png"
            hover "objects/object_chair_02b.png"
            action Show("popup_unfinished")

    if is_here("mom"):
        imagebutton:
            focus_mask True
            pos (470,418)
            idle "objects/character_mom_07.png"
            hover "objects/character_mom_07b.png"
            action Hide("backyard"), Jump("mom_pool_dialogue")

screen mom_finger_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("mom_finger_options"), Jump("mom_finger_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover "buttons/cam_stage01_02b.png"
        action Hide("mom_finger_options"), Jump("mom_finger_cum")

    if M_mom.get("sex speed") < .225:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Hide("mom_finger_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("mom_finger_loop")

    if M_mom.get("sex speed") > 0.126:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Hide("mom_finger_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.025), Jump("mom_finger_loop")