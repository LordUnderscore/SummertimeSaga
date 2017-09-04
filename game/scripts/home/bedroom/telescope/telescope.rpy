default erik_mom_seen = False
default mia_bear_seen = False

label erik_bedroom:
    if sister.started(sis_telescope01):
        scene
        show windowerikday 3a
        player_name "( {b}Erik's mom{/b} is there. )"
        show windowerikday 3b with fastdissolve
        player_name "( She's probably just checking on him... )"
        show windowerikday 3c with fastdissolve
        player_name "..."
        player_name "( They're kissing on the mouth? That's weird... )"
        show windowerikday 3d with fastdissolve
        player_name "( What the... )"
        player_name "( Did he just grab her boob?? )"
        show windowerikday 3l with fastdissolve
        player_name "( She's closing his blinds... )"
        show windowerikday 2 with fastdissolve
        pause
        hide windowerikday
        show telescope_caught 1
        with dissolve

        sis "( Hmm... I wonder what he's up to. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( What is he doing? )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 137 at right with fastdissolve
        pause
        show sis 138
        sis "Having fun?"
        show sis 137
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        show sis 136 at Position(xpos=952)
        player_name "What are you doing here?!"
        show player 361
        show sis 135
        sis "The better question would be, what are YOU doing here?"
        sis "Don't you have anything better to do than to spy on our neighbors?"
        show player 360
        show sis 136
        player_name "I... don't know what you're talking about!"
        show player 361
        show sis 135
        sis "Oh, so you were watching birds then?"
        show player 360
        show sis 136
        player_name "Maybe I am!"
        show player 359
        show sis 135
        sis "Hah! You're pathetic..."
        hide sis with fastdissolve
        pause
        show player 360
        player_name "You could at least close the door!"
        $ sis_telescope01.finish()
        jump bedroom_dialogue
    elif gTimer.is_morning():
        if erik_telescope_random == 0:
            scene windowerikmorning01
            if gTimer.is_weekend():
                player_name "( He's not in his room. )"
            else:
                player_name "( He probably already left for school. )"
        else:

            scene windowerikmorning02
            if gTimer.is_weekend():
                player_name "( He probably stayed up all night playing that game... )"
            else:
                player_name "( He's playing games? He should be getting ready for school... )"

    elif gTimer.is_afternoon():
        if erik_telescope_random == 0:
            scene windowerikday 1
            player_name "( He's not home. )"
        elif erik_telescope_random == 1 and erik.over(erik_orcette_2):
            scene windowerikday04a_b
            player_name "( What's Erik looking at? )"
            player_name "( That looks oddly familiar... )"
        elif erik_telescope_random == 2 and erik.over(erik_vr):
            scene windowerikday05a_b
            player_name "Uhh!!" with hpunch
            player_name "( I can see why he was so excited about getting it... )"
        else:
            scene windowerikday 2
            player_name "( The blinds are closed. He must be using his lotion again. )"
    else:

        if erik_telescope_random == 0:
            scene windoweriknight01
            player_name "( He's always playing that game... )"
        else:
            scene windoweriknight02
            player_name "( The blinds are closed. He must be using his lotion again. )"
    $ callScreen(location_count)

label erikmom_bedroom:
    if sister.started(sis_telescope03):
        show windowmomday 3a
        player_name "( Woah! She's completely naked!! )"
        show windowmomday 3b with fastdissolve
        player_name "( Is that a bouncing ball... with a dildo on it?! )"
        show windowmomday 3c with fastdissolve
        player_name "( Why didn't she close the blinds? )"
        show windowmomday 3c-d
        player_name "( It's like she wants to be seen... )"
        player_name "( I think she knows... )"
        player_name "( She's staring right at me. )"
        hide windowmomday
        show telescope_caught 1
        with dissolve

        sis "( Hmm... I wonder what he's up to. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( Busted! )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 136 at Position(xpos=725,ypos=0,xanchor=0,yanchor=0) with fastdissolve
        pause
        show sis 135
        sis "Gosh, you're such a pervert!!"
        show sis 136
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        player_name "How did you-"
        show player 361
        show sis 135
        sis "Oh, I knew you'd be here."
        sis "You can't get enough of that telescope..."
        sis "Let me see what you've found this time."
        show player 360 at Position(ypos=768)
        show sis 136
        player_name "Wait-"
        show player 361
        show sis 138
        sis "Move over."
        show player 361 at left
        show sis 142 at Position(xpos=284,ypos=231)
        with fastdissolve
        sis "Let's have a look..."
        show sis 140 at Position(ypos=229)
        pause
        show windowmomday 3c-d with dissolve
        sis "{b}Mrs. Johnson{/b}?!!"
        sis "Well, damn..."
        sis "She's naughty, isn't she?"
        scene telescope_window
        show player 361 at left
        show sis 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
        with dissolve
        pause
        show sis 142 at Position(xpos=284,ypos=231,xanchor=0,yanchor=0)
        sis "Does she always do this kind of stuff in front of her window?"
        show sis 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
        sis "It's as if she wants to be seen..."
        show player 360
        player_name "...I guess?"
        show player 361
        sis "This is hot... The way she's grinding on that ball..."
        show sis 145_146_147_148 at Position(xpos=286,ypos=229,xanchor=0,yanchor=0) with fastdissolve
        pause
        show player 364
        player_name "!!!"
        show player 361
        sis "I love the way her ass bounces off it."
        show player 362
        sis "I wish that was me sitting on that ball..."
        show sis 144 at Position(ypos=231)
        show player 361
        sis "What's the matter?"
        sis "Your older {b}sister{/b} can't enjoy herself?"
        show player 360
        show sis 143
        player_name "I didn't say that..."
        show player 361
        show sis 144
        sis "Which do you prefer?"
        sis "Watching {b}Mrs. Johnson{/b}... or watching {b}me{/b}?"
        show player 360
        show sis 143
        player_name "I don't know..."
        show sis 139 at right with fastdissolve
        show player 361
        sis "Oops!"
        sis "Well, would you look at that..."
        sis "I'm all {b}wet{/b}!"
        sis "I should keep these for later... Maybe trade them for something..."
        hide sis with dissolve
        pause
        show player 362
        pause
        $ sis_telescope03.finish()
        $ sister.add_event(sis_shower_cuddle04)
        jump bedroom_dialogue

    elif gTimer.is_morning():
        if erik_mom_seen == False:
            scene windowmommorning01
            player_name "( ...is that {b}Erik's mom{/b}?! )"
            scene windowmommorning01b
            player_name "( Oh wow! She's getting dressed... )"
            scene windowmommorning01c
            player_name "( No! Just a little bit longer! )"
            scene windowmommorning01d
            player_name "( Damn! Show's over... )"
            $ erik_mom_seen = True
        else:

            scene windowmomday02
            player_name "( Her blinds are closed. She's probably not home. )"
    elif gTimer.is_afternoon():
        if erikmom_telescope_random == 0:
            scene windowmomday01
            player_name "( She's not home. )"
        elif erikmom_telescope_random == 1 and erik.over(erik_thief_2):
            show windowmomday 3a
            player_name "( Woah... She's completely naked!! )"
            show windowmomday 3b with fastdissolve
            player_name "( Is that a bouncing ball... with a dildo on it?! )"
            show windowmomday 3c with fastdissolve
            player_name "( Why didn't she close the blinds? )"
            show windowmomday 3c-d
            player_name "( It's like she wants to be seen... )"
            player_name "( I think she knows... )"
            player_name "( She's staring right at me. )"
        else:
            scene windowmomday02
            player_name "( Her blinds are closed. She's probably not home. )"
    else:
        if erikmom_telescope_random == 0:
            scene windowmomnight03
            player_name "( ...Is she practicing yoga? )"
            player_name "( ...On her bed? )"
            scene windowmomnight04
            player_name "..."
            player_name "( {b}Erik's mom{/b} is so fit... )"
            player_name "( ...she really does have a great body... )"

        elif erikmom_telescope_random == 1:
            scene windowmomnight01
            player_name "( She's not in her room... )"
        else:
            scene windowmomnight02
            player_name "( She must be sleeping. )"
    $ callScreen(location_count)

label mia_bedroom:
    if sister.started(sis_telescope02):
        scene
        show windowmiaday 3
        player_name "( Oh my... )"
        player_name "( What's {b}Mia{/b} doing? )"
        player_name "( I hope she doesn't get caught doing that... )"
        hide windowmiaday
        show telescope_caught 1
        with dissolve

        sis "( Hmm... I wonder what he's up to. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( Again?! )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 137 at right with fastdissolve
        pause
        show sis 138
        sis "You seem to be enjoying this."
        show sis 137
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        player_name "Could you stop sneaking up on me like that?!"
        show sis 138
        show player 361
        sis "I was just gonna borrow a pencil."
        sis "I didn't expect to catch you perving on our neighbors again..."
        show player 360
        show sis 137
        player_name "I'm not!"
        show player 361
        show sis 138
        sis "Oh, really?"
        sis "Let's see, then."
        show player 360
        show sis 137
        player_name "What?"
        show player 361
        show sis 138
        sis "Move over."
        show player 361 at left
        show sis 142 at Position(xpos=806,ypos=768)
        with fastdissolve
        sis "Let's have a look..."
        show sis 140
        pause
        show windowmiaday 3 with dissolve
        pause
        scene telescope_window
        show player 361 at left
        show sis 140 at Position(xpos=545,ypos=768)
        with dissolve
        sis "... Is that the girl from your class?"
        show sis 142
        sis "Do you enjoy watching girls masturbate?"
        show sis 141
        show player 360
        player_name "It's not like that! I..."
        player_name "It was an accident, I didn't know she was there!"
        show sis 142
        show player 361
        sis "Yeah, right."
        sis "I bet you love watching her do things in her room..."
        sis "Do you jack off while watching her?"
        show sis 141
        show player 360
        player_name "No..."
        show sis 142
        show player 361
        sis "Haha! Sure..."
        show sis 138 at right with fastdissolve
        sis "Forget the pencil..."
        sis "I'll just let you finish whatever you started here..."
        hide sis with fastdissolve
        show player 359
        pause
        $ sis_telescope02.finish()
        $ sister.add_event(sis_hallway02)
        jump bedroom_dialogue

    elif gTimer.is_morning():
        if mia_telescope_random == 0:
            scene windowmiamorning01
            if gTimer.dayOfWeek() == "Sun":
                player_name "( She's getting ready for church. )"
            elif gTimer.is_weekend():
                player_name "( I wonder what she's doing today? )"
            else:
                player_name "( She's getting ready for school. )"
        else:
            scene windowmiamorning02
            player_name "( Too late... I always miss the best part! )"

    elif gTimer.is_afternoon():
        if mia_telescope_random == 0:
            scene windowmiaday 1
            player_name "( Her blinds are closed. She's probably not home. )"
        else:
            scene windowmiaday 2
            player_name "( She's not home. )"
    else:
        if mia_telescope_random == 0:
            scene windowmianight01
            player_name "( She's always reading or studying... )"

        elif mia_telescope_random == 1 and mia_bear_seen == False:
            scene windowmianight03a_b
            player_name "( What's she doing? )"
            player_name "..."
            player_name "( She's... )"
            player_name "( ...Humping her {b}Teddy Bear{/b}? )"
            player_name "( Wow... )"
            player_name "( That's really hot- )"
            scene windowmianight03c with hpunch
            player_name "!!!"
            scene windowmianight03d
            player_name "( Oh, crap! )"
            player_name "( I think she just got caught... )"
            player_name "( Her {b}Mom{/b} must be furious... She's always so strict with her... )"
            $ mia_bear_seen = True
        else:

            scene windowmianight02
            player_name "( She must be sleeping. )"
    $ callScreen(location_count)


label backyard:
    if gTimer.is_morning():
        scene windowbackyardday01
        player_name "( {b}Mrs. Johnson's{/b} yoga matt is there... )"
        player_name "( ...There's no one in the backyard. )"
    elif gTimer.is_afternoon():
        if backyard_telescope_random == 0:
            scene windowbackyardday01
            player_name "( {b}Mrs. Johnson's{/b} yoga mat is there... )"
            player_name "( ...There's no one in the backyard. )"
        elif backyard_telescope_random == 1:
            scene windowbackyardday02
            player_name "( Man... )"
            player_name "( {b}Erik's mom{/b} is so... flexible... )"
        elif backyard_telescope_random == 2:
            scene windowbackyardday03
            player_name "( {b}Mrs. Johnson{/b} is always doing yoga... )"
            player_name "( I guess she likes to stay in shape. )"
        else:
            scene windowbackyardday04
            player_name "( Oh, yeah... )"
            player_name "( That's my favorite position. )"
            player_name "( I get turned on so much when she does that... I don't know why. )"
    else:
        scene windowbackyardnight01
        player_name "( {b}Mrs. Johnson{/b} left her yoga mat outside. )"
    $ callScreen(location_count)

label helen_room:
    if gTimer.is_morning():
        scene windowhelenmorning01
        player_name "( {b}Mia's mom{/b} is always praying in the morning... )"
    elif gTimer.is_afternoon():
        scene windowhelenday01
        player_name "( They're not home... )"
    else:
        if helen_telescope_random == 0:
            scene windowhelennight01
            player_name "( It's odd how they both have their own bed... )"
            player_name "( ...I've never seen them sleep together. )"
        else:
            scene window_helen_night02
            player_name "( Oh boy. )"
            player_name "( Looks like {b}Helen{/b} is mad at him... )"
            player_name "..."
            player_name "( {b}Harold{/b} always looks so sad... )"
    $ callScreen(location_count)