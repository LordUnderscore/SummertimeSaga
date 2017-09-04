screen school_courtyard:

    add "backgrounds/location_gym.jpg"

    imagebutton:
        focus_mask True
        pos (600,380)
        idle "objects/character_coach_01.png"
        hover "objects/character_coach_01b.png"
        action Hide("school_courtyard"), Jump("coach_button_dialogue")

    imagebutton:
        pos (350,600)
        idle "boxes/door07_option_01.png"
        hover "boxes/door07_option_01b.png"
        action Hide("school_courtyard"), Jump("school_dialogue")