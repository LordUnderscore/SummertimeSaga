default sis_email_01_read = False
default sis_email_02_read = False
default sis_email_04_read = False
default sispc_desktop_seen = False
default sispc_email_seen = False
default sispc_livecrush_seen = False
default sispc_toylist_seen = False
default sispc_webcam_seen = False
default sispc_summertime_seen = False
default sispc_igor_seen = False
default sispc_swimsuit_seen = False
default sispc_family_seen = False
default sispc_nude_seen = False

screen sis_computer:
    if comp_locked == False:
        add "backgrounds/computer_sis_02.jpg"

        imagebutton:
            idle "buttons/computer_button_02.png"
            hover "buttons/computer_button_02b.png"
            action [Hide("sis_computer"), Hide("comp_screen"), SetVariable("in_sis_room", True), Jump("sis_bedroom_dialogue")]
            xpos 105
            ypos 603

        imagebutton:
            idle "buttons/computer_icon_01.png"
            hover "buttons/computer_icon_01b.png"
            action Show("sis_recycle")
            xpos 105
            ypos 140

        imagebutton:
            idle "buttons/computer_icon_02.png"
            hover "buttons/computer_icon_02b.png"
            action Show("sis_family")
            xpos 105
            ypos 250

        imagebutton:
            idle "buttons/computer_icon_03.png"
            hover "buttons/computer_icon_03b.png"
            action Show("summertime")
            xpos 105
            ypos 360

        imagebutton:
            idle "buttons/computer_icon_04.png"
            hover "buttons/computer_icon_04b.png"
            action [Hide("sis_computer"), Hide("sis_webcam_screen"), Jump("sispc_webcam_response")]
            xpos 105
            ypos 470

        imagebutton:
            idle "buttons/computer_icon_05.png"
            hover "buttons/computer_icon_05b.png"
            action [Hide("sis_computer"), Jump("sispc_toylist_response")]
            xpos 215
            ypos 140

        imagebutton:
            idle "buttons/computer_icon_06.png"
            hover "buttons/computer_icon_06b.png"
            action [Hide("sis_computer"), Jump("sispc_livecrush_response")]
            xpos 215
            ypos 250

        imagebutton:
            idle "buttons/computer_icon_22.png"
            hover "buttons/computer_icon_22b.png"
            action [Hide("sis_computer"), Jump("sispc_email_response")]
            xpos 215
            ypos 360

    else:
        add "backgrounds/computer_sis_01.jpg"
        add Input (size=20, color="#5d9aff", default="", changed=sis_comp, length=12, xpos= 425, ypos = 422)
        key "K_RETURN" action Jump("pass_check")
        imagebutton idle "buttons/enter_02.png" hover "buttons/enter_02b.png" at Position(xpos = 780, ypos = 405) action Jump("pass_check")
        imagebutton idle "buttons/computer_button_01.png" hover "buttons/computer_button_01b.png" action [If(comp_locked == True and sis_diary_unlocked == True, [Hide("sis_computer"), SetVariable("in_sis_room", True), Jump("sispc_password_reminder")], [Hide("sis_computer"), SetVariable("in_sis_room", True), Jump("sis_bedroom_dialogue")])] pos 109,576

screen summertime tag comp_screen:
    imagebutton idle "buttons/computer_window_07.png" action [Hide("sis_computer"), Hide("summertime"), Jump("sispc_summertime_response")] pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action [Hide("summertime")]
        xpos 816
        ypos 154

screen summertime_error tag comp_screen:
    add "buttons/computer_window_08.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("summertime_error")
        xpos 816
        ypos 154

screen sis_webcam_screen tag comp_screen:
    if connected == False:
        add "buttons/computer_window_06.png" pos 270,150

        imagebutton:
            idle "buttons/computer_button_04.png"
            hover "buttons/computer_button_04b.png"
            action [SetVariable("connected", True), Function(sister.add_event, sis_webcam01), Show("sis_webcam_screen")]
            xpos 719
            ypos 495
    else:
        add "buttons/computer_window_06b.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_webcam_screen")
        xpos 816
        ypos 154

screen sis_list tag comp_screen:
    add "buttons/computer_window_04.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_list")
        xpos 816
        ypos 154

screen sis_livecrush tag comp_screen:
    add "buttons/computer_window_05.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_livecrush")
        xpos 816
        ypos 154

screen sis_recycle tag comp_screen:
    add "buttons/computer_window_03.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_recycle")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_12.png"
        hover "buttons/computer_icon_12b.png"
        action [Hide("sis_computer"), Hide("sis_recycle"), Jump("sispc_nude_response")]
        xpos 290
        ypos 210

screen sis_family tag comp_screen:
    add "buttons/computer_window_01.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_family")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_07.png"
        hover "buttons/computer_icon_07b.png"
        action Show("sis_newfolder")
        xpos 290
        ypos 210

    imagebutton:
        idle "buttons/computer_icon_09.png"
        hover "buttons/computer_icon_09b.png"
        action [Hide("sis_computer"), Hide("sis_family"), Jump("sispc_igor_response")]
        xpos 390
        ypos 210

    imagebutton:
        idle "buttons/computer_icon_08.png"
        hover "buttons/computer_icon_08b.png"
        action [Hide("sis_computer"), Hide("sis_family"), Jump("sispc_family_response")]
        xpos 490
        ypos 210

screen sis_newfolder tag comp_screen:
    add "buttons/computer_window_02.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_newfolder")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_10.png"
        hover "buttons/computer_icon_10b.png"
        action [Hide("sis_computer"), Hide("sis_newfolder"), Jump("sispc_swimsuit_response")]
        xpos 290
        ypos 210

    imagebutton:
        idle "buttons/computer_icon_11.png"
        hover "buttons/computer_icon_11b.png"
        action Show("sis_picture", number = 2)
        xpos 390
        ypos 210

screen sis_email tag comp_screen:
    add "buttons/computer_window_11.png" pos 135,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("sis_email")
        xpos 839
        ypos 154

    if sis_email_01_read == True:
        imagebutton:
            idle "buttons/computer_email_01_read.png"
            hover "buttons/computer_email_01b_read.png"
            action Show("sis_email_open", email = 1)
            xpos 235
            ypos 251
    else:
        imagebutton:
            idle "buttons/computer_email_01.png"
            hover "buttons/computer_email_01b.png"
            action [SetVariable("sis_email_01_read", True), Show("sis_email_open", email = 1)]
            xpos 235
            ypos 251

    if sis_email_02_read == True:
        imagebutton:
            idle "buttons/computer_email_02_read.png"
            hover "buttons/computer_email_02b_read.png"
            action Show("sis_email_open", email = 2)
            xpos 235
            ypos 291
    else:
        imagebutton:
            idle "buttons/computer_email_02.png"
            hover "buttons/computer_email_02b.png"
            action [SetVariable("sis_email_02_read", True), Show("sis_email_open", email = 2)]
            xpos 235
            ypos 291

    imagebutton:
        idle "buttons/computer_email_03_read.png"
        hover "buttons/computer_email_03b_read.png"
        action Show("sis_email_open", email = 3)
        xpos 235
        ypos 331

    imagebutton:
        idle "buttons/computer_email_04_read.png"
        hover "buttons/computer_email_04b_read.png"
        action [SetVariable("sis_email_04_read", True), Show("sis_email_open", email = 4)]
        xpos 235
        ypos 371

    imagebutton:
        idle "buttons/computer_email_05_read.png"
        hover "buttons/computer_email_05b_read.png"
        action Show("sis_email_open", email = 5)
        xpos 235
        ypos 411

    imagebutton:
        idle "buttons/computer_email_06_read.png"
        hover "buttons/computer_email_06b_read.png"
        action Show("sis_email_open", email = 6)
        xpos 235
        ypos 451

screen sis_picture(number):
    imagebutton idle "backgrounds/menu_ground.png" action [Hide("sis_picture")]

    if number == 1:
        add "buttons/computer_pic_01.png" pos 270,150
    elif number == 2:
        add "buttons/computer_pic_02.png" pos 270,150
    elif number == 3:
        add "buttons/computer_pic_03.png" pos 270,150
    elif number == 4:
        add "buttons/computer_pic_04.png" pos 270,150
    else:
        add "buttons/computer_pic_05.png" pos 270,150

screen sis_email_open(email):
    imagebutton idle "backgrounds/menu_ground.png" action [Hide("sis_email_open"), Show("sis_email")]

    if email == 1:
        add "buttons/computer_email_01_popup.png" pos 235,251
    elif email == 2:
        add "buttons/computer_email_02_popup.png" pos 235,251
    elif email == 3:
        add "buttons/computer_email_03_popup.png" pos 235,251
    elif email == 4:
        add "buttons/computer_email_04_popup.png" pos 235,251
    elif email == 5:
        add "buttons/computer_email_05_popup.png" pos 235,251
    else:
        add "buttons/computer_email_06_popup.png" pos 235,251