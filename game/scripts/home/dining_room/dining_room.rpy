label dining_room_dialogue:
    $ location_count = "Dining Room"
    if sister.started(sis_breakfast):
        scene home_diningroom
        show diningroom_sis_breakfast at Position(xpos=473,ypos=718)
        show player 1f at right
        with dissolve
        player_name "( Huh. {b}[sis_name]{/b} is awake already? )"
        player_name "( She usually sleeps in. )"
        hide player

    elif M_mom.get_state() == S_mom_fetch_towel and towel in inventory.items:
        jump mom_pool_dialogue
    $ callScreen(location_count)

label dining_room_table_dialogue:
    scene expression gTimer.image("dining_room{}")
    if M_mom.get_state() == S_mom_diane_dinner and gTimer.is_evening():
        scene location_home_dining
        show sis 44 at Position(xpos=0.1161,ypos=1.0000)
        show player 213 at Position(xpos=0.5972,ypos=1.0118)
        show aunt 128 at Position(xpos=0.3483,ypos=1.0118)
        show mom 65 at Position(xpos=0.8626,ypos=1.0118)
        show table 1 at Position(xpos=0.4976,ypos=0.7630)
        with fade
        mom "Well I'm glad your fresh milk business is doing well."
        mom "And how's {b}[firstname]{/b} doing in the garden?"
        show sis 45
        mom "He seems like he's always over there working lately."
        show mom 66
        show sis 44
        show player 218
        show aunt 130
        mom "Haha!"
        show aunt 129
        show mom 64
        show player 214
        dia "Oh, he's doing great!"
        dia "My garden has never looked this beautiful..."
        show aunt 128
        dia "..."
        show aunt 130
        dia "But enough talk about me!"
        show aunt 129
        dia "How's life around the house lately?"
        dia "You guys doing okay?"
        show player 213
        show aunt 128
        show mom 67 at Position(xpos=0.8294,ypos=1.0118)
        mom "It's been really tough for us..."
        show sis 45
        show mom 65 at Position(xpos=0.8626,ypos=1.0118)
        mom "But fortunately, I've had some help."
        show sis 44
        show player 220
        show mom 68 at Position(xpos=0.8294,ypos=1.0118)
        $ renpy.pause ()
        show player 221
        show mom 69 at Position(xpos=0.7992,ypos=1.0118)
        $ renpy.pause ()
        show player 222
        show mom 70 at Position(xpos=0.7992,ypos=1.0118)
        $ renpy.pause ()
        show mom 71 at Position(xpos=0.7992,ypos=1.0118)
        show player 224
        mom "{b}[firstname]{/b} has been so helpful and caring lately..."
        mom "He really stepped up and took on all my husband's responsibilities..."
        show player 226
        show aunt 129
        show mom 70
        show sis 45
        dia "That's a really sweet thing to do, {b}[firstname]{/b}."
        show player 225
        show aunt 128
        show sis 44
        player_name "I umm... Was just trying to help!"
        show player 226
        show aunt 129
        dia "You know..."
        dia "If you guys need extra help, I could always move in for a while..."
        show sis 46
        sis "..."
        dia "Just until you get back on your feet, you know?"
        show mom 71
        show aunt 128
        show player 224
        mom "I mean, it might not be a terrible idea..."
        mom "We could use the help."
        show player 226
        show sis 47
        show mom 70
        sis "Wait. {b}Aunt Diane{/b} is moving in, now?"
        show player 224
        show sis 48
        show mom 71
        mom "It's just an idea!"
        mom "Doesn't mean we're doing it but..."
        show sis 47
        show player 226
        show mom 70
        sis "But where would she even sleep?"
        show mom 71
        show player 224
        show sis 48
        mom "I don't know... We could find a way!"
        mom "She could sleep with me for a while, she's my twin sister!"
        show player 226
        show aunt 128
        show mom 70
        dia "I don't mind."
        dia "I would get to spend more time with the family!"
        dia "And with my favorite nephew..."
        show player 221
        show aunt 134 at Position(xpos=0.3981,ypos=1.0118)
        $ renpy.pause ()
        show player 222
        show aunt 135 at Position(xpos=0.3981,ypos=1.0118)
        $ renpy.pause ()
        show sis 47
        show player 226
        sis "This is weird..."
        show sis 48
        show mom 71 at Position(xpos=0.7992,ypos=1.0118)
        $ renpy.pause ()
        show mom 70 at Position(xpos=0.7992,ypos=1.0118)
        $ renpy.pause ()
        show mom 69 at Position(xpos=0.7992,ypos=1.0118)
        $ renpy.pause ()
        show mom 68 at Position(xpos=0.8294,ypos=1.0118)
        $ renpy.pause ()
        show aunt 134
        $ renpy.pause ()
        show aunt 133 at Position(xpos=0.3483,ypos=1.0118)
        show mom 67 at Position(xpos=0.8294,ypos=1.0118)
        mom "We can talk about it another time perhaps."
        show player 218
        mom "Let's just have a nice dinner!"
        show mom 64 at Position(xpos=0.8626,ypos=1.0118)
        show aunt 132
        dia "The food was delicious!"
        scene location_home_entrance_night_blur
        show aunt 137 at right
        show mom 91f
        show player 203 at Position(xpos=0.2820,ypos=1.0000)
        show sis 49f at left
        with fade
        dia "Thanks for inviting me over, guys!"
        dia "It was such a pleasant dinner!"
        show aunt 136
        show mom 92f
        mom "We were all happy to see you, {b}Diane{/b}."
        show mom 91f
        show aunt 137
        dia "Oh! And better watch out: I'll take you up on that offer!"
        show aunt 137
        dia "Just come and ask me! I'll pack my bags and bring my pillow!"
        show aunt 136
        show mom 93f
        mom "Haha!"
        show mom 91f
        show aunt 137
        dia "Goodnight, everyone!"
        show player 2
        player_name "Bye {b}Aunt Diane{/b}!"
        hide mom
        hide aunt
        hide sis
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_diane_dinner_chat)
        $ unlock_ui()
        $ location_count = "Entrance"
        $ gTimer.tick()
    else:

        show player 2 with dissolve
        player_name "( Nobody's here. The table isn't set either. )"
    $ callScreen(location_count)

label dining_room_table_sis:
    scene dining_room with None
    show object_diningtable zorder 1 at Position(ypos=581)
    show sis 44 at left
    show player 316 zorder 0 at Position(xpos=610)
    with dissolve
    if not sister.completed(sis_breakfast):
        pause
        show sis 45
        show player 317
        pause
        show sis 44
        show player 316
        pause
        show sis 45
        show player 318
        pause
        show sis 44
        show player 319
        pause
        show sis 46
        pause
        show sis 47
        show player 320
        sis "So..."
        show sis 48
        player_name "Hmm?"
        show sis 47
        sis "I hear you're now working with {b}aunt Diane{/b}."
        show player 321
        show sis 48
        player_name "Yeah, and?"
        show player 320
        show sis 47
        sis "She paying you?"
        show player 321
        show sis 88
        player_name "Well, yeah."
        show player 322
        show sis 86
        sis "How much?"
        show player 323
        show sis 88
        player_name "That's kind of private..."
        show player 322
        show sis 87
        sis "Is she... paying you in any {b}other{/b} ways?"
        show player 323
        show sis 88
        player_name "What?"
        show player 322
        show sis 87
        sis "Come on, you know {b}aunt Diane{/b}!"
        show player 320
        show sis 86
        sis "She likes to give... hugs and kisses to her nephew."
        show player 321
        show sis 48
        player_name "I don't get it."
        show player 322
        show sis 47
        sis "Gosh, you're so dumb!"
        show sis 48
        player_name "..."
        show player 322
        show sis 47
        sis "Anyway, I was gonna ask you something, now that you're earning money..."
        show player 321
        show sis 88
        player_name "...Okay?"
        show player 320
        show sis 86
        sis "Can I borrow some {b}money{/b}?"
        show player 321
        show sis 88
        player_name "From me?!"
        show player 320
        show sis 86
        sis "Well, yeah."
        show player 320
        show sis 86
        sis "I know you're getting paid..."
        show sis 87
        sis "Plus, I need the money to start something up that will earn me my own money. Get it??"
        show player 322
        show sis 86
        sis "Besides, it's not like you have anything to spend it on!"
        show player 323
        show sis 88
        player_name "I don't know..."
        player_name "I worked hard for that money, {b}[sis_name]{/b}."
        show player 322
        show sis 86
        sis "Look, I'll pay you back one way or another! I'm your sister, dummy!"
        show sis 87
        sis "You can trust me..."
        show player 323
        show sis 88
        player_name "I'll think about it."
        show player 322
        show sis 86
        sis "That's fine, come see me when you've made up your mind."
        show player 323
        show sis 88
        player_name "Alright..."
        $ unlock_ui()
        $ sis_breakfast.finish()
    else:

        sis "..."
        show sis 47
        show player 318
        sis "What are you still doing here?"
        show sis 48
        show player 323
        player_name "Huh?"
        show sis 47
        show player 322
        if gTimer.is_weekend():
            sis "Shouldn't you be hanging out with {b}Erik{/b}?"
        else:
            sis "Shouldn't you be going to school?"
        show sis 48
        show player 321
        player_name "Oh, right..."
        show sis 87
        show player 322
        sis "Gosh, you're so stupid."
        show sis 86
        sis "Just come see me when you've made up your mind about our deal..."
    hide player
    hide sis
    with dissolve
    jump dining_room_dialogue