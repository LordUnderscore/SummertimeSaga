init python:
    if "s" in config.keymap['screenshot']:
        config.keymap['screenshot'].remove('s')
    class Mob:
        def __init__(self, image = ""):
            self.image = image

label Maze:
    $ encounter_chance = 99
    call screen maze_scr

label lose:
    $ renpy.suspend_rollback(False)
    $ gTimer.tick()
    hide screen maze_scr
    show maze_bg
    show player_dead at Position(xpos = (player_pos_x + 41), ypos = (player_pos_y + 99))
    show popup_bad at truecenter with dissolve
    $ renpy.pause()
    $ player_pos_x = 427
    $ player_pos_y = 615
    hide maze_bg
    hide player_dead
    hide popup_bad
    jump MC_computer

label Maze_done:
    $ renpy.suspend_rollback(False)
    $ gTimer.tick()
    $ pStats.increase("int")
    hide screen maze_scr
    show maze_done
    show popup_good at truecenter with dissolve
    $ renpy.pause()
    $ player_pos_x = 427
    $ player_pos_y = 615
    hide maze_done
    hide popup_good
    jump MC_computer

label Kill_gelly:
    show maze_bg
    show player_sprite at Position(xpos = (player_pos_x + 38), ypos = (player_pos_y + 97))
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
    show mob_gelly_dead at Position(xpos = (mob_pos_x + 43), ypos = (mob_pos_y + 95))
    $ renpy.pause(0.5)
    hide maze_bg
    hide player_sprite
    hide mob_gelly_dead
    jump Maze

label Kill_skeleton:
    show maze_bg
    show player_sprite at Position(xpos = (player_pos_x + 38), ypos = (player_pos_y + 97))
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
    show mob_skeleton_dead at Position(xpos = (mob_pos_x + 41), ypos = (mob_pos_y + 98))
    $ renpy.pause(0.5)
    hide maze_bg
    hide player_sprite
    hide mob_skeleton_dead
    jump Maze

label Kill_firespirit:
    show maze_bg
    show player_sprite at Position(xpos = (player_pos_x + 38), ypos = (player_pos_y + 97))
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
    show mob_firespirit_dead at Position(xpos = (mob_pos_x + 43), ypos = (mob_pos_y + 101))
    $ renpy.pause(0.5)
    hide maze_bg
    hide player_sprite
    hide mob_firespirit_dead
    jump Maze