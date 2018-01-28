init python:
    def tele_rand():
        global erik_telescope_random
        if gTimer.is_afternoon():
            erik_telescope_random = renpy.random.randint(0,2)
        else:
            erik_telescope_random = renpy.random.randint(0,1)
        
        global erikmom_telescope_random
        erikmom_telescope_random = renpy.random.randint(0,2)
        
        global mia_telescope_random
        mia_telescope_random = renpy.random.randint(0,1)
        if gTimer.is_afternoon():
            mia_telescope_random = renpy.random.randint(0,2)
        
        global backyard_telescope_random
        if gTimer.is_morning():
            backyard_telescope_random = renpy.random.randint(0,3)
        elif gTimer.is_afternoon():
            backyard_telescope_random = renpy.random.randint(0,1)
        
        global helen_telescope_random
        if gTimer.is_afternoon():
            helen_telescope_random = renpy.random.randint(0,1)

screen ui:
    default ui_location = location_count

    if not ui_locked():
        $ suffix = ""
        if ui_location not in ["Town Map", "Bedroom", "Erik's House", "Mia's House"] and M_player.get_state() != S_player_start:
            $ suffix = "_noskip"
        imagemap:
            ground "buttons/ui_ground.png"
            if renpy.get_screen("town_map"):
                idle "buttons/ui_idle_02{}.png".format(suffix)
                hover "buttons/ui_hover_02.png"
            else:
                idle "buttons/ui_idle{}.png".format(suffix)
                hover "buttons/ui_hover.png"
            alpha False
            if renpy.get_screen("town_map"):
                hotspot (16, 5, 71, 71) action [Hide("town_map"), Function(playMusic), Function(playSound), Jump("bedroom_dialogue")]
            elif M_mom.get_state() == S_mom_bad_guys_driveby and not gTimer.is_dark() and location_count in ["Bedroom", "Hallway", "Sister's Bedroom", "Shower", "Attic", "Entrance", "Kitchen", "Dining Room", "Backyard", "Living Room", "Basement", "Mom's Bedroom", "Garage", "Home Front"]:
                hotspot (16, 5, 71, 71) action [Function(hideScreen, location_count), Function(playMusic), Function(playSound), Jump("bad_guys_driveby")]
            else:
                hotspot (16, 5, 71, 71) action [Function(hideScreen, location_count), Jump("map_dialogue")]
            hotspot (801, 5, 51, 68) action [Show("cellphone"), Play("audio", "audio/sfx_phone_notification.ogg")]
            if new_message == True:
                add "buttons/cellphone_app_alert.png" pos 835,5
            hotspot (867, 5, 60, 71) action If(renpy.get_screen("backpack"), [Hide("backpack"), Play("audio", "audio/sfx_phone_notification.ogg")], [Show("backpack"), Play("audio", "audio/sfx_backpack_open.ogg")])
            hotspot (946, 5, 68, 70) action ShowMenu("navigation")
            if ui_location in ["Town Map", "Bedroom", "Erik's House", "Mia's House"] and M_player.get_state() != S_player_start:
                hotspot (503, 44, 31, 25) action Function(gTimer.tick)

    else:
        imagemap:
            ground "buttons/ui_ground.png"
            idle "buttons/ui_idle_locked.png"
            hover "buttons/ui_hover_locked.png"
            alpha False
            hotspot (16, 5, 71, 71) action NullAction()
            hotspot (801, 5, 51, 68) action [Show("cellphone"), Play("audio", "audio/sfx_phone_notification.ogg")]
            hotspot (867, 5, 60, 71) action If(renpy.get_screen("backpack"), [Hide("backpack"), Play("audio", "audio/sfx_phone_notification.ogg")], [Show("backpack"), Play("audio", "audio/sfx_backpack_open.ogg")])
            hotspot (946, 5, 68, 70) action ShowMenu("navigation")

    text "{b}[inventory.money]{/b}" xpos 765 ypos 16 xalign 1.0
    text "{b}[location_count]{/b}" xpos 105 ypos 15 xalign 0.0
    if gTimer.is_morning():
        add "buttons/ui_day_cycle_bar.png" pos 444,29
        add "buttons/ui_day_cycle_bar.png" pos 499,29
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    elif gTimer.is_afternoon():
        add "buttons/ui_day_cycle_bar.png" pos 499,29
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    elif gTimer.is_evening():
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    $ Day = gTimer.dayOfWeek(full=True)
    text "{b}[Day]{/b}" xpos 105 ypos 45 xalign 0.0