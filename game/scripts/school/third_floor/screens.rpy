screen school_third_floor:
    add gTimer.image("backgrounds/location_school_third{}.jpg")

    imagebutton:
        focus_mask True
        pos (17,294)
        idle gTimer.image("objects/object_sign_04{}.png")
        hover gTimer.image("objects/object_sign_04b{}.png")
        action Hide("school_third_floor"), Jump("stairs_dialogue")

    imagebutton:
        focus_mask True
        pos (277,247)
        idle gTimer.image("objects/object_door_98{}.png")
        hover gTimer.image("objects/object_door_98b{}.png")
        action Hide("school_third_floor"), Function(playSound), Play("audio", sfxDoor()), Jump("bissette_office_dialogue")

    imagebutton:
        focus_mask True
        pos (454,301)
        idle gTimer.image("objects/object_door_99{}.png")
        hover gTimer.image("objects/object_door_99b{}.png")
        action Hide("school_third_floor"), Function(playSound), Play("audio", sfxDoor()), Jump("dewitt_office_dialogue")

    imagebutton:
        focus_mask True
        pos (591,344)
        idle gTimer.image("objects/object_door_100{}.png")
        hover gTimer.image("objects/object_door_100b{}.png")
        action Hide("school_third_floor"), Function(playSound), Play("audio", sfxDoor()), Jump("ross_office_dialogue")

    imagebutton:
        focus_mask True
        pos (700,379)
        idle gTimer.image("objects/object_door_101{}.png")
        hover gTimer.image("objects/object_door_101b{}.png")
        action Hide("school_third_floor"), Function(playSound), Play("audio", sfxDoor()), Jump("okita_office_dialogue")

    imagebutton:
        focus_mask True
        pos (831,367)
        idle gTimer.image("objects/object_door_13{}.png")
        hover gTimer.image("objects/object_door_13b{}.png")
        action Hide("school_third_floor"), Function(playSound), Play("audio", sfxDoor()), Jump("office_dialogue")