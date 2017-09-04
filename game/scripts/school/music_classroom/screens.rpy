screen music_classroom:

    add "backgrounds/location_school_music.jpg"

    imagebutton:
        focus_mask True
        pos (406,295)
        idle "objects/object_door_61.png"
        hover "objects/object_door_61b.png"
        action Hide("music_classroom"), Play("audio", sfxDoor()), Jump("school_dialogue")

    imagebutton:
        focus_mask True
        pos (178,343)
        idle "objects/character_dewitt_01.png"
        hover "objects/character_dewitt_01b.png"
        action Hide("music_classroom"), Jump("dewitt_button_dialogue")