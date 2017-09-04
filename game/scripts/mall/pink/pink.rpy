label pink_dialogue:
    $ location_count = "Pink"
    default ivy_dialogue_count = 0
    default ivy_first_visit = True
    default ivy_xray_toggle = False
    default ivy_condom_on = True
    default xray_front = False
    default xray_needed = False
    default ivy_cum_inside = False

    if pink_count < 1:
        scene pink
        show player 23 with dissolve
        player_name "( Wow! )"
        show player 21
        player_name "( That's... There's a lot of weird stuff in here. )"
        show player 29
        player_name "( Hmm... Maybe these will come in handy one day... )"
        hide player 29 with dissolve
        hide pink
        $ pink_count = 1
    $ callScreen(location_count)

label ivy_button_dialogue:
    if ivy_dialogue_count == 0:
        scene location_pink_closeup
        $ ivy_dialogue_count = 1
        show player 1 at left with dissolve
        show ivy 2 at right with dissolve
        ivy "Hi!"
        ivy "Can I help you with something?"
        show player 29
        show ivy 1
        player_name "It's my first time here. I... Umm..."
        show player 13
        show ivy 3
        ivy "It's okay! I understand! Everyone's a little shy when they first come here..."
        show ivy 2
        ivy "We have a large selection of {b}toys{/b} and {b}sexy apparel{/b} that you can view on our wall display."
        show player 11
        ivy "We can also offer a... {b}full body massage session{/b} in one of our... private rooms."
        ivy "Our masseuse uses a variety of natural body relaxation techniques... That will surely satisfy your needs..."
        show player 12
        show ivy 1
        player_name "Oh... I didn't know you offered massages here."
        show player 1
        show ivy 3
        ivy "It's one of our... less advertised... services."
        show ivy 2
        ivy "Would you like to see our massage selection {b}pamphlet{/b}?"
        menu:
            "Okay.":
                show ivy 5
                show player 21
                player_name "I guess I could have a look at it..."
                show player 13
                show ivy 4
                ivy "Sure! Suit yourself!"
                hide ivy
                hide player
                with dissolve
                call screen pamphlet

            "Package." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show ivy 1
                show player 2
                player_name "I'm here to pick up a {b}package{/b}."
                show player 1
                show ivy 3
                ivy "Sure!"
                show ivy 2
                ivy "What name is it under?"
                show ivy 1
                show player 12
                player_name "{b}Diane{/b}?"
                show player 1
                show ivy 11
                ivy "Let me check... Right! Here it is!"
                show ivy 1
                show player 170
                player_name "Thanks!"
                show ivy 3
                show player 169
                ivy "Is this for your {b}girlfriend{/b}?"
                show ivy 1
                show player 171
                player_name "!!!"
                show player 29
                player_name "Oh... No! It's for... Ummm... Someone asked me to get it for them!"
                show ivy 2
                show player 13
                ivy "Well, it's a really nice item from our collection..."
                show ivy 3
                ivy "I'm sure you'll like it!"
                show player 21
                show ivy 4
                player_name "Thanks..."
                hide player 21
                hide ivy 4
                show unlock29 at truecenter
                with dissolve
                $ inventory.items.append(package)
                $ renpy.pause()
                hide unlock29 with dissolve
            "Just shopping.":

                show player 10
                show ivy 1
                player_name "I'm fine, thank you."
                player_name "I'm just here to do some shopping..."
                show player 13
                show ivy 3
                ivy "Alright, then! Let me know if you need anything else."
        $ callScreen(location_count)
    else:

        scene pink
        show player 1 at left with dissolve
        show ivy 2 at right with dissolve
        ivy "Hi!"
        ivy "Can I help you with something?"
        menu:
            "Package." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show ivy 1
                show player 2
                player_name "Hi!"
                player_name "I'm here to pick up a {b}package{/b}."
                show player 1
                show ivy 3
                ivy "Sure!"
                show ivy 2
                ivy "What name is it under?"
                show ivy 1
                show player 12
                player_name "{b}Diane{/b}?"
                show player 1
                show ivy 11
                ivy "Let me check... Right! Here it is!"
                show ivy 1
                show player 170
                player_name "Thanks!"
                show ivy 3
                show player 169
                ivy "Is this for your {b}girlfriend{/b}?"
                show ivy 1
                show player 171
                player_name "!!!"
                show player 29
                player_name "Oh... No! It's for... Ummm... Someone asked me to get it for them!"
                show ivy 2
                show player 13
                ivy "Well, it's a really nice item from our collection..."
                show ivy 3
                ivy "I'm sure you'll like it!"
                show player 21
                show ivy 4
                player_name "Thanks..."
                hide player 21
                hide ivy 4
                show unlock29 at truecenter
                with dissolve
                $ inventory.items.append(package)
                $ renpy.pause()
                hide unlock29 with dissolve
            "Massage.":

                show ivy 5
                show player 21
                player_name "Could I see... your massage pamphlet?"
                show player 13
                show ivy 4
                ivy "Sure! Suit yourself!"
                player_name "Thanks..."
                hide ivy
                hide player
                with dissolve
                call screen pamphlet
            "Just shopping.":

                show player 10
                show ivy 1
                player_name "I'm just here to do some shopping..."
                show player 13
                show ivy 3
                ivy "Alright, then! Let me know if you need anything."
        $ callScreen(location_count)

label ivy_paizuri:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "I'll try the basic."
    ivy "Testing the waters, huh?"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "Heh, I'm just teasing!"
    show ivy 12
    ivy "Follow me."
    scene massage_room_closeup
    with dissolve
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    if ivy_first_visit == True:
        show player 43 at left
        player_name "{b}*Whistle*{/b} Cool room."
        show player 1
        show ivy 3 at right with dissolve
        ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
        show ivy 2
        ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
        ivy "I'll give you a few minutes to prepare."
        ivy "Have to make sure nobody can interrupt us..."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew! That was way less awkward than I expected it to be! )"
        scene blank with dissolve
        scene massage_room_closeup
        show player 175 at left
        with dissolve
        player_name "( I didn't expect it to be so straightforward, though... )"
        show player 57
        player_name "( Am I really ready for this yet? )"
        player_name "( ...I can't turn back now. )"
        show player 175
        player_name "( Might as well enjoy it. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        with dissolve
        ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
        ivy "We don't need towels for this kind of massage."
        player_name "Oh. Sorry..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "There! That's much better, isn't it?"
        player_name "Yeah, it is."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "How on Earth do you hide that thing?"
        ivy "In any case: name's Ivy."
        ivy "Now, my turn to prepare..."
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Like what you see?"
        player_name "Yeah..."
        ivy "{b}*Giggle*{/b} Well, your friend sure looks like he does."
        ivy "I guess I'll have to take care of that..."
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 7 at Position (xpos=518,ypos=725) with dissolve
        ivy "Before we start, I should let you know something."
        ivy "This room is soundproof..."
        player_name "( Oh? )"
        ivy "...so you don't have to hold anything back."
        ivy "Now, juuussst relax..."
        $ ivy_first_visit = False
    else:

        show player 1
        ivy "You know the drill. I'll be back in a minute."
        hide ivy with dissolve
        pause 0.5
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        with dissolve
        pause 2
        show ivy 18 at Position (xpos=870,ypos=655) with dissolve
        ivy "Okay! Good to go!"
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Let's do this!"
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 6 at Position (xpos=516,ypos=724)
    $ ivy_sex_speed = 0.8
    $ ivy_paizuri_stage = 0
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ xray_needed = False

    label ivy_paizuri_stage1:
        show playersex 19 zorder 1
        show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_paizuri_options
            hide screen ivy_sex_xray_button
            hide playersex 19
            hide ivysex 5
            show ivysex 6_5 at Position (xpos=513,ypos=728)
            pause 4
        else:

            hide screen ivy_paizuri_options
            hide screen ivy_sex_xray_button
            show ivysex 6 zorder 2 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
        $ ivy_paizuri_stage += 1
        if ivy_paizuri_stage == 1:
            if anim_toggle:
                ivy "I bet it doesn't feel this good when you use your hand..."
                player_name "( Not even fucking close! )"
                player_name "Faster..."
                hide ivysex 6_5
                show playersex 19 zorder 1
                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            else:

                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
                ivy "I bet it doesn't feel this good when you use your hand..."
                show ivysex 6 at Position (xpos=516,ypos=724)
                player_name "( Not even fucking close! )"
                show ivysex 5 at Position (xpos=514,ypos=729)
                player_name "Faster..."
                show ivysex 6 at Position (xpos=516,ypos=724)
            window hide

        elif ivy_paizuri_stage == 2:
            if anim_toggle:
                ivy "Are you-{b}*huff*{/b}-getting close?"
                player_name "Yeah..."
                ivy "Then let's kick it into high gear!"
                player_name "Aahh-gonna..."
                hide ivysex 6_5
                show playersex 19 zorder 1
                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            else:

                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
                ivy "Are you-*huff*-getting close?"
                show ivysex 6 at Position (xpos=516,ypos=724)
                player_name "Yeah..."
                ivy "Then let's kick it into high gear!"
                player_name "Aahh-gonna..."
            window hide

        elif ivy_paizuri_stage == 3:
            hide ivysex 6_5
            show playersex 19 zorder 1
            show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            player_name "...Gonna...CUM!"
            show ivysex 7 at Position (xpos=518,ypos=725)
            ivy "Do it!"
            window hide
            show white zorder 4 with dissolve
            hide white with dissolve
            show expression "characters/player/char_player_sex_25.png" zorder 3 at Position (xpos=498,ypos=400)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_25.png"
            show expression "characters/player/char_player_sex_26.png" zorder 3 at Position (xpos=498,ypos=400)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_26.png"
            show expression "characters/player/char_player_sex_27.png" zorder 3 at Position (xpos=500,ypos=434)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_27.png"
            show expression "characters/player/char_player_sex_28.png" zorder 3 at Position (xpos=503,ypos=434)
            with Dissolve(0.3)
            ivy "Wow.... there's so much..."
            ivy "Did you enjoy yourself?"
            player_name "Yeah... you're great at this."
            ivy "{b}*Giggle*{/b} I know."
            ivy "Such a mess though..."
            ivy "Let's get ourselves cleaned up."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_paizuri_options
        jump ivy_paizuri_stage1

label ivy_blowjob:
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Yeah. I'd like the classic, please."
    ivy "Oh? Been eying my lips?"
    show player 29
    player_name "I ehh..."
    show ivy 3
    ivy "Ease up, I'm just messing!"
    show ivy 12
    ivy "Follow me."
    scene massage_room_closeup
    show player 1 at left with dissolve
    show ivy 3 at right with dissolve
    ivy "Okay, I'll just make sure nobody can interrupt us."
    if ivy_first_visit == True:
        show player 43 at left
        player_name "{b}*Whistle*{/b} Cool room."
        show player 1
        ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
        show ivy 2
        ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
        ivy "I'll give you a few minutes to prepare."
        ivy "Have to make sure nobody can interrupt us..."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew, that was way less awkward than I expected it to be! )"
        show player 175 with dissolve
        player_name "( I didn't expect it to be so straightforward, though... )"
        show player 57
        player_name "( Am I really ready for this yet? )"
        player_name "( ...Nah, I can't turn back now. )"
        show player 175
        player_name "( Might as well enjoy it. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        with dissolve
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
        ivy "We don't need towels for this kind of massage."
        player_name "Oh, sorry..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "There, that's much better, isn't it?"
        player_name "Yeah, it is."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "How on Earth do you hide that thing?"
        ivy "In any case: name's Ivy."
        ivy "Now, my turn to prepare..."
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Like what you see?"
        player_name "Yeah..."
        ivy "{b}*Giggle*{/b} Well, your friend sure looks like he does."
        ivy "I guess I'll have to take care of that..."
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 2 at Position (xpos=515,ypos=723) with dissolve
        ivy "Before we start, I should let you know something."
        ivy "This room is soundproof..."
        player_name "( Oh? )"
        ivy "...so you don't have to hold anything back."
        ivy "Oh, and let me know when you're close, alright?"
        player_name "Sure thing."
        ivy "Now, just lay back and relax..."
        $ ivy_first_visit = False
    else:
        ivy "You know the drill, I'll be back in a minute."
        hide ivy with dissolve
        pause 0.5
        hide player
        scene massage_room
        show playersex 19 zorder 1
        with dissolve
        pause 2
        show ivy 18 at Position (xpos=870,ypos=655) with dissolve
        ivy "Okay! Good to go!"
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Let's do this!"
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 2 at Position (xpos=515,ypos=723)
    $ ivy_sex_speed = 0.8
    $ ivy_blowjob_stage = 0
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ xray_needed = False

    label ivy_blowjob_stage1:
        show playersex 19 zorder 1
        show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_blowjob_options
            hide screen ivy_sex_xray_button
            hide playersex 19
            hide ivysex 3
            show ivysex 4_3 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_blowjob_options
            hide screen ivy_sex_xray_button
            show ivysex 4 zorder 2 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
        $ ivy_blowjob_stage += 1
        if ivy_blowjob_stage == 1:
            if anim_toggle:
                player_name "( Man, if her mouth feels this good, actual sex must be insane... )"
                player_name "Aaah... Faster..."
                hide ivysex 4_3
                show playersex 19 zorder 1
                show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            else:
                show ivysex 3 at Position (xpos=515,ypos=724)
                player_name "( Man, if her mouth feels this good, actual sex must be insane... )"
                show ivysex 4 at Position (xpos=515,ypos=723)
                player_name "Aaah... Faster..."
            window hide
        elif ivy_blowjob_stage == 2:
            if anim_toggle:
                player_name "( Crap, I'm getting close... )"
                player_name "Faster."
                hide ivysex 4_3
                show playersex 19 zorder 1
                show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            else:
                show ivysex 3 at Position (xpos=515,ypos=724)
                player_name "( Crap, I'm getting close... )"
                show ivysex 4 at Position (xpos=515,ypos=723)
                player_name "Faster."
            window hide
        elif ivy_blowjob_stage == 3:
            hide ivysex 4_3
            show playersex 19 zorder 1
            show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            player_name "( Gotta warn her... )"
            show ivysex 4 at Position (xpos=515,ypos=723)
            player_name "I'm about to-"
            show ivysex 3 at Position (xpos=515,ypos=724)
            player_name "SHIT!"
            show white zorder 4 with dissolve
            hide white
            show ivysex 24 at Position (xpos=515,ypos=750)
            with dissolve
            show ivysex 25 at Position (xpos=515,ypos=750) with dissolve
            player_name "I uhh..."
            show ivysex 26 at Position (xpos=548,ypos=730)
            ivy "{b}*Cough*{/b} {b}*Cough*{/b}"
            ivy "What happened to the whole \"let me know\" part?"
            player_name "Uhh, sorry about that..."
            ivy "You know, usually I charge extra for swallowing."
            player_name "I..."
            player_name "( Crap, maybe I shouldn't have done that. )"
            show ivysex 1
            ivy "{b}*Giggle*{/b} Oh man, you should see the look on your face!"
            ivy "Don't worry about it, you were good practice! It's on the house."
            player_name "*nervous laugh* Thanks."
            player_name "Again, sorry about that..."
            ivy "Really, it's fine... You know, my usual customers don't usually pack this much {b}heat{/b}."
            player_name "Oh, uh, thanks, I guess."
            ivy "Now, let's get ourselves cleaned up."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_blowjob_options
        jump ivy_blowjob_stage1

label ivy_reverse_cowgirl:
    $ xray_front = False
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Yeah, I'll try the premium, please."
    ivy "Ohoh, quite bold for your age!"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "{b}*Giggle*{/b} I like an eager man!"
    show ivy 2
    ivy "Follow me."
    scene massage_room_closeup
    with dissolve
    show ivy 2 at right with dissolve
    show player 43 at left with dissolve
    ivy "Alright, I'll just make sure nobody can interrupt us."
    if ivy_first_visit == True:
        player_name "{b}*Whistle*{/b} Cool room."
        show player 1
        show ivy 3 at right
        ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
        show ivy 2
        ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
        ivy "I'll give you a few minutes to prepare."
        ivy "Have to make sure nobody can interrupt us."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew, that was way less awkward than I expected it to be! )"
        show player 175 with dissolve
        player_name "( I didn't expect it to be so straightforward though... )"
        show player 57
        player_name "( Am I really ready for this yet? )"
        player_name "( ...Nah, I can't turn back now. )"
        show player 175
        player_name "( Might as well enjoy it. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        with dissolve
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
        ivy "We don't need towels for this kind of massage."
        player_name "Oh. sorry..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "There! That's much better, isn't it?"
        player_name "Yeah, it is."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "How on Earth do you hide that thing?"
        ivy "In any case: Name's Ivy."
        ivy "Now, my turn to prepare..."
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "We're gonna need a condom for this one."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww, man..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Oh don't fret! you won't even notice that it's there. Trust me."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "And for the final part..."
    $ ivy_first_visit = False
    hide player
    scene massage_room
    show playersex 19 zorder 1
    if ivy_condom_on == True:
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 15 zorder 2 at Position (xpos=510,ypos=715)
    with dissolve
    pause
    show ivysex 16 zorder 2 at Position (xpos=520,ypos=720) with dissolve
    pause
    show ivysex 17 zorder 2 at Position (xpos=530,ypos=720) with dissolve
    ivy "{b}*Giggle*{/b} I wonder if it'll fit..."
    ivy "You ready to feel heaven?"
    player_name "{b}*Gulp*{/b} Yeah."
    ivy "Here we go..."
    show playersex 22
    show ivysex 18 zorder 2 at Position (xpos=538,ypos=726) with dissolve
    show ivysex 19 zorder 2 at Position (xpos=538,ypos=707) with dissolve
    player_name "Haaah-"
    show ivysex 20 zorder 2 at Position (xpos=538,ypos=724)
    ivy "You okay back there?"
    player_name "Yeah, go ahead..."
    $ ivy_sex_speed = 0.8
    $ ivy_rcowgirl_stage = 0
    $ xray = 1
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ ivy_cum_inside = False
    $ xray_front = False
    $ xray_needed = True

    label ivy_rcgirl_stage1:
        show playersex 22 zorder 1
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
        show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
        show screen ivy_sex_xray
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_rcowgirl_options
            hide screen ivy_sex_xray
            hide screen ivy_sex_xray_button
            hide playersex 22
            hide expression "characters/player/char_player_sex_29.png"
            hide ivysex 19
            if ivy_xray_toggle == True:
                show ivysex_xray 39_40 at Position (xpos=515,ypos=724)
            else:
                show ivysex 18_19 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_rcowgirl_options
            hide screen ivy_sex_xray_button
            $ xray = 0
            show ivysex 18 zorder 2 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
        $ ivy_rcowgirl_stage += 1
        if ivy_rcowgirl_stage == 1:
            if anim_toggle:
                player_name "( Holy shit, this feels amazing! )"
                player_name "You can go faster. I think I can handle it..."
                ivy "Okay. You asked for it!"
                hide ivysex 18_19
                hide ivysex_xray 39_40
                show playersex 22 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
                show screen ivy_sex_xray
            else:
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( Holy shit, this feels amazing! )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                player_name "You can go faster... I think I can handle it..."
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                ivy "Okay. You asked for it!"
            window hide
        elif ivy_rcowgirl_stage == 2:
            if anim_toggle:
                player_name "( Gotta hold out for just a while longer... )"
                ivy "Haah-I gotta say..."
                ivy "...you may be just a teenager..."
                ivy "...but you-aah-put some of my clients to shame!"
                player_name "( That's one way to boost my ego. )"
                player_name "( I wonder how she'd react to... )"
                hide ivysex 18_19
                hide ivysex_xray 39_40
                show playersex 22 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
                show screen ivy_sex_xray
            else:
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( Gotta hold out for just a while longer... )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                ivy "Haah-I gotta say..."
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                ivy "...you may be just a teenager..."
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                ivy "...but you-aah-put some of my clients to shame!"
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( That's one way to boost my ego. )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                player_name "( I wonder how she'd react to... )"
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
            window hide
        elif ivy_rcowgirl_stage == 3:
            show screen ivy_sex_xray
            $ xray = 1
            hide ivysex 18_19
            hide ivysex_xray 39_40
            show playersex 22 zorder 1
            show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
            show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
            player_name "( Crap, I'm at my limit! )"
            player_name "( She's way too good at this! )"
            player_name "I'm gonna cum!"
            menu:
                "Cum inside":
                    ivy "Haah- go ahead!"
                    hide screen ivy_sex_xray
                    $ ivy_cum_inside = True
                "Cum outside":
                    ivy "Haah- go ahead!"
                    hide screen ivy_sex_xray
                    $ ivy_cum_inside = False
            if ivy_cum_inside == True:
                show playersex 22
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=708)
            else:
                hide expression "characters/player/char_player_sex_29.png"
                show playersex 19
                show ivysex 16 zorder 2 at Position (xpos=521,ypos=718)
                show expression "characters/player/char_player_sex_25.png" zorder 3 at Position (xpos=494,ypos=415)
            show white zorder 3 with hpunch
            if ivy_cum_inside == True:
                show screen ivy_sex_xray
            hide white
            with dissolve
            ivy "Haaa..."
            hide expression "characters/player/char_player_sex_25.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_51.png" zorder 3 at Position (xpos=490,ypos=338)
            ivy "Haah... You lasted a pretty long time there... for a teenager."
            if ivy_cum_inside == True:
                hide screen ivy_sex_xray

            hide expression "characters/player/char_player_sex_29.png"
            if ivy_cum_inside == True:
                show playersex 19
                show ivysex 16 zorder 2 at Position (xpos=521,ypos=718)
                show expression "characters/player/char_player_sex_35.png" zorder 3 at Position (xpos=523,ypos=500)
            player_name "Thanks. You're amazing..."
            hide expression "characters/player/char_player_sex_35.png"
            hide expression "characters/player/char_player_sex_51.png"
            show playersex 19
            show ivysex 15 zorder 2 at Position (xpos=510,ypos=710)
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_52.png" zorder 3 at Position (xpos=511,ypos=275)
            else:
                show expression "characters/player/char_player_sex_31.png" zorder 3 at Position (xpos=513,ypos=526)
            window hide
            pause
            ivy "Let's get ourselves cleaned up..."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_rcowgirl_options
        jump ivy_rcgirl_stage1

label ivy_slap_ass:
    hide screen ivy_sex_xray_button
    show playersex 23
    show ivysex 20 at Position (xpos=538,ypos=724)
    pause 0.2
    if ivy_xray_toggle == True:
        hide screen ivy_sex_xray
        show expression "characters/player/char_player_sex_40b.png" zorder 3 at Position (xpos=517,ypos=581)
    show ivysex 21 at Position (xpos=537,ypos=724)
    show playersex 24 with vpunch
    pause 0.2
    ivy "{b}*Giggle*{/b} Getting even bolder?"
    ivy "Faster it is, then!"
    hide expression "characters/player/char_player_sex_40b.png"
    show playersex 22
    $ ivy_sex_speed -= 0.25
    jump ivy_rcgirl_stage1

label ivy_cowgirl:
    show ivy 5 at right
    show player 174 at left
    with dissolve
    player_name "Yeah, I'll have the ultimate, please."
    ivy "{b}*Giggle*{/b} You want to see it all, don't you?"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "I like myself an eager man."
    show ivy 2
    ivy "Follow me."
    scene massage_room_closeup
    with dissolve
    show ivy 2 at right with dissolve
    show player 43 at left with dissolve
    ivy "Alright, I'll just make sure nobody can interrupt us."
    if ivy_first_visit == True:
        player_name "{b}*Whistle*{/b} Cool room."
        show player 1
        show ivy 3
        ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
        show ivy 2
        ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
        ivy "I'll give you a few minutes to prepare."
        hide ivy 2
        scene blank with dissolve
        scene massage_room_closeup
        show player 175 at left
        with dissolve
        player_name "( Phew, that was way less awkward than I expected it to be! )"
        player_name "( I didn't expect this to be so straightforward, though. )"
        player_name "( Maybe I'm not really ready for something like this yet... )"
        player_name "( ...Nah. I can't turn back now. )"
        player_name "( I might as well enjoy it. )"
        scene massage_room
        hide player
        show playersex 19
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655)
        with dissolve
        ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
        ivy "We don't need towels for this kind of massage."
        player_name "Oh, sorry..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "There! That's much better, isn't it?"
        player_name "Yeah, it is."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "How on Earth do you hide that thing?"
        ivy "In any case: name's Ivy."
        ivy "Now, my turn to prepare..."
        $ ivy_first_visit = False
    scene massage_room
    hide player
    show playersex 19
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "We're gonna need a condom for this one."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww man..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Oh don't fret, you won't even notice that it's there. Trust me."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "And for the final part..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 8 zorder 2 at Position (xpos=496,ypos=750)
    with dissolve
    pause
    show ivysex 9 zorder 2 at Position (xpos=482,ypos=768) with dissolve
    pause
    show playersex 20
    show ivysex 10 zorder 2 at Position (xpos=532,ypos=770) with dissolve
    ivy "{b}*Giggle*{/b} I wonder if it'll fit..."
    show playersex 20
    ivy "You ready to feel heaven?"
    player_name "{b}*gulp*{/b} Yeah."
    ivy "Here we go..."
    show playersex 21
    show ivysex 11 zorder 2 at Position (xpos=535,ypos=766)
    player_name "Haaah-"
    show playersex 20
    show ivysex 10 zorder 2 at Position (xpos=532,ypos=770)
    ivy "You okay?"
    player_name "Yeah, go ahead..."
    $ ivy_sex_speed = 0.8
    $ ivy_cowgirl_stage = 0

    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ ivy_cum_inside = False
    $ xray_front = True
    $ xray_needed = True

    label ivy_cowgirl_stage1:
        $ xray = 1
        show playersex 21 zorder 1
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
        show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
        show screen ivy_sex_xray
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_cowgirl_options
            hide screen ivy_sex_xray
            hide screen ivy_sex_xray_button
            hide playersex 21
            hide expression "characters/player/char_player_sex_29.png"
            hide ivysex 11
            if ivy_xray_toggle == True:
                show ivysex_xray 36_37 at Position (xpos=515,ypos=724)
            else:
                show ivysex 10_11 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_cowgirl_options
            hide screen ivy_sex_xray_button
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
        $ ivy_cowgirl_stage += 1
        if ivy_cowgirl_stage == 1:
            if anim_toggle:
                player_name "( Holy shit, this feels amazing! )"
                player_name "You can go faster... I think I can handle it..."
                ivy "Okay, you asked for it!"
                hide ivysex 10_11
                hide ivysex_xray 36_37
                show playersex 21 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
                show screen ivy_sex_xray
            else:
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( Holy shit, this feels amazing! )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                player_name "You can go faster... I think I can handle it..."
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                ivy "Okay. You asked for it!"
            window hide
        elif ivy_cowgirl_stage == 2:
            if anim_toggle:
                player_name "( Gotta hold out for just a while longer... )"
                ivy "Haah-I gotta say..."
                ivy "...you may be just a teenager..."
                ivy "...but you-aah-put some of my clients to shame!"
                player_name "( That's one way to boost my ego. )"
                player_name "( I wonder how she'd react to... )"
                hide ivysex 10_11
                hide ivysex_xray 36_37
                show playersex 21 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
                show screen ivy_sex_xray
            else:
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( Gotta hold out for just a while longer... )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                ivy "Haah-I gotta say..."
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                ivy "...you may be just a teenager..."
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                ivy "...but you-aah-put some of my clients to shame!"
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( That's one way to boost my ego. )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                player_name "( I wonder how she'd react to... )"
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
            window hide
        elif ivy_cowgirl_stage == 3:
            show screen ivy_sex_xray
            $ xray = 1
            hide ivysex 10_11
            hide ivysex_xray 36_37
            show playersex 21 zorder 1
            show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
            show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
            player_name "( Crap, I'm at my limit! )"
            player_name "( She's way too good at this! )"
            player_name "I'm gonna cum!"
            menu:
                "Cum inside":
                    ivy "Haah- go ahead!"
                    hide screen ivy_sex_xray
                    $ ivy_cum_inside = True
                "Cum outside":
                    ivy "Haah- go ahead!"
                    hide screen ivy_sex_xray
                    $ ivy_cum_inside = False
            if ivy_cum_inside == True:
                show playersex 21
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
            else:
                hide expression "characters/player/char_player_sex_29.png"
                show playersex 20
                show ivysex 13 zorder 2 at Position (xpos=533,ypos=770)
                show expression "characters/player/char_player_sex_32.png" zorder 3 at Position (xpos=485,ypos=423)
            show white zorder 3 with hpunch
            if ivy_cum_inside == True:
                show screen ivy_sex_xray
            hide white
            with dissolve
            ivy "Haaa..."
            hide expression "characters/player/char_player_sex_32.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_33.png" zorder 3 at Position (xpos=460,ypos=405)
            ivy "Haah... You lasted a pretty long time there... for a teenager."
            hide expression "characters/player/char_player_sex_33.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_34.png" zorder 3 at Position (xpos=442,ypos=401)
            player_name "Thanks... You're amazing..."
            if ivy_cum_inside == True:
                hide screen ivy_sex_xray

            hide expression "characters/player/char_player_sex_34.png"
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 19
            show ivysex 9 zorder 2 at Position (xpos=483,ypos=769)
            if ivy_cum_inside == True:
                show expression "characters/player/char_player_sex_30.png" zorder 3 at Position (xpos=522,ypos=510)
                with dissolve
            pause
            hide expression "characters/player/char_player_sex_30.png"
            show ivysex 8 zorder 2 at Position (xpos=499,ypos=750)
            if ivy_cum_inside == True:
                show expression "characters/player/char_player_sex_31.png" zorder 3 at Position (xpos=514,ypos=524)
                with dissolve
            window hide
            pause
            ivy "Let's get ourselves cleaned up..."
            hide expression "characters/player/char_player_sex_31.png"
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_cowgirl_options
        jump ivy_cowgirl_stage1

label ivy_no_money:
    show player 13 at left
    show ivy 4 at right
    with dissolve
    player_name "( Darn, I can't afford this. )"
    player_name "On second thought, maybe some other time."
    $ callScreen(location_count)