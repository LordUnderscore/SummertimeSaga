screen garage:
    add gTimer.image("backgrounds/location_home_garage{}.jpg")

    imagebutton:
        focus_mask True
        pos (380,356)
        idle gTimer.image("objects/object_car_01{}.png")
        hover gTimer.image("objects/object_car_01b{}.png")
        action Hide("garage"), Jump("car_dialogue")

    imagebutton:
        focus_mask True
        pos (43,486)
        idle gTimer.image("objects/object_mower_01{}.png")
        hover gTimer.image("objects/object_mower_01b{}.png")
        action Hide("garage"), Jump("lawnmower_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("garage"), Jump("home_front")

    if not shovel_taken:
        imagebutton:
            focus_mask True
            pos (30,250)
            idle gTimer.image("objects/object_shovel_01{}.png")
            hover gTimer.image("objects/object_shovel_01b{}.png")
            action Function(inventory.get_item, item= shovel), SetVariable("shovel_taken", True), Hide("garage"), Jump("shovel")

    if not stool_taken:
        imagebutton:
            focus_mask True
            pos (257,250)
            idle gTimer.image("objects/object_stool_01{}.png")
            hover gTimer.image("objects/object_stool_01b{}.png")
            action Function(inventory.get_item, item= stool), SetVariable("stool_taken", True), Hide("garage"), Jump("stool")

screen car_engine:
    add gTimer.image("backgrounds/location_home_garage_car{}.jpg")

    imagebutton:
        focus_mask True
        pos (110,97)
        idle gTimer.image("objects/object_engine_01{}.png")
        hover gTimer.image("objects/object_engine_01b{}.png")
        action Hide("car_engine"), Jump("engine_broken_dialogue")

screen car_mom_jerk_options:
    imagebutton:
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("car_mom_jerk_options"), Jump("mom_car_jerk_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover "buttons/cam_stage01_02b.png"
        action Hide("car_mom_jerk_options"), Jump("car_mom_jerk_end")

screen car_mom_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        if M_mom.is_set("car jerk"):
            action Hide("car_mom_sex_options"), Jump("car_mom_jerk_loop")
        else:
            action Hide("car_mom_sex_options"), Jump("car_mom_bj_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        if M_mom.is_set("car jerk"):
            idle "buttons/cam_stage01_02.png"
            hover "buttons/cam_stage01_02b.png"
            action Hide("car_mom_sex_options"), Jump("car_mom_jerk_cum")
        else:
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Hide("car_mom_sex_options"), Jump("car_mom_bj_cum")

    if (M_mom.get("sex speed") < .225 and M_mom.is_set("car jerk")) or (M_mom.get("sex speed") < .175 and not M_mom.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            if M_mom.is_set("car jerk"):
                action Hide("car_mom_sex_options"), Jump("car_mom_slower_jerk")
            else:
                action Hide("car_mom_sex_options"), Jump("car_mom_slower_bj")

    if (M_mom.get("sex speed") > .126 and M_mom.is_set("car jerk")) or (M_mom.get("sex speed") > .076 and not M_mom.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            if M_mom.is_set("car jerk"):
                action Hide("car_mom_sex_options"), Jump("car_mom_faster_jerk")
            else:
                action Hide("car_mom_sex_options"), Jump("car_mom_faster_bj")