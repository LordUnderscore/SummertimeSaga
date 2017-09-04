label school_dialogue:
    $ location_count = "School Hall"
    $ tick_skip_active = False
    if not gTimer.is_weekend():
        if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg"):
            $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

        if player.in_progress(intense_gymercise):
            scene school
            show jersey 10 with dissolve
            player_name "( Woah! it's hard to breathe! )"
            player_name "( It's so damn hot outside... )"
            show jersey 33 at Position(xoffset=22) with fastdissolve
            player_name "( ... And I'm SOAKED! )"
            player_name "( I should {b}take a shower{/b} before going to my next class. )"
            $ player.complete_events(intense_gymercise)

        elif roxxy.over(roxxy_homework_copy01) and not player.known(intense_gymercise):
            scene school
            show erik 28 at right
            show player 1 at left
            with dissolve
            eri "Hey, {b}[firstname]{/b}."
            show erik 27
            show player 14
            player_name "Hey, {b}Erik{/b}."
            player_name "Why are you dressed-"
            show erik 28
            show player 11
            eri "That's why I came to get you! {b}Coach Bridget{/b} is looking for you!"
            eri "It's gym class right now!"
            show erik 27
            show player 10
            player_name "Crap, I missed a lot of training already! She's gonna kill me!"
            show erik 28
            show player 5
            eri "Quick! You'd better go!"
            show erik 27
            show player 10
            player_name "Thanks for letting me know!"
            show erik 29
            show player 11
            eri "No problem, man!"
            show erik 27
            hide player with dissolve
            pause
            show erik 28
            eri "Good luck!"
            hide erik with dissolve
            $ ui_lock_count = 1
            $ player.add_event(intense_gymercise)

        elif erik.started(erik_bullying_2):
            scene school
            show dexter 9 at right with dissolve
            eri "Ugh!!"
            eri "Let... me go... {b}Dexter{/b}!"
            dex "Not a chance, chubby."
            dex "You still haven't given me your homework."
            dex "I guess you didn't get the message."
            eri "I told you already! I already turned them in! I don't even have them anymore!"
            dex "Well, then I guess you'll have to give me something else..."
            dex "How much money do you got on you?"
            eri "What?!"
            dex "I said, how much money are you going to give me before I shove your face into a locker!!"
            eri "!!!"
            eri "{b}Dexter{/b}! I... I..."
            show player 15 at left with dissolve
            show dexter 10
            player_name "HEY!!!"
            player_name "Leave him alone, {b}Dexter{/b}!"
            show player 16
            show dexter 9
            dex "Well, if it isn't your loser friend."
            show dexter 10
            show player 15
            player_name "{b}Dexter{/b}, stop picking on {b}Erik{/b}."
            show player 16
            show dexter 9
            dex "Why? Would you like to take his place?"
            player_name "..."
            show dexter 12 with dissolve
            dex "Step up, {b}[firstname]{/b}."
            show dexter 13
            dex "Let's see what you got!"


            if pStats.dex() >= 4:
                show dexter 14
                show player 387 with dissolve
                player_name "I'm not scared of you, {b}Dexter{/b}!"
                show player 388
                show dexter 15
                dex "Well, you should be scared of... THIS!"
                hide player
                hide dexter
                show dexter 16 at left
                with dissolve
                pause
                show dexter 17 at right with dissolve
                player_name "Haiii!!"
                hide dexter
                show player 390 at left
                show dexter 18 at right
                with dissolve
                dex "Arghh!!"
                dex "You... Little... Shit..."
                show dexter 15 with dissolve
                show player 389
                player_name "!!!"
                show player 391
                show dexter 19 with hpunch
                pause
                hide player
                show dexter 20 at left
                with dissolve
                dex "Not so fast this time, huh?!"
                dex "I'll make you pay for this..."
                hide player
                with dissolve

                scene school_fight_cs1 with fade
                show text "Even after all my recent training at the gym,\n{b}Dexter{/b} was still too strong for me...\n...but I knew now, that I could hurt him..." at Position (xpos= 512, ypos = 700) with dissolve
                pause
                hide text

                scene school_fight_cs2 with fade
                show text "...And then, everything went dark." at Position (xpos= 512, ypos = 700) with dissolve
                pause
                hide text

                scene black with fade
                pause

                scene school with None
                show mia 24 at left
                show dexter 21 at Position (xpos=713)
                with dissolve
                mia "{b}[firstname]{/b}!! Are you okay?!"
                show mia 23
                pause
                show mia 28 with dissolve
                mia "What's your problem, {b}Dexter{/b}?"
                mia "You really hurt him!"
                show mia 27
                show dexter 22
                dex "Mind your own business!"
                dex "He had it coming!!"
                show dexter 23
                show roxxy 30 at right with dissolve
                rox "{b}Dexter{/b}?"
                show roxxy 29
                show dexter 24
                dex "What?!"
                show dexter 23
                show mia 23 with dissolve
                show roxxy 27
                rox "..."
                show roxxy 28
                rox "Umm.... {b}Dexter{/b}, what's going on?"
                rox "Did you do that?"
                show roxxy 29
                show mia 27 with dissolve
                show dexter 24
                dex "Nothing's going on!!"
                show dexter 12
                dex "I just finished teaching this little shit a lesson."
                show dexter 23
                show roxxy 30
                rox "Really? You had to do this now? In the hallway?"
                show roxxy 29
                show dexter 24
                dex "Shut up, {b}Roxxy{/b}."
                dex "Come on. Lets get out of here!"
                show roxxy 27
                dex "I've got better things to do than watch a bunch of idiots standing around."
                hide dexter
                hide roxxy
                with dissolve
                hide mia
                show eve 9 at Position (xpos=75)
                show mia 23 at left
                show judith 40 at Position (xpos=600)
                show erik 50 at Position (xpos=900)
                with dissolve
                jud "Oh my gosh! What happened?!"
                show judith 41
                show eve 10
                eve "{b}Dexter{/b} is such a jerk."
                eve "He went too far this time."
                show eve 9
                hide erik
                show teacher 15 at Position (xpos=700)
                show erik 50 at Position (xpos=900)
                with dissolve
                bis "!!!"
                bis "What's going on over here?"
                bis "What happened to {b}[firstname]{/b}?"
                show teacher 14
                show mia 26 with dissolve
                mia "He got into a fight with {b}Dexter{/b} and {b}Dexter{/b} slammed him into the lockers."
                mia "He's still breathing. I hope he'll be alright."
                show mia 25
                bis "..."
                show teacher 15
                bis "I'll call the ambulance!"
                $ playSound()
                scene black with fade
                hide mia
                hide eve
                hide teacher
                hide erik
                hide judith
                jump erik_bullying_2
            else:

                show dexter 14 at right with dissolve
                show player 6 at left with dissolve
                player_name "[dex_warn]I don't want to fight you, {b}Dexter{/b}!"
                show player 23 with dissolve
                player_name "[dex_warn]I just want you to leave {b}Erik{/b} alone..."
                show player 22
                show dexter 15
                dex "Really?"
                show dexter 14
                show player 10
                player_name "[dex_warn]That's all..."
                show player 22
                show dexter 12 with dissolve
                dex "Hah!"
                dex "Weak and pathetic..."
                dex "...Just like your father!"
                hide dexter
                with dissolve
                show player 24
                player_name "[dex_warn]..."
                hide player
                with dissolve

        elif erik.started(erik_intro):
            scene school
            show duo 6 at left with dissolve
            show mia 1 at right with dissolve
            player_name "Hey, {b}Mia{/b}!"
            show duo 1 at left
            show mia 4 at right
            mia "Hey, {b}[firstname]{/b}! Glad to see you're back!"
            mia "Hi, {b}Erik{/b}! How was your weekend?"
            show duo 10 at left
            show mia 1 at right
            eri "I mostly stayed in my room..."
            show duo 1 at left
            show mia 3 at right
            mia "That's cool. Sometimes I like alone time too!"
            show mia 4 at right
            mia "What about you, {b}[firstname]{/b}? What have you been up to?"
            show mia 2 at right
            show duo 9 at left
            player_name "Well... I'm not sure if you've heard or not, but my {b}Dad{/b} passed away, so we pretty much had to deal with that..."
            show mia 6 at right
            mia "Oh yeah. I heard from my mom..."
            show duo 15 at left
            mia "I didn't mean to bring it up. I'm sorry you had to go through that. I'm just glad you're finally back!"
            show mia 2 at right
            player_name "Thanks. I'll be fine. Don't worry."
            show mia 4 at right
            mia "Listen... I was looking for someone to {b}help me get ready for the final exams{/b}, so..."
            show duo 7 at left
            mia "...if you're interested, let me know!"
            show duo 8 at left
            show mia 1 at right
            player_name "Uhh... sure? I guess?"
            show mia 3 at right
            mia "You know where I live, so just drop by whenever you want!"
            show duo 7 at left
            show mia 5 at right
            mia "Alright! Talk to you later, guys!"
            hide mia 5 with dissolve

            show unlock1 at truecenter
            $ renpy.pause()
            hide unlock1 with dissolve
            $ loc_mia_unlocked = True
            show duo 1 at left
            show dexrox 1 at right with dissolve
            rox "What're you two losers looking at?!"
            show duo 2 at left
            show dexrox 4 at right
            eri "I think we're looking at the combined IQ of 2."
            show duo 3 at left
            player_name "Hah!!"
            show duo 7 at left
            show dexrox 2 at right
            dex "Hey! Watch your mouth, before I smash your face in, you little shit!"
            show duo 4 at left
            show dexrox 4
            rox "...and what are {b}YOU{/b} laughing at?"
            rox "Didn't your gambling loser of a father kill himself or something?"
            show dexrox 3
            show duo 9
            eri "..."
            show dexrox 4
            show player 15 at left
            show roxxy 3 at right
            player_name "At least I {b}HAD{/b} a father growing up..."
            player_name "...And I don't live in a {b}TRAILER{/b}!!"
            show player 16
            show roxxy 3
            rox "!!!" with hpunch
            show roxxy 14
            rox "I'm going to-"
            show roxxy 29
            show player 11
            show dexrox 3
            dex "Aw, shit! {b}Principal Smith{/b} is coming!!"
            dex "Let's get out of here."
            hide dexrox with dissolve
            show roxxy 14
            show player 16
            rox "I'll deal with you later."
            hide roxxy with dissolve

            show unlock39 at truecenter
            $ renpy.pause()
            $ loc_trailer_unlocked = True
            hide unlock39 with dissolve

            $ renpy.pause()
            hide player
            show duo 1 at left
            show principal 5 at right with dissolve
            smi "You two! Get over here, {b}RIGHT NOW{/b}!!!"
            show duo 11 at left
            smi "What are you still doing in the damn hallway??!"
            show duo 12 at left
            show principal 3 at right
            eri "Sorry, {b}Mrs. Smith{/b}! We were just heading to class..."
            show duo 11 at left
            show principal 4 at right
            smi "You have exactly 3 minutes to get to class, or I'm sending both of you to {b}DETENTION!!{/b}"
            show duo 13 at left
            show principal 2 at right with hpunch
            smi "{b}UNDERSTOOD{/b}?!"
            show duo 14 at left
            show principal 1 at right
            player_name "Yes, {b}Mrs. Smith{/b}!"
            hide duo 14 at left with dissolve
            hide principal 1 at right with dissolve

            show player 1 at left with dissolve
            show erik 5 at right with dissolve
            eri "Okay. I better go to my Maths..."
            show erik 1 at right
            show player 14 at left
            player_name "Yeah, I have Athletics, outside in the {b}Field{/b}, with {b}Coach Bridget{/b}..."
            player_name "... I have to go change in the {b}Locker Room{/b} first though."
            show player 1 at left
            show erik 5 at right
            eri "Oh yeah, I forgot to tell you something!"
            eri "The girl's Locker Room has been closed for the last week, due to repairs..."
            show player 11 at left
            eri "...so the girls have been changing in ours."
            show erik 1 at right
            player_name "..."
            show player 23 at left
            player_name "{b}WHOA?!{/b}"
            show player 5 at left
            show erik 3 at right
            eri "Yeah... Just a heads up - it's a bit awkward in there."
            show player 12 at left
            show erik 1 at right
            player_name "That's crazy..."
            show player 11 at left
            show erik 3 at right
            eri "Everyone's been complaining, especially the girls, as you can imagine..."
            show player 10 at left
            show erik 1 at right
            player_name "I'll see how it goes..."
            show player 1 at left
            show erik 7 at right
            eri "Okay! I gotta go! See ya later... And welcome back!"
            show player 36 at left
            show erik 6 at right
            player_name "Thanks..."
            hide player 36 at left with dissolve
            hide erik 6 at right with dissolve

            $ erik_intro.finish()
            $ school_count = 1
            $ ui_lock_count = 1

        elif not roxxy_copied1 and homework1 in inventory.items:
            scene school
            show player 11 at left with dissolve
            show roxxy 3 at right with dissolve
            rox "Hey!!"
            show roxxy 1 at right
            player_name "..."
            show player 12 at left
            player_name "What do you want?"
            show player 90 at left
            show roxxy 2 at right
            rox "You don't have to be ruuuude..."
            show roxxy 5 at right
            rox "...To your favorite classmate!"
            show roxxy 6 at right
            show player 12 at left
            player_name "Why do I have the feeling you want something from me..."
            show roxxy 10 at right
            show player 90 at left
            rox "Let's cut the bullshit, then!"
            show roxxy 11 at right
            show player 11 at left
            rox "I {b}know{/b} you've finished last week's {b}homework{/b} and you have it."
            show roxxy 9 at right
            show player 56 at left
            player_name "Ehh... Yeah? And?"
            player_name "Shouldn't you have handed in that {b}homework{/b} last week like everyone else?"
            show player 90 at left
            show roxxy 11 at right
            rox "Well... I didn't."
            show roxxy 5 at right
            rox "I'm also behind, like you."
            show roxxy 6 at right
            show player 33 at left
            player_name "Yeah, but I had an excuse... I wasn't at school for a month!"
            show roxxy 10 at right
            show player 30 at left
            player_name "What's your excuse?"
            show roxxy 11 at right
            show player 90 at left
            rox "Haha. You really think I'd waste my time doing {b}homework{/b}..."
            show roxxy 10 at right
            show player 11 at left
            rox "Look, why don't you do me a favor, and let me copy off your {b}homework{/b}!"
            show roxxy 5 at right
            show player 90 at left
            rox "You're the {b}last person{/b} with a {b}copy{/b}. Everyone else gave it to {b}Mrs. Bissette{/b} already..."
            show roxxy 6
            show player 30
            player_name "Why should I help you after all the things you said about my dad?"
            show player 90
            show roxxy 5
            rox "Look, I didn't mean to say those things..."
            show roxxy 11
            rox "...I was just messing with you, alright?"
            show roxxy 6 at right
            rox "It'll only take me a minute... What do you say?"
            $ roxxy_copied1 = True
            $ roxxy.add_event(roxxy_homework_copy01)
            $ roxxy_homework_copy01.finish()
            menu:
                "Not for free!":
                    show player 12 at left
                    show roxxy 10 at right
                    player_name "Why would I do that?"
                    show roxxy 11 at right
                    show player 11 at left
                    rox "Because I'm {b}Roxxy{/b}??"
                    show roxxy 10 at right
                    show player 16 at left
                    rox "...And if you don't, I can always ask my boyfriend to... Change you mind..."
                    show roxxy 9 at right
                    show player 30 at left
                    player_name "You can have it... But not for free!"
                    show roxxy 10 at right
                    show player 91 at left
                    rox "..."
                    rox "What do you want for it?"
                    menu:
                        "Your lolipop!":
                            $ asked_for_lollipop = True
                            show roxxy 9 at right
                            show player 34 at left
                            player_name "Hmm..."
                            show player 92 at left
                            player_name "I want your {b}lolipop{/b}!"
                            show player 91 at left
                            show roxxy 10 at right
                            rox "..."
                            rox "What??"
                            show roxxy 12 at right
                            rox "You want... This, {b}lolipop{/b}?"
                            menu:
                                "Not wet enough...":
                                    show player 34 at left
                                    player_name "Hmm..."
                                    show player 56 at left
                                    player_name "More {b}saliva{/b} on it."
                                    show player 91 at left
                                    show roxxy 13 at right
                                    rox "...You're sick..."
                                    show roxxy 7 at right
                                    rox "..."
                                    show roxxy 8 at right
                                    show player 11 at left
                                    window hide
                                    pause
                                    show roxxy 13 at right
                                    show player 91 at left
                                    rox "...There!"
                                    show player 97 at left
                                    show roxxy 14 at right
                                    player_name "Thanks!"
                                    show player 93 at left
                                    window hide
                                    pause
                                    show player 94 at left
                                    player_name "...Is that cherry flavored?"
                                    show player 93 at left
                                    window hide
                                    pause
                                    show player 95 at left
                                    player_name "Hmmm..."
                                    show player 96 at left
                                    player_name "Here's the {b}homework{/b}!"
                                    show roxxy 15 at right
                                    show player 93 at left
                                    rox "Give me a minute to copy it..."
                                    show player 94 at left
                                    show roxxy 14 at right
                                    rox "...I'll see you later, perv..."
                                    hide roxxy 14 at right with dissolve
                                    hide player 94 at left with dissolve
                                "Of course!":

                                    show player 92 at left
                                    player_name "Of course!"
                                    show roxxy 13 at right
                                    show player 91 at left
                                    rox "That is... So weird..."
                                    rox "...There!"
                                    show player 97 at left
                                    show roxxy 14 at right
                                    player_name "Thanks!"
                                    show player 93 at left
                                    window hide
                                    pause
                                    show player 94 at left
                                    player_name "...Is that cherry flavored?"
                                    show player 93 at left
                                    window hide
                                    pause
                                    show player 95 at left
                                    player_name "Hmmm..."
                                    show player 96 at left
                                    player_name "Here's the {b}homework{/b}!"
                                    show roxxy 15 at right
                                    show player 93 at left
                                    rox "...give me a minute to copy it..."
                                    show roxxy 14 at right
                                    show player 94 at left
                                    rox "...I'll see you later, perv..."
                                    hide roxxy 1 at right with dissolve
                                    hide player 94 at left with dissolve
                "Sure...":

                    show player 12 at left
                    show roxxy 13 at right
                    player_name "Sure..."
                    show player 73 at left
                    player_name "I guess you can have it."
                    show player 86 at left
                    player_name "Here's the {b}homework{/b}!"
                    show roxxy 15 at right
                    show player 1 at left
                    rox "Thanks!"
                    show roxxy 5 at right
                    rox "It'll only take a minute to copy it..."
                    show roxxy 11 at right
                    rox "See you in later!"
                    hide roxxy 11 at right with dissolve
                    hide player 1 at left with dissolve

            label dexter_dialogue:
                if asked_for_lollipop:
                    show player 93 at left
                else:
                    show player 1 at left
                show dexter 3 at right
                with dissolve
                dex "Where do you think {b}you're{/b} going?!"
                if asked_for_lollipop:
                    show player 93 at left
                else:
                    show player 90 at left
                show dexter 2 at right
                player_name "..."
                if asked_for_lollipop:
                    show player 94 at left
                else:
                    show player 12 at left
                player_name "To class?"
                show dexter 6 at right
                if asked_for_lollipop:
                    show player 93 at left
                else:
                    show player 11 at left
                dex "I just saw you talking to my {b}girlfriend{/b}, you loser!"
                dex "What the fuck were you doing?"
                menu:
                    "She wants help.":
                        show dexter 5 at right
                        if asked_for_lollipop:
                            show player 94 at left
                        else:
                            show player 21 at left
                        player_name "Calm down..."
                        show dexter 2 at right
                        if asked_for_lollipop:
                            show player 94 at left
                        else:
                            show player 33 at left
                        player_name "...She asked to see my {b}homework{/b}, so she could copy it."
                        if asked_for_lollipop:
                            show player 94 at left
                        else:
                            show player 2 at left
                        player_name "That's it."
                        show dexter 8 at right
                        if asked_for_lollipop:
                            show player 93 at left
                        else:
                            show player 90 at left
                        dex "Why would she even ask you? You're a fucking loser!"
                        show dexter 4 at right
                        dex "Just stay away from my {b}girlfriend{/b} or I'm gonna kick your ass!"
                        dex "{b}GOT IT{/b}?!"
                        show dexter 2 at right
                        if asked_for_lollipop:
                            show player 94 at left
                        else:
                            show player 90 at left
                        player_name "Yeah, yeah..."
                        hide dexter 2 at right with dissolve
                        hide player with dissolve

                    "She gave me her lolipop." if asked_for_lollipop:
                        show dexter 5 at right
                        show player 93 at left
                        player_name "..."
                        show player 94 at left
                        player_name "You know what, {b}Dexter{/b}?"
                        show player 97 at left
                        player_name "She wanted me to have her {b}lolipop{/b}!"
                        show player 94 at left
                        player_name "...And it's delicious-"
                        hide player
                        show dexter 7 at left with hpunch
                        window hide
                        pause
                        show dexter 2 at right
                        show player 88 at left
                        player_name "{b}UUgghh{/b}..."
                        show dexter 6 at right
                        show player 89 at left
                        dex "Just stay away from my {b}girlfriend{/b} or I'm gonna fuck you up."
                        show dexter 4 at right
                        dex "{b}GOT IT{/b}?!"
                        hide dexter 4 at right
                        hide player 89 at left
                        with dissolve
    else:

        $ location_count = "Town Map"
        if not gTimer.is_dark():
            if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
                $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
        else:
            if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
                $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
        scene event01
        show player 12 with dissolve
        player_name "( It's the {b}weekend{/b}. )"
        player_name "( The school is {b}closed{/b} until {b}Monday{/b}. )"
        hide player 12 with dissolve
        hide event01
    $ callScreen(location_count)

label roxxy_button_dialogue:
    scene location_school_closeup
    show player 2 at left with dissolve
    show roxxy 6 at right
    player_name "Hey Roxxy..."
    show player 1
    show roxxy 11
    rox "Ehm... You talking to me?"
    show player 12
    show roxxy 10
    player_name "...Well, yeah?"
    show player 11
    show roxxy 11
    rox "You're stupid. Please don't talk to me..."
    show player 90
    show roxxy 5
    player_name "..."
    $ callScreen(location_count)

label door06_locked_dialogue:
    scene school
    show player 35 at left
    player_name "( This is the wrong class. )"
    $ callScreen(location_count)

label door06_locked2_dialogue:
    scene school
    show jersey 10 at left
    player_name "( I should go to the {b}Field{/b} for my {b}Athletics{/b} class. )"
    $ callScreen(location_count)

label door05_locked_dialogue:
    scene school
    show player 35 at left
    player_name "( I need to change in the {b}Locker Room{/b} first. )"
    $ callScreen(location_count)

label door05_locked2_dialogue:
    scene school
    show jersey 10 at left
    player_name "( I should go to the {b}Field{/b} for my {b}Athletics{/b} class. )"
    $ callScreen(location_count)

label door05_locked3_dialogue:
    scene school
    show player 35 at left
    player_name "( I should go to {b}Mrs. Bissette's{/b} class now. )"
    $ callScreen(location_count)

label door05_locked4_dialogue:
    scene school
    show jersey 10 at left
    player_name "( I need to shower in the {b}Locker Room{/b}, first. )"
    $ callScreen(location_count)

label night_closed_school:
    if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
        $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    scene event01_night
    if webcam_quest and not webcam_planted:
        if webcam_erik_help:
            $ location_count = "School Hall"
            show player 14 at left
            show erik 1 at right
            player_name "Hey!"
            show player 17
            player_name "I thought you wouldn't show up."
            show player 1
            show erik 4
            eri "I told {b}Mom{/b} I went to see a movie at the mall..."
            show player 17
            show erik 1
            player_name "Nice..."
            show player 11
            show erik 5
            eri "But I can't be out too long: I have to be home before bedtime."
            show player 92
            show erik 1
            player_name "You have a bedtime?!"
            show player 91
            show erik 3
            eri "...I just don't like to upset {b}Mom{/b}, you know?"
            show player 113
            show erik 1
            player_name "Anyway, we have to be quick and quiet!"
            show player 1
            show erik 5
            eri "Is there an alarm, though?"
            show erik 1
            show player 2
            player_name "We don't have to worry about that! We'll use the window!"
            player_name "Just follow me..."
            hide player
            hide erik
            hide event01_night
            hide ui
            scene black
            with dissolve
            with Pause(0.5)
            show outside_school_night02a with dissolve
            show text "After some convincing, {b}Erik{/b} followed me to the right side of the school.\nWe quickly ran through the yard towards one of the main floor windows." at Position (xpos= 512, ypos = 700) with dissolve
            $ renpy.pause ()
            hide text with dissolve

            scene black with dissolve
            with Pause(0.5)

            show outside_school_night02b with dissolve
            show text "I had to give {b}Erik{/b} a boost first.\n I have to say, it was a lot harder than I thought..." at Position (xpos= 512, ypos = 700) with dissolve
            $ renpy.pause ()
            hide text with dissolve

            scene black with dissolve
            with Pause(0.5)

            show outside_school_night02c with dissolve
            show text "It was then my turn, as I jumped up and snuck inside...\n We had finally made it in, and no one had seen us." at Position (xpos= 512, ypos = 700) with dissolve
            $ renpy.pause ()
            $ playMusic()
            hide text with dissolve

            hide outside_school_night02a
            hide outside_school_night02b
            hide outside_school_night02c
            scene black
            with dissolve
            with Pause(0.5)
            scene expression "backgrounds/location_school_night.jpg" with dissolve
            player_name "!!!"
            player_name "I hear someone coming..."
            scene cult_event 1
            with Dissolve(0.3)
            eri "What the-"
            scene cult_event 2
            with Dissolve(0.3)
            player_name "Shhh!"
            player_name "Stay quiet..."
            scene cult_event 3
            with Dissolve(0.3)
            window hide
            pause
            scene cult_event 4
            with Dissolve(0.3)
            scene school_night
            show player 22 at left
            show erik 5 at right
            with dissolve
            eri "I have a bad feeling about this..."
            show player 10
            show erik 1
            player_name "Yeah... Something's going on here."
            show player 11
            show erik 5
            eri "What are they doing in the school this late?"
            eri "Wearing... Strange outfits..."
            show player 92
            show erik 1
            player_name "Let's follow them and see where they're going."
            show player 91
            show erik 5
            eri "I was thinking maybe we should just leave, actually."
            show player 26
            show erik 3
            player_name "Don't be a chicken!"
            player_name "Plus, we still have to finish what we came here for anyway..."
            show player 91
            show erik 2
            eri "{b}*Sigh*{/b}"
            show erik 3
            eri "Okay..."
            hide player 91 with dissolve
            hide erik 3 with dissolve
            $ ui_lock_count = 1
            $ callScreen(location_count)
        else:

            show player 114 with dissolve
            player_name "Hmm..."
            show player 10
            player_name "( I'm gonna need some {b}help{/b} sneaking into the school at night. )"
            hide player 10 with dissolve
    else:

        show player 2 with dissolve
        player_name "( The {b}school{/b} is closed at night... I should come back tomorrow. )"
        hide player 2 with dissolve
        hide event01_night
    jump map_dialogue

label denied_access_mainhall:
    if location_count == "School Hall":
        scene school_night
    elif location_count == "School left Hallway":
        scene expression "backgrounds/location_lefthall_night.jpg"
    show erik 1f at Position (xpos = 550, ypos = 768)
    show player 34 at Position (xpos = 370, ypos = 768)
    player_name "Hmm..."
    show player 113
    player_name "( We should find {b}another way{/b}. )"
    hide player 113
    hide erik 1f
    $ callScreen(location_count)