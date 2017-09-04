screen maze_scr:
    $ renpy.suspend_rollback(True)
    if (player_pos_x, player_pos_y) != (151, 523):
        if encounter_chance < 30:
            $ encounters = [renpy.random.choice(mob_list)]
    add "images/backgrounds/minigame03.jpg"
    add "images/objects/minigame03_hero01.png" pos player_pos_x, player_pos_y
    if player_pos_x == 151 and player_pos_y == 523:
        if renpy.variant("pc"):
            text "Press {b}ENTER{/b} or click on the {b}CHEST{/b}!" pos 300, 659
            key "K_RETURN" action Jump("Maze_done")
        elif renpy.variant("mobile"):
            text "Click on the {b}CHEST{/b}!" pos 300, 659
        imagebutton idle "images/objects/minigame03_chest01.png" action Jump("Maze_done") focus_mask True pos 256, 528
    for Mob in encounters:
        if player_pos_x < 795 and player_pos_y > 431:
            $ mob_pos_x = player_pos_x + 92
            $ mob_pos_y = player_pos_y
        elif player_pos_x == 795 and player_pos_y > 339:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y - 92
        elif player_pos_x == 795 and player_pos_y == 339:
            $ mob_pos_x = player_pos_x -92
            $ mob_pos_y = player_pos_y
        elif player_pos_x == 703 and player_pos_y > 155:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y - 92
        elif player_pos_x > 519 and player_pos_y == 155:
            $ mob_pos_x = player_pos_x - 92
            $ mob_pos_y = player_pos_y
        elif player_pos_x == 519 and player_pos_y < 339:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y + 92
        elif player_pos_x > 335 and player_pos_y == 339:
            $ mob_pos_x = player_pos_x - 92
            $ mob_pos_y = player_pos_y
        elif player_pos_x == 335 and player_pos_y > 155:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y - 92
        elif player_pos_x > 151 and player_pos_y == 155:
            $ mob_pos_x = player_pos_x - 92
            $ mob_pos_y = player_pos_y
        elif player_pos_x == 151 and player_pos_y < 523:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y + 92
        else:
            $ mob_pos_x = player_pos_x
            $ mob_pos_y = player_pos_y - 92
        add Mob.image pos (mob_pos_x, mob_pos_y)

    if Mob not in encounters:
        if renpy.variant("pc"):
            key "K_UP" action [If((player_pos_x, player_pos_y - 92) not in unpassable, (SetVariable("player_pos_y", player_pos_y - 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())]
            key "K_DOWN" action [If((player_pos_x, player_pos_y + 92) not in unpassable, (SetVariable("player_pos_y", player_pos_y + 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())]
            key "K_RIGHT" action [If((player_pos_x + 92, player_pos_y) not in unpassable, (SetVariable("player_pos_x", player_pos_x + 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())]
            key "K_LEFT" action [If((player_pos_x - 92, player_pos_y) not in unpassable, (SetVariable("player_pos_x", player_pos_x - 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())]
        elif renpy.variant("mobile"):
            imagebutton idle "buttons/attack_01.png" action [If((player_pos_x - 92, player_pos_y) not in unpassable, (SetVariable("player_pos_x", player_pos_x - 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())] focus_mask True pos 50,650
            imagebutton idle "buttons/attack_02.png" action [If((player_pos_x, player_pos_y - 92) not in unpassable, (SetVariable("player_pos_y", player_pos_y - 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())] focus_mask True pos 100,600
            imagebutton idle "buttons/attack_03.png" action [If((player_pos_x + 92, player_pos_y) not in unpassable, (SetVariable("player_pos_x", player_pos_x + 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())] focus_mask True pos 145,650
            imagebutton idle "buttons/attack_04.png" action [If((player_pos_x, player_pos_y + 92) not in unpassable, (SetVariable("player_pos_y", player_pos_y + 92), SetVariable("encounter_chance", renpy.random.randint(0,99))), NullAction())] focus_mask True pos 100,695
    elif Mob == gelly:
        if renpy.variant("pc"):
            add "images/buttons/maze_button_01.png" pos 616, 649
            add "images/buttons/maze_button_02.png" pos 728, 650
            add "images/buttons/maze_button_03.png" pos 834, 642
            key "K_a" action [Jump("Kill_gelly"), encounters.remove(Mob), SetVariable("encounter_chance", 99)]
            key "K_s" action Jump("lose")
            key "K_d" action Jump("lose")
        elif renpy.variant("mobile"):
            imagebutton idle "images/buttons/maze_button_01.png" action [Jump("Kill_gelly"), encounters.remove(Mob), SetVariable("encounter_chance", 99)] focus_mask True pos 616, 649
            imagebutton idle "images/buttons/maze_button_02.png" action [Jump("lose")] focus_mask True pos 728, 650
            imagebutton idle "images/buttons/maze_button_03.png" action [Jump("lose")] focus_mask True pos 834, 642
    elif Mob == skeleton:
        if renpy.variant("pc"):
            add "images/buttons/maze_button_01.png" pos 616, 649
            add "images/buttons/maze_button_02.png" pos 728, 650
            add "images/buttons/maze_button_03.png" pos 834, 642
            key "K_a" action [Jump("lose")]
            key "K_s" action [Jump("Kill_skeleton"), encounters.remove(Mob), SetVariable("encounter_chance", 99)]
            key "K_d" action [Jump("lose")]
        elif renpy.variant("mobile"):
            imagebutton idle "images/buttons/maze_button_01.png" action [Jump("lose")] focus_mask True pos 616, 649
            imagebutton idle "images/buttons/maze_button_02.png" action [Jump("Kill_skeleton"), encounters.remove(Mob), SetVariable("encounter_chance", 99)] focus_mask True pos 728, 650
            imagebutton idle "images/buttons/maze_button_03.png" action [Jump("lose")] focus_mask True pos 834, 642
    elif Mob == firespirit:
        if renpy.variant("pc"):
            add "images/buttons/maze_button_01.png" pos 616, 649
            add "images/buttons/maze_button_02.png" pos 728, 650
            add "images/buttons/maze_button_03.png" pos 834, 642
            key "K_a" action [Jump("lose")]
            key "K_s" action [Jump("lose")]
            key "K_d" action [Jump("Kill_firespirit"), encounters.remove(Mob), SetVariable("encounter_chance", 99)]
        elif renpy.variant("mobile"):
            imagebutton idle "images/buttons/maze_button_01.png" action [Jump("lose")] focus_mask True pos 616, 649
            imagebutton idle "images/buttons/maze_button_02.png" action [Jump("lose")] focus_mask True pos 728, 650
            imagebutton idle "images/buttons/maze_button_03.png" action [Jump("Kill_firespirit"), encounters.remove(Mob), SetVariable("encounter_chance", 99)] focus_mask True pos 834, 642