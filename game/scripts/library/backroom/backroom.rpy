label backroom_blocked_dialogue:
    scene library
    show player 35 with dissolve
    player_name "Hmm... I'm not sure where the school {b}textbooks{/b} are..."
    player_name "Maybe I should ask the {b}Librarian{/b} at the {b}reception desk{/b} first."
    hide player 35 with dissolve
    $ callScreen(location_count)

label backroom_dialogue:
    $ location_count = "Library Backroom"
    if backroom_count == 0:
        scene backroom01
        show library 1_2 at Position(xpos = 486, ypos = 707) with dissolve
        player_name "( OH SHIT!!! )"
        player_name "..."
        player_name "( People are having sex back here... )"
        pause 4
        player_name "..."
        player_name "( Is that a webcam on the shelf? )"
        player_name "( I think it's filming... Do they even know that it's there? )"
        player_name "( Should I tell the {b}librarian{/b}? )"
        call screen backroom_couple_sex01

    elif backroom_count == 2:
        scene backroom01
        show jane 8 at right
        show player 23 at left
        with dissolve
        jan "Oh for crying out loud!"
        show player 22
        jan "Didn't I tell you not to go back here?!"
        jan "I said I had to clean up first!!"
        show jane 12
        show player 10
        player_name "Yeah but I saw-"
        show jane 8
        show player 11
        jan "I KNOW!!!" with hpunch
        show jane 7
        jan "Ugh..."
        jan "That's why I told you not to come here..."
        show jane 12
        show player 12
        player_name "You knew people were doing it in here?!"
        show jane 8
        show player 11
        jan "I... I don't have a choice, okay?"
        show jane 7
        jan "How else am I supposed to keep this place open?"
        show jane 12
        show player 12
        player_name "Wait, you're making {b}money{/b} off of this??"
        show jane 8
        show player 11
        jan "Of course, dummy!"
        jan "I'm getting paid to live stream it."
        show jane 4
        jan "It's the only way I can keep this place {b}open{/b}, okay?"
        show jane 5
        jan "I have no choice..."
        show player 30
        show jane 1
        player_name "But... What about the people being filmed?"
        player_name "Do they know?"
        show jane 4
        show player 11
        jan "Of course not... But who cares? This back room is popular among couples."
        show jane 2
        jan "People love doing it back here and I'm not gonna stop them!"
        jan "Just keep this to yourself if you ever wanna get those textbooks..."
        show jane 1
        show player 12
        player_name "Alright! I won't tell anyone..."
        show player 4
        player_name "..."
        show player 12
        player_name "But when can I expect my {b}textbook{/b} to arrive?"
        show player 1
        show jane 2
        jan "I'll make you a deal... If you buy me a {b}Supersaga Digital Webcam{/b}, I'll place the order now!"
        show jane 1
        show player 34
        player_name "..."
        show player 35
        player_name "Aren't those really expensive?"
        show jane 7
        show player 11
        jan "Look, do you want your {b}textbook{/b} or not?"
        show jane 2
        show player 12
        player_name "Alright... I'll see what I can do."
        show jane 8
        show player 11
        jan "Good, now get out of here! I'm expecting more couples to arrive soon..."
        hide jane 8
        hide player 11
        with dissolve
        if quest06 not in completed_quests:
            $ quest_list.append(quest06)
        $ library_desk_count = 1
        $ backroom_count = 3
        $ ui_lock_count = 0
        $ gTimer.tick()
    $ callScreen(location_count)

label backroom_couple_finish01:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707)
    pause 4
    hide library 1_2
    pause .2
    show library 3 at Position(xpos = 486, ypos = 707) with dissolve
    window hide
    pause
    show library 4
    window hide
    pause
    player_name "( Oh shit! )"
    player_name "( I hear someone coming!! )"
    show library 5 at Position(xpos = 512, ypos = 707) with hpunch
    window hide
    pause
    hide library 5 with dissolve
    $ backroom_count = 2
    jump backroom_dialogue