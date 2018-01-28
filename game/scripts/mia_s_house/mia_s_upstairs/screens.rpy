screen mias_house_upstairs:
    add gTimer.image("backgrounds/location_mia_house_upstairs{}.jpg")

    imagebutton:
        focus_mask True
        pos (444,419)
        idle gTimer.image("objects/object_door_33{}.png")
        hover gTimer.image("objects/object_door_33b{}.png")
        action Hide("mias_house_upstairs"), Jump("mias_bedroom_screen")

    imagebutton:
        focus_mask True
        pos (615,337)
        idle gTimer.image("objects/object_door_92{}.png")
        hover gTimer.image("objects/object_door_92b{}.png")
        action Hide("mias_house_upstairs"), Jump("helens_bedroom")

    imagebutton:
        focus_mask True
        pos (257,238)
        idle gTimer.image("objects/object_door_93{}.png")
        hover gTimer.image("objects/object_door_93b{}.png")
        action Hide("mias_house_upstairs"), If(M_mia.is_set('helens locked room locked'), Jump("helens_locked_room_block"), Jump("helens_locked_room"))

    imagebutton:
        focus_mask True
        pos (758,110)
        idle gTimer.image("objects/object_door_94{}.png")
        hover gTimer.image("objects/object_door_94b{}.png")
        action Hide("mias_house_upstairs"), Jump("harolds_office")

    imagebutton:
        focus_mask True
        pos (0,0)
        idle gTimer.image("objects/object_door_95{}.png")
        hover gTimer.image("objects/object_door_95b{}.png")
        action Hide("mias_house_upstairs"), Jump("mias_entrance")