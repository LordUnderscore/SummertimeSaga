label yoga_room:
    $ location_count = "Yoga Room"
    if mrsj.started(mrsj_yoga_help) and is_here("anna"):
        jump mrsj_yoga_help
    elif not is_here("mrsj") and not is_here("anna"):
        scene expression gTimer.image("yoga_room{}")
        show player 12
        with dissolve
        player_name "( There's no one I know here... )"
        show player 35
        player_name "( I should come back another time, perhaps... )"
        hide player 35 with dissolve
    $ callScreen(location_count)

label mrsj_yoga_help:
    scene yoga_room_night
    if yoga_fail_retry:
        show player 385 at left with dissolve
        show anna 2 at right with dissolve
        anna "Ready to try again?"
        show anna 1
        show player 386
        player_name "I think I got the positions memorized this time."
        show player 385
        anna "Just tell me which positions to get into and I'll follow your lead."
    else:

        show player 380 at left with dissolve
        show anna 12 at right with dissolve
        if Anna.known(anna_intro):
            anna "Excuse me?"
        else:
            "Excuse me?"
        show player 385
        if Anna.known(anna_intro):
            anna "Have you seen {b}Mrs. Johnson{/b} around lately?"
        else:
            "Have you seen {b}Mrs. Johnson{/b} around lately?"
        show anna 11
        show player 384
        player_name "Actually, she won't be able to make it tonight."
        show player 386
        player_name "She sent me to help teach her class..."
        show player 385
        show anna 12
        if Anna.known(anna_intro):
            anna "Oh, has she told you what to do?"
        else:
            "Oh, has she told you what to do?"
        show anna 11
        show player 386
        player_name "Well, {b}Mrs. Johnson{/b} gave me this list of instructions."
        show player 381
        player_name "I looked over them a bit... I think I can manage."
        if Anna.known(anna_intro):
            show player 386
            player_name "She said you could maybe help me?"
            show player 385
            show anna 2 with dissolve
            anna "Of course I'll help you!"
            anna "And don't worry! You just tell me which positions and I'll follow your lead."
        else:

            show player 384
            player_name "Have you seen a girl named, {b}Anna{/b}?"
            player_name "{b}Mrs. Johnson{/b} said she'd be able to assist me."
            show player 385
            show anna 3 with dissolve
            anna "I'm {b}Anna{/b}!!"
            show anna 1
            show player 386
            player_name "Oh!!"
            show player 385
            show anna 3
            anna "I hope you know what you're doing. Ha ha!"
            show anna 2
            anna "I'll be there to help you through the moves, don't worry."
    hide player
    hide anna
    scene black
    with fade

    scene yoga_front
    show anna 14
    show player 411 at left
    with dissolve
    player_name "Hmm..."
    show player 412
    player_name "Okay, we have to do three consecutive positions, in the right order..."
    show player 411
    show anna 13
    anna "Ummm... Are you ready?"
    show anna 14
    show player 414 with dissolve
    player_name "I think so?"
    show player 413
    show anna 13
    anna "Well, which pose do we start with first?"
    show anna 14
    show player 412 with dissolve
    $ yoga_position = ""
    $ boner_fail = False
    $ gTimer.tick()
    menu yoga_class:
        player_name "The first position is..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            jump yoga_failure
        "Plow Position.":

            $ yoga_position = "Plow Position"
            jump yoga_failure
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            show player 414 with dissolve
            player_name "We need to do the {b}[yoga_position]{/b}?"
            show player 413
            show anna 15
            anna "Oh, right. I love that position!"
            show anna 18 with dissolve
            anna "Why don't I get myself on the mat and you help me stretch?"
            show anna 17
            show player 416
            player_name "Uhh... Okay."
            hide player
            show anna 19
            with dissolve
            pause
            pause
            anna "Don't hesitate to add some force to your push!"
            show anna 19_20
            pause
            show player 411 at left
            show anna 18
            with dissolve
            anna "That was good! I already feel more limber!"
            show anna 17
            show player 412

        "End Lesson." if mrsj.completed(mrsj_yoga_help):
            jump yoga_end_lesson

    menu:
        player_name "Okay, for the second position, I think we should try..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            player_name "...the {b}[yoga_position]{/b}?"
            show player 413 with dissolve
            show anna 18
            anna "Of course!"
            anna "It's one of my favorites."
            anna "Let me get on my back so you can push on my legs to stretch..."
            show anna 21 with dissolve
            show player 416
            player_name "!!!"
            hide player
            show anna 23
            with dissolve
            player_name "Push on your legs?"
            show anna 24
            anna "Yeah!"
            anna "Just push them back so I can stretch..."
            show anna 25 with dissolve
            pause
            pause
            pause
            show anna 27 with dissolve
            anna "That felt great..."
            show anna 28
            player_name "..."
            anna "Oh!!"
            show anna 26
            player_name "Ha ha! I think we are ready for the last position!"
        "Plow Position.":

            $ yoga_position = "Plow Position"
            jump yoga_failure
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            jump yoga_failure

        "End Lesson." if mrsj.completed(mrsj_yoga_help):
            jump yoga_end_lesson

    menu:
        player_name "The last position should follow up this one..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            $ boner_fail = True
            jump yoga_failure
        "Plow Position.":

            $ yoga_position = "Plow Position"
            player_name "...The {b}[yoga_position]{/b}?"
            show anna 27
            anna "Perfect!"
            show player 420 at left
            show anna 29
            with dissolve
            pause
            show anna 30
            anna "All you have to do is press your... pelvis against my butt."
            show anna 29
            show player 421
            player_name "Umm... Okay..."
            hide player
            show anna 31
            with dissolve
            pause
            show anna 32
            anna "Ahh, yes!"
            hide anna
            show anna_slow 31_32
            pause
            anna "Just a bit more!!"
            hide anna_slow 31_32
            show anna_fast 31_32
            pause
            hide anna_fast 31_32
            jump yoga_success
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            $ boner_fail = True
            jump yoga_failure

        "End Lesson." if mrsj.completed(mrsj_yoga_help):
            $ boner_fail = True
            jump yoga_end_lesson

    label yoga_failure:
        $ yoga_fail_retry = True
        if boner_fail:
            show player 419 at left
            show anna 21
        else:
            show player 418 at left
        with dissolve
        player_name "Umm... I think {b}[yoga_position]{/b} is the next position."
        player_name "I'm not really sure though."
        player_name "I can't remember..."
        if boner_fail:
            show player 420
        else:
            show player 417
        show anna 13 with dissolve
        if mrsj.started(mrsj_yoga_help):
            anna "It's probably best if we just skip this class for now."
        anna "We can try again tomorrow."
        if boner_fail:
            show player 419
        else:
            show player 418
        show anna 14
        player_name "Yeah..."
        player_name "Sorry."
        if boner_fail:
            show player 420
        else:
            show player 417
        show anna 13
        if mrsj.started(mrsj_yoga_help):
            anna "Just look over {b}Mrs. Johnson{/b}'s notes and be sure to memorize them for the next class."
        else:
            anna "Just look over {b}Mrs. Johnson{/b}'s notes and be sure to memorize them for next time."
        if boner_fail:
            show player 419
        else:
            show player 418
        show anna 14
        player_name "Alright. I'll do my best..."
        hide anna
        hide player
        with dissolve

        scene yoga_room_night
        show player 24 with dissolve
        player_name "Damn... I couldn't do it."
        if mrsj.started(mrsj_yoga_help):
            player_name "I should memorize the moves and try again tomorrow."
            show player 25
            player_name "I can't let {b}Mrs. Johnson{/b} and {b}Anna{/b} down like that..."
        else:
            player_name "I should memorize the moves and try again."
        hide player with dissolve
        $ callScreen(location_count)

    label yoga_success:
        show player 420 at left
        show anna 22
        with dissolve
        anna "That was... excellent!"
        show anna 21
        show player 419
        player_name "I... I'm sorry about..."
        show player 420
        show anna 15 with dissolve
        anna "Oh! Ha ha!"
        show anna 13
        anna "It's fine!"
        anna "That always happens to guys who come to our class!"
        show anna 16
        anna "And I didn't mind the extra... push..."
        if mrsj.completed(mrsj_yoga_help):
            $ callScreen(location_count)

        $ mrsj_yoga_help.finish()
        $ mrsj.add_event(mrsj_yoga_help_2)
        scene yoga_room_night
        show player 82 at left
        show anna 2 at right
        with dissolve
        anna "I'm impressed!"
        anna "You did such a great job..."
        show anna 3
        anna "...And I really enjoyed being your assistant!"
        show anna 1
        show player 83
        player_name "I was just trying to help {b}Mrs. Johnson{/b}."
        show player 79 with dissolve
        player_name "It was kinda fun."
        show player 82 at left with dissolve
        show anna 2
        anna "Hopefully, you can come by again soon to teach the class... with my help?"
        anna "That is... if you'd like to..."
        show anna 1
        show player 79 with dissolve
        player_name "That might be fun!"
        show player 82 at left with dissolve
        show anna 2
        anna "Just make sure you come at night."
        anna "It's when {b}Mrs. Johnson{/b} is away and I need the help..."
        show anna 1
        show player 83
        player_name "Umm... Sure."
        hide player
        hide anna
        with dissolve
        show unlock43 at truecenter with dissolve
        pause
        hide unlock43 with dissolve
        $ callScreen(location_count)

    label yoga_end_lesson:
        scene yoga_room_night
        if boner_fail:
            show player 82 at left
            show player 79
        else:
            show player 14 at left
        show anna 1 at right
        with dissolve
        player_name "That was fun!"
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 3
        anna "Yeah!"
        show anna 2
        anna "You sure did good this time. I'm impressed!"
        show anna 1
        if boner_fail:
            show player 79 with dissolve
        else:
            show player 14
        player_name "Thanks!"
        player_name "I was just trying to help."
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 2
        anna "I wouldn't mind doing it again with you..."
        anna "...If you'd like."
        show anna 1
        if boner_fail:
            show player 79 with dissolve
        else:
            show player 14
        player_name "Of course!"
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 2
        anna "Great! See you next time..."
        hide player
        hide anna
        with dissolve
        $ callScreen(location_count)

label anna_yoga_button_dialogue:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Hello, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Hi, {b}Anna{/b}."
    show player 13
    show anna 2
    anna "What's up?"
    show anna 1
    menu:
        "Where's {b}Mrs. Johnson{/b}?":
            show player 14
            player_name "I'm looking for {b}Mrs. Johnson{/b}."
            show player 30
            player_name "Do you know where I could find her?"
            show player 5
            show anna 2
            anna "She usually teaches during the day."
            anna "She must be home by now..."
            show anna 1
            show player 14
            player_name "Oh. I see. Thanks!"
            show player 13
            show anna 3
            anna "No problem!"
            show anna 1

        "Yoga" if mrsj.completed(mrsj_yoga_help):
            show player 10
            player_name "Do you want to practice some yoga poses with me?"
            show player 5
            show anna 3
            anna "Of course!!"
            show anna 2
            anna "I like when someone can help me reach those... hard postures..."
            show anna 1
            show player 33
            player_name "Right, you're quite flexible as I remember."
            show player 13
            show anna 2
            anna "Alright, let's find a yoga mat..."
            hide anna
            scene location_yoga_front
            with fade
            show player 413 at left
            show anna 13
            with dissolve
            anna "Which position should we practice?"
            $ yoga_position = ""
            $ boner_fail = False
            $ gTimer.tick()
            jump yoga_class
    $ callScreen(location_count)

label mrsj_yoga_button_dialogue:
    scene expression gTimer.image("yoga_room{}")
    if not mrsj.known(mrsj_yoga_intro):
        show player 1 at left with dissolve
        show erikmom 10 at right with dissolve
        player_name "Umm-"
        show player 11 at left
        window hide
        pause
        player_name "..."
        show erikmom 11 at right
        window hide
        pause
        show erikmom 12 at right
        window hide
        pause
        show erikmom 13 at right with hpunch
        erimom "Oh!"
        show player 18 at left
        erimom "...{b}[firstname]{/b}?"
        show erikmom 14 at right
        show player 17 at left
        player_name "Hi, {b}Mrs. Johnson{/b}!"
        show erikmom 17 at right
        show player 1 at left
        erimom "What are you doing here?"
        show erikmom 14 at right
        show player 29 at left
        player_name "I... saw you from the main {b}Gym{/b}!"
        player_name "I just came to say hi!"
        show player 13 at left
        show erikmom 18 at right
        erimom "That's so sweet!"
        show erikmom 17 at right
        erimom "So you're working out now, huh?"
        show erikmom 14 at right
        show player 21 at left
        player_name "Haha. Yeah..."
        player_name "...Just started to train to get fit!"
        show erikmom 19 at right
        show player 11 at left
        erimom "And I bet you'll get nice and {b}hard{/b}-"
        erimom "..."
        show player 13 at left
        show erikmom 18 at right
        erimom "I mean, {b}strong{/b}!"
        show erikmom 14 at right
        show player 17 at left
        player_name "I hope so..."
        show erikmom 17 at right
        show player 1 at left
        erimom "Anyway, is there anything you wanted to talk about?"
        $ mrsj.add_event(mrsj_yoga_intro)
        $ mrsj_yoga_intro.finish()
    else:

        show player 14 at left
        show erikmom 14 at right
        with dissolve
        player_name "Hi, {b}Mrs. Johnson{/b}!"
        show player 1 at left
        show erikmom 17 at right
        erimom "Hi, {b}[firstname]{/b}!"
        show player 11 at left
        show erikmom 18 at right
        erimom "You're starting to look fit, young man!"
        show player 29 at left
        show erikmom 14 at right
        player_name "Oh. Thanks..."
        player_name "So are you..."
        show player 1 at left
        show erikmom 17 at right
        erimom "Is there anything you wanted to talk about?"

    menu erikmom_options_repeat:
        "How's Erik?":
            show player 10 at left
            show erikmom 14 at right
            player_name "How's {b}Erik{/b} these days?"
            player_name "I hardly see him."
            show erikmom 18 at right
            show player 5 at left
            erimom "Well... You know how he is!"
            erimom "He just loves his video games..."
            show player 10 at left
            show erikmom 14 at right
            player_name "Yeah, but it's been even worse lately."
            player_name "I don't even get text messages from him..."
            show erikmom 19 at right
            show player 5 at left
            erimom "..."
            show erikmom 20 at right
            show player 11 at left
            erimom "You know that his {b}Father{/b} left us when he was born so..."
            erimom "...He's had a lonely upbringing!"
            show erikmom 19 at right
            show player 12 at left
            player_name "...I never knew that..."
            show erikmom 20 at right
            show player 11 at left
            erimom "He's never had a {b}Dad{/b} or {b}brothers{/b}!"
            erimom "He also never had any girls in his life... Other than his mom..."
            show erikmom 19 at right
            erimom "...So, I just try to give him all the affection he needs!"
            show erikmom 14 at right
            show player 21 at left
            player_name "...Yeah. I think I understand."
            show erikmom 18 at right
            show player 13 at left
            erimom "Anyway, I want to thank you for being so friendly to my boy!"
            erimom "You are such a good friend to him..."
            show erikmom 14 at right
            show player 17 at left
            player_name "Well, we've always been friends so..."
            show erikmom 18 at right
            show player 1 at left
            erimom "I'll tell him to text you more often!"
            show erikmom 14 at right
            show player 14 at left
            player_name "It's alright, I just wanted to make sure he's okay."
            show erikmom 17 at right
            show player 1 at left
            erimom "Is there anything else you wanted to talk about?"
            jump erikmom_options_repeat
        "What was that?":

            show erikmom 14 at right
            show player 14 at left
            player_name "What was that {b}yoga pose{/b} you were doing earlier?"
            show erikmom 13 at right
            show player 13 at left
            show player 1 at left
            erimom "Oh, I'll show you!"
            show erikmom 12 at right
            show player 11 at left
            erimom "You start like this!"
            show erikmom 11 at right
            window hide
            pause
            show player 21 at left
            show erikmom 10 at right
            window hide
            pause
            erimom "All the way down on your knees!"
            window hide
            pause
            show player 21 at left
            player_name "Uhhh..."
            player_name "...Yeah..."
            show player 11 at left
            erimom "It's called the {b}Cat Cow{/b}!"
            show erikmom 11 at right
            window hide
            pause
            show erikmom 12 at right
            window hide
            pause
            show erikmom 13 at right
            show player 18 at left
            erimom "Not bad, right?"
            if not Anna.known(anna_intro):
                show anna 12f at Position (xpos=600)
                show erikmom 13 at right
                show player 13
                with dissolve
                anna "Hello, {b}Mrs. Johnson{/b}."
                show anna 5f
                anna "Don't tell me you started without me."
                show anna 4f
                show erikmom 18
                erimom "Of course not! I'm just chatting with a friend of my son!"
                show anna 11 at Position (xpos=700) with dissolve
                show erikmom 17b
                erimom "{b}Anna{/b}, this is {b}[firstname]{/b}. {b}[firstname]{/b}, this is my friend, {b}Anna{/b}."
                show erikmom 14
                show player 36 with dissolve
                player_name "Hi!"
                show player 13 with dissolve
                show erikmom 14b
                show anna 12
                anna "You're a friend of {b}Erik{/b}?"
                show anna 11
                show player 14
                show erikmom 14
                player_name "Yeah. We've been friends for a long time."
                show player 12
                player_name "Are you a trainer here too?"
                show player 5
                show anna 2 with dissolve
                show erikmom 14b
                anna "Oh, no. I'm just a student."
                show anna 1
                show player 13
                show erikmom 17
                erimom "{b}Anna{/b} is one of my best. She could teach here if she wanted to!"
                show erikmom 14b
                show anna 3
                anna "Oh, I don't think so! Ha ha!"
                show anna 2
                anna "She's a great teacher and I'm just a novice."
                show anna 1
                show erikmom 17
                erimom "{b}Anna{/b}, is just being humble."
                show erikmom 17b
                erimom "She might be a beginner, but she is very talented... and extremely flexible."
                show erikmom 14b
                show anna 3
                anna "Ha ha."
                show anna 2
                anna "I've gotta go now and get ready for my next lesson."
                show anna 3
                anna "Goodbye, {b}Mrs. Johnson{/b}!"
                show anna 1
                show erikmom 17b
                erimom "See you soon."
                show erikmom 14b
                show anna 2
                anna "It was a pleasure meeting you, {b}[firstname]{/b}."
                show anna 1
                show player 14
                show erikmom 14
                player_name "Bye!"
                $ Anna.add_event(anna_intro)
                $ anna_intro.finish()
                hide anna with dissolve
            show erikmom 17 at right
            show player 1 at left
            erimom "Is there anything else you wanted to talk about?"
            jump erikmom_options_repeat
        "You're so fit!":

            show erikmom 14 at right
            show player 29 at left
            player_name "I have to say, {b}Mrs. Johnson{/b}, you are really fit!"
            player_name "Do you exercise a lot?"
            show erikmom 18 at right
            show player 13 at left
            erimom "Aw... You're so nice!"
            show erikmom 17 at right
            erimom "Well, I come here as often as I can and try to use the Gym..."
            erimom "...I also go jogging! And I do yoga in my room at night as well..."
            show erikmom 19 at right
            show player 21 at left
            player_name "Well, it's working!"
            show player 13 at left
            erimom "You think?"
            show erikmom 15 at right
            show player 11 at left
            erimom "My {b}butt{/b} is still a bit big..."
            show erikmom 16 at right
            show player 23 at left
            erimom "...And my {b}boobs{/b} are not like they used to be..."
            player_name "..."
            show player 28 at left
            show erikmom 19 at right
            player_name "*gulp*"
            show player 1 at left
            show erikmom 18 at right
            erimom "Is there anything else you wanted to talk about?"
            jump erikmom_options_repeat
        "I have to go train!":

            show erikmom 14 at right
            show player 14 at left
            player_name "I should get back to my training!"
            show erikmom 18 at right
            show player 1 at left
            erimom "Okay, then!"
            show erikmom 14 at right
            show player 17 at left
            player_name "Bye, {b}Mrs. Johnson{/b}!"
            hide player 17 at left with dissolve
            hide erikmom 14 at right with dissolve
    $ callScreen(location_count)