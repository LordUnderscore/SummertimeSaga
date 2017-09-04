screen weightlifting:
    if press_count >= 1:
        timer 0.01 repeat True action If(time_count > 0, true=[SetVariable("time_count", time_count - 0.01), If(y_value < 600, SetVariable("y_value", y_value +6), NullAction()), SetVariable("time_y_value", time_y_value -1)], false=[Hide("weightlifting"), If(wl_win == 1, Jump("weightlifting_done"), Jump("weightlifting_fail"))])
    if renpy.variant("pc"):
        key "K_SPACE" action [SetVariable(("y_value"), y_value -50), SetVariable(("press_count"), press_count + 1), If(press_count % 6 == 0, SetVariable(("pic_count"), pic_count + 1), NullAction())]
    else:
        imagebutton idle "backgrounds/minigame04a_mobile.jpg" action [SetVariable(("y_value"), y_value -50), SetVariable(("press_count"), press_count + 1), If(press_count % 6 == 0, SetVariable(("pic_count"), pic_count + 1), NullAction())]
    if pic_count % 2 == 0:
        if renpy.variant("pc"):
            if pStats.str() < 3:
                add "backgrounds/minigame04a.jpg"
            elif pStats.str() < 7:
                add "backgrounds/minigame04a_medium.jpg"
            else:
                add "backgrounds/minigame04a_heavy.jpg"
        else:
            if pStats.str() < 3:
                add "backgrounds/minigame04a_mobile.jpg"
            elif pStats.str() < 7:
                add "backgrounds/minigame04a_mobile_medium.jpg"
            else:
                add "backgrounds/minigame04a_mobile_heavy.jpg"
    else:
        if renpy.variant("pc"):
            if pStats.str() < 3:
                add "backgrounds/minigame04b.jpg"
            elif pStats.str() < 7:
                add "backgrounds/minigame04b_medium.jpg"
            else:
                add "backgrounds/minigame04b_heavy.jpg"
        else:
            if pStats.str() < 3:
                add "backgrounds/minigame04b_mobile.jpg"
            elif pStats.str() < 7:
                add "backgrounds/minigame04b_mobile_medium.jpg"
            else:
                add "backgrounds/minigame04b_mobile_heavy.jpg"
    if y_value < 45:
        $ wl_win = 1
        $ time_count = 0
    if time_y_value < 144:
        $ time_count = 0
    add "buttons/meter_03.png" pos 42,54
    add LiveCrop((-42, -54,160, y_value), "buttons/meter_04.png")
    add "buttons/arrows.png" pos 74, time_y_value