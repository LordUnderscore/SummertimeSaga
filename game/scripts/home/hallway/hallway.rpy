default attic_unlocked = False

label hallway_dialogue:
    $ location_count = "Hallway"
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and shower != "" and gTimer.is_morning():
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if not gTimer.is_dark():
        if hallway_count == 0:
            scene hallway with None
            show player 1 at left
            show sis 10 at right
            with dissolve
            sis "Shouldn't you be at school?"
            show player 2
            player_name "Shouldn't you have a job?"
            show sis 6
            show player 1
            sis "!!!"
            show sis 9
            sis "Oh, you don't want to play this game with me, smart ass."
            show sis 6
            show player 14
            player_name "Hey, you started it!"
            show player 34
            player_name "..."
            show sis 10
            sis "What is it?"
            player_name "{b}*Sniff*{/b}"
            show player 35
            player_name "Do you smell that? {b}Mom's{/b} cooking!"
            show sis 9
            show player 11
            sis "Duh! {b}Mom{/b} made breakfast. She's {b}downstairs{/b} waiting for you."
            show sis 12
            sis "You'd know if, you were actually on time, for once."
            show player 2
            show sis 11
            player_name "Perfect! I was just on my way, actually..."
            hide player with dissolve
            pause 0.5
            show sis 10
            sis "Ugh. What have I done to deserve a younger brother like you..."
            hide sis
            with dissolve
            call screen sis_name_input
            if sis_name != "":
                $ sis = Character('[sis_name]', color="#ff6df0")
            $ hallway_count = 1

        elif henchmen_count == 2 and mother.over(mom_cuddling) and not mom_cuddling_unlocked and mom_count >= 10 and mom_revealing:
            scene hallway with None
            show mom 3 at right
            show player 1 at left
            with dissolve
            mom "Good morning, {b}[firstname]{/b}."
            show player 17
            show mom 1
            player_name "Morning, {b}Mom{/b}."
            show mom 2
            show player 1
            mom "Did you sleep well last night?"
            show player 10
            show mom 14
            player_name "I had a little trouble falling asleep at first, but I was fine."
            show mom 52
            show player 13
            mom "I know how you feel, Sweetie... I've been having trouble sleeping too."
            show player 5
            mom "Ever since your {b}dad{/b}... left us..."
            show player 24
            show mom 51
            player_name "It's okay, {b}Mom{/b}."
            show mom 52
            show player 5
            mom "I miss him so much..."
            show player 25
            show mom 51
            player_name "Me too, {b}Mom{/b}, me too..."
            hide player
            show mom 4 at center
            with fastdissolve
            pause
            show player 13 at left
            show mom 13 at right
            with fastdissolve
            mom "Mmm... Thanks for the hug, Sweetie."
            show mom 14
            pause
            show mom 13
            mom "If you ever have trouble sleeping at night, don't be afraid to let me know."
            show player 14
            show mom 14
            player_name "Will do, {b}Mom{/b}."
            show player 1
            show mom 2
            mom "Have a nice day, Sweetie."
            show player 17
            player_name "You too, {b}Mom{/b}."
            hide player
            hide mom
            with dissolve
            $ mom_cuddling_unlocked = True
            show unlock34 at truecenter with dissolve
            pause
            hide unlock34 with dissolve

        elif sister.started(sis_hallway01) and sister.over(sis_shower_cuddle02):
            scene hallway with None
            show sis 7 at right
            show player 11 at left
            with dissolve
            sis "Hey!"
            show sis 8
            show player 12
            player_name "What do you want?"
            show sis 9 at Position(xpos=937)
            show player 11
            sis "Have you been on my computer?"
            show sis 6
            show player 12
            player_name "Uh... No?"
            show sis 9
            show player 11
            sis "Don't {b}lie{/b} to me."
            sis "I know you've been snooping around my stuff..."
            show sis 10
            show player 12
            player_name "What?"
            player_name "I haven't even been in your room!"
            show sis 9
            show player 11
            sis "How did you know my password?"
            show sis 6
            show player 11
            player_name "..."
            show sis 9
            show player 5
            sis "What were you looking for anyway?"
            show sis 10
            show player 10
            player_name "Nothing! I told you-"
            show sis 9
            show player 11
            sis "Were you trying to find my {b}private{/b} pictures?"
            sis "So you could {b}use{/b} them?"
            show sis 6
            show player 10
            player_name "No! I told you-"
            show sis 9
            show player 11
            sis "It doesn't matter."
            sis "If you go through my things again, I'm telling {b}Mom{/b}."
            show sis 7 at right
            show player 5
            sis "UNDERSTOOD?!" with vpunch
            show sis 8
            show player 10
            player_name "Yeah..."
            hide player
            hide sis
            with dissolve
            $ sis_hallway01.finish()
            $ sister.add_event(sis_couch01)

        elif sister.started(sis_hallway02) and sister.over(sis_telescope02) and played_with_mom_panties == 1:
            scene hallway with None
            show sis 7 at right
            show player 11 at left
            with dissolve
            sis "Hold it right there!"
            show sis 8
            show player 12
            player_name "What do you want?"
            show sis 9 at Position(xpos=937)
            show player 11
            sis "Where are you going?"
            show sis 10
            show player 10
            player_name "Huh?"
            show sis 9
            show player 11
            sis "Meeting with {b}Mom{/b} in her room, perhaps?"
            show sis 6
            show player 29
            player_name "What?"
            show sis 9
            show player 11 at left
            sis "You've been sucking up to {b}Mom{/b} a lot lately."
            sis "I don't really care, to be honest: You always were her favorite."
            show sis 6
            show player 10
            player_name "... I don't understand."
            show sis 9
            show player 11
            sis "You can pretend all you want..."
            sis "... but I see the little game you're playing."
            show sis 10
            show player 14
            player_name "Well, {b}Mom{/b} needs help around the house so I'm-"
            show sis 9
            show player 11
            sis "Oh, stop it!"
            sis "Look, I don't care what you and {b}Mom{/b} do in secret."
            show player 16
            sis "We both know you're just a pervert."
            show player 11

            sis "What's important here is that I need you focused!"
            sis "I can't let you get distracted by {b}Mom{/b}."
            sis "I need fresh content for my {b}cam streams{/b}..."
            sis "... so you better get me those {b}props{/b}."
            show sis 11
            show player 12
            player_name "Chill out. I'll get them, okay?"
            show sis 12
            show player 13
            sis "Good."
            hide player
            hide sis
            with dissolve
            $ sis_hallway02.finish()
            $ sister.add_event(sis_shower_cuddle03)

        elif sister.started(sis_final) and sister.over(sis_shower_cuddle04) and not gTimer.is_dark():
            scene hallway with None
            show player 11 with dissolve
            player_name "..."
            player_name "( There're voices coming from my sister's room... )"
            show player 4
            player_name "( It sounds like... she's talking to someone? But who... )"
            show player 1
            player_name "( Maybe I can sneak up to her door and find out... )"
            hide player with dissolve
            $ ui_lock_count = 1

        elif sister.over(sis_final) and not sister.known(sis_final2):
            scene hallway with None
            show player 11 at left
            show sis 9 at right
            show sis 9 at Position(xpos=937)
            with dissolve
            sis "Psst, hey!!"
            show player 10
            show sis 9b
            player_name "Huh?"
            player_name "What're you doing?"
            show player 11
            show sis 9
            sis "Get in my room. Now!"
            show player 10
            show sis 10
            player_name "But, why?"
            show player 11
            show sis 9
            sis "Don't ask. Just do it, twerp!"
            scene sisbedroom
            show player 12 at left
            show sis 82 at right
            show sis 82 at Position(xpos=937)
            with fade
            player_name "What's going on?"
            show player 11
            show sis 12
            sis "I need a favor."
            show player 12
            show sis 82
            player_name "Let me guess, more sex toys?"
            show player 16
            show sis 9
            sis "No, you idiot!"
            show player 12
            show sis 10
            player_name "I'm not your servant, you know?"
            show player 16
            show sis 7 at right
            sis "Just SHUT UP already, and let me explain!!" with hpunch
            show player 11
            show sis 19
            sis "We'll both get what we want out of this..."
            sis "I promise."
            show player 12
            show sis 18
            player_name "... Okay?"
            show player 11
            show sis 12 at Position(xpos=937)
            sis "Good. Now, I need you to find some stuff for me. It's kind of specific, so you might have to look around."
            show player 10
            show sis 11
            player_name "What stuff?"
            show player 11
            show sis 12
            sis "First, I'm going to need a {b}cheerleader outfit{/b}."
            sis "Then, I'll need some {b}handcuffs{/b}."
            show player 10
            show sis 10
            player_name "Those are really specific... Where am I going to find those?"
            show player 11
            show sis 7 at right
            sis "I DON'T KNOW!"
            show sis 9 at Position(xpos=937)
            sis "That's your part of the deal! I don't care where you get them from, as long as you get them!"
            show player 12
            show sis 9b
            player_name "What do I get in return?"
            player_name "I don't need any more panties..."
            show player 11
            show sis 12
            sis "Don't worry about that! I'll get you something way better than panties!"
            show player 12
            show sis 10
            player_name "You won't even tell me what it is?"
            show player 11
            show sis 7 at right
            sis "I said, {b}DON'T WORRY{/b}!!"
            show sis 9 at Position(xpos=937)
            sis "It's more than you deserve, and you'll definitely like it, so just DO IT!"
            show player 10
            show sis 9b
            player_name "{b}*Sigh*{/b}"
            show sis 82
            player_name "Fine. I'll see what I can find..."
            show player 1
            show sis 12
            sis "Good."
            show player 11
            show sis 7 at right
            sis "Now {b}GET OUT{/b}!!" with hpunch
            hide player
            hide sis
            $ sister.add_event(sis_final2)

        if gTimer.is_morning() and shower == "sister" and (
                sister.started(sis_shower_cuddle01) or
                sister.started(sis_shower_cuddle02) or
                sister.started(sis_shower_cuddle03) or
                sister.started(sis_shower_cuddle04) or
                sister.started(sis_shower_cuddle05)
        ):
            scene hallway with None
            show player 14 at left
            with dissolve
            player_name "( Someone's in the shower. )"
            show player 26
            player_name "( I think they left the door unlocked... )"
            hide player
            with dissolve

        elif learn_kissing and not mom_revealing_tommorow and gTimer.is_morning() and shower == "mom":
            scene hallway with None
            show player 14 at left
            with dissolve
            player_name "( Someone's in the shower. )"
            show player 26
            player_name "( I think they left the door unlocked... )"
            hide player
            with dissolve
    $ callScreen(location_count)

label hallway_dialogue_sis_spy:
    scene hallway with None
    show player 11 with dissolve
    player_name "( I really want to know who {b}[sis]{/b} is talking to. )"
    show player 4 at Position(xpos=518)
    player_name "( Maybe I can sneak up to her door and find out... )"
    hide player with dissolve
    $ callScreen(location_count)

label hallway_dialogue_sis_door:
    scene expression gTimer.image("hallway{}")
    show player 12 at left
    player_name "( Her door is locked... )"
    hide player 12 at left
    $ callScreen(location_count)

label hallway_check_on_mom:
    scene expression gTimer.image("hallway{}")
    show player 10 with dissolve
    player_name "I should really go check on {b}Mom{/b}..."
    hide player 10 with dissolve
    $ callScreen(location_count)

label too_tired:
    scene hallway_night
    show player 24 at left
    player_name "( I'm so tired right now, I better go to bed... )"
    hide player 17 at left
    $ callScreen(location_count)

label attic_entry_dialogue:
    if attic_unlocked:
        jump attic_dialogue

    elif attic_key in inventory.items and stool in inventory.items:
        scene expression gTimer.image("hallway{}")
        $ inventory.items.remove(attic_key)
        $ inventory.items.remove(stool)
        $ attic_unlocked = True
        show expression "boxes/popup_attic.png" at truecenter with dissolve
        $ renpy.pause()
        hide expression "boxes/popup_attic.png" with dissolve
        jump attic_entry_dialogue
    else:

        scene expression gTimer.image("hallway")
        show player 34 with dissolve
        player_name "Hmm..."
        show player 35
        player_name "( That small trap door is {b}locked{/b}. )"
        player_name "( I also need something to {b}stand on{/b} to reach the opening... )"
        jump hallway_dialogue