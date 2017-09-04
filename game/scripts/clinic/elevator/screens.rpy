screen hospital_elevator:
    add "backgrounds/location_hospital_elevator.jpg"

    imagebutton:
        focus_mask True
        pos (454,356)
        idle "buttons/elevator_01.png"
        hover "buttons/elevator_01b.png"
        action Hide("hospital_elevator"), Jump("hospital_dialogue")

    imagebutton:
        focus_mask True
        pos (454,235)
        idle "buttons/elevator_02.png"
        hover "buttons/elevator_02b.png"
        action Hide("hospital_elevator"), Jump("hospital_second_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (454,120)
        idle "buttons/elevator_03.png"
        hover "buttons/elevator_03b.png"
        action Show("popup_unfinished")