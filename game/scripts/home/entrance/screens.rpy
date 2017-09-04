screen entrance:

    if not gTimer.is_dark():
        $ suffix=""

    elif gTimer.is_evening() and mom_count == 11 and not mom_dialogue_advance:
        $ suffix="_evening"

    else:
        $ suffix="_night"


    add "backgrounds/location_home_entrance{}.jpg".format(suffix)

    if not attic_key_taken:
        imagebutton:
            focus_mask True
            pos (982,356)
            idle "objects/object_key_01{}.png".format(suffix)
            hover "objects/object_key_01b{}.png".format(suffix)
            action Function(inventory.get_item, item= attic_key), SetVariable("attic_key_taken", True), Hide("entrance"), Jump("attic_key")


    if mom_count == 9 and mom_dialogue_advance == False and gTimer.is_evening() and mom_revealing:
        imagebutton:
            focus_mask True
            pos (699,236)
            idle "objects/object_door_35_evening.png"
            hover "objects/object_door_35b_evening.png"
            action Hide("entrance"), Function(playSound), Jump("home_kitchen_dialogue")


    elif mom_count == 11 and mom_dialogue_advance == False:
        imagebutton:
            focus_mask True
            pos (699,236)
            idle "objects/object_door_35_evening02.png"
            hover "objects/object_door_35b_evening02.png"
            action Hide("entrance"), Function(playSound), SetVariable("ui_lock_count", 0), Jump("dining_room_table_dialogue")

    else:



        if player.in_progress(lawn_mowed):
            $ act = [Hide("entrance"), Jump("lawn_mower_dirty")]

        elif mother.in_progress(mom_dinner_outfit):
            $ act = [Hide("entrance"), Jump("mom_dinner_outfit")]

        else:

            $ act = [Hide("entrance"), Function(playSound)]

        imagebutton:
            focus_mask True
            pos (699,236)
            idle gTimer.image("objects/object_door_35{}.png")
            hover gTimer.image("objects/object_door_35b{}.png")
            action act+[Jump("home_kitchen_dialogue")]

        imagebutton:
            focus_mask True
            pos (141,165)
            idle gTimer.image("objects/object_stairs_02{}.png")
            hover gTimer.image("objects/object_stairs_02b{}.png")
            action act+[Jump("hallway_dialogue")]

        imagebutton:
            focus_mask True
            pos (0,243)
            idle gTimer.image("objects/object_door_39{}.png")
            hover gTimer.image("objects/object_door_39b{}.png")
            action Hide("entrance"), Function(playSound), Jump("home_livingroom_dialogue")


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
            action Hide("entrance"), Jump("home_front")