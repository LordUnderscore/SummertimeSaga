screen living_room:
    if M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two] or (M_mom.is_set("movie night") and gTimer.is_dark()):
        add "backgrounds/location_home_livingroom_night_mom.jpg"
    else:
        add gTimer.image("backgrounds/location_home_livingroom{}.jpg")

    if sister.started(sis_couch01) and gTimer.is_evening() and (M_mom.get_state() != S_mom_sleepover or not is_here("mom")):
        imagebutton:
            focus_mask True
            pos (412,331)
            idle "images/objects/object_tv_02_night.png"
            hover "images/objects/object_tv_02b_night.png"
            action Hide("living_room"), Jump("couch_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (1002,251)
            idle gTimer.image("objects/object_door_42{}.png")
            hover gTimer.image("objects/object_door_42b{}.png")
            action Hide("living_room"), If(
                                                                                   M_mom.is_set("fetch lotion") and where_is("mom") == "Basement",
                                                                                   Jump("mom_lotion_block"),
                                                                                   If(
                                                                                      M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two],
                                                                                      Jump("mom_movie_block"),
                                                                                      Jump("home_entrance")
                                                                                   )
            )

        imagebutton:
            focus_mask True
            pos (809,311)
            idle gTimer.image("objects/object_door_43{}.png")
            hover gTimer.image("objects/object_door_43b{}.png")
            action Hide("living_room"), If(
                                           M_mom.get_state() == S_mom_dinner_outfit,
                                           Jump("mom_dinner_outfit"),
                                           If(
                                              M_mom.is_set("fetch lotion") and where_is("mom") == "Kitchen",
                                              Jump("mom_lotion_block"),
                                              If(
                                                 M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two],
                                                 Jump("mom_movie_block"),
                                                 If(
                                                    M_mom.get_state() == S_mom_fetch_laundry,
                                                    Jump("mom_laundry_block"),
                                                    Jump("home_basement_dialogue")
                                                 )
                                              )
                                           )
            )

        imagebutton:
            focus_mask True
            pos (108,312)
            idle gTimer.image("objects/object_door_44{}.png")
            hover gTimer.image("objects/object_door_44b{}.png")
            action Hide("living_room"), If(
                                           M_mom.get_state() == S_mom_wash_clothes,
                                           Jump("lawn_mower_dirty"),
                                           If(
                                              M_mom.is_set("bedroom locked"),
                                              Jump("mom_bedroom_locked"),
                                              If(
                                                 M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two],
                                                 Jump("mom_movie_block"),
                                                 Jump("mom_bedroom")
                                              )
                                           )
            )

        imagebutton:
            focus_mask True
            pos (412,331)
            idle gTimer.image("objects/object_tv_01{}.png")
            hover gTimer.image("objects/object_tv_01b{}.png")
            action Hide("living_room"), If(
                                           M_mom.get_state() == S_mom_wash_clothes,
                                           Jump("lawn_mower_dirty"),
                                           If(
                                              M_mom.is_set("fetch lotion"),
                                              Jump("mom_lotion_block"),
                                              If(
                                                 M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two] or (M_mom.is_set("movie night") and gTimer.is_dark()),
                                                 Jump("mom_movie_night"),
                                                 If(
                                                    sister.over(sis_couch01),
                                                    Jump("home_livingroom_tv"),
                                                    Jump("home_livingroom_tv_locked")
                                                 )
                                              )
                                           )
            )

screen home_livingroom_tv:
    add "backgrounds/location_tv.jpg"

    if tv_channel == 0:
        add "buttons/tv_channel_01.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 1:
        add "buttons/tv_channel_02.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 2:
        add "buttons/tv_channel_03.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 3:
        add "buttons/tv_channel_04.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 4:
        add "buttons/tv_channel_05.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 5:
        add "buttons/tv_channel_06.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 6:
        add "buttons/tv_channel_07.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 7:
        if tv_pink_channel == 7 and not tv_channel_pink:
            add "buttons/tv_channel_09.png" at Position(xpos=86, ypos=107)

        elif tv_pink_channel == 8 and not tv_channel_pink:
            add "buttons/tv_channel_10.png" at Position(xpos=86, ypos=107)

        else:
            add "buttons/tv_channel_08.png" at Position(xpos=86, ypos=107)

            $ tv_channel = 7
            default pink_screen = True

            imagemap:
                ground "pink_channel_login" at Position(xpos=0, ypos=0)
                hotspot (390,325,270,29) background "buttons/tv_channel_08.png" action SetScreenVariable("pink_screen", True)
                hotspot (390,398,270,29) background "buttons/tv_channel_08.png" action SetScreenVariable("pink_screen", False)
                if pink_screen:
                    add Input (size=20, color="#ff4bdf", default=pink_user, changed=pink_channel_user, length=12, xpos = 433, ypos = 329)
                    text "{size=20}{color=#ff4bdf}[pink_pass]{/color}{/size}" at Position(xpos = 433, ypos = 400)

                else:
                    text "{size=20}{color=#ff4bdf}[pink_user]{/color}{/size}" at Position(xpos = 433, ypos = 329)
                    add Input (size=20, color="#ff4bdf", default=pink_pass, changed=pink_channel_pass, length=12, xpos = 433, ypos = 400)

            key "K_RETURN" action Jump("tv_pink_channel_pass_check")

            imagebutton:
                idle "buttons/enter_01.png"
                hover "buttons/enter_01b.png" at Position(xpos=460, ypos= 450)
                action Jump("tv_pink_channel_pass_check")

    imagebutton:
        focus_mask True
        pos (398,633)
        idle "buttons/tv_buttons_01.png"
        hover "buttons/tv_buttons_01b.png"
        action Hide("home_livingroom_tv"), Jump("home_livingroom_dialogue")

    imagebutton:
        focus_mask True
        pos (393,677)
        idle "buttons/tv_buttons_02.png"
        hover "buttons/tv_buttons_02b.png"
        action SetVariable("tv_channel", tv_channel - 1), Jump("tv_channel_responses")

    imagebutton:
        focus_mask True
        pos (554,678)
        idle "buttons/tv_buttons_03.png"
        hover "buttons/tv_buttons_03b.png"
        action SetVariable("tv_channel", tv_channel + 1), Jump("tv_channel_responses")

screen sis_couch_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("sis_couch_sex_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("sis_couch_sex_cum")
        xpos 450
        ypos 700

    if M_sis.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("sis_couch_slower_sex")
            xpos 250
            ypos 735

    if M_sis.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("sis_couch_faster_sex")
            xpos 450
            ypos 735