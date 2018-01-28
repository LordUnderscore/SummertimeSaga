default lower_bait = False
default fish_caught = ""
default fishing_first = True
default bait_dialogue = False
default first_fish = False
default fish_caught_count = 0
default pier_first_visit = True
default pier_board_first = True

label pier_dialogue:
    $ location_count = "Pier"
    $ playSound(audio.a_pier, 1.0)
    if pier_first_visit:
        $ pier_first_visit = False
        scene expression gTimer.image("pier{}")
        show player 2 at left with dissolve
        player_name "( It smells like the ocean around here. )"
        player_name "( People say it's the best spot for {b}fishing{/b}. )"
    $ callScreen(location_count)

label terry_button_dialogue:
    $ playMusic(audio.m_pier)
    scene expression gTimer.image("pier_closeup{}")
    if M_terry.get_state() == S_terry_start:
        show terry 1 at Position(xpos=0.6992,ypos=0.7047)
        show player 13 at left with dissolve
        pause
        show player 36
        player_name "Hello."
        show player 13
        show terry 2
        Terry "Well what have we here? Come to do a bit fishin' have we?"
        show player 29
        show terry 1
        player_name "What makes you think that?"
        show player 3
        show terry 2
        Terry "Oh ho, I know the look of a fisherman when I see one."
        show player 11
        Terry "What's your name lad?"
        show terry 1
        show player 14
        player_name "{b}[firstname]{/b}."
        show player 13
        show terry 2
        Terry "Good to meet ya, {b}[firstname]{/b}!"
        Terry "Captain Terry at your service!"
        show player 14
        show terry 1
        player_name "Is this your dock?"
        show player 13
        show terry 2 zorder2
        Terry "Indeed it is. And this here's my shop. Fish and tequila, the two things I love best in this world!"
        show terry 1

        show sara 4 zorder1 at right with dissolve
        sara "..."
        show sara 5
        sara "The two things you love best, huh?"
        show player 11
        show sara 4
        show terry 17b
        Terry "Err... Well, not more than you of course..."
        show terry 18b
        show sara 5
        sara "Uh huh."
        show sara 2
        sara "And who's this then?"
        show player 13
        show sara 1
        player_name "..."
        show terry 2
        Terry "This here's {b}[firstname]{/b}. He's come to do a bit of fishin'."
        show terry 1
        show player 29
        player_name "Hello, Miss?"
        show terry 15
        Terry "Meet the lovely {b}Sara{/b}."
        show player 14
        show terry 1
        player_name "Your wife?"
        show player 13
        show terry 16
        Terry "Lord no, lad. My wife is the Sea."
        show terry 15
        show sara 4
        Terry "Sara here means far more to me than any wife!"
        show sara 3
        Terry "She's the love of my life! My first mate and business partner."
        show terry 1
        show sara 6
        sara "Hehe, alright, well done. I forgive you for the fish and tequilla remark."
        show player 13
        show sara 2
        sara "Anything I can get for you boys, just give me a holler."
        show sara 1
        show terry 16
        Terry "Will do my love, will do!"
        show terry 1
        show sara 2
        sara "Nice to meet you, {b}[firstname]{/b}!"
        show player 36
        show sara 1
        player_name "You too Miss {b}Sara{/b}!"
        hide sara
        with dissolve

        show player 13
        show terry 15
        Terry "Oh ho, I always hate to see her go but I sure do love to watch her leave."
        player_name "..."
        show player 2
        show terry 1
        player_name "So where's the best place to fish around here Captain Terry?"
        show player 1
        show terry 2
        Terry "Well right off the dock, of course!"
        Terry "Just cast a line from that {b}chair{/b} over yonder and the fish won't be long comin'."
        show player 2
        show terry 1
        player_name "Alright! Any other tips?"
        show player 1
        show terry 4 at Position(xpos=0.71,ypos=0.7047)
        Terry "Hmm..."
        show terry 2 at Position(xpos=0.6992,ypos=0.7047)
        Terry "Pay close attention to what bait you're using."
        Terry "Not every fish likes the same type."
        show player 2
        show terry 1
        player_name "Okay, got it."
        show player 1
        show terry 2
        Terry "Oh, and anything you catch out there. I'll buy it off ya for a good price."
        show player 2
        show terry 1
        player_name "Alright, I'll give it a shot. Anything else?"
        show player 1
        show terry 2
        Terry "Don't go in the water!"
        show player 10
        show terry 1
        player_name "Huh? Why not?"
        show player 11
        show terry 2
        Terry "There's dangerous things swimming 'round this dock."
        show player 10
        show terry 1
        player_name "Really?"
        show player 11
        show terry 2
        Terry "You betcha'. The fishin's great but you don't wanna be swimmin' here!"
        show player 10
        show terry 1
        player_name "Oh... Okay Captain. Thanks for all the advice."
        show player 11
        show terry 2
        Terry "Aye, Good Luck out there Skipper!"
        hide player with dissolve
        $ M_terry.trigger(T_terry_intro)
        $ callScreen(location_count)

    elif M_terry.get_state() == S_terry_nemesis:
        show player 2 at left
        player_name "Hey, Captain Terry, I-"
        show player 10
        player_name "Oh..."

        show player 11
        show tstand 3 at right with dissolve
        Terry "I almost had him, Sara! Had him *hic* had him right there on the dock!"
        show tstand 14
        sara "Yes, I know Dear..."
        show tstand 3
        Terry "The little demon snapped at my hand and I dropped em!"
        Terry "Right back in th- *hic* right back in the drink he went!"
        show tstand 14
        sara "Uh huh..."
        show tstand 3
        Terry "Ker Ssssplaaaaash! Oh hohohoho!"
        show player 10
        show tstand 5
        player_name "Uhh... You alright Captain Terry?"
        show player 11
        show tstand 3
        Terry "Skipper!"
        show tstand 15
        Terry "Ooooh... Oh ho...I'm *hic* I'm fiiiiiine."
        Terry "Feelin' just wonderfuuuul."
        show tstand 6
        sara "Hello {b}[firstname]{/b}."
        show player 36
        show tstand 5
        player_name "Hi Miss Sara."
        show player 10
        player_name "What's wrong with the Captain?"
        show player 11
        show tstand 6
        sara "Nothings wrong. He just had a bad day and too much tequila."
        show tstand 3
        Terry "Ooh noooo... No, I'm *hic* I'm sober as a.. *hic* sober as a church mouse."
        show tstand 6
        sara "I'm taking him to bed."
        show player 10
        show tstand 5
        player_name "Oh, okay."
        show player 11
        show tstand 3
        Terry "That *hic* devil fish don't know who he's messin' with, I telllll yooouu!"
        show tstand 14
        sara "Aww, Terry..."
        sara "You can't keep doing this to yourself."
        show tstand 4
        show player 38
        player_name "Devil fish? What's he on about?"
        show player 11
        show tstand 6
        sara "*sigh*"
        sara "I don't think he'd want me telling you."
        show tstand 3
        Terry "Oh ho, non- *hic* nonsense! I trust the Skipper here."
        show tstand 4
        sara "..."
        show tstand 14
        sara "You're sure?"
        show tstand 3
        Terry "Ayeeee."
        show tstand 6
        sara "You see, Terry here..."
        sara "... He's been chasing after this particular fish for years."
        show tstand 15
        Terry "Tigger! Damn his scaley hide!"
        show player 10
        show tstand 5
        player_name "That's an odd name for a fish."
        show player 11
        show tstand 15
        Terry "He ain't no fish! He's a devil the ocean shat out to torment me, I tell you!"
        show tstand 5
        player_name "..."
        show player 10
        player_name "Why does Terry want him so bad?"
        show player 11
        show tstand 6
        sara "Well you see, a few years back, Tigger kinda... Attacked Terry."
        show tstand 5
        show player 12
        player_name "Attacked him?!"
        show player 11
        show tstand 3
        Terry "Took me- *hic* Took my little piggy."
        show player 10
        show tstand 5
        player_name "Little piggy?"
        show player 11
        show tstand 15
        Terry "You know... The one that went wee wee wee all the way home?"
        show player 3
        show tstand 5
        player_name "..."
        show tstand 6
        sara "... His toe."
        show player 29
        show tstand 5
        player_name "Ooooh!"
        show player 30
        player_name "Gross."
        show player 2
        player_name "So that's why you warned me not to swim around the dock."
        show player 1
        show tstand 15
        Terry "That's it exactly!"
        show player 2
        show tstand 5
        player_name "Can I help?"
        show player 1
        show tstand 3
        Terry "Oh no, lad. Tigger's my curse. I can't be unleashin' him on someone else!"
        show tstand 6
        sara "I really think its best I get him into bed."
        sara "{b}[firstname]{/b}, why don't you come back another time?"
        show player 10
        show tstand 5
        player_name "Oh, okay Miss Sara."
        show player 11
        show tstand 14
        sara "Come on Terry..."
        show tstand 3
        Terry "Whatever you say, my- *hic* my love!"

        show tstand 3f at Position(xpos=1.05,ypos=1.0):
        Terry "♪Ohhh, better far to live and die...♪"
        show tstand 3f at Position(xpos=1.25,ypos=1.0):
        Terry "♪Under the brave black flag I fly...♪"
        hide tstand with dissolve

        show player 10
        player_name "I feel bad for the Captain... I wish I could help him."
        hide player with dissolve
        $ M_terry.trigger(T_terry_tigger)
        $ callScreen(location_count)

    elif M_terry.get_state() == S_terry_retire and tigger in inventory.items:
        show tstand 11 at right with dissolve
        Terry "I'm tellin' you, Love. That fish is livin' on borrowed time!"
        Terry "I'll mount his cursed hide in the shop for all to see!"
        show tstand 16
        sara "Oh Terry, I don't see how a compass is going to accomplish that..."
        show tstand 10
        show player 36 at left with dissolve
        player_name "Hey Captain!"
        show tstand 12
        pause
        player_name "Hello, Miss Sara."
        show player 1
        show tstand 13
        sara "Well hi there, {b}[firstname]{/b}. Come for a drink?"
        show tstand 11
        Terry "Aye, a nice shot of tequila before you head out to fish!"
        show player 29
        show tstand 17
        player_name "Oh, no thank you..."
        player_name "I actually came by to give you something, Captain."
        show player 3
        show tstand 17
        Terry "Oh ho, your too kind, Skipper. What have you got for me this time?"
        show player 2
        player_name "Well..."
        show player 239_240
        pause
        show player 465 with hpunch
        show tstand 18
        player_name "This!"
        show player 464

        Terry "Sweet Jesus!"
        show tstand 2 zorder 1 at Position(xpos=.9,ypos=1.0)
        show sara 4 zorder 2 at Position(xpos=.8325,ypos=1.0) with dissolve
        Terry "That's him!"
        Terry "The Skipper here caught old Tigger!"
        show player 465
        show tstand 1
        player_name "I did!"
        show player 464
        show sara 2
        sara "Wow, That is one ugly fish..."
        show sara 1
        show tstand 2
        Terry "I told you! Straight outta hell that fish!"
        Terry "Let me see him."

        show player 1
        show tstand 7
        Terry "I can't believe it."
        show tstand 9
        Terry "..."
        show tstand 8
        Terry "I CAN'T believe it!"
        Terry "You see Sara! I told you the compass would do the trick!!"
        show tstand 9
        show sara 5
        sara "Terry, the Compass didn't do this. {b}[firstname]{/b} did!"
        show tstand 8
        show sara 4
        Terry "Aye, he did. Because I have the compass! Don't you see!?"
        Terry "I've gotta get him inside. Be right back!"
        show tstand 9
        hide tstand with dissolve

        show sara 2
        sara "It's finally over."
        sara "This obsession of his is finally at an end!"
        sara "You have no idea how much this means to me, {b}[firstname]{/b}."
        sara "I'm afraid I'll never be able to repay you!"
        show player 2
        show sara 1
        player_name "Oh, that's okay, Miss Sara."
        player_name "I just wanted to help Captain Terry."
        show player 1
        sara "..."
        show sara 2
        sara "You're a good kid."
        sara "I..."
        show sara 1

        show tstand 2 at Position(xpos=.725,ypos=1.0)
        show sara 3
        Terry "Do you know what this means?!"
        show tstand 1
        player_name "..."
        show sara 6
        sara "That we can finally talk about you retiring?"
        show tstand 2
        show sara 3
        Terry "What?! ...Oh, sure, Suuure! We'll get right to that."
        Terry "After I've had myself a nice long swim!"
        hide tstand with dissolve
        show sara 4f
        Terry "Hahahaha!"
        show sara 5f

        sara "Wait a second!"
        show sara 4f
        pause
        show sara 5f
        sara "Terry!!!"
        show player 23
        sara "Oh my gosh, Don't take those off!"
        sara "Terry, there's people watching!"
        show player 11
        show sara 4f
        pause
        show sara 5f
        sara "Ugh."
        hide sara with dissolve

        show player 13
        player_name "..."

        scene location_pier_running
        with fade
        show text "Captain Terry had spent years avoiding that water..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "But now that Tigger was finally gone, it seems he couldn't wait to get reacquainted." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "I couldn't contain my smile as I watched him gleefully bound into the water." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "The pride I felt at bringing him this moment..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Is something I'll never forget." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve
        $ M_terry.trigger(T_terry_overjoyed_swim)
        $ M_aqua.trigger(T_aqua_test_pass)
        $ location_count = "Town Map"
        $ callScreen(location_count)

    elif M_terry.get_state() == S_terry_tigger_sign:
        scene location_pier_cutscene
        with fade
        show text "My first return to the Captain's shack found him hard at work." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "It seemed Captain Terry had wasted little time getting Tigger stuffed and mounted." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "True to his word, he was hanging his trophy up for all to see." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve

        scene location_pier_closeup
        show tstand 1f with dissolve
        show tstand 2f
        Terry "Haha! Bet my toe isn't tasting so good now is it, ya big ugly bastard?!"
        show tstand 1f
        show player 13 at left with dissolve
        player_name "..."
        show player 14
        player_name "I like the new wall ornament, Captain."
        show player 13
        show tstand 2 at right
        Terry "Aye, it's a hell of a thing isn't Skipper?"
        Terry "Thanks again, fer catchin' that menace."
        show tstand 1
        show player 14
        player_name "I'm just happy I could help."
        show tstand 2
        show player 13
        Terry "Well... Your a good Lad."
        Terry "You let me know if there's ever anything me and mine can do for ya."
        show tstand 1
        show player 14
        player_name "Okay, Captain. I will!"
        show tstand 2
        show player 13
        Terry "Anything at all now! You hear me?"
        show tstand 1
        show player 14
        player_name "I hear you."
        show player 13
        pause
        show player 12
        player_name "So, where is Miss Sara at today?"
        show tstand 2
        show player 11
        Terry "Ahh, she's off plannin' for our vacation."
        show tstand 1
        show player 10
        player_name "Vacation, huh?"
        player_name "Where you going?"
        show tstand 2
        show player 11
        Terry "Wherever the lady says... Hah!"
        show tstand 1
        show player 14
        player_name "Haha! Well I'm happy for you guys."
        player_name "When are you leaving?"
        show tstand 2
        show player 13
        Terry "Bah, I'd wager not anytime soon Skipper."
        Terry "The little lady is just full of excitement right now."
        Terry "What with me finally hanging up the hat and all."
        show tstand 1
        show player 14
        player_name "Oh, okay!"
        show tstand 2
        show player 13
        Terry "Speaking of my retirement; I wanted to let you know..."
        Terry "I'll still buy any fish that you catch off my dock there Skipper."
        show tstand 1
        show player 10
        player_name "... But I thought you weren't gonna sell them anymore?"
        show tstand 2
        show player 11
        Terry "Well I'm still allowed to eat 'em aren't I?"
        show tstand 1
        show player 10
        player_name "Oh, y-yeah! Of course!"
        show tstand 2
        show player 11
        Terry "Oh ho... You know I can't get on without my fish and tequila!"
        show player 13
        Terry "... And the fresher the fish the better!"
        show tstand 1
        show player 14
        player_name "Alright, I'll keep that in mind Captain."
        show tstand 2
        show player 13
        Terry "Good lad!"
        Terry "Well, I reckon I'd best be off."
        show tstand 1
        pause
        show tstand 2
        Terry "Remember now, anything you need, I'm yer man!"
        show tstand 1
        show player 14
        player_name "Alright, Captain! I'll see ya around!"
        show player 13
        hide tstand with dissolve
        show player 4
        player_name "(Hmm, I bet Aqua would let me catch a few fish here and there.)"
        player_name "(Now that Terry is retired.)"
        $ M_terry.trigger(T_terry_hang_tigger)
        $ callScreen(location_count)
    else:

        show terry 1 at Position(xpos=0.6992,ypos=0.7047)
        show player 36 at left with dissolve
        player_name "Hey Captain!"
        show player 203
        show terry 2
        Terry "Well Hello there Skipper!"
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
                "Seatrout":
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

        "What's your secret?" if M_terry.get_state() == S_terry_secret:
            show player 2 at left
            show terry 1 at Position(xpos=0.6992,ypos=0.7047)
            player_name "How did you get so good at fishing, Captain?"
            show terry 2
            show player 203
            Terry "Oh ho, years of practice Skipper."
            show player 2
            show terry 1
            player_name "Is that all?"
            show terry 2
            show player 203
            Terry "... Well..."
            Terry "... I also got a secret weapon!"
            show terry 1
            show player 14
            player_name "Really?! What is it?"
            show terry 15
            show player 203
            Terry "Hah, you can't be expectin' a Master Fisherman to reveal all his secrets!"
            show terry 1
            show player 2
            player_name "Aww, c'mon Captain. You can tell me!"
            show terry 2
            show player 203
            Terry "Hmm..."
            show terry 16
            Terry "Ahaha, well aren't you persistant? I like that!"
            show terry 15
            Terry "A good fisherman needs persistance!"
            show terry 2
            Terry "Alright Skipper, C'mere and I'll show you my secret lure."
            show terry 9 at Position(xpos=0.671,ypos=0.7047)
            show player 14
            player_name "Secret lure? Neat!"
            player_name "What's it do?"
            show terry 10
            show player 203
            Terry "Oh ho, this baby catches everything!"
            Terry "The fish just can't resist it!"
            show terry 9
            show player 14
            player_name "Wow!"
            player_name "Would you sell it to me?"
            show terry 11
            show player 203
            Terry "Haha, sell it to you?! Lad, it's priceless!"
            show terry 13
            show player 24
            player_name "Oh, I see..."
            show terry 11
            Terry "Hmm... Well don't be lookin' so down."
            show terry 10
            Terry "I tell you what. You find me something equally priceless and I'll trade you."
            show terry 1 at Position(xpos=0.6992,ypos=0.7047)
            show player 12
            player_name "Well what did you have in mind?"
            show terry 2
            show player 11
            Terry "How about the {b}Golden Compass{/b}?"
            show terry 1
            show player 12
            player_name "What's that?"
            show terry 2
            show player 11
            Terry "An old fisherman's tale."
            Terry "Long ago, there was a great builder of ships livin' in these parts."
            Terry "They say he possessed a {b}Golden Compass{/b} that could lead you to your hearts desire."
            show terry 1
            show player 12
            player_name "That sounds made up!"
            show terry 15
            show player 11
            Terry "Ho ho, aye, that it does lad."
            show terry 2
            Terry "But if such a thing were to exist..."
            Terry "I reckon it would be well worth tradin' my lure for."
            Terry "What do you say?"
            show terry 1
            show player 14
            player_name "Hmm... I suppose I could look into it."
            show terry 2
            show player 13
            Terry "That's a good lad!"
            show terry 1
            show player 14
            player_name "Where do you recommend I start?"
            show terry 2
            show player 13
            Terry "I'd start searchin' for the ship builder."
            Terry "If he really existed, I reckon he's buried somewhere in the town cemetery."
            show terry 1
            show player 14
            player_name "Sounds good, what was his name?"
            show terry 16
            show player 13
            Terry "Oh ho, I haven't the slightest."
            show terry 1
            show player 10
            player_name "Ah, jeez."
            show terry 2
            show player 11
            Terry "Maybe you should ask around town. One of the {b}older residents{/b} might now something."
            show terry 1
            show player 10
            player_name "Alright, I guess I'd better get started."
            show terry 2
            show player 13
            Terry "Best of luck, Skipper!"
            show terry 1
            show player 14
            player_name "Thanks Captain."
            $ M_terry.trigger(T_terry_secret_lure)
            $ M_aqua.trigger(T_aqua_special_lure)

        "About that lure..." if M_terry.get_state() in [S_terry_lure, S_terry_trade] and M_aqua.get_state() != S_aqua_trade:
            show terry 1 at Position(xpos=0.6992,ypos=0.7047)
            show player 14 at left
            player_name "What did you want in trade for the lure again?"
            show terry 2
            show player 13
            Terry "I'm afraid nothin' short of the {b}Golden Compass{/b} will do, Skipper."
            show terry 1
            show player 14
            player_name "Oh, that's right! Where should I start looking?"
            show terry 2
            show player 13
            Terry "I'd ask around town if I were you."
            Terry "See if any of the {b}older residents{/b} know somethin' about the guy who owned it."
            Terry "It's said he was a great builder of ships."
            show terry 1
            show player 14
            player_name "Okay, Thanks Captain."

        "Golden Compass." if M_aqua.get_state() == S_aqua_trade and M_terry.get_state() == S_terry_trade:
            show player 2 at left
            show terry 1 at Position(xpos=0.6992,ypos=0.7047)
            player_name "You still got that lure, Captain?"
            show player 1
            show terry 15
            Terry "You betcha! Never let it out of my sight."
            show player 2
            show terry 1
            player_name "Good, because guess what I've brought you?"

            show terry 19
            show player 239_240
            pause
            show player 466
            show terry 17
            Terry "Couldn't be..."
            show player 467
            show terry 19
            player_name "I found it! I found the Golden Compass!"
            show player 466
            show terry 17
            Terry "You're kiddin'!"
            show player 467
            show terry 19
            player_name "Here, have a look!"

            show player 1
            show terry 21 at Position(xpos=0.654,ypos=0.712)
            pause
            show terry 22
            Terry "By Blackheart's slimy backside!"
            Terry "The damned thing does exist!"
            show player 10
            show terry 21
            player_name "..."
            player_name "You mean you didn't really believe in it?"
            show player 5
            show terry 22
            Terry "Lord no, Lad. I never intended to part with my lure..."
            Terry "I need it to catch Tigger and my lure is the only bait he's ever gone after."
            Terry "Well, ignorin' my missin' piggy, of course."
            show player 24
            show terry 21
            player_name "Oh, I see."

            show terry 4 at Position(xpos=0.71,ypos=0.7047)
            pause
            show terry 10 at Position(xpos=0.671,ypos=0.7047)
            Terry "I reckon this belongs to you now!"

            show player 470
            show terry 2 at Position(xpos=0.6992,ypos=0.7047)
            pause
            show player 471
            player_name "What? But you just said-"
            show player 470
            show terry 15
            Terry "Well I don't need it now, Do I Skipper?!"
            show terry 16
            Terry "I've got a Golden Compass."
            show terry 15
            show player 13
            Terry "A Golden Compass that will lead me to my hearts desire."
            Terry "And since my heart desires that little bastard's head..."
            Terry "Well I'd say this is a fair trade, wouldn't you?"

            show player 14
            show terry 1
            player_name "Yeah!"
            show player 13
            show terry 2
            Terry "Now you just be careful usin' that lure!"
            Terry "It sometimes catches... {b}Unexpected things{/b}."
            show player 14
            show terry 1
            player_name "I'll be careful, Captain."
            show player 13
            show terry 22 at Position(xpos=0.654,ypos=0.712)
            Terry "Good lad. Now, let me have a look at this beauty!"
            show terry 21
            show player 34f
            player_name "(Hmm... {b}Unexpected things?{/b})"
            player_name "(I wonder what that means?)"
            show popup_lure at truecenter with dissolve
            $ inventory.items.remove(golden_compass)
            $ inventory.items.append(special_lure)
            pause
            hide popup_lure with dissolve
            $ M_terry.trigger(T_terry_lure_trade)
            $ M_aqua.trigger(T_terry_lure_trade)

        "Retire." if M_terry.get_state() in [S_terry_bored, S_terry_retire] and M_aqua.get_state() == S_aqua_valor_test:
            show player 2 at left
            show terry 1 at Position(xpos=0.6992,ypos=0.7047)
            player_name "Hey, Captain. I have a question for you."
            show player 1
            show terry 2
            Terry "Oh? What can I do for you, Skipper?"
            show player 2
            show terry 1
            player_name "You ever thought about retiring from the fishing business?"
            show player 1
            show terry 19
            Terry "Hmm..."
            show terry 20
            Terry "To tell ya the truth. Yes. I've been thinkin' about it for a few years now."
            show player 2
            show terry 1
            player_name "Really?"
            show player 1
            show terry 17
            Terry "Don't get me wrong, lad. I love the hunt!"
            show terry 20
            Terry "Nothin' beats a day on the sea, rod in the water, the breeze in my beard..."
            show terry 15
            Terry "That is... Nothin' but my Sara."
            show player 2
            show terry 1
            player_name "You really love her, huh, Captain?"
            show player 1
            show terry 15
            Terry "Aye lad, I really do."
            show terry 17
            Terry "And she's been wantin' me to retire for as long as I can remember."
            show terry 20
            Terry "Says she wants to travel a bit, see the world."
            show terry 17
            Terry "Truth be told I think she just want's me around more often."
            show player 2
            show terry 1
            player_name "So why don't you do it?"
            show player 1
            show terry 17
            Terry "I can't, Skipper!"
            Terry "Not in good conscious!"
            Terry "Not while that monster's still out there lurkin' about!"
            show player 10
            show terry 18
            player_name "Ahh, Tigger?"
            show player 11
            show terry 20
            Terry "*spits* Devil Fish!"
            show terry 2
            Terry "But now that you've brought me the Golden Compass..."
            Terry "It's only a matter of time till that bastard meets his end!"
            show player 10
            show terry 1
            player_name "Okay, well thanks for being honest with me Captain."
            show player 11
            show terry 2
            Terry "Don't mention it, Skipper!"
            show terry 16
            Terry "You've proved yourself a true blue friend to me and mine."
            show player 34
            show terry 1
            player_name "(I bet if I caught Tigger, Captain Terry would quit fishing.)"
            player_name "(I have to try. Aqua is counting on me!)"
            $ M_terry.trigger(T_terry_retire)
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