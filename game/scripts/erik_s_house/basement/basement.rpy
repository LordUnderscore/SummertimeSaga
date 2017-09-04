label erik_basement:
    $ location_count = "Erik's Basement"
    if erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        jump erik_vr
    elif not erik_basement_seen:
        $ poker_table_seen = False
        $ cabinet_seen = False
        scene erik_basement
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "Duuuuuude! This place looks freaking awesome!"
        player_name "Why have you not shown me this before?"
        show player 1
        show erik 4
        eri "I've never had any reason to."
        eri "That and well... My dad didn't exactly want me wandering around down here."
        show erik 14
        eri "Something about it being bad for my future..."
        show erik 4
        eri "But I don't have to worry about that anymore!"
        show erik 1
        show player 14
        player_name "Can I take a look around the place?"
        show erik 1
        show player 1
        eri "Feel free, man."
        show erik 1
        show player 14
        player_name "Cool!"
        show player 1
        show erik 5
        eri "Just... Please be careful not to break anything."
        eri "This is all I have to remind me of my dad..."
        show erik 1
        show player 14
        player_name "I promise. I'll be careful."
        hide player with dissolve
        hide erik with dissolve
        $ erik_basement_seen = True
    $ callScreen(location_count)

label poker_table:
    scene erik_basement
    if not poker_table_seen:
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "You have a freaking {b}poker table{/b} down here?"
        show player 1
        show erik 4
        eri "Yeah. You wanna play?"
        $ poker_table_seen = True
        menu:
            "Play poker with Erik?"
            "Yes":
                player_name "I would, but I've never played poker before..."
                show player 14
                eri "That's fine, I'll explain the rules."
                show player 1
                show erik 4
                player_name "In that case, let's play!"
                show player 14
                show erik 1

                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                $ callScreen(location_count)
            "No":

                player_name "Maybe some other time, man. I'm not in the mood right now."
                show player 14
                show erik 1
                eri "That's cool. No problem."
                show player 1
                show erik 4
                hide player
                hide erik
    else:

        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Let's play a game of poker!"
        show player 1
        show erik 5
        eri "Yeah I guess we could try it..."
        eri "But don't we need more players?"
        show erik 1
        show player 4
        player_name "Hmm..."
        player_name "Yeah. You're right."
        player_name "We should {b}find someone{/b} who'd want to play with us."
        hide erik
        hide player
        with dissolve
    $ callScreen(location_count)

label mrsj_poker:
    if poker_bot02 == "erik_mom" and not poker_drunk:
        scene erik_basement_c
        show erikmom 19 at right with fastdissolve
        show erik 1f at Position(xpos=300,ypos=768) with fastdissolve
        show player 1 at left with dissolve
        erimom "You boys aren't planning on playing like this, are you?"
        show player 11
        show erikmom 14
        player_name "..."
        show player 10
        player_name "What do you mean?"
        show player 11
        show erikmom 18
        erimom "You can't play poker without a nice drink!"
        show erikmom 14
        show player 1
        show erik 4f
        eri "A drink?"
        show erik 1f
        show erikmom 18
        erimom "Let's see what's left in the {b}alcohol cabinet{/b}, shall we?"
        hide player
        hide erikmom
        hide erik
        with dissolve

    elif poker_bot02 == "erik_mom" and poker_drunk:
        scene poker_table
        show erikmompoker 2 zorder 1 at Position(xpos=857,ypos=626)
        show erikmompokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
        show erikmompokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
        with fade

        erimom "So..."
        erimom "Are we playing {b}Omaha{/b}, or {b}Texas Hold'em{/b}?"
        show erikmompoker 1
        player_name "..."
        player_name "We only know {b}Strip poker{/b}..."
        show erikmompoker 2
        erimom "Ha ha! Are you kidding me?"
        show erikmompoker 10 at Position(xpos=856,ypos=627)
        player_name "It's the only kind people play at school..."
        show erikpoker 2
        eri "You don't have to... {b}Mom{/b}."
        show erikpoker 11
        show erikmompoker 9 at Position(xpos=856,ypos=627)
        erimom "I'll play!"
        show erikmompoker 4 at Position(xpos=857,ypos=626)
        erimom "Your mom is not a prude. She can have fun, too!"
        show erikmompoker 2
        erimom "I Used to play Strip poker back in the day..."
        show erikmompoker 5
        erimom "...And I was the {b}best{/b} at it!"
        show erikpoker 12
        show erikmompoker 1
        eri "So, what do we do now?"
        show erikpoker 1
        menu mrsj_poker_repeat:
            "Play.":
                show erikmompoker 10 at Position(xpos=856,ypos=627)
                show erikpoker 1
                player_name "Let's play!!"
                jump start_poker
            "How to play.":

                player_name "Remind me again, how do I play poker?"
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                jump mrsj_poker_repeat

            "Skip Mini-Game (Cheat)" if cheat_mode:
                menu:
                    "Mrs Johnson Loses":
                        jump mrsj_lost
                    "Erik Loses":
                        jump erik_lost
                    "[player_name] Loses":
                        jump player_lost
    $ callScreen(location_count)

label cabinet:
    scene erik_basement_cabinet
    if poker_bot02 == "":
        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "That's a lot of alchohol..."
        show player 1
        show erik 4
        eri "Yeah, Dad stocked up on this stuff."
        show erik 1
        show player 14
        player_name "Should we try some?"
        show player 1
        show erik 4
        eri "I was thinking maybe we should keep it for a special occasion?"
        show erik 1
        show player 4
        player_name "I guess you're right."
        player_name "We should {b}find someone{/b} who'd want drink with us."
        hide erik
        hide player
        with dissolve

    elif poker_bot02 == "erik_mom":
        if mrsj.completed(mrsj_poker_night_2):
            show erik 4f at Position(xpos=300)
            show player 1 at left
            show erikmom 14 at right
            with dissolve
            eri "I'll fetch the whiskey!"
            show erik 1f
            show erikmom 19
            show player 11
            erimom "Oh, are you two sure about that?"
            show erikmom 19c
            show player 10
            player_name "About what?"
            show erikmom 19
            show player 11
            erimom "The alcohol, you remember what happened last time, right?"
            show erikmom 19c
            show erik 5f
            eri "But, we all had fun, didn't we?"
            show erik 1f
            pause
            show erikmom 14 with fastdissolve
            pause
            show erikmom 17
            show player 1
            erimom "I suppose you're right..."
            show erikmom 18
            erimom "Oh, what the heck, let's do it!"
        else:

            show erik 5f at Position(xpos=300,ypos=768)
            show player 1 at left
            show erikmom 14 at right
            with dissolve
            eri "Whiskey..."
            eri "Whiskey... whiskey..."
            eri "Whiskey... whiskey... whiskey..."
            eri "There's nothing but whiskey in here..."
            show erik 1f
            show erikmom 17
            erimom "Your father only drank whiskey."
            show erikmom 14
            show player 14
            player_name "That's fine!"
            player_name "We'll take whatever's in there, ha ha!"
            show erik 15
            show player 1
            eri "Should we try it before we take it to the table?"
            show erik 16
            show erikmom 22
            erimom "Let's see how this tastes..."
            show erik 20
            show erikmom 21
            show player 185
            with fastdissolve
            eri "Here we go..."
            show player 186
            show erik 17
            player_name "Cheers!"
            show player 189
            show erik 19
            show erikmom 25
            with fastdissolve

            pause
            show erikmom 26
            show erik 17
            show player 190
            with fastdissolve
            pause
            show player 191
            player_name "Ugh!!"
            show player 188
            show erikmom 24
            show erik 17
            erimom "Woaa.."
            show erik 20
            show erikmom 14
            eri "Hmm... Not bad!"
            show erik 17
            player_name "..."
            show player 187
            player_name "You liked that?!"
            show player 188
            show erik 20
            eri "Yeah, it's kind of sweet."
            show player 185
            show erik 17
            show erikmom 18
            erimom "Alright, boys! Let's take this back and start the game!"
        hide erikmom
        hide erik
        hide player
        with dissolve
        $ poker_drunk = True
    $ callScreen(location_count)

label mrsj_afterpoker_fun_block:
    scene erik_basement
    show player 11 at left
    show erik 4 at right
    with dissolve
    eri "I thought we were *Hic* going to the backroom..."
    eri "My mom is waiting for us, remember?"
    show player 14
    show erik 1
    player_name "Oh, riiiight!"
    player_name "Let's go back there and see what she wants."
    show player 1
    show erik 4
    eri "I *Hic* agree."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_vr:
    scene location_erik_basement01_closeup
    show erik 15f at right
    show player 13 at left
    with dissolve
    eri "Hey, {b}[firstname]{/b}."
    show erik 15bf
    show player 14
    player_name "Hey!"
    show player 11
    player_name "..."
    show player 12
    player_name "Are you... Drinking?"
    show player 11
    show erik 15f
    eri "Oh, Mom wanted me to clean up the basement."
    eri "So I'm sorting through Dad's stuff and throwing things out."
    show erik 15bf
    pause
    show player 38 with dissolve
    player_name "!!!" with hpunch
    show player 23 with dissolve
    player_name "Wait!"
    player_name "Can't you see?"
    show player 18
    show erik 15f
    eri "Huh?"
    show erik 15bf
    show player 14
    player_name "We can use all these things!!"
    show player 13
    show erik 5 with dissolve
    eri "What for?"
    show erik 3b
    show player 17
    player_name "Well, I have an idea."
    show player 14
    player_name "What if we put this liquor to good use!"
    show player 17
    player_name "I mean, it'd be a shame to waste it all..."
    show player 13
    show erik 5
    eri "Hmmm.... Yeah, I guess."
    show erik 3b
    show player 14
    player_name "What if we had some friends from school come over and... Have fun!"
    show player 33
    player_name "This place is the perfect party room!"
    show player 14
    player_name "Just think, we could invite girls over, play poker, and get drunk!"
    show player 13
    show erik 5
    eri "I'm not so sure."
    eri "My mom might flip out if things got out of hands..."
    show erik 3b
    show player 12
    player_name "Come on, {b}Erik{/b}... This place is perfect!"
    show player 14
    player_name "Just think of the cool stuff we could do!"
    show player 33
    player_name "We could even get girls to play some strip poker..."
    show player 18
    show erik 4 with hpunch
    eri "!!!"
    eri "I don't know, {b}[firstname]{/b}..."
    show erik 1
    show player 30
    player_name "Hmm..."
    pause
    show player 12
    player_name "What if I bought you something you always wanted?"
    player_name "Would you help me invite friends over?"
    show player 14
    player_name "I've been making some money! I can definitely help you get what you want..."
    show player 13
    eri "..."
    show erik 4
    eri "Well, there is something I've always wanted... But it costs a LOT!"
    show erik 1
    show player 14
    player_name "Yeah? What is it?"
    show player 13
    show erik 4
    eri "Down at {b}Cosmic Cumics{/b}, I saw they were selling the VR headset {b}Virtual Saga X{/b}."
    show erik 1
    show player 17
    player_name "Done!"
    show player 13
    show erik 5
    eri "Really?!"
    eri "But, wait! I... I also want a game with it, too."
    show erik 4
    eri "It's called... {b}World of Orcette{/b}."
    show erik 1
    show player 11
    player_name "..."
    show player 12
    player_name "Is that one of those lewd games about-"
    show player 5
    show erik 5b
    eri "Uhh!!"
    show erik 5
    eri "Anyway!"
    show erik 4
    eri "Those would do it, I think!"
    eri "You can find them at {b}Cosmic Cumics{/b}, in the mall."
    show erik 1
    show player 14
    player_name "Alright."
    player_name "It's a deal!"
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_vr)
    $ callScreen(location_count)

label erik_card_hunt:
    scene location_erik_basement01_closeup
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Hi, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Hey, {b}Erik{/b}."
    show player 2
    player_name "Thought I'd stop by and see what you're up to."
    show player 1
    show erik 5
    eri "Oh, just looking for my {b}Magic the Fappening{/b} cards."
    eri "I have to get ready for the next tournament, but I can't seem to find them..."
    show erik 1
    show player 14
    player_name "Oh yeah?"
    show player 13
    show erik 5
    eri "I usually leave them down in the basement, but they aren't here."
    show erik 1
    show player 12
    player_name "Hmm..."
    player_name "I can help you look for them. They shouldn't have gone too far."
    show player 13
    show erik 5
    eri "They should be right here."
    eri "I wonder if Mom moved them..."
    show erik 1
    show player 14
    player_name "Oh yeah: She just left."
    show player 17
    player_name "She said that she'd bring back dinner."
    show player 5
    show erik 5
    eri "Damn it. Missed her."
    eri "Maybe I left them upstairs."
    eri "Could you look down here, so I check upstairs?"
    show erik 1
    show player 14
    player_name "Yeah."
    show player 5

    hide erik with dissolve
    show player 4
    player_name "( I wonder where he left the cards. )"
    show player 12
    player_name "( They have to be down here somewhere... )"
    hide player with dissolve
    $ erik.add_event(erik_card_hunt)
    $ callScreen(location_count)

label erik_orcette:
    scene location_erik_basement01_closeup
    show erik 1 at right
    show player 14 at left
    with dissolve
    player_name "Down in the basement, again?"
    player_name "What are you up to?"
    show player 13
    show erik 5
    eri "Hey, {b}[firstname]{/b}!"
    eri "Well, I'm thinking of selling my dad's poker table..."
    show erik 1
    show player 23
    player_name "What?!"
    show player 30
    player_name "Why!"
    show player 12
    player_name "That poker table is so cool!"
    show player 5
    show erik 3b
    eri "..."
    show player 10
    player_name "I mean that thing is made out of solid oak! Didn't your dad say he had it custom made?"
    show player 11
    show erik 5
    eri "Yeah... But we don't use it."
    eri "And I could use some money."
    show erik 3b
    show player 12
    player_name "Yeah, but is your mom even ok with you selling it?"
    show player 11
    show erik 5
    eri "Probably not, but I really need to get some cash for... something."
    show erik 3b
    show player 12
    player_name "Come on, {b}Erik{/b}. I thought you said all these things down here reminded you of your dad."
    player_name "What's so important that you need to sell your dad's poker table?"
    show player 5
    show erik 3
    eri "Well..."
    show erik 5
    eri "It's sort of personal?"
    show erik 3b
    show player 26
    player_name "Oh, come on."
    pause
    show player 14
    player_name "Fine! I'll buy the item if you promise not to sell the table."
    show player 30
    player_name "Deal?"
    show player 5
    eri "..."
    show erik 4
    eri "Why would you do that?"
    show erik 1
    show player 43
    player_name "Because I have some plans for this basement!"
    show player 14
    player_name "I think we could use it to hang out... And maybe invite... people over!"
    show player 13
    show erik 4
    eri "Alright..."
    show erik 5
    eri "But promise you won't make fun of me?"
    show erik 3b
    show player 12
    player_name "Ehh... Sure?"
    show player 5
    eri "..."
    show erik 5
    eri "You can only buy this thing online..."
    eri "So if your computer is still broken, you're gonna need to fix it."
    show erik 1
    show player 12
    player_name "What is it you want me to buy, {b}Erik{/b}?"
    show player 5
    eri "..."
    show erik 4
    eri "Well, have you ever heard of the {b}Orcette{/b}?"
    show erik 1
    pause
    show player 10
    player_name "The what?"
    show player 11
    show erik 5
    eri "It's like... a rubber... tube?"
    show erik 1
    show player 12
    player_name "What?"
    show player 11
    show erik 5
    eri "And it's green!"
    show erik 1
    show player 14
    player_name "Wait... Is it a, sex toy?!"
    show player 13
    show erik 5
    eri "Hey! You promised!"
    show erik 3
    show player 17
    player_name "Alright. Alright."
    show player 26
    player_name "So you want one of those, huh?"
    show player 13
    show erik 5
    eri "I don't know, I've always wanted to try it, but..."
    show erik 3
    show player 14
    player_name "But, what?"
    show player 13
    show erik 5
    eri "Well, I can't have my mom see this package come in the mail..."
    eri "...So you'd have to deliver it to your address!"
    show erik 1
    show player 12
    player_name "But what if my mom sees it?"
    show player 10
    player_name "Or my sister!"
    show player 11
    show erik 5
    eri "You just have to keep track of when it will arrive."
    show erik 1
    show player 12
    player_name "What?"
    show player 11
    show erik 5
    eri "Just get to your mailbox as soon as the mail arrives on the day it's delivered."
    show erik 4
    eri "The package never has to set foot in your house!"
    show erik 1
    show player 12
    player_name "Alright. I'll see what I can do."
    show player 5
    show erik 4
    eri "Thanks, {b}[firstname]{/b}. You're the best!"
    show erik 1
    show player 14
    player_name "Yeah. Yeah."

    hide erik with dissolve
    show player 12
    player_name "( I guess I should get on my computer and look up this {b}Orcette{/b}... )"
    hide player with dissolve
    $ erik.add_event(erik_orcette)
    $ callScreen(location_count)