label fishing_night:
    scene expression gTimer.image("pier{}")
    show player 4 at left with dissolve
    player_name "( It's too late to go fishing. )"
    $ callScreen(location_count)

label no_fish_rod:
    scene expression gTimer.image("pier{}")
    show player 2 with dissolve
    player_name "( Hmm... I'll need a {b}fishing rod{/b} before I can fish... )"
    $ callScreen(location_count)

label before_fishing:
    scene minigame06b
    if M_aqua.get_state() == S_aqua_chase:
        menu:
            "Speak to Monster Girl.":
                show player 474 at Position(xpos=0.715,ypos=.9425)
                player_name "Hey! Aqua!"
                show player 475
                pause
                show player 474
                player_name "I know you can hear me!"

                show player 475
                show aqua 17b at Position (xpos=0.4175,ypos=1.0) with dissolve
                pause
                show aqua 18b
                aqua "What you want now?"
                show player 474
                show aqua 17b
                player_name "Don't play dumb! You know, I want my lure back!"
                show player 475
                show aqua 18b
                aqua "Shiiiny?"
                show player 474
                show aqua 17b
                player_name "Yes, Shiny. Give it back!"
                show player 475
                show aqua 18b
                aqua "No! You just ussse it to steals fishies!"
                aqua "Aqua keeps it. Fishies sssafe."
                show player 474
                show aqua 17b
                player_name "Grr..."
                show player 475
                show aqua 18b
                aqua "You want shiny, you come get!!!"
                hide aqua with dissolve
                show player 476
                player_name "Crap!"
                player_name "..."
                jump follow_aqua
            "Fish.":

                $ pass

    if worm in inventory.items or lure01 in inventory.items or special_lure in inventory.items:
        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( Terry said something about the right bait for the right fish... )"
        call screen bait_menu

        show player 235 at Position(xpos=0.6062,ypos=0.9455)
        player_name "( Hope I catch something good with this... )"
        show player 236 at Position(xpos=0.4956,ypos=0.9455)
        player_name "..."

        $ fishes = {}
        $ fishes["Seatrout"] = Fish("buttons/fishing_fish01a.png", "Seatrout", 550, "worms", 11, -1.0)
        $ fishes["Snapper"] = Fish("buttons/fishing_fish02a.png", "Snapper", 350, "standard lure", 16, -1.0)
        $ fishes["Mackerel"] = Fish("buttons/fishing_fish03a.png", "Mackerel", 450, "fancy lure", 14)
        $ fishes["Tiger Fish"] = Fish("buttons/fishing_fish04a.png", "Tiger Fish", 625, "golden lure", 10, variation = 2)

        call screen fishing_minigame(bait)
    else:

        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( I can’t fish without bait. )"
        player_name "( I should look around the town and see what I can find. )"
    $ callScreen(location_count)

label after_fishing(fish_name, chosen_bait):
    scene minigame06b
    if fish_name != None:
        play audio randomizer("audio/sfx_reel{}.ogg", 1, 2)
        show player 237 at Position(xpos=0.7173,ypos=0.9455)
        if fish_name == "Seatrout":
            show xtra 4 at Position(xpos=0.5786,ypos=0.4810)
            $ inventory.items.append(seatrout)
        elif fish_name == "Snapper":
            show xtra 5 at Position(xpos=0.5786,ypos=0.4810)
            $ inventory.items.append(snapper)
        elif fish_name == "Mackerel":
            show xtra 6 at Position(xpos=0.5786,ypos=0.4810)
            $ inventory.items.append(mackerel)
        elif fish_name == "Tiger Fish":
            show xtra 29 at Position(xpos=0.56,ypos=0.52)
            player_name "Whew, this mean bastard put up quite a fight."
            player_name "... and just look at those teeth!"
            player_name "It's no wonder why Terry wanted him dead."
            player_name "I can't wait to show him!"
            $ inventory.items.append(tigger)

        if fish_name != "Tiger Fish":
            player_name "( Yes! I caught a {b}[fish_name]{/b}! )"
        $ fish_caught_count += 1
        $ first_fish = True
    else:
        show player 238 at Position(xpos=0.7173,ypos=0.9455)
        if chosen_bait == "worms":
            show xtra 7 at Position(xpos=0.5786,ypos=0.4479)
        elif chosen_bait == "standard lure":
            show xtra 8 at Position(xpos=0.5796,ypos=0.4645)
        elif chosen_bait == "fancy lure":
            show xtra 9 at Position(xpos=0.5796,ypos=0.4479)
        elif chosen_bait == "golden lure":
            show xtra 10 at Position(xpos=0.5796,ypos=0.4479)
        player_name "!!!" with hpunch
        player_name "( I didn't catch anything! )"
        player_name "( Maybe I need to {b}aim better{/b}, or use the correct {b}bait{/b}... )"
    $ gTimer.tick()
    $ callScreen(location_count)