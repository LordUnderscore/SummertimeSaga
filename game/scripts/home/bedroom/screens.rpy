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
        action Show("telescope_options")

    imagebutton:
        focus_mask True
        pos (225,187)
        idle gTimer.image("objects/object_door_01{}.png")
        hover gTimer.image("objects/object_door_01b{}.png")
        action If(player_room_lock,
                  [Hide("bedroom"), Play("audio", sfxDoor(True)), Jump("player_room_lock")],
                  [Hide("bedroom"), Play("audio", sfxDoor()), Jump("hallway_dialogue")]
        )

    if not m6_note:
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

    else:
        imagebutton:
            focus_mask True
            pos (445,336)
            idle "objects/object_desk_01_note.png"
            hover "objects/object_desk_01b_note.png"
            action Hide("bedroom"), Jump("M6_note")

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
            action Show("bed01_options")

    if not cookies_taken:
        imagebutton:
            focus_mask True
            pos (30,630)
            idle gTimer.image("objects/object_cookies_01{}.png")
            hover gTimer.image("objects/object_cookies_01b{}.png")
            action Function(inventory.get_item, item = cookies), SetVariable("cookies_taken", True), Hide("bedroom"), Jump("cookies")

screen telescope_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("telescope_options")

    imagebutton:
        idle "boxes/telescope_option_01.png"
        hover "boxes/telescope_option_01b.png"
        action Hide("telescope_options"), Hide("bedroom"), Jump ("erik_bedroom")
        xpos 350
        ypos 500

    imagebutton:
        idle "boxes/telescope_option_02.png"
        hover "boxes/telescope_option_02b.png"
        action Hide("telescope_options"), Hide("bedroom"), Jump ("erikmom_bedroom")
        xpos 350
        ypos 550

    imagebutton:
        idle "boxes/telescope_option_03.png"
        hover "boxes/telescope_option_03b.png"
        action Hide ("telescope_options"), Hide("bedroom"), Jump ("mia_bedroom")
        xpos 350
        ypos 600

    imagebutton:
        idle "boxes/telescope_option_04.png"
        hover "boxes/telescope_option_04b.png"
        action Hide ("telescope_options"), Hide("bedroom"), Jump ("backyard")
        xpos 350
        ypos 650

    imagebutton:
        idle "boxes/telescope_option_05.png"
        hover "boxes/telescope_option_05b.png"
        action Hide("telescope_options"), Hide("bedroom"), Jump ("helen_room")
        xpos 350
        ypos 700

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
            action If(player_room_count == 1,
                      [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                      [Hide("bed01_options"), Hide("bedroom"), Jump("sleeping")]
            )
            xpos 350
            ypos 600