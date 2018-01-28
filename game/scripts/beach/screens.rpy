screen beach:
    add gTimer.image("backgrounds/location_beach{}.jpg")

    if not gTimer.is_dark() and M_aqua.is_set("treasure search"):
        imagebutton:
            focus_mask True
            pos (666,569)
            idle "objects/object_island_01.png"
            hover "objects/object_island_01b.png"
            action Hide("beach"), Jump("beach_island_dialogue")

    imagebutton:
        focus_mask True
        pos (187,495)
        idle gTimer.image("objects/object_stall_01{}.png")
        hover gTimer.image("objects/object_stall_01b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (444,318)
        idle gTimer.image("objects/object_tower_01{}.png")
        hover gTimer.image("objects/object_tower_01b{}.png")
        action Show("popup_unfinished")

screen beach_island:
    add "backgrounds/location_beach_island.jpg"

    imagebutton:
        focus_mask True
        if M_aqua.get_state() == S_aqua_treasure_search:
            pos (409,124)
            idle "private/objects/object_statue_02.png"
            hover "private/objects/object_statue_02b.png"

        else:
            pos (311,124)
            idle "private/objects/object_statue_03.png"
            hover "private/objects/object_statue_03b.png"
        action Hide("beach_island"), With(fade), Jump("beach_statue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover "boxes/auto_option_generic_02b.png"
        action Hide("beach_island"), Jump("beach_dialogue")

screen treasure_lock:
    default lock01 = 0
    default lock02 = 0
    default lock03 = 0
    default lock04 = 0
    default open_lock = False

    imagemap:
        ground "private/backgrounds/location_beach_lock.jpg"

        imagebutton:
            focus_mask True
            align (0.99,0.99)
            idle "boxes/auto_option_generic_02.png"
            hover "boxes/auto_option_generic_02b.png"
            action Hide("treasure_lock"), With(fade), Jump("beach_island_dialogue")

        if lock01 == 1 and lock02 == 5 and lock03 == 1 and lock04 == 3:
            imagebutton:
                focus_mask True
                if not open_lock:
                    pos (460,125)
                    idle PulseImage("private/objects/object_keyhole_01.png", "private/objects/object_keyhole_01b.png", delay = 2)
                    hover "private/objects/object_keyhole_01b.png"
                else:
                    pos (460,74)
                    idle "private/objects/object_keyhole_02.png"
                action If(treasure_key in inventory.items, SetScreenVariable("open_lock", True), NullAction()), Hide("treasure_lock"), With(fade), Jump("treasure_open")

        if lock01 > 0:
            imagebutton:
                focus_mask True
                pos (110,407)
                idle "private/buttons/lock_icon_" + str(lock01).zfill(2) + ".png"
                hover "private/buttons/lock_icon_" + str(lock01).zfill(2) + "b.png"
                action If(lock01 < 10, SetScreenVariable("lock01", lock01 + 1), SetScreenVariable("lock01", 0))
        else:
            hotspot (110,407,188,186) background "private/backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock01", 1)

        if lock02 > 0:
            imagebutton:
                focus_mask True
                pos (317,407)
                idle "private/buttons/lock_icon_" + str(lock02).zfill(2) + ".png"
                hover "private/buttons/lock_icon_" + str(lock02).zfill(2) + "b.png"
                action If(lock02 < 10, SetScreenVariable("lock02", lock02 + 1), SetScreenVariable("lock02", 0))
        else:
            hotspot (317,407,188,186) background "private/backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock02", 1)

        if lock03 > 0:
            imagebutton:
                focus_mask True
                pos (522,407)
                idle "private/buttons/lock_icon_" + str(lock03).zfill(2) + ".png"
                hover "private/buttons/lock_icon_" + str(lock03).zfill(2) + "b.png"
                action If(lock03 < 10, SetScreenVariable("lock03", lock03 + 1), SetScreenVariable("lock03", 0))
        else:
            hotspot (522,407,188,186) background "private/backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock03", 1)

        if lock04 > 0:
            imagebutton:
                focus_mask True
                pos (728,407)
                idle "private/buttons/lock_icon_" + str(lock04).zfill(2) + ".png"
                hover "private/buttons/lock_icon_" + str(lock04).zfill(2) + "b.png"
                action If(lock04 < 10, SetScreenVariable("lock04", lock04 + 1), SetScreenVariable("lock04", 0))
        else:
            hotspot (728,407,188,186) background "private/backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock04", 1)

screen treasure_chest:
    imagebutton:
        focus_mask True
        pos (440,275)
        idle "private/objects/object_compass_01.png"
        hover "private/objects/object_compass_01b.png"
        action Return()