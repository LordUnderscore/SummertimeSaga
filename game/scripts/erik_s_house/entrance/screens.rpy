screen eriks_house_entrance tag eriks_house:
    add gTimer.image("backgrounds/location_erik_house_inside{}.jpg")

    imagebutton:
        focus_mask True
        pos (401,40)
        idle gTimer.image("objects/object_door_30{}.png")
        hover gTimer.image("objects/object_door_30b{}.png")
        action If(
            not erik.completed(erik_breastfeeding),
            [Hide("eriks_house_entrance"), Jump("mrsj_room_locked_dialogue")],
            If(
                erik.over(erik_path_split) and erik.started(erik_sex_ed),
                [Hide("eriks_house_entrance"), Jump("erik_sex_ed_block")],
                If(
                    mrsj_filled,
                    [Hide("eriks_house_entrance"), Jump("mrsj_filled_block")],
                    [Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("mrsj_room")],
                )
            )
        )

    imagebutton:
        focus_mask True
        pos (340,0)
        idle gTimer.image("objects/object_door_68{}.png")
        hover gTimer.image("objects/object_door_68b{}.png")
        action If(
                   erik_funky and where_is("june") == "Erik's Room",
                   [Hide("eriks_house_entrance"), Jump("erik_funky_block")],
                   [Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("erik_room_dialogue")],
               )

    imagebutton:
        focus_mask True
        pos (576,325)
        idle gTimer.image("objects/object_door_31{}.png")
        hover gTimer.image("objects/object_door_31b{}.png")
        action Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("erik_basement")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("eriks_house_entrance"), Jump("erik_house_dialogue")

    if is_here("mrsj"):
        imagebutton:
            focus_mask True
            pos (700,300)
            idle "objects/character_erikmom_01.png"
            hover "objects/character_erikmom_01b.png"
            action Hide("eriks_house_entrance"), Jump("mrsj_button_dialogue")