screen bedroom:
    if MC_computer_broken:
        add gTimer.image("backgrounds/location_bedroom_broken{}.jpg")
    else:
        add gTimer.image("backgrounds/location_bedroom{}.jpg")

    imagebutton:
        focus_mask True
        pos (44,352)
        idle gTimer.image("objects/object_telescope_01{}.png")
        hover gTimer.image("objects/object_telescope_01b{}.png")
        action Hide("bedroom"), If((M_mia.get_state() == S_mia_midnight_call or M_mia.get_state() == S_mia_urgent_message) and gTimer.is_dark(), Jump("player_message_lock"), Jump("telescope"))

    imagebutton:
        focus_mask True
        pos (225,187)
        idle gTimer.image("objects/object_door_01{}.png")
        hover gTimer.image("objects/object_door_01b{}.png")
        action Hide("bedroom"), If(
                                   M_mom.get_state() == S_mom_note,
                                   Jump("player_room_lock"),
                                   If(
                                      M_mia.get_state() == S_mia_midnight_call or M_mia.get_state() == S_mia_urgent_message,
                                      Jump("player_message_lock"),
                                      [Play("audio", sfxDoor()), Jump("hallway_dialogue")]
                                      )
        )

    if M_mom.get_state() == S_mom_note:
        imagebutton:
            focus_mask True
            pos (445,336)
            idle "objects/object_desk_01_note.png"
            hover "objects/object_desk_01b_note.png"
            action Hide("bedroom"), Jump("M6_note")

    else:
        if not MC_computer_broken:
            imagebutton:
                focus_mask True
                pos (445,336)
                idle gTimer.image("objects/object_desk_01{}.png")
                hover gTimer.image("objects/object_desk_01b{}.png")
                action If(MC_computer_broken,
                          Show ("desk01_options"),
                          [Hide("bedroom"), Jump("MC_computer")]
                )

        else:
            imagebutton:
                focus_mask True
                pos (445,336)
                idle gTimer.image("objects/object_desk_broken_01{}.png")
                hover gTimer.image("objects/object_desk_broken_01b{}.png")
                action If(MC_computer_broken,
                          Show ("desk01_options"),
                          [Hide("bedroom"), Jump("MC_computer")]
                )

    if is_here("june"):
        imagebutton:
            focus_mask True
            pos (670,350)
            idle "images/objects/character_june_02.png"
            hover "images/objects/character_june_02b.png"
            action Hide("bedroom"), Jump("june_bedroom_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (639,439)
            idle gTimer.image("objects/object_bed_01{}.png")
            hover gTimer.image("objects/object_bed_01b{}.png")
            action If(M_mia.get_state() == S_mia_midnight_help, [Hide("bedroom"), Jump("mia_midnight_text")], Show("bed01_options"))

    if not cookies_taken:
        imagebutton:
            focus_mask True
            pos (30,630)
            idle gTimer.image("objects/object_cookies_01{}.png")
            hover gTimer.image("objects/object_cookies_01b{}.png")
            action Function(inventory.get_item, item = cookies), SetVariable("cookies_taken", True), Hide("bedroom"), Jump("cookies")

    if M_player.is_set("pet cat"):
        imagebutton:
            focus_mask True
            pos (350,670)
            idle gTimer.image("objects/character_cat_01{}.png")
            hover gTimer.image("objects/character_cat_01b{}.png")
            action Hide("bedroom"), Jump("pet_cat")

screen desk01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("desk01_options")]
    imagebutton:
        idle "boxes/desk01_option_03.png"
        hover "boxes/desk01_option_03b.png"
        action If(parts in inventory.items, [SetVariable("MC_computer_broken", False), (Function(inventory.remove_item, parts), Hide("desk01_options"), Show("popup_repaired01"))], (Hide("desk01_options"), Show("popup_broken")))
        xpos 350
        ypos 600

screen popup_broken:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_broken")
    imagebutton:
        idle "boxes/popup_broken_comp.png"
        action Hide("popup_broken")
        xpos 280
        ypos 360

screen popup_repaired01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_repaired01")

    imagebutton:
        idle "boxes/popup_broken_comp2.png"
        action Hide("popup_repaired01"), SetVariable("computer_count", 1)
        xpos 280
        ypos 360

screen bed01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bed01_options")

    if bed_locked == 0:
        imagebutton:
            idle "boxes/bed01_option_01.png"
            hover "boxes/bed01_option_01b.png"
            action Hide("bed01_options"), Hide("bedroom"), Jump("sleeping_locked")
            xpos 350
            ypos 600

    else:
        imagebutton:
            idle "boxes/bed01_option_01.png"
            hover "boxes/bed01_option_01b.png"
            action If(M_mom.get_state() == S_mom_debt_call,
                      [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                      If(ui_locked(),
                         [Hide("bed01_options"), Hide("bedroom"), Jump("bed_locked")],
                         [Hide("bed01_options"), Hide("bedroom"), Jump("sleeping")]
                      )
            )
            xpos 350
            ypos 600

screen june_mcbedroom_normal_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("june_mcbedroom_normal_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("june_mcbedroom_normal_sex_cum_outside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("june_mcbedroom_normal_sex_cum_inside")
        xpos 550
        ypos 700

    if M_june.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("june_mcbedroom_normal_slower_sex")
            xpos 250
            ypos 735

    if M_june.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("june_mcbedroom_normal_faster_sex")
            xpos 450
            ypos 735

screen june_mcbedroom_cosplay_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("june_mcbedroom_cosplay_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("june_mcbedroom_cosplay_sex_cum_outside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("june_mcbedroom_cosplay_sex_cum_inside")
        xpos 550
        ypos 700

    if M_june.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("june_mcbedroom_cosplay_slower_sex")
            xpos 250
            ypos 735

    if M_june.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("june_mcbedroom_cosplay_faster_sex")
            xpos 450
            ypos 735