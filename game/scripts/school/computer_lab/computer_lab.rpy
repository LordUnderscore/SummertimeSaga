label computer_lab_dialogue:
    $ location_count = "Computer Lab"
    $ callScreen(location_count)

label june_dialogue:
    scene school_computer_b
    if June.completed(june_mc_help):
        show player 14 at left
        show june 5 at right
        player_name "Hey, {b}June{/b}!"
        show player 1
        show june 6
        june "Hi, {b}[firstname]{/b}!"
        june "What's up?"
        show june 5
    else:

        if is_here("erik"):
            show erik 1b at Position (xpos=700)
        show june 1 at right
        show player 14 at left
        with dissolve
        player_name "Hi!"
        show june 3
        show player 1
        june "Oh, uh, hi?"
        june "What's up?"
        show june 2
    menu:
        "Nothing.":
            show june 2 at right
            show player 14
            player_name "Oh, nothing!"
            player_name "Just saying hi."
            show player 1
            show june 4
            june "Oh, okay then..."
            show june 1
            show player 29 at Position(xoffset=8)
            player_name "Err... I'll see you later!"

        "Hang out." if June.completed(june_mc_help) and not june_hang_out:
            show player 14 at left
            player_name "I was wondering if you wanted to hang out at my place?"
            show player 1
            show june 6
            june "Sure!"
            june "After school?"
            show player 14
            show june 5
            player_name "Yeah."
            show player 1
            show june 6
            june "So, your room it is, then?"
            show player 10
            show june 5
            player_name "My room?"
            show player 11
            show june 6
            june "Yeah! We need a nice quiet place to chill and play games."
            show player 14
            show june 5
            player_name "Heh, okay!"
            show player 1
            show june 6
            june "Awesome!"
            june "I got classes coming up, I should get going."
            june "I'll see ya after school, {b}[firstname]{/b}!"
            if not June.known(june_mc_help_2):
                $ June.add_event(june_mc_help_2)
            $ june_hang_out = True

        "Cosplay." if June.started(june_cosplay) and orcette_cosplay not in inventory.items:
            show player 14 at left
            show june 2 at right
            player_name "What cosplay were you trying to make again?"
            show player 1
            show june 3
            june "Oh, it's an orcette costume."
            june "It should have the teeth, necklace and belt!"
            show player 14
            show june 2
            player_name "Ah, right!"
            player_name "I think I know a place in the {b}mall{/b} that has costumes..."
            show player 1
            show june 6
            june "Oh yeah?"
            show player 14
            show june 5
            player_name "I might go by there and check it out!"
            show player 1
            show june 6
            june "Cool! See ya."
            hide june
            hide player
            with dissolve

        "Cosplay." if June.started(june_cosplay) and orcette_cosplay in inventory.items:
            show player 17 at left
            show june 2 at right
            player_name "I think I found something you might like!"
            show player 1
            show june 3
            june "Huh?"
            show june 6
            june "What is it?"
            show june 5
            show player 423 with fastdissolve
            player_name "It's an orcette costume!!"
            show player 422
            show june 6
            june "For my cosplay?!"
            show player 1
            show june 7
            with fastdissolve
            pause
            show player 13
            show june 8
            june "Oh my gosh!!"
            june "It has all the missing pieces I needed!"
            june "Those even look like real teeth!"
            show player 17
            show june 5 with fastdissolve
            player_name "I'm glad you like it."
            show player 14
            player_name "It's going to look great on you!"
            show player 1
            show june 6
            june "Thank you so much, {b}[firstname]{/b}."
            show player 14
            show june 5
            player_name "I'm just glad you'll have a cool cosplay at the comic con."
            show player 11
            show june 6
            june "I'll probably get a lot of attention from the crowds, I'm sure!"
            show player 10
            show june 5
            player_name "You mean like, guys?"
            show player 11
            show june 6
            june "Well, I guess, yeah..."
            show june 5
            player_name "..."
            show june 6
            june "But you know what?"
            june "I think I should test out the cosplay before I go!"
            june "Maybe put it on... in front of a friend?"
            show june 5
            show player 10
            player_name "Like who?"
            show player 11
            show june 6
            june "You!! Silly..."
            show player 17
            show june 5
            player_name "Oh, ha ha!"
            show player 14
            player_name "Sure, I could emm... give you some feedback!"
            show player 1
            show june 6
            june "Great! How about we meet at your house... Like last time?"
            show player 14
            show june 5
            player_name "Okay, I'll see you after school then!"
            show player 1
            show june 6
            june "See you later!"
            hide player
            hide june
            with dissolve
            $ june_hang_out = True
            $ inventory.items.remove(orcette_cosplay)
            $ june_cosplay.finish()

        "Ask about class." if June.completed(june_intro) and (not June.known(june_erik_help) and not June.known(june_mc_help)):
            if not June.known(june_intro_2):
                $ June.add_event(june_intro_2)
            $ june_intro_2.finish()
            show player 14
            show june 2
            player_name "Hey, what class are you in?"
            player_name "I don't see you around school often."
            show player 1
            show june 3
            june "Oh, I don't do sports."
            june "I prefer hanging around here..."
            show player 14
            show june 2
            player_name "What do you do in the computer room?"
            show player 1
            show june 3
            june "You know, just stuff... like browsing the internet..."
            june "... going on message boards, watching streams and playing games."
            show june 2
            show player 14
            player_name "Games, huh?"
            show player 1
            show june 3
            june "Yeah."
            show june 1
            show player 14
            player_name "Like the one you're holding?"
            show player 1
            show june 3
            june "Oh, this thing? It's just a silly game..."
            show player 14
            show june 2
            player_name "What's it called?"
            show player 1
            show june 3
            june "It's called Orc Bork."
            show player 14
            show june 2
            player_name "A game about orcs?"
            show player 1
            show june 3
            june "Yeah."
            show june 4
            june "It's pretty hard."
            show player 11
            june "I've been trying to beat it for months..."
            show player 14
            show june 2
            player_name "Is it really that difficult?"
            show player 1
            show june 3
            june "Well, it's easier when you play with two players."
            show june 4
            june "I just haven't found anyone who plays these kind of games at school..."
            show june 3
            june "Unless, maybe you know someone?"
            show june 1
            $ config.skipping = None
            show popup_warning at truecenter with dissolve
            $ renpy.pause(3, hard=True)
            pause
            hide popup_warning with dissolve
            menu june_route_split:
                "My friend {b}Erik{/b}!":
                    hide screen save
                    show player 14 at left
                    show june 2 at right
                    player_name "Actually, I do!"
                    player_name "My good friend {b}Erik{/b} LOVES games with orcs in them!"
                    player_name "Especially... the orcettes."
                    player_name "I think you two should totally play together!"
                    show player 1
                    show june 3
                    june "{b}Erik{/b}?"
                    show player 11
                    june "I don't think I know him..."
                    show player 10
                    show june 1
                    player_name "He said you borrowed one of his pencils once."
                    show player 1
                    show june 4
                    june "Huh..."
                    show player 14
                    show june 5
                    player_name "Well, he spends a lot of time in his room... playing games..."
                    show player 1
                    show june 6
                    june "Seriously?"
                    show player 14
                    show june 5
                    player_name "I think he could help you beat that game."
                    show player 1
                    show june 6
                    june "That would be awesome."
                    june "Let me know if he's up for it!"
                    show player 17
                    show june 5
                    player_name "Sweet!!"
                    show player 14
                    player_name "I'll definitely let him know."
                    $ June.add_event(june_erik_help)
                "I'll play!":

                    hide screen save
                    show player 14
                    show june 2
                    player_name "I'm not really good at those games... But I'll try!"
                    show player 1
                    show june 4
                    june "You... want to play with me?"
                    june "Are you sure you would like that?"
                    show player 14
                    show june 2
                    player_name "Sure, why not?"
                    show player 11
                    show june 3
                    june "Well, it's just that no one has ever asked before..."
                    show player 17
                    show june 2
                    player_name "I'd gladly be your first!"
                    show player 21
                    show june 5
                    player_name "Err... I mean... Not like-"
                    show player 11
                    show june 6
                    june "Ha ha, you're funny."
                    show june 5
                    player_name "..."
                    show player 14
                    player_name "So... You want to play now?"
                    show player 11
                    show june 6
                    june "Umm... How about we play somewhere else?"
                    june "I'm a bit tired of spending all my time in this computer room..."
                    show player 14
                    show june 5
                    player_name "Okay, where then?"
                    show player 10
                    player_name "If we play in the hallway, {b}Annie{/b} will give us detention..."
                    show player 11
                    show june 6
                    june "Hmm... How about we play at your house?"
                    show player 12
                    show june 5
                    player_name "My... My house?!"
                    show player 11
                    show june 6
                    june "Yeah!"
                    june "After school?"
                    show player 10
                    show june 5
                    player_name "Uhh... I guess we could?"
                    show player 11
                    show june 6
                    june "Awesome!"
                    june "Thanks for wanting to play with me..."
                    show player 13
                    june "It's... really nice of you!"
                    show player 14
                    show june 5
                    player_name "Oh, ha ha. It's nothing..."
                    show player 1
                    show june 6
                    june "Just come ask me when you're ready to hang out!"
                    june "I'll be waiting in here."
                    show player 17
                    show june 5
                    player_name "Sure!"
                    $ June.add_event(june_mc_help)
                "Save Menu.":

                    show screen save
                    pause
                    hide screen save
                    jump june_route_split
    hide june
    hide player
    with dissolve
    $ callScreen(location_count)