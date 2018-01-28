label beach_dialogue:
    $ location_count = "Beach"
    if getPlayingSound("<loop 2>audio/ambience_beach.ogg"):
        $ playSound("<loop 2>audio/ambience_beach.ogg")
    $ callScreen(location_count)

label beach_island_dialogue:
    $ location_count = "Beach Island"
    if M_aqua.get_state() == S_aqua_treasure_search:
        scene location_beach_island_blur
        show player 11 at left with dissolve
        pause
        show player 10
        player_name "That's one {b}strange looking statue.{/b}"
        show player 2
        player_name "... But according to the map, the {b}treasure{/b} should be right here."
        hide player with dissolve
    $ callScreen(location_count)

label beach_statue:
    if shovel not in inventory.items:
        scene location_beach_island_blur
        show player 2 at left
        player_name "I can't dig for {b}buried treasure{/b} without a {b}shovel.{/b}"
        show player 4
        player_name "...I think we have one at {b}home{/b} somewhere."
        hide player with dissolve
        $ callScreen(location_count)

    if M_aqua.get_state() == S_aqua_treasure_search:
        scene location_beach_digging01 with fade
        show text "I continued to dig for what must have been hours..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "...before long I started to tire, my arms aching." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Exhaustion was about to overtake me and I considered giving up." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Was I in the wrong spot?" at Position (xpos= 512, ypos= 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve

        scene location_beach_digging02 with fade
        show text "... Then, bang! My shovel hit something hard!" at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "My strength returned in an instant as I hurried to uncover what Ben Dover had buried." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "...It was a large heavy chest; This was it! I had found the treasure!" at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve
        $ M_aqua.trigger(T_aqua_treasure_found)

    if M_aqua.get_state() not in [S_aqua_treasure_search, S_aqua_treasure_unlock]:
        jump treasure_unlocked

    scene location_beach_lock with fade
    player_name "oh man.."
    player_name "It looks like I need a {b}key{/b}...And a {b}combination{/b} to open this."
    $ callScreen("Treasure Lock", False, False)

label treasure_unlocked:
    scene location_beach_treasure
    if M_aqua.get_state() == S_aqua_treasure_unlock:
        show expression "objects/object_compass_01.png" at Position(xpos = 537, ypos = 473)
        with fade
        hide expression "objects/object_compass_01.png"
        call screen treasure_chest
        show closeup_compass_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
        player_name "Whoa!!"
        player_name "I can't believe it! I found the treasure!."
        player_name "This has to be the compass Terry was talking about."
        show popup_item_compass1 at truecenter with dissolve
        $ inventory.items.append(golden_compass)
        pause
        hide popup_item_compass1 with dissolve
        hide closeup_compass_01 with dissolve
        $ M_aqua.trigger(T_aqua_treasure_unlocked)
    else:

        with fade
        pause
    $ callScreen(location_count)