default lower_bait = False
default bait = 0
default fish_caught = ""
default fishing_first = True
default bait_dialogue = False
default first_fish = False
default fish_caught_count = 0
default pier_board_first = True

label pier_dialogue:
    $ location_count = "Pier"
    $ playSound(audio.a_pier, 1.0)
    scene expression gTimer.image("pier{}")
    show player 2 at left with dissolve
    player_name "( It smells like the ocean around here. )"
    player_name "( People say it's the best spot for {b}fishing{/b}. )"
    $ callScreen(location_count)

label terry_button_dialogue:
    $ playMusic(audio.m_pier)
    scene expression gTimer.image("pier_closeup{}")
    if first_fish:
        show player 203 at left with dissolve
        show terry 2 at Position(xpos=0.6992,ypos=0.7047)
        Terry "How's fishing treating you?"
        show player 2
        show terry 1
        player_name "It's okay, my bait doesn't always seem to work."
        show player 203
        show terry 2
        Terry "Don't get discouraged."
        Terry "It took me years to find good bait!"
        show player 203
        show terry 4
        player_name "..."
        show player 203
        show terry 9
        Terry "This is my lucky {b}gold coin{/b}!"
        Terry "This little thing will catch anything you want!"
        show player 2
        show terry 13
        player_name "It's so shiny..."
        player_name "Is it for sale?"
        show player 203
        show terry 12
        Terry "!!!"
        show terry 11
        Terry "Well... I uhh..."
        show terry 12
        show player 3
        Terry "You see... It has a sentimental value to me."
        show terry 11
        Terry "I just don't think I could let go of it just yet."
        show player 10
        show terry 14
        player_name "Isn't there anything I could do?"
        show player 5
        show terry 12
        Terry "..."
        show terry 11
        Terry "Alright: I'll make you a deal."
        label thedeal:
        show player 203
        show terry 10
        Terry "There's this local legend about an old buried treasure along the beach..."
        Terry "They say pirates put it there, and it contains a {b}gold compass{/b} with a {b}skull{/b} on it!"
        Terry "If you ever find it, I'll trade my {b}gold coin{/b} to you for it!!"
        show player 2
        show terry 13
        player_name "Really?"
        player_name "Hmm... Has anyone ever seen this compass?"
        show player 203
        show terry 10
        Terry "Haha! I don't think so! That's why it's a legend!"
        Terry "But don't get discouraged! Look around and you might find {b}clues{/b}..."
        show player 2
        show terry 13
        player_name "Okay! Deal!"
    else:
        show terry 2 at Position(xpos=0.6992,ypos=0.7047)
        show player 203 at left with dissolve
        Terry "Hey there, mate!"
    Terry "Anything I can do for ya?"
    menu:
        "Buy some fish ($100)":
            show terry 1
            show player 4
            $ renpy.pause ()
            show player 12
            player_name "Do you have any fresh fish for sale?"
            show player 203
            show terry 2
            Terry "Of course! You came to the right place."
            Terry "I have {b}Sea trout{/b}, {b}Snapper{/b} and {b}Mackerel{/b}."
            Terry "What'll it be?"
            menu:
                "Sea trout":
                    $ fish = "Seatrout"
                "Snapper":
                    $ fish = "Snapper"
                "Mackerel":
                    $ fish = "Mackerel"
                "Nevermind":
                    jump fish_nevermind

            label buyfish:
                if inventory.money < 100:
                    player_name "( I don't have enough money... )"
                    jump fish_nevermind
                show player 4
                $ renpy.pause ()
                show player 2
                player_name "{b}[fish]{/b}."
                Terry "That’s a great choice!"
                show terry 4
                Terry "Let me get that for you..."
                if fish == "Seatrout":
                    show terry 5
                    $ inventory.items.append(seatrout)
                elif fish == "Snapper":
                    show terry 6
                    $ inventory.items.append(snapper)
                elif fish == "Mackerel":
                    show terry 7
                    $ inventory.items.append(mackerel)
                Terry "Here ya go, mate!"
                play audio coins2
                show player 17
                player_name "Thank you!"
                $ inventory.money -= 100
                $ playMusic()
                $ callScreen(location_count)

            label fish_nevermind:
                show player 10
                show terry 1
                player_name "Hmm... I think I’ll pass."
                show player 203
                show terry 2
                Terry "No problem, mate! Maybe some other time."
                $ playMusic()
                $ callScreen(location_count)
        "Buy a drink (5$)":

            show player 12
            show terry 1
            player_name "You sell drinks?"
            show player 11
            show terry 3
            $ renpy.pause ()
            show terry 2
            Terry "Only one kind: Pure tequila gold!"
            Terry "$5 a shot, mate."
            menu:
                "Buy a shot.":
                    if inventory.money < 5:
                        player_name "( I don't have enough money... )"
                        $ callScreen(location_count)
                    show player 188
                    show terry 1
                    play audio coins2
                    $ renpy.pause ()
                    show player 189
                    $ renpy.pause ()
                    show player 190
                    $ renpy.pause ()
                    show player 191
                    $ inventory.money -= 5
                    player_name "Ugh! That’s really strong!"
                    show player 185
                    show terry 2
                    Terry "Haha!"
                    Terry "It’s the good stuff! You’ll get used to it!"
                "I’ll pass.":
                    show terry 1
                    show player 10
                    player_name "I think I’ll pass. I can’t drink that stuff."
                    show terry 2
                    show player 203
                    Terry "No problem, mate! Maybe some other time."
            $ playMusic()
            $ callScreen(location_count)
        "Go fishing":

            show player 2
            show terry 1
            player_name "Can I try to catch some fish here?"
            show player 203
            show terry 3
            $ renpy.pause ()
            show terry 2
            Terry "I see the open water is catching your eye."
            show player 31f at Position(xpos=-0.1412,ypos=1.0000) with dissolve
            show terry
            Terry "Just use the {b}chair{/b} at the end of the pier. It's a great spot!"
            show player 203 at left with dissolve
            Terry "Make sure you have a {b}fishing rod{/b}, and that you're using the right {b}bait{/b}."
            show terry 3
            $ renpy.pause()
            show terry 2
            Terry "Oh! If you catch anything, come back here, and I’ll buy them off you for a reasonable price."
            $ bait_dialogue = True

        "Bait" if bait_dialogue:
            show player 2
            show terry 1
            player_name "Can you tell me more about the bait types?"
            show player 203
            show terry 2
            Terry "Sure thing, mate!"
            Terry "First, you need to know what kind of fish you're tying to catch."
            Terry "Every {b}kind{/b} of fish likes a specific type of {b}bait{/b}!"
            Terry "{b}Sea trout{/b} like worms, {b}Snapper{/b} like blue bait, and {b}Mackerel{/b} like the green baits!"
            show player 2
            show terry 1
            player_name "Awesome! Thanks for the tip!"
            player_name "But where could I find those different types of bait?"
            show player 203
            show terry 2
            Terry "I don't sell equipment in my shack."
            Terry "You'll have to {b}look around town{/b} to find them."
            show player 2
            show terry 1
            player_name "I see..."
            player_name "Thanks, {b}Terry{/b}!"
        "Leave":

            $ playMusic()
            $ callScreen(location_count)
    $ playMusic()
    $ callScreen(location_count)

label pier_board:
    if pier_board_first:
        scene expression gTimer.image("pier{}")
        show player 4 at left with dissolve
        player_name "( These must be the {b}types of fish{/b} you can catch on the Pier and what {b}bait{/b} to use. )"
        $ pier_board_first = False
    scene expression gTimer.image("pier_board{}")
    pause
    $ callScreen(location_count)

label fishing_night:
    scene expression gTimer.image("pier{}")
    show player 4 at left with dissolve
    player_name "( It's too late to go fishing. )"
    $ callScreen(location_count)

label before_fishing:
    scene minigame06b
    if not mother.known(mom_dinner_outfit):
        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( What kind of fish did {b}Mom{/b} want again?! )"
        player_name "( I'd better go back home and ask her. )"

    if worm in inventory.items:
        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( Terry said something about the right bait for the right fish... )"
        call screen bait_menu

        show player 235 at Position(xpos=0.6062,ypos=0.9455)
        player_name "( Hope I catch something good with this... )"
        show player 236 at Position(xpos=0.4956,ypos=0.9455)
        player_name "..."
        jump fishing_minigame
    else:

        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( I can’t fish without bait. )"
        player_name "( I should look around the town and see what I can find. )"
    $ callScreen(location_count)

screen bait_menu:
    add "buttons/fishing_instructions02.png" pos 110,100
    add "buttons/fishing_button01c.png" pos 250,250
    add "buttons/fishing_button02c.png" pos 150,250
    add "buttons/fishing_button03c.png" pos 250,150
    add "buttons/fishing_button04c.png" pos 150,150
    if worm in inventory.items:
        imagebutton:
            focus_mask True
            idle "buttons/fishing_button01a.png"
            hover "buttons/fishing_button01b.png"
            action SetVariable("bait", 1), Return()
            xpos 250
            ypos 250

    if lure01 in inventory.items:
        imagebutton:
            focus_mask True
            idle "buttons/fishing_button02a.png"
            hover "buttons/fishing_button02b.png"
            action SetVariable("bait", 2), Return()
            xpos 150
            ypos 250

label fishing_minigame:
    scene minigame06a
    show screen fishing
    $ lower_bait = False
    $ fish1_caught = False
    $ fish2_caught = False
    $ fish3_caught = False
    $ fish1 = At(ImageReference("fish1"), move_fish1)
    $ fish2 = At(ImageReference("fish2"), move_fish2)
    $ fish3 = At(ImageReference("fish3"), move_fish3)

    $ time_count = 4
    $ timer_range = 4

    $ fish1_flip = False
    $ fish2_flip = False
    $ fish3_flip = False

    show expression fish1
    show expression fish2
    show expression fish3

    $ hook = At(ImageReference("hook"), move_hook)
    $ hook_xpos = 500
    $ hook_ypos = 7

    call screen try_fish(hook, fish1, fish2)

screen fishing:
    add "backgrounds/menu_ground.png"

screen try_fish(hook, fish1, fish2):
    if fishing_first:
        if renpy.variant("pc"):
            add "buttons/fishing_instructions01.png" pos 70,100
        elif renpy.variant("mobile"):
            add "buttons/fishing_instructions01b.png" pos 70,100

    if not lower_bait:
        if renpy.variant("pc"):
            if bait == 1:
                add "buttons/fishing_bait01.png" pos hook_xpos,hook_ypos
            elif bait == 2:
                add "buttons/fishing_bait02.png" pos hook_xpos,hook_ypos
            key "K_LEFT" action [If(hook_xpos > 36, SetVariable("hook_xpos", hook_xpos-4), NullAction())]
            key "repeat_K_LEFT" action [If(hook_xpos > 36, SetVariable("hook_xpos", hook_xpos-4), NullAction())]
            key "K_RIGHT" action [If(hook_xpos < 884, SetVariable("hook_xpos", hook_xpos+4), NullAction())]
            key "repeat_K_RIGHT" action [If(hook_xpos < 884, SetVariable("hook_xpos", hook_xpos+4), NullAction())]
        elif renpy.variant("mobile"):
            if bait == 1:
                imagebutton idle "buttons/fishing_bait01.png" action [SetVariable("lower_bait", True)] pos hook_xpos, hook_ypos
            elif bait == 2:
                imagebutton idle "buttons/fishing_bait02.png" action [SetVariable("lower_bait", True)] pos hook_xpos, hook_ypos
            imagebutton idle "buttons/attack_01.png" action [If(hook_xpos > 36, SetVariable("hook_xpos", hook_xpos-4), NullAction())] focus_mask True pos 10,70
            imagebutton idle "buttons/attack_03.png" action [If(hook_xpos < 884, SetVariable("hook_xpos", hook_xpos+4), NullAction())] focus_mask True pos 955,70
    else:
        if bait == 1:
            add "buttons/fishing_bait01b.png" pos hook_xpos,hook_ypos
        elif bait == 2:
            add "buttons/fishing_bait02b.png" pos hook_xpos,hook_ypos

    key "K_RETURN" action SetVariable("lower_bait", True)

    if lower_bait:
        timer 0.01 repeat True action If(time_count > 0, true=[SetVariable("time_count", time_count - 0.01), If(hook_ypos < 800, SetVariable("hook_ypos", hook_ypos +2), Jump("fish_caught"))], false=NullAction())

    if fish1_flip and hook_ypos > 380 and hook_ypos < 420 and fish1.xpos+170 > hook_xpos-30 and fish1.xpos+170 < hook_xpos+50 or not fish1_flip and hook_ypos > 380 and hook_ypos < 420 and fish1.xpos > hook_xpos-50 and fish1.xpos < hook_xpos+30:
        if bait == 2:
            $ fish1_caught = True
    if not fish2_flip  and hook_ypos > 580 and hook_ypos < 620 and fish2.xpos+170 > hook_xpos-30 and fish2.xpos+170 < hook_xpos+50 or fish2_flip and hook_ypos > 580 and hook_ypos < 620 and fish2.xpos > hook_xpos-50 and fish2.xpos < hook_xpos+30:
        if bait == 1:
            $ fish2_caught = True
    if fish3_flip and hook_ypos > 480 and hook_ypos < 520 and fish3.xpos+170 > hook_xpos-30 and fish3.xpos+170 < hook_xpos+50 or not fish3_flip and hook_ypos > 480 and hook_ypos < 520 and fish3.xpos > hook_xpos-50 and fish3.xpos < hook_xpos+30:
        if bait == 3:
            $ fish3_caught = True

    if fish1.xpos < 0:
        $ fish1_flip = True
    elif fish1.xpos > 1000:
        $ fish1_flip = False
    if fish2.xpos < 0:
        $ fish2_flip = False
    elif fish2.xpos > 1000:
        $ fish2_flip = True
    if fish3.xpos < 0:
        $ fish3_flip = True
    elif fish3.xpos > 1000:
        $ fish3_flip = False

    if fish1_caught:
        $ renpy.play(audio.fish_slapping)
        $ lower_bait = False
        add "backgrounds/minigame06a.jpg"
        add "buttons/fishing_fish02a.png" pos hook_xpos,hook_ypos
        add "buttons/fishing_done.png" pos hook_xpos-70,hook_ypos-90
        add "buttons/fishing_exclamation.png" pos 800,90
        imagebutton:
            idle "buttons/fishing_catch.png"
            hover "buttons/fishing_catchb.png"
            action SetVariable("fish_caught", "fish1"), Jump("fish_caught")
            pos hook_xpos-50,hook_ypos-50
    elif fish2_caught:
        $ renpy.play(audio.fish_slapping)
        $ lower_bait = False
        add "backgrounds/minigame06a.jpg"
        add "buttons/fishing_fish01a.png" pos hook_xpos,hook_ypos
        add "buttons/fishing_done.png" pos hook_xpos-70,hook_ypos-90
        add "buttons/fishing_exclamation.png" pos 800,90
        imagebutton:
            idle "buttons/fishing_catch.png"
            hover "buttons/fishing_catchb.png"
            action SetVariable("fish_caught", "fish2"), Jump("fish_caught")
            pos hook_xpos-50,hook_ypos-50
    elif fish3_caught:
        $ renpy.play(audio.fish_slapping)
        $ lower_bait = False
        add "backgrounds/minigame06a.jpg"
        add im.Flip("buttons/fishing_fish03a.png", horizontal = True) pos hook_xpos-170,hook_ypos
        add "buttons/fishing_done.png" pos hook_xpos-70,hook_ypos-90
        add "buttons/fishing_exclamation.png" pos 800,90
        imagebutton:
            idle "buttons/fishing_catch.png"
            hover "buttons/fishing_catchb.png"
            action SetVariable("fish_caught", "fish3"), Jump("fish_caught")
            pos hook_xpos-50,hook_ypos-50

label fish_caught:
    scene minigame06b
    if fish_caught != "":
        play audio randomizer("audio/sfx_reel{}.ogg", 1, 2)
        $ fishname = ""
        show player 237 at Position(xpos=0.7173,ypos=0.9455)
        if fish_caught == "fish2":
            show xtra 4 at Position(xpos=0.5786,ypos=0.4810)
            $ renpy.pause()
            $ fishname = "Seatrout"
            $ inventory.items.append(seatrout)
        elif fish_caught == "fish1":
            show xtra 5 at Position(xpos=0.5786,ypos=0.4810)
            $ renpy.pause()
            $ fishname = "Snapper"
            $ inventory.items.append(snapper)
        elif fish_caught == "fish3":
            show xtra 6 at Position(xpos=0.5786,ypos=0.4810)
            $ renpy.pause()
            $ fishname = "Mackerel"
            $ inventory.items.append(mackerel)
        player_name "( Yes! I caught a {b}[fishname]{/b}! )"
        $ fishname = ""
        $ fish_caught = ""
        $ fish_caught_count += 1
    else:
        show player 238 at Position(xpos=0.7173,ypos=0.9455)
        if bait == 1:
            show xtra 7 at Position(xpos=0.5786,ypos=0.4479)
            $ renpy.pause()
        elif bait == 2:
            show xtra 8 at Position(xpos=0.5796,ypos=0.4645)
            $ renpy.pause()
        elif bait == 3:
            show xtra 9 at Position(xpos=0.5796,ypos=0.4479)
            $ renpy.pause()
        elif bait == 4:
            show xtra 10 at Position(xpos=0.5796,ypos=0.4479)
            $ renpy.pause()
        player_name "!!!" with hpunch
        player_name "( I didn't catch anything! )"
        player_name "( Maybe I need to {b}aim better{/b}, or use the correct {b}bait{/b}... )"
    if fish_caught_count == 1:
        $ first_fish = True
    $ gTimer.tick()
    $ callScreen(location_count)

image hook:
    "buttons/fishing_bait01b.png"
    xpos 500
    ypos 0

image fish1:
    "buttons/fishing_fish02a.png"
    xpos 1150
    ypos 400

image fish2:
    "buttons/fishing_fish01a.png"
    xpos 1150
    ypos 600

image fish3:
    im.Flip("buttons/fishing_fish03a.png", horizontal=True)
    xpos -250
    ypos 500

transform move_fish1:
    xpos 1150 ypos 400
    ease 3.5 xpos 650
    ease 3.5 xpos 200
    ease 3.5 xpos -250
    xzoom -1.0
    ease 3.5 xpos 200
    ease 3.5 xpos 650
    ease 3.5 xpos 1150
    xzoom 1.0
    repeat

transform move_fish2:
    xpos 1150 ypos 600
    ease 2.5 xpos 700
    ease 2.5 xpos 250
    ease 2.5 xpos -250
    xzoom -1.0
    ease 2.5 xpos 250
    ease 2.5 xpos 700
    ease 2.5 xpos 1150
    xzoom 1.0
    repeat

transform move_fish3:
    xpos -250 ypos 500
    ease 3.0 xpos 300
    ease 3.0 xpos 750
    ease 3.0 xpos 1150
    xzoom -1.0
    ease 3.0 xpos 750
    ease 3.0 xpos 300
    ease 3.0 xpos -250
    xzoom 1.0
    repeat

transform move_hook:
    xpos 512 ypos 7
    linear 5.0 ypos 728
    repeat

label no_fish_rod:
    scene expression gTimer.image("pier{}")
    show player 2 with dissolve
    player_name "( Hmm... I'll need a {b}fishing rod{/b} before I can fish... )"
    $ callScreen(location_count)