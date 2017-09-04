screen bag_minigame:
    add "backgrounds/minigame02_input.jpg"


    if renpy.variant("pc"):
        key "K_UP" action [If(move_list[arrow_index] == m_up, Function(add_arrow, m_up), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_a" action [If(move_list[arrow_index] == K_a, Function(add_key, K_a), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_DOWN" action [If(move_list[arrow_index] == m_down, Function(add_arrow, m_down), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_s" action [If(move_list[arrow_index] == K_s, Function(add_key, K_s), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_RIGHT" action [If(move_list[arrow_index] == m_right, Function(add_arrow, m_right), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_d" action [If(move_list[arrow_index] == K_d, Function(add_key, K_d), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_LEFT" action [If(move_list[arrow_index] == m_left, Function(add_arrow, m_left), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]
        key "K_f" action [If(move_list[arrow_index] == K_f, Function(add_key, K_f), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())]

    if task_list == move_list:
        if renpy.variant("pc"):
            key "K_RETURN" action [Hide("bag_minigame"), SetVariable("training_done", True), Jump("bag_minigame_attack")]
            text "Press {b}ENTER{/b}!" pos 660,550
        else:
            imagebutton idle "backgrounds/minigame02_input.jpg" action [Hide("bag_minigame"), SetVariable("training_done", True), Jump("bag_minigame_attack")]
            text "Tap to {b}ATTACK{/b}!" pos 660,550




    else:
        if renpy.variant("mobile"):
            imagebutton idle "buttons/attack_01.png" action [If(move_list[arrow_index] == m_left, Function(add_arrow, m_left), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 50,650
            imagebutton idle "buttons/attack_02.png" action [If(move_list[arrow_index] == m_up, Function(add_arrow, m_up), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 100,600
            imagebutton idle "buttons/attack_03.png" action [If(move_list[arrow_index] == m_right, Function(add_arrow, m_right), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 145,650
            imagebutton idle "buttons/attack_04.png" action [If(move_list[arrow_index] == m_down, Function(add_arrow, m_down), Jump("bag_minigame_listing")), If(arrow_index < move_list_number - 1, SetVariable("arrow_index", arrow_index + 1), NullAction())] focus_mask True pos 100,695
        timer 0.01 repeat True action If(time_count > 0, SetVariable("time_count", time_count - 0.01), [Hide("bag_minigame"), Jump("training_failed_dialogue")])
        bar value time_count range timer_range pos 440,700 xmaximum 513 ymaximum 33 style "time_bar"
        if training_tier == 1:
            $ a = 525

        elif training_tier == 2:
            $ a = 465

        elif training_tier == 3:
            $ a = 405

        elif training_tier == 4:
            $ a = 345
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