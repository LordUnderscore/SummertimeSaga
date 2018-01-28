screen hallway:
    add gTimer.image("backgrounds/location_hallway{}.jpg")


    if not gTimer.is_dark() and sister.started(sis_final):
        $ act = [Hide("hallway"), Jump("hallway_dialogue_sis_spy")]

    elif M_mom.get_state() == S_mom_debt_call:
        $ act = [Hide("hallway"), Jump("hallway_check_on_mom")]

    elif M_mom.get_state() == S_mom_fetch_towel:
        $ act = [Hide("hallway"), Jump("mom_midnight_swim_towel_block")]

    else:
        $ act = [Hide("hallway"), Function(playSound), Play("audio", sfxDoor()), Jump("bedroom_dialogue")]

    imagebutton:
        focus_mask True
        pos (175,280)
        idle gTimer.image("objects/object_door_02{}.png")
        hover gTimer.image("objects/object_door_02b{}.png")
        action act


    if sis_door_locked_count == 0:
        $ act = [Hide("hallway"), Play("audio", sfxDoor(True)), Jump("hallway_dialogue_sis_door")]

    elif gTimer.is_night():
        $ act = [Hide("hallway"), Jump("too_tired")]

    elif M_mom.get_state() == S_mom_debt_call:
        $ act = [Hide("hallway"), Jump("hallway_check_on_mom")]

    elif M_mom.get_state() == S_mom_fetch_towel:
        $ act = [Hide("hallway"), Jump("mom_midnight_swim_towel_block")]

    else:
        $ act = [Hide("hallway"), Function(playSound), Play("audio", sfxDoor()), Jump("sis_bedroom_dialogue")]

    imagebutton:
        focus_mask True
        pos (387,225)
        idle gTimer.image("objects/object_door_03{}.png")
        hover gTimer.image("objects/object_door_03b{}.png")
        action act


    if not gTimer.is_dark() and sister.started(sis_final):
        $ act = [Hide("hallway"), Jump("hallway_dialogue_sis_spy")]

    elif M_mom.get_state() == S_mom_debt_call:
        $ act = [Hide("hallway"), Jump("hallway_check_on_mom")]

    else:
        $ act = [Hide("hallway"), Play("audio", sfxDoor()), Jump("shower_dialogue")]

    imagebutton:
        focus_mask True
        if not shower.occupied():
            pos (526,108)
            idle "objects/object_door_04_busy.png"
            hover "objects/object_door_04b_busy.png"
        else:
            pos (580,108)
            idle gTimer.image("objects/object_door_04{}.png")
            hover gTimer.image("objects/object_door_04b{}.png")
        action act


    if gTimer.is_dark():
        $ act = [Hide("hallway"), Function(playSound), Jump("home_entrance")]

    elif not gTimer.is_dark() and sister.started(sis_final):
        $ act = [Hide("hallway"), Jump("hallway_dialogue_sis_spy")]

    else:
        $ act = [Hide("hallway"), Jump("home_entrance")]

    imagebutton:
        focus_mask True
        pos (830,0)
        idle gTimer.image("objects/object_door_19{}.png")
        hover gTimer.image("objects/object_door_19b{}.png")
        action act


    if not gTimer.is_dark() and sister.started(sis_final):
        $ act = [Hide("hallway"), Jump("hallway_dialogue_sis_spy") ]

    elif M_mom.get_state() == S_mom_fetch_towel:
        $ act = [Hide("hallway"), Jump("mom_midnight_swim_towel_block")]

    else:
        $ act = [Hide("hallway"), Function(playSound), Jump("attic_entry_dialogue")]

    imagebutton:
        focus_mask True
        pos (360,40)
        idle gTimer.image("objects/object_door_40{}.png")
        hover gTimer.image("objects/object_door_40b{}.png")
        action act

screen sis_name_input:
    add "boxes/popup_name_sis.png" pos 250,250
    add Input (size=24, color="#5d9aff", default="", changed=sister_name, length=12, xpos= 347, ypos = 347)
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover "buttons/menu_skip_01b.png" action Return pos 362,447