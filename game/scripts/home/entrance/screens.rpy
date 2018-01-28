screen entrance:

    if not gTimer.is_dark():
        $ suffix = ""

    elif (M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening()) or (M_mom.get_state() == S_mom_diane_dinner and gTimer.is_evening()):
        $ suffix = "_evening"

    else:
        $ suffix = "_night"


    add "backgrounds/location_home_entrance{}.jpg".format(suffix)

    if not attic_key_taken:
        imagebutton:
            focus_mask True
            pos (982,356)
            idle "objects/object_key_01{}.png".format(suffix)
            hover "objects/object_key_01b{}.png".format(suffix)
            action Function(inventory.get_item, item = attic_key), SetVariable("attic_key_taken", True), Hide("entrance"), Jump("attic_key")


    if M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening():
        imagebutton:
            focus_mask True
            pos (699,236)
            idle "objects/object_door_35_evening.png"
            hover "objects/object_door_35b_evening.png"
            action Hide("entrance"), Function(playSound), Jump("home_kitchen_dialogue")


    elif M_mom.get_state() == S_mom_diane_dinner and gTimer.is_evening():
        imagebutton:
            focus_mask True
            pos (699,236)
            idle "objects/object_door_35_evening02.png"
            hover "objects/object_door_35b_evening02.png"
            action Hide("entrance"), Function(playSound), Jump("dining_room_table_dialogue")

    else:



        if M_mom.get_state() == S_mom_wash_clothes:
            $ act = [Hide("entrance"), Jump("lawn_mower_dirty")]

        elif M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two]:
            $ act = [Hide("entrance"), Jump("mom_movie_block")]

        elif M_mom.get_state() == S_mom_mall_outing:
            $ act = [Hide("entrance"), Jump("mom_outing_block")]

        elif M_mom.get_state() == S_mom_dinner_outfit:
            $ act = [Hide("entrance"), Jump("mom_dinner_outfit")]

        else:

            $ act = [Hide("entrance"), Function(playSound)]

        imagebutton:
            focus_mask True
            pos (699,236)
            if not gTimer.is_dark():
                idle "objects/object_door_35.png"
                hover "objects/object_door_35b.png"
            else:
                idle "objects/object_door_35_night.png"
                hover "objects/object_door_35b_night.png"
            action act + [Jump("home_kitchen_dialogue")]

        imagebutton:
            focus_mask True
            pos (141,165)
            idle gTimer.image("objects/object_stairs_02{}.png")
            hover gTimer.image("objects/object_stairs_02b{}.png")
            action act + [If(
                             M_mom.is_set("fetch lotion"),
                             Jump("mom_lotion_block"),
                             If(
                                M_mom.get_state() == S_mom_midnight_search,
                                Jump("mom_midnight_swim_block"),
                                Jump("hallway_dialogue")
                             )
            )]

        imagebutton:
            focus_mask True
            pos (0,243)
            if not gTimer.is_dark():
                idle "objects/object_door_39.png"
                hover "objects/object_door_39b.png"
            else:
                idle "objects/object_door_39_night.png"
                hover "objects/object_door_39b_night.png"
            action Hide("entrance"), Function(playSound), If(
                                                             M_mom.get_state() == S_mom_mall_outing,
                                                             Jump("mom_outing_block"),
                                                             If(
                                                                M_mom.get_state() == S_mom_midnight_search,
                                                                Jump("mom_midnight_swim_block"),
                                                                If(
                                                                   M_mom.get_state() == S_mom_fetch_towel,
                                                                   Jump("mom_midnight_swim_towel_block"),
                                                                   Jump("home_livingroom_dialogue")
                                                                )
                                                             )
            )

        if is_here("mom"):
            imagebutton:
                focus_mask True
                pos (550,350)
                idle "objects/character_mom_04.png"
                hover "objects/character_mom_04b.png"
                action Hide("entrance"), Jump("vacuum_dialogue")

        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/auto_option_08.png"
            hover "boxes/auto_option_08b.png"
            action Hide("entrance"), If(
                                        M_mom.is_set("fetch lotion"),
                                        Jump("mom_lotion_block"),
                                        If(
                                           M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two],
                                           Jump("mom_movie_block"),
                                           If(
                                              M_mom.get_state() == S_mom_midnight_search,
                                              Jump("mom_midnight_swim_block"),
                                              Jump("home_front")
                                           )
                                        )
            )