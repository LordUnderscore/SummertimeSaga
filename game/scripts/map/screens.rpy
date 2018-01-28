screen town_map:
    if not gTimer.is_dark():
        if getPlayingMusic("<loop 0 to 66.459>audio/music_map.ogg"):
            $ playMusic("<loop 0 to 66.459>audio/music_map.ogg")
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    else:
        if getPlayingMusic("<loop 107 to 215>audio/music_map_night.ogg"):
            $ playMusic("<loop 107 to 215>audio/music_map_night.ogg")
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    add gTimer.image("map/map_base{}.jpg")

    imagebutton:
        focus_mask True
        pos (837,613)
        idle gTimer.image("map/home01{}.png")
        hover gTimer.image("map/home01b{}.png")
        if not gTimer.is_dark():
            action Hide("town_map"), Hide("ui"), Function(playMusic), SetVariable("in_sis_room", False), Jump("home_front")
        else:
            action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("home_front")
        hovered SetVariable("location_count", "Home")
        unhovered SetVariable("location_count", "Town Map")

    imagebutton:
        focus_mask True
        pos (728,593)
        idle gTimer.image("map/erikhouse01{}.png")
        hover gTimer.image("map/erikhouse01b{}.png")
        if not gTimer.is_dark():
            action Hide("town_map"), Hide("ui"), Function(playMusic), SetVariable("in_erik_house", False), Jump("erik_house_dialogue")
        else:
            action If(
                gTimer.is_evening(),
                [Hide("town_map"), Hide("ui"), Function(playMusic), Jump("erik_house_dialogue")],
                [Hide("town_map"), Hide("ui"), Jump("night_sleep_map")]
            )
        hovered SetVariable("location_count", "Erik's House")
        unhovered SetVariable("location_count", "Town Map")

    if loc_school_unlocked:
        imagebutton:
            focus_mask True
            pos (407,233)
            idle gTimer.image("map/school01{}.png")
            hover gTimer.image("map/school01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), If(erik.started(erik_intro), NullAction(), Function(playSound)), Jump("school_dialogue")
            else:
                action If(
                    gTimer.is_evening(),
                    [Hide("town_map"), Hide("ui"), Function(playMusic), Jump("night_closed_school")],
                    [Hide("town_map"), Hide("ui"), Jump("night_sleep_map")]
                )
            hovered SetVariable("location_count", "School")
            unhovered SetVariable("location_count", "Town Map")

    if loc_court_unlocked:
        imagebutton:
            focus_mask True
            pos (417,220)
            idle gTimer.image("map/bball01{}.png")
            hover gTimer.image("map/bball01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("basket_court_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Basket Ball Court")
            unhovered SetVariable("location_count", "Town Map")

    if loc_aunt_unlocked:
        imagebutton:
            focus_mask True
            pos (468,62)
            idle gTimer.image("map/dianehouse01{}.png")
            hover gTimer.image("map/dianehouse01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), SetVariable("in_garden", False), Jump("diane_front_yard")
            else:
                action If(
                    gTimer.is_evening(),
                    [Hide("town_map"), Hide("ui"), Function(playMusic), Jump("diane_front_yard")],
                    [Hide("town_map"), Hide("ui"), Jump("night_sleep_map")]
                )
            hovered SetVariable("location_count", "Diane's House")
            unhovered SetVariable("location_count", "Town Map")

    if loc_mia_unlocked:
        imagebutton:
            focus_mask True
            pos (621,592)
            idle gTimer.image("map/miahouse01{}.png")
            hover gTimer.image("map/miahouse01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("mias_house_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), If(M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room], [Function(playMusic), Jump("mias_house_dialogue")], Jump("night_sleep_map"))
            hovered SetVariable("location_count", "Mia's House")
            unhovered SetVariable("location_count", "Town Map")

    if loc_gym_unlocked:
        imagebutton:
            focus_mask True
            pos (851,320)
            idle gTimer.image("map/gym01{}.png")
            hover gTimer.image("map/gym01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("training_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Gym")
            unhovered SetVariable("location_count", "Town Map")

    if loc_library_unlocked:
        imagebutton:
            focus_mask True
            pos (697,323)
            idle gTimer.image("map/library01{}.png")
            hover gTimer.image("map/library01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("library_front")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Library")
            unhovered SetVariable("location_count", "Town Map")

    if loc_park_unlocked:
        imagebutton:
            focus_mask True
            pos (310,179)
            idle gTimer.image("map/park01{}.png")
            hover gTimer.image("map/park01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), If(not gTimer.is_dark(), Function(playMusic)), Jump("park_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Park")
            unhovered SetVariable("location_count", "Town Map")

    if loc_pool_unlocked:
        imagebutton:
            focus_mask True
            pos (462,578)
            idle gTimer.image("map/pool01{}.png")
            hover gTimer.image("map/pool01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), SetVariable("wearing_swimsuit", False), SetVariable("changing_count", 0), Jump("pool_dialogue")
            else:
                action If(
                    gTimer.is_evening(),
                    [Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("pool_dialogue")],
                    [Hide("town_map"), Hide("ui"), Jump("night_sleep_map")]
                )
            hovered SetVariable("location_count", "Pool")
            unhovered SetVariable("location_count", "Town Map")

    if loc_mall_unlocked:
        imagebutton:
            focus_mask True
            pos (791,79)
            idle gTimer.image("map/mall01{}.png")
            hover gTimer.image("map/mall01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("mall_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Mall")
            unhovered SetVariable("location_count", "Town Map")

    if loc_bank_unlocked:
        imagebutton:
            focus_mask True
            pos (708,198)
            idle gTimer.image("map/bank01{}.png")
            hover gTimer.image("map/bank01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("bank_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Bank")
            unhovered SetVariable("location_count", "Town Map")

    if loc_pizza_unlocked:
        imagebutton:
            focus_mask True
            pos (98,338)
            idle gTimer.image("map/pizza01{}.png")
            hover gTimer.image("map/pizza01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("pizza_exterior_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Pizzeria")
            unhovered SetVariable("location_count", "Town Map")

    if loc_dealership_unlocked:
        imagebutton:
            focus_mask True
            pos (104,176)
            idle gTimer.image("map/dealership01{}.png")
            hover gTimer.image("map/dealership01b{}.png")
            if not gTimer.is_dark():
                action If(
                    gTimer.is_weekend(),
                    [Hide("town_map"), Hide("ui"), Jump("weekend_locked")],
                    [Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("dealership_dialogue")]
                )
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Car Dealership")
            unhovered SetVariable("location_count", "Town Map")

    if loc_pier_unlocked:
        imagebutton:
            focus_mask True
            pos (58,529)
            idle gTimer.image("map/pier01{}.png")
            hover gTimer.image("map/pier01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("pier_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Pier")
            unhovered SetVariable("location_count", "Town Map")

    if loc_forest_unlocked:
        imagebutton:
            focus_mask True
            pos (0,107)
            idle gTimer.image("map/forest01{}.png")
            hover gTimer.image("map/forest01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("forest_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Forest")
            unhovered SetVariable("location_count", "Town Map")

    if loc_church_unlocked:
        imagebutton:
            focus_mask True
            pos (588,48)
            idle gTimer.image("map/church01{}.png")
            hover gTimer.image("map/church01b{}.png")
            if not gTimer.is_dark() or (gTimer.is_evening() and not M_mia.is_set('church night locked')):
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("church_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Church")
            unhovered SetVariable("location_count", "Town Map")

    if loc_police_unlocked:
        imagebutton:
            focus_mask True
            pos (834,227)
            idle gTimer.image("map/police01{}.png")
            hover gTimer.image("map/police01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("police_lobby_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Police Station")
            unhovered SetVariable("location_count", "Town Map")

    if loc_tattoo_unlocked:
        imagebutton:
            focus_mask True
            pos (259,47)
            idle gTimer.image("map/tattoo01{}.png")
            hover gTimer.image("map/tattoo01b{}.png")
            if not gTimer.is_dark():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("tattoo_parlor_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Tattoo Parlor")
            unhovered SetVariable("location_count", "Town Map")

    if loc_beach_unlocked:
        imagebutton:
            focus_mask True
            pos (204,570)
            idle gTimer.image("map/beach01{}.png")
            hover gTimer.image("map/beach01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("beach_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Beach")
            unhovered SetVariable("location_count", "Town Map")

    if loc_hill_unlocked:
        imagebutton:
            focus_mask True
            pos (692,-3)
            idle gTimer.image("map/hill01{}.png")
            hover gTimer.image("map/hill01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("hill_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Hill")
            unhovered SetVariable("location_count", "Town Map")

    if loc_clinic_unlocked:
        imagebutton:
            focus_mask True
            pos (342,499)
            idle gTimer.image("map/clinic01{}.png")
            hover gTimer.image("map/clinic01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Function(playSound), Jump("hospital_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Clinic")
            unhovered SetVariable("location_count", "Town Map")

    if loc_trailer_unlocked:
        imagebutton:
            focus_mask True
            pos (3,294)
            idle gTimer.image("map/trailer01{}.png")
            hover gTimer.image("map/trailer01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("trailer_park_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Trailer Park")
            unhovered SetVariable("location_count", "Town Map")

    if loc_treehouse_unlocked:
        imagebutton:
            focus_mask True
            pos (805,512)
            idle gTimer.image("map/treehouse01{}.png")
            hover gTimer.image("map/treehouse01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("treehouse_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Treehouse")
            unhovered SetVariable("location_count", "Town Map")

    if loc_donuts_unlocked:
        imagebutton:
            focus_mask True
            pos (982,222)
            idle gTimer.image("map/donut01{}.png")
            hover gTimer.image("map/donut01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("donut_shop_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Donut Shop")
            unhovered SetVariable("location_count", "Town Map")

    if M_aqua.is_set('altar pass') and M_aqua.is_set('treasure pass') and M_aqua.is_set('squid pass') and M_aqua.is_set('maze pass') and loc_lair_unlocked:
        imagebutton:
            focus_mask True
            pos (10,675)
            if not gTimer.is_dark():
                idle "private/map/lair01.png"
                hover "private/map/lair01b.png"
            else:
                idle "private/map/lair01_night.png"
                hover "private/map/lair01b_night.png"
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("lair_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Lair")
            unhovered SetVariable("location_count", "Town Map")

    if loc_warehouse_unlocked:
        imagebutton:
            focus_mask True
            pos (110,58)
            idle gTimer.image("map/warehouse01{}.png")
            hover gTimer.image("map/warehouse01b{}.png")
            if not gTimer.is_night():
                action Hide("town_map"), Hide("ui"), Function(playMusic), Jump("warehouse_dialogue")
            else:
                action Hide("town_map"), Hide("ui"), Jump("night_sleep_map")
            hovered SetVariable("location_count", "Lair")
            unhovered SetVariable("location_count", "Town Map")

    add gTimer.image("car01{}")
    add gTimer.image("car02{}")
    add gTimer.image("car03{}")
    add "sparkle01"
    add "sparkle02"
    add "sparkle03"
    add "cloud01"