default attic_unlocked = False

label hallway_dialogue:
    $ location_count = "Hallway"
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and not shower.occupied():
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if not gTimer.is_dark():
        if hallway_count == 0:
            scene hallway
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
            player_name "Do you smell that? {b}[mom_name]'s{/b} cooking!"
            show sis 9
            show player 11
            sis "Duh! {b}[mom_name]{/b} made breakfast. She's {b}downstairs{/b} waiting for you."
            show sis 12
            sis "You'd know, if you were actually on time for once."
            show player 2
            show sis 11
            player_name "Perfect! I was just on my way actually..."
            hide player with dissolve
            pause 0.5
            show sis 10
            sis "Ugh. What have I done to deserve a younger brother like you..."
            hide sis
            with dissolve
            call screen sis_name_input
            if sis_char_name.strip() == "":
                $ sis_char_name = "Jenny"
            $ sis = Character("[sis_char_name]", color="#ff6df0")
            $ hallway_count = 1

        elif M_mom.get_state() == S_mom_sis_boobs_afterthoughts:
            scene hallway
            show player 26 with dissolve
            player_name "Wow..."
            player_name "I can't believe {b}[sis_name]{/b} actually took her top off in front of me..."
            if sister.completed(sis_shower_cuddle01):
                player_name "I've never seen them up close before..."
            else:
                player_name "I've never seen them before."
            player_name "Her breasts are so nice..."
            hide player with dissolve
            $ M_mom.trigger(T_mom_sis_nice_boobs)

        elif sister.started(sis_hallway01) and sister.over(sis_shower_cuddle02):
            scene hallway
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
            sis "If you go through my things again, I'm telling {b}[mom_name]{/b}."
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

        elif sister.started(sis_hallway02) and sister.over(sis_telescope02) and M_mom.is_set("jerk available"):
            scene hallway
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
            sis "Meeting with {b}[mom_name]{/b} in her room, perhaps?"
            show sis 6
            show player 29
            player_name "What?"
            show sis 9
            show player 11 at left
            sis "You've been sucking up to {b}[mom_name]{/b} a lot lately."
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
            player_name "Well, {b}[mom_name]{/b} needs help around the house so I'm-"
            show sis 9
            show player 11
            sis "Oh, stop it!"
            sis "Look, I don't care what you and {b}[mom_name]{/b} do in secret."
            show player 16
            sis "We both know you're just a pervert."
            show player 11

            sis "What's important here is that I need you focused!"
            sis "I can't let you get distracted by {b}[mom_name]{/b}."
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

        elif sister.started(sis_final) and sister.over(sis_shower_cuddle04):
            scene hallway
            show player 11 with dissolve
            player_name "..."
            player_name "( There're voices coming from my sister's room... )"
            show player 4
            player_name "( It sounds like... she's talking to someone? But who... )"
            show player 1
            player_name "( Maybe I can sneak up to her door and find out... )"
            hide player with dissolve
            $ lock_ui()

        elif sister.over(sis_final) and not sister.known(sis_final2):
            scene hallway
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

        if shower.occupied("sis") and (
                sister.started(sis_shower_cuddle01) or
                sister.started(sis_shower_cuddle02) or
                sister.started(sis_shower_cuddle03) or
                sister.started(sis_shower_cuddle04) or
                sister.started(sis_shower_cuddle05)
        ):
            scene hallway
            show player 14 at left
            with dissolve
            player_name "( Someone's in the shower. )"
            show player 26
            player_name "( I think they left the door unlocked... )"
            hide player
            with dissolve

        elif M_mom.get_state() in [S_mom_shower_peek, S_mom_shower_walk_in] and shower.occupied("mom"):
            scene hallway
            show player 14 with dissolve
            player_name "( Someone's in the shower? )"
            player_name "( I wonder if it's {b}[mom_name]{/b}. )"
            show player 26
            player_name "( Maybe I can peek just a little... )"
            hide player with dissolve
    else:

        if M_mom.get_state() == S_mom_sleepover_offer:
            scene hallway_night
            show mom 3 at right
            show player 1 at left
            with dissolve
            mom "Hey, Sweetie."
            show player 17
            show mom 1
            player_name "Hey, {b}[mom_name]{/b}."
            show mom 2
            show player 1
            mom "Did you sleep well last night?"
            show player 10
            show mom 14
            player_name "I had a little trouble falling asleep at first, but I'm okay."
            show player 5
            show mom 13
            mom "You thinking about all the things that have been happening lately?"
            show mom 14b
            show player 10
            player_name "Maybe..."
            show player 5
            show mom 13
            mom "Don't worry about it, Sweetie."
            mom "Everything will be okay, I promise."
            show mom 14
            show player 10
            player_name "Are you sure?"
            show player 5
            show mom 13
            mom "Just try not to think about it."
            show mom 14
            pause
            show mom 13
            mom "You know, I've been having trouble sleeping too."
            show player 11
            mom "Ever since your dad... left us, you know..."
            show mom 14b
            show player 12
            player_name "Really?"
            show player 5
            show mom 13
            mom "I just miss him so much..."
            show mom 14
            pause
            show mom 2
            mom "...But, it's okay! I still have you."
            show mom 1
            show player 13
            pause
            hide player
            show mom 4 at center
            with dissolve
            pause
            show player 13 at left
            show mom 2 at right
            with dissolve
            mom "Mmm... Thanks for the hug, Sweetie."
            show mom 1
            pause
            show mom 2
            mom "If you have trouble sleeping again just come visit me, okay?"
            show mom 1
            show player 10
            player_name "In your bedroom?"
            show player 5
            show mom 3
            mom "Sure!"
            show mom 2
            mom "Maybe we can cuddle up a little... Might help us fall asleep..."
            show mom 1
            show player 10
            player_name "You don't mind me sleeping in your bed?"
            show player 11
            pause
            show mom 13
            mom "I think it could do us some good..."
            show player 13
            mom "...Having some company... and feeling close."
            show mom 14
            show player 14
            player_name "...Okay. Sure, {b}[mom_name]{/b}."
            hide player
            hide mom
            with dissolve
            show unlock34 at truecenter with dissolve
            $ M_mom.trigger(T_mom_sleepover_accept)
            pause
            hide unlock34 with dissolve

        elif M_mom.get_state() == S_mom_movie_night_two and gTimer.is_evening():
            scene hallway_night
            show player 1 at left
            show mom 62 at right
            mom "Hey there, Sweetie!"
            show player 2
            show mom 61
            player_name "Hey {b}[mom_name]{/b}, what's up?"
            show player 1
            show mom 62
            mom "I was gonna watch another movie."
            mom "Care to join me?"
            show player 2
            show mom 61
            player_name "Of course, I'd love to!"
            show player 1
            show mom 62
            mom "Wonderful! I'll go get situated then. Come join me when your ready, alright?"
            show player 2
            show mom 61
            player_name "Sounds good! I'll be right down."
            hide mom
            hide player
            with dissolve
            $ M_mom.trigger(T_mom_movie_invite)
            $ lock_ui()
    $ callScreen(location_count)

label hallway_dialogue_sis_spy:
    scene hallway
    show player 11 with dissolve
    player_name "( I really want to know who {b}[sis_name]{/b} is talking to. )"
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
    player_name "( I should really go check on {b}[mom_name]{/b}... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label too_tired:
    scene hallway_night
    show player 24 at left
    player_name "( I'm so tired right now. I better go to bed... )"
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