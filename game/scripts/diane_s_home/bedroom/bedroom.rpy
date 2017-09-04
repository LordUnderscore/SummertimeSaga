label dianebedroom_dialogue:
    $ location_count = "Diane's Bedroom"
    if aunt.started(aunt_drunken_splur):
        scene dianebedroom_b with None
        show diane_passedout_b at Position(xanchor = 0, yanchor = 0, xpos = 228, ypos = 141)
        show player 13 at left
        player_name "( Looks like she made it to her bed. )"
        show player 11
        player_name "( Is she okay? )"
        hide player with dissolve
    $ callScreen(location_count)

label diane_bedroom_dialogue:
    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        scene dianebed with None
        show diane 5
        player_name "!!!"
        player_name "( Her breasts are still hanging out of her overalls. )"
        player_name "( I don't know why she always thinks her body is old and ugly. )"
        player_name "..."
        player_name "( I should leave her alone and start working on the garden... )"
        $ ui_lock_count = 0
        $ aunt_drunken_splur.finish()

    elif aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        scene dianebedroom_closeup with None
        show aunt 152 at Position (xpos = 695)
        pause
        show player 23 at left with dissolve
        player_name "{b}Aunt Diane{/b}!"
        player_name "What's going on?!"
        show aunt 152
        show player 22 at left
        dia "EEEEEKKKKKK!!!!"
        show aunt 154
        dia "Help me!"
        show aunt 153
        pause
        show player 23
        player_name "What is it?!"
        show aunt 154
        show player 11
        dia "M-MM-MM-MOUSE!"
        show aunt 152
        dia "OVER THERE!"
        hide player
        show aunt 155
        with dissolve
        pause
        show aunt 156
        player_name "What? I can't see anything..."
        show aunt 155
        dia "No, over there!"
        show aunt 156
        player_name "I still don't see a mouse."
        show aunt 155
        dia "Its tail is right there between those shoes!"
        show aunt 155b
        pause
        show aunt 156
        player_name "{b}Aunt Diane{/b}..."
        player_name "I think your mouse is actually just a shoe lace."
        show aunt 155
        dia "What? Really!?"
        show aunt 156
        player_name "Yup."
        show aunt 155
        dia "..."
        dia "Well, set me down then. You better not be lying!"
        show aunt 156
        player_name "Don't worry, that shoe lace won't bite."
        show player 14 at Position(xpos=200)
        show aunt 144 at Position(xpos=650)
        with dissolve
        player_name "Are you alright?"
        show player 13
        show aunt 146
        dia "Yes, I'm fine."
        dia "Although, now I feel very silly for screaming at a shoe lace."
        show aunt 147
        dia "I could've sworn I saw it move..."
        show aunt 148
        show player 10
        player_name "You scared me!"
        player_name "I thought you were being robbed or something..."
        show player 5
        show aunt 145
        dia "Sorry! Just your {b}auntie{/b} screaming about an imaginary rodent. Haha."
        show aunt 144
        pause
        show aunt 149
        dia "I have to say... It was very sweet of you to come rescue me."
        show aunt 150
        show player 29 at Position(xoffset=34)
        player_name "Oh, I uhhh... It's just a normal reaction..."
        show player 13
        show aunt 149
        dia "Oh, how I wish I had a handsome man like you around the house!"
        show aunt 151
        dia "Someone strong... Willing to protect me, and to satisf-"
        show aunt 144b
        dia "!!!"
        show aunt 147
        dia "Oh, Heavens! I'm almost nude!!"
        show aunt 148
        show player 14
        player_name "It's alright, {b}Aunt Diane{/b}. I don't mind."
        show aunt 144
        player_name "I'm just happy you're safe."
        show player 13
        show aunt 149
        dia "Well, I'm still very inappropriately dressed right now."
        show aunt 151
        dia "I'm sorry you had to see this old lady's body."
        show aunt 150
        show player 33
        player_name "I don't think you look old at all."
        show player 13
        show aunt 147
        dia "Really?"
        show aunt 150
        show player 26
        player_name "Yeah, you... look beautiful, I think."
        show player 13
        show aunt 148
        dia "!!!"
        pause
        show player 11
        show aunt 146
        dia "Hahaha!"
        dia "You sure know how to make me laugh."
        show player 13
        show aunt 145
        dia "Thank you, {b}[firstname]{/b}, for everything. You're such a sweetheart."
        show player 14
        show aunt 144
        player_name "You're welcome {b}Aunt Diane{/b}."
        show player 26
        pause
        show player 25
        show aunt 150
        pause
        show aunt 149
        dia "I better finish changing into my clothes..."
        show player 29
        show aunt 150
        player_name "And I should probably go and tend to that garden now."
        hide player with dissolve
        scene dianeentrance
        show player 33 with dissolve
        player_name "(Wow...)"
        player_name "(Never thought I'd see {b}Aunt Diane{/b} like this.)"
        show player 203
        player_name "(...)"
        player_name "(She looks... Great.)"
        hide player with dissolve
        $ ui_lock_count = 0
        $ aunt_mouse_attack.finish()
        $ aunt.complete_events(aunt_mouse_attack)
        jump dianelobby_dialogue
    $ callScreen(location_count)