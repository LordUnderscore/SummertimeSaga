screen library_meeting_room:
    add "backgrounds/location_library_meeting.jpg"

    imagebutton:
        focus_mask True
        pos (418,491)
        idle "objects/object_table_03.png"
        hover "objects/object_table_03b.png"
        action Hide("library_meeting_room"), Jump("meeting_room_table_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_04.png"
        hover "boxes/auto_option_04b.png"
        action Hide("library_meeting_room"), Jump("library_dialogue")