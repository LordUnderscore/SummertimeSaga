label pass_check:
    if sis_pass == "BAD MONSTER" or sis_pass == "bad monster" or sis_pass == "Bad Monster" or sis_pass == "Bad monster":
        scene sis_comp
        $ comp_locked = False
        jump sispc_desktop_response
    elif sis_pass.lower().strip() != "bad monster":
        scene sis_comp
        show sis_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide sis_wrong_pass with dissolve
        call screen sis_computer

label sispc_desktop_response:
    if sispc_desktop_seen == False:
        scene sis_computer_bg with None
        player_name "It worked!"
        player_name "I wonder what {b}[sis_name]{/b} has on her computer..."
        $ sispc_desktop_seen = True
    call screen sis_computer

label sispc_nude_response:
    if sispc_nude_seen == False:
        scene sis_computer_bg
        show sis_computer_nude
        with None
        player_name "!!!" with hpunch
        player_name "Is that... {b}Her{/b}?!"
        $ sispc_nude_seen = True
    show screen sis_computer
    show screen sis_recycle
    call screen sis_picture(3)

label sispc_family_response:
    if sispc_family_seen == False:
        scene sis_computer_bg
        show sis_computer_family
        with None
        player_name "( I never knew she had this picture. )"
        player_name "( I miss {b}Dad{/b}... )"
        $ sispc_family_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(5)

label sispc_swimsuit_response:
    if sispc_swimsuit_seen == False:
        scene sis_computer_bg
        show sis_computer_swimsuit
        with None
        player_name "( She loves taking pictures of herself... )"
        $ sispc_swimsuit_seen = True
    show screen sis_computer
    show screen sis_newfolder
    call screen sis_picture(1)

label sispc_igor_response:
    if sispc_igor_seen == False:
        scene sis_computer_bg
        show sis_computer_igor
        with None
        player_name "..."
        player_name "( I think I've seen this guy before. )"
        player_name "( He used to work with {b}Dad{/b}... )"
        $ sispc_igor_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(4)

label sispc_summertime_response:
    if sispc_summertime_seen == False:
        scene sis_computer_bg
        show sis_computer_summertime
        with None
        player_name "( Man... This game {b}always{/b} has bugs. )"
        $ sispc_summertime_seen = True
    show screen sis_computer
    call screen summertime_error

label sispc_webcam_response:
    if sispc_webcam_seen == False:
        scene sis_computer_bg
        show sis_computer_webcam
        with None
        player_name "( Ooh, this is interesting... )"
        player_name "( ... her {b}webcam{/b} is on the network. )"
        player_name "( Maybe I could {b}connect{/b} it to my computer? )"
        $ sispc_webcam_seen = True
    show screen sis_computer
    call screen sis_webcam_screen

label sispc_toylist_response:
    if sispc_toylist_seen == False:
        scene sis_computer_bg
        show sis_computer_toylist
        with None
        player_name "( Looks like a list of... {b}toys{/b}? )"
        $ sispc_toylist_seen = True
    show screen sis_computer
    call screen sis_list

label sispc_livecrush_response:
    if sispc_livecrush_seen == False:
        scene sis_computer_bg
        show sis_computer_livecrush
        with None
        player_name "( {b}[sis_name]{/b} has a profile on LiveCrush?! )"
        player_name "Woah..."
        player_name "( Does she do these {b}live shows{/b} in her room? )"
        player_name "( She must be pretty careful keeping this a secret; I had no idea... )"
        $ sispc_livecrush_seen = True
    show screen sis_computer
    call screen sis_livecrush

label sispc_email_response:
    if sispc_email_seen == False:
        scene sis_computer_bg
        show sis_computer_email
        with None
        player_name "( I don't know If I should go through these... )"
        $ sispc_email_seen = True
    show screen sis_computer
    call screen sis_email

label sispc_email04_response:
    if sis_email_04_read == False:
        player_name "( Sis has a pink account?! The only time she'd have a chance to watch that adult cable TV channel would be when everybody's asleep. )"
        player_name "( I should check to see if she's downstairs at night. )"
        $ sis_email_04_read = True
    show screen sis_computer
    call screen sis_email

label sis_computer:
    if comp_locked == True:
        scene expression "backgrounds/computer_sis_01.jpg"
        player_name "( Hmm... She has a {b}password{/b}... )"
        if sis_diary_unlocked == False:
            player_name "( I should try to find out what it is. )"
            $ in_sis_room = True
            hide screen sis_computer
            hide screen comp_screen
            jump sis_bedroom_dialogue
        else:
            player_name "( Let's see if I can log into her computer... )"
    jump sis_computer_response

label sis_computer_response:
    if comp_locked == False and sis_email_04_read == False:
        player_name "( I should look for other secrets she might have on here... )"
    call screen sis_computer

label sispc_password_reminder:
    scene sisbedroom_night
    show player 35 at left
    player_name "( If I remember right, the password was in her diary... )"
    jump sis_bedroom_dialogue