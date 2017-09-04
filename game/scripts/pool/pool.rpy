label pool_dialogue:
    $ location_count = "Pool"
    $ used_changing_girls = []
    if not gTimer.is_dark():
        if banned_from_pool:
            scene pool
            show player 108f at left with dissolve
            player_name "( I can't stay here. )"
            player_name "( I've been {b}banned{/b} from the pool grounds. )"
            show player 34 at left
            player_name "Hmm..."
            show player 35 at left
            player_name "( Maybe I should come back when {b}nobody is around{/b}... )"
            hide player 35 at left with dissolve
            hide pool
            hide ui
            jump map_dialogue

        elif gloryhole_done == 1 and not banned_from_pool:
            scene pool
            if wearing_swimsuit:
                show player 53f at left with dissolve
            else:
                show player 1 at left with dissolve
            show ronda 8 at right with dissolve
            ron "That took you long enough..."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 51f at left
            else:
                show player 11 at left
            player_name "..."
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "What do you mean?"
            show ronda 8 at right
            if wearing_swimsuit == True:
                show player 51f at left
            else:
                show player 13 at left
            ron "...Really?"
            ron "You think I'm stupid?"
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            show ronda 10 at right
            player_name "...What?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 53f at left
            else:
                show player 13 at left
            ron "You just spent an hour in the medic room with {b}Cassie{/b}."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "...And?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 53f at left
            else:
                show player 13 at left
            ron "Your dramatic performance in the pool earlier: Flashing everybody with your... boner..."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "What are you trying to say?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "Everybody knows {b}Cassie{/b} brings guys she likes in her medic room!!!"
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 37 at left
            player_name "You think she likes me?"
            show ronda 9 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "{b}OMG{/b}! Stop playing stupid with me!"
            ron "You don't think she was impressed with your {b}giant{/b} cock?!"
            ron "It's the only reason she took you {b}in there{/b}!!!"
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45
            else:
                show player 21 at left
            player_name "...You think my penis is big?"
            show ronda 9 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 22 at left
            ron "!!!"
            ron "That's not-"
            ron "I ain't saying that!"
            show ronda 10 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            player_name "..."
            show ronda 8 at right
            ron "She's a total slut, okay?"
            show ronda 10 at right
            if wearing_swimsuit:
                show player 50f at left
            else:
                show player 17 at left
            player_name "...She was very nice to me, actually."
            show ronda 8 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "Ugh. You pig..."
            hide player
            hide ronda 8 at right
            with dissolve
            hide pool
            $ gloryhole_done = 2
        $ callScreen(location_count)
    else:

        if banned_from_pool:
            scene pool_night zorder 1
            show player 14 zorder 2 at left with dissolve
            player_name "( There we go! )"
            show player 17 zorder 2 at left
            player_name "( I can finally swim in peace! )"
            show player 11 at left
            player_name "{b}*Water splashing*{/b}"
            show player 90 at left
            player_name "..."
            show player 127 at left
            player_name "( Is someone in the pool? )"
            player_name "( I can't see that well in the dark... )"
            hide player with dissolve
            scene pool_night02
            with dissolve
            scene pool_night03
            with Dissolve(0.2)
            scene pool_night04
            with Dissolve(0.2)
            scene pool_night05
            with Dissolve(0.2)
            show player 17 at left with dissolve
            player_name "( I guess I wasn't the only one with this idea! )"
            player_name "( I'm going in, too! )"
            show player 8 at left
            player_name "Here I come!!"
            jump in_pool_dialogue
        else:

            scene pool_night
            if wearing_swimsuit:
                show player 49f with dissolve
            else:
                show player 2 with dissolve
            player_name "( The {b}pool{/b} is closed. I don't think I can swim right now. )"
            hide player with dissolve
            hide pool_night
    $ callScreen(location_count)

label cassie_button_dialogue:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    cas "Can I help you with something?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm... What are the {b}rules{/b} again?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cas "Well, you can't swim in your clothes..."
    show cassie 3
    cas "You have to use one of the {b}changing rooms{/b} to put on a {b}swimsuit{/b}!"
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    show cassie 4
    player_name "Oh. Great! Thanks!"
    $ callScreen(location_count)

label ronda_button_dialogue:
    scene location_pool_closeup2
    if gloryhole_done == 0:
        if wearing_swimsuit:
            show player 53f at left with dissolve
        else:
            show player 1 at left with dissolve
        show ronda 5 at right with dissolve
        ron "..."
        show ronda 6 at right
        ron "What are you even doing here?"
        show ronda 5 at right
        if wearing_swimsuit:
            show player 50f at left
        else:
            show player 17 at left
        player_name "Just getting some exercise!"
        player_name "I figured I had to start somewhere, and it can help me get ready for the qualifiers!"
        show ronda 6 at right
        if wearing_swimsuit:
            show player 51 at left
        else:
            show player 11 at left
        ron "Look: I ain't helping you, let alone go in the water at the same time as you... So forget it, okay?"
        show ronda 5 at right
        if wearing_swimsuit:
            show player 53 at left
        else:
            show player 26 at left
        player_name "That's fine!"
        player_name "I can manage on my own..."
        show ronda 7 at right
        if wearing_swimsuit:
            show player 51 at left
        else:
            show player 11 at left
        ron "Ugh... Whateva."
        $ pool_count = 4
        hide player
        hide ronda 7 at right
        with dissolve
        hide pool
    else:

        if wearing_swimsuit:
            show player 53f at left with dissolve
        else:
            show player 1 at left with dissolve
        show ronda 8 at right with dissolve
        ron "Here to pay Cassie a little visit?"
        show ronda 10 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 12 at left
        player_name "Uhh... I'm just here to swim?"
        show ronda 8 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 11 at left
        ron "You can stop pretending..."
        ron "...You ain't here to train, like I am."
        show ronda 8 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 12 at left
        player_name "Uhh... okay?"
        show ronda 9 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 11 at left
        ron "Ugh... you're pathetic."
        hide player
        hide ronda 9 at right
        with dissolve
    $ callScreen(location_count)

label poolrules01_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*WHISTLE*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Hey!"
    cas "You can't go in the pool dressed like that!"
    cas "You have to change, first!"
    if quest03 not in completed_quests:
        $ quest_list.append(quest03)
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Sorry! It's my first time here..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "Just use one of the {b}three changing rooms{/b}..."
    show cassie 3 at right
    cas "...And if you don't have a {b}swimsuit{/b}, then I can't let you in!"
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Right! Gotcha!"
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label poolrules02_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53 at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*WHISTLE*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Hey! {b}[firstname]{/b}!!"
    cas "Did you forget to change again?"
    cas "You know you have to change first..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Oh, hey, {b}Cassie{/b}!"
    player_name "Sorry, I forgot!"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "You should use the medic room... No one else is using it..."
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Okay! Thanks..."
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label poolrules03_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*WHISTLE*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Hey!"
    cas "That's the medic room!"
    cas "You can't go in there. It's for staff only."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Sorry! It's my first time here..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "Just use one of the {b}three changing rooms{/b}..."
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Right! Gotcha!"
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label pool_cutscene01:
    $ first_swim = False
    $ almost_drowned = True
    show poolcutscene01 with dissolve
    show text "It's my first time in the pool since I was in grade school.\nI'm only a few laps into my training and I'm tired!\nOnly a few more laps..." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show poolcutscene01b with dissolve
    show text "What's happening...\nI don't have the strength... so heavy...\nI can't-" at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    hide poolcutscene01
    hide poolcutscene01b with dissolve

    $ changing_count = 0

    scene black with dissolve
    with Pause(0.5)
    jump rescued_dialogue

label pool_cutscene02:
    show poolcutscene01 with dissolve
    show text "It's not my first time in the pool anymore and I've learned to pace myself.\nI'm able to do a few laps without issues and finish my training!." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide ui
    hide text with dissolve
    scene black with dissolve
    hide poolcutscene01

    $ changing_count = 0

    with Pause(0.3)
    if not ronda_after_swimming:
        jump ronda_after_swimming
    else:
        jump pool_dialogue

label ronda_after_swimming:
    scene pool
    show player 46 at left with dissolve
    show ronda 6 at right with dissolve
    ron "Not bad!"
    ron "At least you didn't drown this time..."
    show ronda 5 at right
    show player 47 at left
    player_name "Uhh... Thanks?"
    show player 48 at left
    show ronda 8 at right
    ron "Don't be too flatered. I've seen dogs swim better..."
    hide player
    hide ronda 8 at right
    with dissolve
    hide pool
    $ ronda_after_swimming = True
    $ callScreen(location_count)

label changing01_dialogue:
    $ rand_girl = renpy.random.choice(changing_girls)
    if wearing_swimsuit:
        scene changeroom01
        show player 45 with dissolve
        player_name "Uhm..."
        player_name "( I've already changed... I don't need to be here. )"
        hide player 45 with dissolve
        hide changeroom01
        $ callScreen(location_count)

    elif changing_count == 0 and not wearing_swimsuit:
        scene changeroom01
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1 at right with dissolve
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2 at right with dissolve
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3 at right with dissolve
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4 at right with dissolve
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5 at right with dissolve
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6 at right with dissolve
        else:
            jump changing01_dialogue
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 at left with hpunch
        player_name "..."
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1b at right
            $ used_changing_girls.append("girl1")
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2b at right
            $ used_changing_girls.append("girl2")
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3b at right
            $ used_changing_girls.append("girl3")
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4b at right
            $ used_changing_girls.append("girl4")
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5b at right
            $ used_changing_girls.append("girl5")
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6b at right
            $ used_changing_girls.append("girl6")
        if rand_girl == "girl1":
            Character("Emma") "Hey! Get out of here!!!"
        elif rand_girl == "girl2":
            Character("Lily") "What are you doing, you creep?!"
        elif rand_girl == "girl3":
            Character("Olivia") "Hey, you should buy me a drink first!"
        elif rand_girl == "girl4":
            Character("Ivy") "Hey, you should buy me a drink first!"
        elif rand_girl == "girl5":
            Character("Amelie") "Hey! Get out of here!!!"
        elif rand_girl == "girl6":
            Character("Sammy") "What are you doing, you creep?!"
        show player 42 at left
        player_name "Oops!"
        player_name "...Sorry!"
        hide player 42 at left with dissolve
        hide changing
        hide changeroom01
        $ changing_count = 1
        $ callScreen(location_count)

    elif changing_count == 1 and not wearing_swimsuit:
        scene changeroom01
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1 at right with dissolve
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2 at right with dissolve
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3 at right with dissolve
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4 at right with dissolve
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5 at right with dissolve
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6 at right with dissolve
        else:
            jump changing01_dialogue
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 at left with hpunch
        player_name "..."
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1b at right
            $ used_changing_girls.append("girl1")
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2b at right
            $ used_changing_girls.append("girl2")
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3b at right
            $ used_changing_girls.append("girl3")
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4b at right
            $ used_changing_girls.append("girl4")
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5b at right
            $ used_changing_girls.append("girl5")
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6b at right
            $ used_changing_girls.append("girl6")
        if rand_girl == "girl1":
            Character("Emma") "Hey!... Get out of here!!!"
        elif rand_girl == "girl2":
            Character("Lily") "What are you doing, you creep?!"
        elif rand_girl == "girl3":
            Character("Olivia") "Hey, you should buy me a drink first!"
        elif rand_girl == "girl4":
            Character("Ivy") "Hey, you should buy me a drink first!"
        elif rand_girl == "girl5":
            Character("Amelie") "Hey! Get out of here!!!"
        elif rand_girl == "girl6":
            Character("Sammy") "What are you doing, you creep?!"
        show player 42 at left
        player_name "Oops!"
        player_name "...Sorry!"
        hide changing with dissolve
        $ changing_count = 2
        if first_time_changing:
            $ first_time_changing = False
            jump caught_dialogue
        hide player 42 at left with dissolve
        hide changeroom01
        $ callScreen(location_count)

    elif changing_count == 2 and not wearing_swimsuit:
        scene changeroom01
        show player 43 with dissolve
        player_name "Finally! A free room!"
        show player 35
        player_name "( They should really add signs to let you know when it's busy... )"
        show player 8
        window hide
        pause
        hide player 8
        show player 44
        player_name "( There we are! All ready! )"
        hide player 44
        hide changeroom01
        $ wearing_swimsuit = True
        $ changing_count = 3
        $ poolrules_count = 3
        $ used_changing_girls = []
    $ callScreen(location_count)

label caught_dialogue:
    scene changeroom01
    show player 5f at right
    show cassie 61 at left
    with dissolve
    cas "What's going on in here?!"
    show cassie 60
    show player 22f
    player_name "!!!"
    show cassie 59
    show player 13f
    cas "{b}You{/b} again?!"
    cas "I just got a harassment complaint-"
    show cassie 60
    show player 10f
    player_name "No, It's not what it looks like!!"
    show player 11f
    show cassie 59
    cas "To me, it looks like you're trying to watch girls changing..."
    show player 10f
    show cassie 60
    player_name "I was just trying to find a room-"
    show player 5f
    show cassie 59
    cas "And you didn't think to check first??"
    show player 10f
    show cassie 60
    player_name "But, there's no door to knock on-"
    show player 11f
    show cassie 59
    cas "Save your excuses for someone else."
    show player 23f with hpunch
    cas "You're {b}banned{/b} from the pool grounds."
    show player 10f
    show cassie 60
    player_name "What?!"
    player_name "But I need to train for my school trial-"
    show player 5f
    show cassie 61
    cas "And that's my problem, how?"
    cas "I'm gonna have to ask you to {b}leave{/b} now."
    show player 10f
    show cassie 60
    player_name "..."
    $ banned_from_pool = True
    $ used_changing_girls = []
    hide player
    hide cassie
    hide changeroom01
    hide ui
    jump map_dialogue

label in_pool_dialogue:
    scene pool_water_night
    show cassie 62 zorder 2 at right
    with fade
    window hide
    pause
    show player 115 zorder 1 at Position(xpos = 230, ypos = 470) with Dissolve(0.3)
    window hide
    show player 116 zorder 1 at left
    show cassie 63 zorder 2
    with Dissolve(0.4)
    cas "!!!"
    show player 123 at left with dissolve
    player_name "OH! SHIT!"
    show cassie 73
    player_name "You're {b}naked{/b}!!?"
    show cassie 67
    show player 125 at left
    cas "WHAT ARE YOU DOING HERE??!"
    show player 120 at left
    show cassie 73
    player_name "Hey! You're the {b}lifeguard{/b} who works here during the day!!"
    show player 121 at left
    show cassie 72
    cas "..."
    show player 124 at left
    show cassie 67
    cas "Wait... You're that pervert spying on the girls!"
    show player 125 at left
    cas "Didn't I say you're not allowed here anymore??"
    show player 120 at left
    show cassie 66
    player_name "Hey!! That's {b}NOT{/b} what I was doing!"
    show player 126 at left
    player_name "And I'm not allowed here during the day so I had to come at night!"
    show player 120 at left
    player_name "...Wait a second..."
    show cassie 73
    player_name "What are {b}YOU{/b} doing here naked at night anyway??"
    show player 121 at left
    show cassie 64
    cas "I... Ugh... Just don't tell anyone!"
    show player 124 at left
    cas "We can both get in trouble for being here after hours..."
    show cassie 65
    show player 126 at left
    player_name "Well... I won't tell anyone but you have to let me train again!"
    show cassie 64
    show player 122 at left
    cas "Ugh... Just get me a towel..."
    show cassie 65
    show player 118 at left
    window hide
    pause
    show player 119 at left
    player_name "Here."
    show player 117 at left
    show cassie 68
    with dissolve
    cas "Thanks."
    show cassie 69
    cas "..."
    show player 124 at left
    show cassie 68
    cas "Sorry about kicking you out of the pool grounds..."
    cas "I'll let you in next time, I promise."
    show player 122 at left
    show cassie 70
    player_name "Sweet! Thanks!"
    player_name "I'll do a few laps now If you don't mind."
    show player 124 at left
    show cassie 71
    cas "Are you crazy?! We're both leaving now before someone sees us!"
    show player 126 at left
    show cassie 70
    player_name "Okay, okay!"
    $ banned_from_pool = False
    hide cassie
    hide player
    with dissolve
    hide pool_water_night
    hide ui
    jump map_dialogue

label rescued_dialogue:
    scene rescued
    show cassie 6 at Position (xpos = 564, ypos = 768) with dissolve
    cas "OKAY, LISTEN EVERYONE!!!"
    cas "YOU HAVE TO MAKE SOME ROOM!"
    show cassie 7
    cas "I have to perform {b}CPR{/b}!"
    show cassie 8
    window hide
    pause
    show cassie 8
    cas "Okay, this should work..."
    show cassie 9
    window hide
    pause
    show cassie 8
    cas "Come on..."
    show cassie 9
    window hide
    pause
    show cassie 10
    window hide
    pause
    show cassie 11
    window hide
    pause
    show cassie 12 with hpunch
    window hide
    pause
    show cassie 12
    cas "..."
    show cassie 13
    cas "Nothing to see here folks!!!"
    cas "You can go back in the pool now..."
    show cassie 15
    player_name "{b}*Cough*{/b}"
    show cassie 14
    cas "...All right, you're causing way too much trouble around here..."
    cas "I'm taking you in my medical room until you're fit to go."
    hide cassie 1
    hide rescued
    jump medic_dialogue

label medic_dialogue:
    if gloryhole_done == 0:
        $ gloryhole_done = 1
    scene changeroom02
    if medic_dialogue_count == 0:
        show cassie 36 with dissolve
        cas "How are you feeling?"
        show cassie 38
        player_name "{b}*Cough*{/b}"
        show cassie 37
        player_name "I think I'm alright..."
        show cassie 36
        cas "Well, I'm just glad that you're alive..."
        show cassie 41
        cas "...And don't you know how to swim?!"
        show cassie 38
        player_name "{b}*Cough*{/b}, it's not like that..."
        show cassie 37
        player_name "...I was, {b}*cough*{/b}, training..."
        player_name "...And I ran out of stamina."
        show cassie 41
        cas "Look, it's great that you're training, but you have to start slow."
        cas "I don't mind you staying at the pool and continue you training, but..."
        cas "...I can't let you walk around like that..."
        show cassie 38
        player_name "I'm, {b}*cough*{/b}, so sorry about that."
        show cassie 39
        player_name "When I felt you touching me, your lips... I..."
        player_name "...I don't know why this keeps happening lately..."
        show cassie 40
        cas "Haha!"
        cas "Hmmm... Well..."
        show cassie 41
        cas "Have you ever been... You know, with a girl?"
        show cassie 44
        player_name "Yeah... Obviously! Like, so many times..."
        show cassie 41
        cas "...Really?"
        show cassie 39
        player_name "{b}*Sigh*{/b}"
        player_name "I almost dated a girl once..."
        show cassie 40
        cas "Haha!"
        cas "That's it??"
        show cassie 39
        player_name "Well! ...We touched hands and stuff..."
        player_name "...But then, {b}this{/b} happened... And she screamed, and..."
        player_name "Anyway, it was a long time ago so."
        show cassie 41
        cas "Wow... so, you're like a virgin?"
        show cassie 39
        player_name "I, I guess so?"
        show cassie 40
        cas "You're cute."
        show cassie 45
        player_name "..."
        show cassie 46
        cas "Do you mind If I have a look at this problem we have here?"
        player_name "Uhh... Sure."
        show cassie 42 with hpunch
        window hide
        pause
        show cassie 43 with hpunch
        window hide
        pause
        show cassie 42 with hpunch
        window hide
        pause
        show cassie 46
        cas "Okay, I know how to fix this."
        cas "Listen carefully now..."
        show cassie 47 at Position (xpos=447)
        cas "All you have to do, is place your dick in that hole on the wall."
        cas "It's gonna feel nice and warm on the other side..."
        show cassie 49
        cas "...And then, you will feel {b}much{/b} better after. Trust me..."
        show cassie 48
        player_name "You mean... I have to put my penis in that hole?!"
        show cassie 49
        cas "That's right! Simple, right?"
        menu:
            "Ok, let's try it.":
                show cassie 37 at center
                player_name "Uhmm... Okay, but you can't look."
                show cassie 46
                cas "Oh, don't you worry about that..."
                show cassie 44
                player_name "Why? You're leaving?"
                show cassie 40
                cas "Of course! I'll be right back..."
                hide cassie 1 with dissolve
                hide changeroom02
                $ pool_count = 1
                $ medic_dialogue_count = 1
                jump gloryhole_medic
            "I don't feel like it.":

                show cassie 39 at center
                player_name "I don't know... I don't really feel comfortable with this."
                show cassie 41
                cas "..."
                show cassie 41
                cas "No wonder you've never been with a girl..."
                show cassie 44
                player_name "I'll just wait here for a bit, until it goes away..."
                player_name "Thanks for saving me earlier..."
                show cassie 41
                cas "...Sure, no problem..."
                hide cassie 41 with dissolve
                hide changeroom02
                $ medic_dialogue_count = 2
                jump pool_dialogue

    if medic_dialogue_count == 1:
        show player 49 at right with dissolve
        show cassie 58 at left with dissolve
        player_name "Woah... That was..."
        show cassie 50 at left
        show player 53 at right
        cas "...Amazing huh?"
        show player 52 at right
        show cassie 53 at left
        player_name "Yeah..."
        show cassie 52 at left
        show player 51 at right
        cas "Listen, this medic room is not open to the public, okay?"
        cas "So I can't just let anyone come in here at all times..."
        show cassie 54 at left
        cas "...but for you I'll make an exception."
        show cassie 53 at left
        show player 52 at right
        player_name "Really?"
        show cassie 52 at left
        show player 51 at right
        cas "Just don't tell anyone, alright?"
        show cassie 53 at left
        show player 50 at right
        player_name "...sure thing {b}Cassie{/b}!"
        show cassie 55 at left
        show player 52 at right
        cas "Alright, see ya next time... my big man!"
        hide player 52 at right with dissolve
        hide cassie 55 at left with dissolve

        show unlock19 at truecenter
        $ renpy.pause()
        hide unlock19 with dissolve

        $ medic_dialogue_count = 2
        hide changeroom02
        jump pool_dialogue

    if medic_dialogue_count == 2:
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 1f at right with dissolve
        show cassie 52 at left with dissolve
        cas "I thought I saw you walk in here..."
        show cassie 53 at left
        if wearing_swimsuit:
            show player 49 at right
        else:
            show player 14f at right
        player_name "Hey {b}Cassie{/b}!"
        show cassie 52 at left
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 1f at right with dissolve
        cas "Let me guess..."
        cas "You're having some issues down there again big man?"
        show cassie 54 at left
        cas "You need some... relief?"
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 29f at right
        show cassie 53 at left
        player_name "Well..."
        menu:
            "I'd love to.":
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 21f at right
                show cassie 53 at left
                player_name "Yeah, actually I do..."
                show cassie 52 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 13f at right
                cas "That's what I thought..."
                show cassie 53 at left
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 21f at right
                player_name "You think I can do that thing again? And... put it in the hole?"
                show cassie 55 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 13f at right
                cas "Of course! Just stick it in there and I'll come back in a minute..."
                hide player
                hide cassie 55 at left
                with dissolve
                hide changeroom02
                $ medic_dialogue_count = 3
                jump gloryhole_medic
            "Just changing.":

                if wearing_swimsuit:
                    show player 50 at right
                else:
                    show player 17f at right
                show cassie 53 at left
                player_name "Actually, I just needed to change in here..."
                show cassie 57 at left
                if wearing_swimsuit:
                    show player 51 at right
                else:
                    show player 11f at right
                cas "..."
                show cassie 56 at left
                cas "Well, that's unfortunate..."
                show cassie 57 at left
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 10f at right
                player_name "Sorry..."
                player_name "I'd love to spend some time here, but I have to get back to my training!"
                show cassie 55 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 1f at right
                cas "...It's okay. You get back out there, then."
                hide cassie 55 at left with dissolve
                show player 8f at right with dissolve
                window hide
                pause
                hide player 8f at right
                if wearing_swimsuit:
                    show player 33f at right
                    $ wearing_swimsuit = False
                    $ changing_count = 0
                else:
                    show player 44f at right
                    $ wearing_swimsuit = True
                player_name "There we are! All ready!"
                $ used_changing_girls = []
                hide player 44 at right with dissolve
                hide changeroom02
                jump pool_dialogue
    else:

        show player 17f at right with dissolve
        show cassie 50 at left with dissolve
        player_name "That was... Amazing..."
        show player 13f at right
        show cassie 51 at left
        cas "I'm glad you feel better..."
        show player 14f at right
        show cassie 53 at left
        player_name "Thank you so much..."
        show cassie 54 at left
        show player 1f at right
        cas "Just remember to keep this between us, okay?"
        show cassie 53 at left
        show player 18f at right
        player_name "Yeah, of course!"
        show cassie 55 at left
        show player 1f at right
        cas "Alright... I'll see you again soon, then."
        $ medic_dialogue_count = 2
        hide player 1f at right with dissolve
        hide cassie 55 at left with dissolve
        hide changeroom02
        jump pool_dialogue

label gloryhole_medic:
    $ gTimer.tick()
    scene changeroom03
    show cassie 16 at Position(xpos = 431, ypos = 768)
    with fade
    window hide
    pause
    show cassie 17
    window hide
    pause
    show cassie 18 with hpunch
    window hide
    pause
    cas "!!!"
    show cassie 19
    cas "Oh wow..."
    cas "( I just love his cock... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    cas "( The length... )"
    show cassie 21 at Position (xpos = 440, ypos = 768)
    cas "( ...the thickness... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 21 at Position (xpos = 440, ypos = 768)
    window hide
    pause
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 22 at Position (xpos = 434, ypos = 768) with hpunch
    window hide
    pause
    show cassie 23 at Position (xpos = 430, ypos = 768)
    cas "( It just twitched! )"
    show cassie 24 at Position (xpos = 431, ypos = 768)
    cas "( Let's see... what should I do with this thing? )"
    hide cassie 24
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_bj:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_27 at Position (xpos = 444, ypos = 768)
    pause 4
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    hide cassie 26_28
    hide changeroom03
    call screen gloryhole_stage02

label gloryhole_medic_bjfacefinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 29 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 30 with hpunch
    pause .3
    show cassie 31
    pause .5
    show cassie 31
    cas "Wow... So much cum..."
    hide cassie 31
    hide changeroom03
    jump medic_dialogue

label gloryhole_medic_bjtitsfinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 32 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 33 with hpunch
    pause .3
    show cassie 34
    pause .5
    show cassie 34
    cas "Wow... That's a lot of cum..."
    hide cassie 34
    hide changeroom03
    jump medic_dialogue

label gloryhole_medic_fuck_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( I don't know this guy well enough to do that... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_fuckraw_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( That's crazy!!! I can't do that... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_swallow_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( I don't know this guy well enough to do that... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage02

label locked_door26_dialogue:
    scene pool
    show player 35 with dissolve
    player_name "( I should get a {b}swimsuit{/b} before I can change... )"
    player_name "( ...They should have some at the {b}Mall{/b}. )"
    hide player 35
    $ callScreen(location_count)