screen lair_entrance:
    add "private/backgrounds/location_lair_ocean.jpg"

    imagebutton:
        focus_mask True
        pos (387,433)
        idle "private/objects/object_lair_01.png"
        hover "private/objects/object_lair_01b.png"
        action Hide("lair_entrance"), Jump("maze_pre")

screen lair:
    add "private/backgrounds/location_lair.jpg"

    if is_here("aqua"):
        imagebutton:
            focus_mask True
            pos (291,436)
            idle "private/objects/object_mount_01.png"
            hover "private/objects/object_mount_01b.png"
            action Hide("lair"), Jump("aqua_dialogue")

    if M_aqua.is_set("seasucc available"):
        imagebutton:
            focus_mask True
            pos (5,442)
            idle "private/objects/object_seathrone_01.png"
            hover "private/objects/object_seathrone_01b.png"
            action Hide("lair"), Jump("seasucc_dialogue")

screen aqua_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("aqua_sex_options"), Jump("aqua_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Hide("aqua_sex_options"), Jump("aqua_sex_cum")

    if M_aqua.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Hide("aqua_sex_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") + 0.05), Jump("aqua_sex_loop")

    if M_aqua.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Hide("aqua_sex_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") - 0.05), Jump("aqua_sex_loop")

screen seasucc_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("seasucc_options"), Jump("seasucc_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover "buttons/cam_stage01_02b.png"
        action Hide("seasucc_options"), Jump("seasucc_cum")

    if M_aqua.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Hide("seasucc_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") + 0.05), Jump("seasucc_loop")

    if M_aqua.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Hide("seasucc_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") - 0.05), Jump("seasucc_loop")

screen squid_fight:
    add "private/backgrounds/location_lair_ocean_fight.jpg"

    if renpy.variant("pc"):
        key "K_UP" action [If(move_list[arrow_index] == m_up, Function(add_arrow, m_up), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_a" action [If(move_list[arrow_index] == K_a, Function(add_key, K_a), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_DOWN" action [If(move_list[arrow_index] == m_down, Function(add_arrow, m_down), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_s" action [If(move_list[arrow_index] == K_s, Function(add_key, K_s), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_RIGHT" action [If(move_list[arrow_index] == m_right, Function(add_arrow, m_right), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_d" action [If(move_list[arrow_index] == K_d, Function(add_key, K_d), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_LEFT" action [If(move_list[arrow_index] == m_left, Function(add_arrow, m_left), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_f" action [If(move_list[arrow_index] == K_f, Function(add_key, K_f), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]

    if task_list == move_list:
        if renpy.variant("pc"):
            key "K_RETURN" action [Hide("squid_fight"), Jump("squid_attack")]
            text "Press {b}ENTER{/b}!" pos 660,550
        else:
            imagebutton idle "private/backgrounds/location_lair_ocean_fight.jpg" action [Hide("squid_fight"), Jump("squid_attack")]
            text "Tap to {b}ATTACK{/b}!" pos 660,550




    else:
        if renpy.variant("mobile"):
            imagebutton idle "buttons/attack_01.png" action [If(move_list[arrow_index] == m_left, Function(add_arrow, m_left), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 50,650
            imagebutton idle "buttons/attack_02.png" action [If(move_list[arrow_index] == m_up, Function(add_arrow, m_up), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 100,600
            imagebutton idle "buttons/attack_03.png" action [If(move_list[arrow_index] == m_right, Function(add_arrow, m_right), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 145,650
            imagebutton idle "buttons/attack_04.png" action [If(move_list[arrow_index] == m_down, Function(add_arrow, m_down), Jump("squid_fight_pre")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 100,695

        timer 0.01 repeat True action If(time_count > 0, SetVariable("time_count", time_count - 0.01), [Hide("squid_fight"), Jump("squid_fail")])
        bar value time_count range timer_range pos 440,700 xmaximum 513 ymaximum 33 style "time_bar"

        $ a = 405
        $ b = 530
        $ c = 0
        for Move in move_list:
            $ a += 60
            if c < len(task_list):
                if move_list[c] == task_list[c]:
                    add Move.passive pos a,b

                else:
                    add Move.image pos a,b

            else:
                add Move.image pos a,b
            $ c += 1

screen lair_maze:
    default bg_no = 1
    default bg = randomizer("private/backgrounds/location_lair_cave{}.jpg", bg_no, 3)
    if bg_no == 4:
        $ bg_no = 1
    add bg

    imagebutton:
        focus_mask True
        pos (0,175)
        idle "private/objects/object_cavehole_01.png"
        hover "private/objects/object_cavehole_01b.png"
        action SetScreenVariable("bg_no", bg_no + 1), SetScreenVariable("bg", randomizer("private/backgrounds/location_lair_cave{}.jpg", bg_no, 3)), Function(maze_choices.append, "Left"), If(len(maze_choices) > 5, [Hide("lair_maze"), Jump("maze_finish")], NullAction())

    imagebutton:
        focus_mask True
        pos (356,170)
        idle "private/objects/object_cavehole_02.png"
        hover "private/objects/object_cavehole_02b.png"
        action SetScreenVariable("bg_no", bg_no + 1), SetScreenVariable("bg", randomizer("private/backgrounds/location_lair_cave{}.jpg", bg_no, 3)), Function(maze_choices.append, "Middle"), If(len(maze_choices) > 5, [Hide("lair_maze"), Jump("maze_finish")], NullAction())

    imagebutton:
        focus_mask True
        pos (858,212)
        idle "private/objects/object_cavehole_03.png"
        hover "private/objects/object_cavehole_03b.png"
        action SetScreenVariable("bg_no", bg_no + 1), SetScreenVariable("bg", randomizer("private/backgrounds/location_lair_cave{}.jpg", bg_no, 3)), Function(maze_choices.append, "Right"), If(len(maze_choices) > 5, [Hide("lair_maze"), Jump("maze_finish")], NullAction())

    timer 0.01 repeat True action If(time_count > 0, SetVariable("time_count", time_count - 0.01), [Hide("lair_maze"), Jump("maze_fail")])
    bar value time_count range timer_range pos 440,700 xmaximum 513 ymaximum 33 style "time_bar"