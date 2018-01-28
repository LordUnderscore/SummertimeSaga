default forest_count = 0
default awesomo_lured = False
default dirt_pile_done = False

label forest_dialogue:
    $ location_count = "Forest"
    scene expression gTimer.image("forest{}_b")
    if forest_count == 0:
        show player 43 with dissolve
        player_name "Wow!"
        player_name "( I've never been to the forest before... )"
        player_name "( It's so... calm... )"
        $ forest_count = 1

    if Anna.started(anna_missing_pup) and not awesomo_lured:
        if gTimer.is_dark():
            show player 4
            player_name "( It's too dark to look for {b}Awesomo{/b}. )"
            hide player
            with dissolve

        elif cookies in inventory.items:
            show player 4 with dissolve
            player_name "( Let's see if I can find that dog. )"
            scene forest_closeup
            show player 239 at left
            with dissolve
            player_name "( Now... )"
            show player 240
            player_name "( ...I should be able to lure him out... )"
            show player 245 at Position(xpos=8)
            player_name "( ...using {b}this{/b}! )"
            show player 246 at left
            pause
            show player 1 with dissolve

            show player 1
            player_name "( Let's see if he comes out. )"
            show player 31
            player_name "( He must be around here somewhere... )"
            $ awesomo_lured = True
            $ inventory.items.remove(cookies)
            hide player
            with dissolve
        else:

            show player 4
            player_name "( I should find some {b}cookies{/b} to lure {b}Awesomo{/b} out with. )"
            hide player
            with dissolve
    $ callScreen(location_count)

label awesomo_dialogue_button:
    scene forest_closeup
    show player 177
    with dissolve
    player_name "Hey there little guy..."

    player_name "What're you doing all the way out here?"
    awesomo "Bark!"
    player_name "You got your owner all worried about you!"
    awesomo "Bark!"
    player_name "You're a funny looking doggo..."
    label awesomo_dialogue_loop:
        menu:
            "Give Cookie.":
                player_name "Want a cookie?"
                show player 178 at Position(xpos=517)
                player_name "Here you go..."
                show player 179 with hpunch
                player_name "!!!"
                show player 180
                player_name "Jeez!"
                player_name "Someone's hungry..."
                show player 181
                player_name "Hmm..."
                show player 182
                player_name "I like you!"
                awesomo "Bark!"
                jump awesomo_dialogue_loop
            "Check name tag.":

                show player 177 at center
                player_name "Let's see if you're the one I'm looking for..."
                show awesomo_tag zorder 2 with dissolve
                player_name "{b}Awesomo{/b}... Yup! Must be you!"
                $ awesomo = Character("Awesomo")
                hide awesomo_tag

                show player 177
                with dissolve
                player_name "Let's get you back to your owner."
                player_name "She's worried sick..."
                awesomo "Bark!"
                player_name "Haha! Alright, let's go then..."
                hide player
                scene forest
                with dissolve
                $ inventory.items.append(dog)
    $ callScreen(location_count)

label dirt_pile:
    show location_forest_dirt1 zorder 2 with dissolve
    if shovel in inventory.items:
        player_name "( There's something strange about this patch of dirt... )"
        player_name "( It seems like something's moving under it. )"
        player_name "( Maybe I could dig it out? )"
        menu:
            "Dig with a shovel." if shovel in inventory.items:
                player_name "( Let's see what's in there... )"
                hide location_forest_dirt1
                show location_forest_dirt2
                with dissolve
                pause
                show location_forest_dirt3
                with dissolve
                player_name "{b}Worms{/b}?!"
                player_name "( They say these make great {b}fishing bait{/b}. )"
                player_name "( Maybe I'll keep some for later... )"
                call screen forest_worms
            "Leave it alone.":

                player_name "( On second thought... )"
                player_name "( Perhaps I should leave them alone... )"
                with dissolve

        player_name "( There's something strange about this patch of dirt... )"
        player_name "( It seems like something's moving under it. )"
        player_name "( I need to find a {b}shovel{/b} to dig it out. )"
        hide location_forest_dirt1
        with dissolve
    $ callScreen(location_count)

label worm_popup:
    show expression "boxes/popup_item_worm1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_worm1.png" with dissolve
    $ dirt_pile_done = True
    $ callScreen(location_count)

label altar:
    if M_aqua.is_set("altar pass"):
        scene expression gTimer.image("location_forest_puzzle_day{}")
        pause
        $ callScreen(location_count)

    scene expression gTimer.image("forest_altar{}")
    with fade
    show text "A strange stone structure stands in the middle of the forest." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "It looks old! Completely overgrown in moss..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    if not gTimer.is_dark():
        show text "...and there's {b}sunlight{/b} shining directly down upon it." at Position (xpos= 512, ypos= 700) with dissolve
    else:
        show text "...and there's {b}moonlight{/b} shining directly down upon it." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "This must be what I'm looking for." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    if not gTimer.is_dark():
        scene location_forest_puzzle_day
        player_name "Hmm..."
        player_name "This looks like the alter that was on the church bell"
        player_name "...But something's not right. This just looks like a dead end."
        player_name "Hmm, what were the clues again?"
        player_name "A stone alter, with trees around it and the {b}moon{/b} shining down."
        player_name "I should think it over."
        $ callScreen(location_count)
    else:

        scene location_forest_puzzle_night_closed
        $ gTimer.tick()
        player_name "Well that's strange."
        player_name "It looks like the moon is effecting the alter somehow."
        player_name "These symbols must be important and it looks like I can move them around to make a picture..."
        player_name "Maybe it's some kind of puzzle?"
        label altar_puzzle:
            call screen altar_puzzle
            if piecelist[9] == [162,143] and piecelist[18] == [382,20] and piecelist[16] == [600,139] and piecelist[14] == [383,263] and piecelist[10] == [163,385] and piecelist[12] == [603,387] and piecelist[20] == [384,516]:
                call screen altar_puzzle_finish
            jump altar_puzzle
        label altar_puzzle_finish:
            scene expression "location_forest_puzzle_night"
            show expression "objects/object_map_01.png" at Position(xalign = 0.473, yalign = 0.44)
            with None
            show popup_item_map1 at truecenter with dissolve
            $ inventory.items.append(treasure_map)
            pause
            hide popup_item_map1 with dissolve
            $ M_aqua.trigger(T_aqua_altar_puzzle_solve)
        $ callScreen(location_count)