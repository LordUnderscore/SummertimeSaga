default fingered_mom = False
default shower_sex_count = 0
default sis_shower_intro_first = True
default mom_shower_sex_first = True

label shower_dialogue:
    $ location_count = "Shower"
    if gTimer.is_dark():
        $ callScreen(location_count)


    scene shower2
    if quest17 in quest_list and quest17 not in completed_quests and wrench in inventory.items and quest17_1:
        scene shower_cutscene2 with None
        show text "Once I got back home I rushed into the bathroom and took out the wrench.\nI replaced the joint with a new length of pipe and tightened it until it stopped completely.\nIt kind of felt weird having {b}Mom{/b} and {b}Sis{/b} watch me the whole time.\nHowever, they seemed quite pleased…" at Position(xpos=500, ypos=700)
        with dissolve
        $ renpy.pause()
        hide shower_cutscene2
        hide text
        scene shower2
        show player 203f at right
        show sis 11f at Position(xpos=0.3649,ypos=1.0000)
        show mom 62f at left
        with dissolve
        mom "Wow!!"
        mom "You did it!"
        show sis 9f
        show mom 61f
        sis "Finally..."
        show sis 11f
        show mom 62f
        mom "It was very nice of you to do this for us..."
        show player 2f
        show sis 11f
        show mom 61f
        player_name "It’s fine, {b}Mom{/b}."
        player_name "It wasn’t that hard..."
        player_name "And it’s something I needed to learn how to do, anyway..."
        show player 29f
        show sis 10f
        show mom 62f
        mom "My little boy is going to make a great husband one day!"
        show player 203f
        show sis 9f
        show mom 61f
        sis "Gosh, {b}Mom{/b}..."
        sis "Do you really have to talk like that?"
        show player 16f
        show sis 12f
        sis "And don’t get too excited; he still can’t tie his own shoes..."
        show player 15f
        show sis 11f
        show mom 61f
        player_name "Heyy!"
        show player 16f
        show sis 12f
        sis "Haha!"
        show player 1f
        show sis 11f
        show mom 62f
        mom "Be nice to your {b}brother{/b}!"
        show sis 9f
        show mom 59f
        sis "Anyway, can you two leave, now?"
        show player 11f
        sis "I'm going out tonight and need to get ready."
        show sis 10f
        show mom 60f
        show player 1f
        mom "Don’t stay out too late..."
        show sis 9f
        show mom 59f
        sis "I’m not a kid anymore {b}Mom{/b}..."
        $ completed_quests.append(quest17)
        $ mom_dialogue_advance = True
        $ inventory.items.remove(wrench)
        hide mom
        hide sis
        hide player
        with dissolve
        jump hallway_dialogue

    elif quest17 in quest_list and quest17 not in completed_quests and not quest17_1 and closed_valve == 0:
        scene shower_cutscene1 with None
        show text "I rush upstairs as I hear my {b}Sister{/b} yelling my name.\nI open the door and see her standing by, soaked with water and staring at the sink.\nAn exposed pipe had burst and was leaking water all over the floor…" at Position(xpos=500, ypos=700)
        with dissolve
        $ renpy.pause()
        hide shower_cutscene1
        hide text
        scene shower2
        show player 11 at left
        show sis 27 at right
        with dissolve
        sis "About time you showed up!"
        show player 10
        show sis 26
        player_name "What happened to the sink??"
        show player 11
        show sis 27
        sis "Can’t you see!? The pipe's broken!"
        show player 12
        show sis 26
        player_name "What am I supposed to do?"
        show player 11
        show sis 27
        sis "Get your ass down to the {b}basement{/b} and close the water {b}valve{/b}!"
        show sis 26
        show player 12
        player_name "Okay! I'm going!"
        hide player
        hide sis
        with dissolve
        hide shower2
        hide ui
        $ closed_valve = 1
        jump hallway_dialogue

    elif closed_valve == 1:
        scene shower2 with None
        show sis 27 at right
        show player 11 at left
        with dissolve
        sis "The water's still spraying everywhere!"
        sis "Go to the {b}basement{/b} and shut off the water {b}valve{/b}!"
        hide player
        hide sis
        with dissolve
        hide shower2
        jump hallway_dialogue

    elif quest17 in quest_list and quest17 not in completed_quests and not quest17_1 and closed_valve == 2:
        scene shower2 with None
        show sis 29 at Position (xpos=800)
        show player 11 at left
        with dissolve
        sis "Looks like you got it. The water stopped."
        show player 12
        show sis 26 at right
        player_name "Any idea what I'm supposed to do next?"
        show player 5
        show sis 27
        sis "If I knew, do you think I'd be standing here telling you to fix it!?"
        show player 10
        show sis 26
        player_name "I’ve never fixed this kind of stuff before..."
        show player 5
        show sis 27
        sis "Well I don’t know how, and neither does {b}Mom{/b}. So man up and find a solution, quick!"
        show player 10
        show sis 26
        player_name "Okay! Okay! I’m going to the store now to get a {b}wrench{/b}..."
        show player 212
        player_name "!!!"
        show player
        show sis 28
        $ renpy.pause()
        show sis 27
        sis "..."
        sis "What are you looking at? Shouldn't you be going somewhere?"
        show player 23
        show sis 26
        player_name "Um, nothing!"
        show player 22
        show sis 41 at Position(xpos=0.9123,ypos=1.0000)
        sis "Wait, are you... staring at my boobs?"
        player_name "..."
        sis "What is it? Is it because you can see my nipples through my shirt?"
        show player 24
        show sis 30
        player_name "I’m sorry! I was just-"
        show sis 31
        sis "Stop it."
        show player 25
        sis "I know you're always looking at me that way."
        sis "Is that what you always wanted?"
        sis "To see what they look like... under my shirt?"
        show player 5
        player_name "{b}*Gulp*{/b}"
        show sis 27 at right
        sis "Well, I wouldn’t be all wet, if you had shown up earlier!"
        show sis 41 at Position(xpos=0.9123,ypos=1.0000)
        sis "This is YOUR fault."
        sis "So why don’t you take this..."
        show player 22
        show sis 32
        $ renpy.pause()
        show sis 33
        $ renpy.pause()
        show player 23
        show sis 42 at right
        sis "And put it in the laundry for me?"
        player_name "!!!" with hpunch
        show player 21
        player_name "S-Sure..."
        show sis 37
        show player 211
        sis "..."
        show sis 38
        sis "Now go and get that {b}PIPE FIXED{/b}!!!"
        show player 22
        player_name "!!!"
        hide player with dissolve
        show sis 36
        sis "I knew it!"
        sis "Little brother has a thing for me!"
        hide sis with dissolve
        hide shower2
        $ ui_lock_count = 0
        $ quest17_1 = True
        jump hallway_dialogue

    elif quest17 in quest_list and quest17 not in completed_quests:
        scene shower2
        show player 11 at left
        with dissolve
        player_name "I need to fix the {b}broken pipe{/b} first."
        hide player
        with dissolve
        hide shower2
        jump hallway_dialogue

    elif gTimer.is_morning() and shower == "sister":
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        jump sis_shower

    elif is_here("mom"):
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        scene shower06a
        player_name "!!!"
        player_name "...{b}Mom's{/b} using her body soap..."
        scene shower06b
        player_name "..."
        scene shower06c
        player_name "...She's so pretty..."
        scene shower06d
        player_name "I should go, before she sees me..."
        menu:
            "Walk inside":
                $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
                if henchmen_count >= 2:
                    scene shower_closeup
                    with dissolve
                    show mom 35 at right
                    show player 1 at left
                    mom "Oh! didn't expect you to just barge in like that."
                    show mom 33
                    mom "Though, now that you're here..."
                    show mom 36
                    mom "Care to join me, Sweetie?"
                    hide mom
                    hide player
                    show moms 37 with dissolve
                    label mom_shower_question:
                        $ fingered_mom = False
                        scene shower_closeup
                        show moms 37_36
                        pause 4.8
                        show moms 35
                        player_name "I love showering with you, {b}Mom{/b}"
                        show moms 76 with dissolve
                        pause .1
                        show moms 41_76
                        pause 4
                        show moms 42
                        mom "Can I help you down here too?"
                        show moms 43
                        mom "So..."
                        show moms 44
                        mom "What do you have planned today?"
                        show moms 43
                        mom "Something fun?"
                        show moms 72_71
                        pause 4
                        show moms 45 with dissolve
                        mom "You're all hard. It's up to you now, Sweetie..."
                        if mom_count == 8 and mom_dialogue_advance:
                            jump mom_shower_blowjob
                    label mom_shower:
                        show moms 73 with dissolve
                        menu:
                            "Wash mom.":
                                player_name "I want to wash you this time."
                                show moms 50 with dissolve
                                mom "Go ahead, Sweetie."
                                show moms 51
                                pause 1
                                show moms 52_53_52_51
                                pause 4.8
                                show moms 54
                                player_name "So soft..."
                                label mom_shower_boobs:
                                    menu:
                                        "Handjob.":
                                            label mom_shower_hj:
                                                show moms 45 with dissolve
                                                pause .4
                                                show moms 73_74
                                                pause 4
                                                show moms 73
                                                player_name "{b}Mom{/b}, I'm gonna..."
                                                show moms 47 at Position(xpos=526,ypos=768)
                                                player_name "!!!"
                                                show white zorder 4 with dissolve
                                                show moms 47 at Position(xpos=526,ypos=768)
                                                show playersex 33 zorder 3 at Position(xpos=549,ypos=508)
                                                hide white with dissolve
                                                pause
                                                show moms 48
                                                hide playersex
                                                with dissolve
                                                mom "You sure had a lot in there."
                                            jump mom_shower_end

                                        "Finger Mom." if pStats.chr() >= 3 and mom_count >= 8 and not fingered_mom:
                                            player_name "I haven't washed {b}everywhere{/b} yet..."
                                            show moms 55 at Position(xpos=688,ypos=768) with dissolve
                                            pause .35
                                            show moms 56_55
                                            pause 4
                                            mom "Almost there, Sweetie..."
                                            show moms 56
                                            mom "I-Aaaaah!!!"
                                            show moms 50 at Position(xpos=498,ypos=768) with dissolve
                                            mom "Where did you learn to do {b}that{/b} with your fingers?"
                                            show moms 49
                                            player_name "Nowhere, really..."
                                            show moms 50

                                            $ fingered_mom = True
                                            jump mom_shower_boobs

                                        "Blowjob." if mom_count >= 9:
                                            label mom_shower_blowjob:
                                                show moms 111 with dissolve
                                                mom "Just stay still and let {b}Mommy{/b} take care of this."
                                                show moms 110
                                                player_name "Okay..."
                                                show moms 112 at Position(xpos=512) with dissolve
                                                pause .3
                                                label bj_loop:
                                                    show moms 113_114 at Position(xpos=513)
                                                    pause 5
                                                    show moms 112 at Position(xpos=512)
                                                menu:
                                                    "Cum in mouth":
                                                        show moms 113 at Position(xpos=513)
                                                        pause .3
                                                        show moms 116 at Position(xpos=517)
                                                        player_name "Ahhh!!!"
                                                        mom "!!!"
                                                        show white with dissolve
                                                        hide white with dissolve
                                                        pause
                                                        show moms 117 at Position(xpos=523) with dissolve
                                                        mom "Hmm!!!"
                                                        show moms 118 at Position(xpos=516)
                                                        mom "{b}*Gulp*{/b}"
                                                        show moms 115 at Position(xpos=531)
                                                        mom "I did not expect that.."
                                                        show moms 110 at Position(xpos=512)
                                                        player_name "Sorry, {b}Mom{/b}."
                                                        show moms 111
                                                        mom "It’s okay, Sweetie."
                                                        mom "I kind of missed the taste of it."
                                                        jump mom_shower_end
                                                    "Cum on face":

                                                        show moms 113 at Position(xpos=513)
                                                        pause .3
                                                        show moms 116 at Position(xpos=517)
                                                        player_name "Ahhh!!!"
                                                        mom "!!!"
                                                        show white with dissolve
                                                        show moms 115 at Position(xpos=531)
                                                        show playersex 74 at Position(xpos=530,ypos=519)
                                                        hide white with dissolve
                                                        pause  
                                                        show playersex 75 at Position(xpos=574,ypos=655)
                                                        mom "Wow... It came out so fast!"
                                                        mom "And I’m covered..."
                                                        player_name "Sorry, {b}Mom{/b}."
                                                        mom "It’s okay!"
                                                        mom "Good thing we did it in the shower."
                                                        mom "We can just clean it off!"
                                                        jump mom_shower_end
                                                    "Keep going":

                                                        jump bj_loop

                                        "Sex." if fingered_mom and pStats.chr() >= 7 and mom_count >= 12 and not mom_shower_sex_first:
                                            show moms 49
                                            player_name "Can I put it in?"
                                            show moms 50
                                            mom "Sweetie, I just came... It's a little too sensitive right now..."
                                            mom "I'll finish you off with my hand."
                                            jump mom_shower_hj

                                        "Sex." if not fingered_mom and pStats.chr() >= 7 and mom_count >= 12 and not mom_shower_sex_first:
                                            jump mom_shower_sex
                                        "Leave":

                                            jump mom_shower_end

                            "Sex." if pStats.chr() >= 7 and mom_count >= 12 and mom_basement_sex == True and mom_shower_sex_first == True:
                                label mom_shower_sex:
                                    $ shower_sex_count = 0
                                    $ anim_toggle = False
                                    $ xray = False
                                    $ cum = False
                                    $ mom_shower_sex_first = False
                                    show moms 49 with dissolve
                                    player_name "{b}Mom{/b}..."
                                    player_name "Can I put it in?"
                                    show moms 50
                                    mom "Of course, Sweetie..."
                                    show moms 57 at Position(xpos=688,ypos=768) with dissolve
                                    mom "I've been waiting all day for this..."
                                    show moms 58 with dissolve
                                    mom "Haah!"
                                    show screen xray_scr
                                    label mom_shower_sex_loop:
                                        show moms 59
                                        show screen xray_scr
                                        pause
                                        if anim_toggle == True:
                                            hide moms 59
                                            hide screen xray_scr
                                            if xray == True:
                                                show moms_xray 56_54 at Position(xpos=844,ypos=784)
                                            else:
                                                show moms 61_59 at Position(xpos=688,ypos=768)
                                            pause 8
                                            hide moms_xray 56_54
                                            hide moms 61_59
                                            show moms 59 at Position(xpos=688,ypos=768)
                                        else:

                                            hide screen xray_scr
                                            show moms 61 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 59 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 61 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 59 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 61 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 59 at Position(xpos=688, ypos=768)
                                            pause
                                            show moms 61 at Position(xpos=688, ypos=768)
                                    $ shower_sex_count += 1
                                    if shower_sex_count == 1:
                                        hide screen xray_scr
                                        mom "Give it to me, Sweetie!"
                                        jump mom_shower_sex_loop

                                    elif shower_sex_count == 2:
                                        hide screen xray_scr
                                        mom "Cum for {b}Mommy{/b}!"
                                        jump mom_shower_sex_loop

                                    elif shower_sex_count == 3:
                                        hide screen xray_scr
                                        mom "HAAAAAHH!"
                                    $ cum = True
                                    show moms 60
                                    hide ui
                                    show white zorder 4 with dissolve
                                    hide white with dissolve
                                    pause
                                    show playersex 53 zorder 3 at Position(xpos=663,ypos=632)
                                    show moms 57
                                    with dissolve
                                    hide ui
                                    mom "You let out so much..."
                                    mom "Such a mess."
                                    mom "Good thing we're in the shower..."
                                    jump mom_shower_end
                else:

                    scene shower_closeup
                    show player 3 at left with dissolve
                    show mom 35 at right with dissolve
                    mom "Sweetie, what are you doing in here?"
                    mom "If you need something in the bathroom, I'll be done in a few minutes."
                    mom "Now, let me finish my shower, Sweetie."
                    hide mom
                    hide player
                    jump hallway_dialogue
            "Leave":

                if not mom_revealing_tommorow and learn_kissing:
                    scene hallway
                    show player 26 at left
                    with dissolve
                    player_name "( Now's my chance to sneak into {b}Mom's room{/b}! )"
                    hide player
                    with dissolve
                $ location_count = "Hallway"
                $ callScreen(location_count)
    else:


        scene shower1
        player_name "There's no one in here."
    $ callScreen(location_count)

label mom_shower_end:
    hide playersex
    show moms 34 at Position(xpos=498,ypos=768)
    with dissolve
    mom "That was fun, but we have to finish."
    mom "I'm looking forward to our... next session."
    mom "Make sure {b}[sis]{/b} doesn't see you leave the bathroom, okay?"
    $ gTimer.tick()
    hide screen xray_scr
    $ playSound()
    jump hallway_dialogue

label sis_shower:
    scene shower3 with None
    player_name "( {b}[sis]{/b} is in the shower... )"
    player_name "( ... and she hasn't noticed me yet? )"
    player_name "( Maybe I could... )"
    menu:
        "Peep." if sister.known(sis_shower_cuddle01):
            if sister.over(sis_shower_cuddle01):
                scene shower05a
                player_name "( ...She left her door open again... )"
                scene shower05b
                player_name "( ...It's like she wanted me to watch? )"
                scene shower05c
                player_name "( She really has a great body. )"
                scene shower05b
                scene shower05a
                player_name "..."
                show shower 05d_05e
                player_name "( ...Is she- )"
                player_name "( Wow... )"
                player_name "( ...I should... )"
                player_name "( ...leave, before she notices... )"
                hide shower 05d_05e
                hide shower05a
                jump hallway_dialogue
            else:

                scene shower3
                player_name "Oh shit! {b}[sis]{/b} is in the shower..."
                scene shower4 with hpunch
                player_name "( CRAP!! She saw me! )"
                scene shower2
                show sis 3 at right
                show player 6 at left
                with dissolve
                sis "What's wrong with you??!"
                sis "Can't you see I'm in here?"
                show sis 2 at Position(xpos=962) with fastdissolve
                player_name "The door was unlocked!"
                show player 3 with fastdissolve
                sis "Knock first next time, you pervert!"
                show player 29
                player_name "Sorry! I thought no one was in here..."
                hide sis
                hide player
                with dissolve
                hide shower2
                $ sis_shower_count = 1
                $ sis_shower_cuddle01.finish()
                jump hallway_dialogue

        "Go inside." if sister.known(sis_shower_cuddle02):
            $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
            scene shower2b
            show player 11 at Position(xpos=261)
            with fade
            player_name "( I can't believe I'm about to do this... )"
            show player 4 at Position(xpos=267)
            player_name "( Will she scream at me this time, or will she let me stay? )"
            player_name "( She left the door open like she's inviting me... )"
            show player 13 at Position(xpos=261)
            player_name "( I know... )"
            show player 249 at left with fastdissolve
            player_name "( I can just pretend like I didn't see her! )"
            show player 261f at Position(xpos=137) with fastdissolve
            player_name "( Alright, I'm going in... )"
            jump sis_shower_sex_intro
        "Leave.":

            player_name "No, too risky..."
            jump hallway_dialogue

label sis_shower_sex_intro:
    $ gTimer.tick()
    if not sis_shower_intro_first:
        scene shower_closeup
        show player 342 at Position(xpos=160)
        show sis 163 at Position(xpos=791)
        with fade
        pause
        show sis 163b with fastdissolve
        pause  
        show sis 106 with fastdissolve
        sis "Well well..."
        sis "I was wondering when you'd follow me in here."
        show sis 105
        menu:
            "Oops, Sorry!":
                show sis 105
                show player 343
                player_name "Oops!"
                player_name "Sorry! I didn't see you..."
                show sis 106
                show player 342
                sis "Didn't I tell you to knock first?! You idiot!"
                show player 343
                show sis 105
                player_name "I know but-"
                show sis 104
                show player 342
                sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                hide sis
                hide player
                with dissolve
                $ playSound()
                jump hallway_dialogue
            "Need help?":

                show sis 105
                show player 343
                player_name "I thought, maybe you needed help again..."
                show sis 107
                show player 342
                sis "Help? Ha!!"
                show sis 106
                sis "More like me helping myself, while my perverted {b}little brother{/b} watches..."
                sis "You really can't stop spying on me, can you?"
                show sis 105
                player_name "..."
                jump sis_shower_sex
    else:

        $ sis_shower_intro_first = False
        $ sis_shower_cuddle02.finish()
        $ sister.add_event(sis_hallway01)
        scene shower_closeup
        show player 342 at Position(xpos=160)
        show sis 163 at Position(xpos=791)
        with fade
        pause
        show sis 163b with fastdissolve
        sis "Huh?"
        show sis 104
        sis "{b}[firstname]{/b}?!" with hpunch
        sis "What the fuck?!"
        sis "Can't you see I'm in here?!!"
        show sis 105
        menu:
            "Oops, Sorry!":
                show sis 105
                show player 343
                player_name "Oops!"
                player_name "Sorry! I didn't see you..."
                show sis 106
                show player 342
                sis "Didn't I tell you to knock first?! You idiot!"
                show player 343
                show sis 105
                player_name "I know but-"
                show sis 104
                show player 342
                sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                hide sis
                hide player
                with dissolve
                $ playSound()
                jump hallway_dialogue
            "Need help?":

                show sis 105
                show player 343
                player_name "I know..."
                player_name "I was wondering if... you know... you need help?"
                show sis 104
                show player 342
                sis "Help??"
                show sis 106
                sis "Oh! Haha!"
                show sis 105
                show player 343
                player_name "What's so funny?"
                show player 342
                show sis 106
                sis "Gosh... you're so {b}pathetic{/b}."
                sis "I know you just want to see me naked!"
                show sis 105
                player_name "..."
                jump sis_shower_sex

label sis_shower_sex:
    show sis 107
    show player 342
    sis "Okay, I'll let you stay..."
    show sis 106
    sis "... but, you'll only help by {b}looking{/b} with your {b}eyes{/b}."
    show sis 104
    sis "Got it?!"
    show sis 105
    show player 343
    player_name "Yes, {b}[sis]{/b}..."
    show player 342
    show sis 109 at right
    sis "Good."
    sis "Now..."
    show sis 110 with fastdissolve
    sis "I like my breasts nice and soapy..."
    show sis 111
    sis "So, I like to use loooots of soap!"
    show sis 112 with fastdissolve
    pause
    show sis 113 with fastdissolve
    pause
    show sis 115 with fastdissolve
    sis "Do you like seeing all this... {b}cream{/b} on me?"
    sis "Does it make you think of something {b}else{/b}?"
    show sis 114
    show player 343
    player_name "I... I don't know..."
    show player 342
    sis "Hmm..."
    show sis 115
    show player 344
    sis "Let's lather them up a little!"
    show sis 116 at Position(xpos=984) with fastdissolve
    pause
    show sis 117_118_119_116 at Position(xpos=980)
    pause 8
    show player 345 at left
    show sis 122 at Position(xpos=980)
    player_name "Uh oh..."
    show sis 120b
    show player 346 with fastdissolve
    pause 0.05
    show player 347 with vpunch
    pause
    show sis 120
    sis "Well... that was easy!"
    show player 348 at Position(xpos=60)
    show sis 109 at Position(xpos=1024)
    sis "Since you seem to be enjoying this, maybe we can wash {b}another{/b} part of my body..."
    show sis 108
    show player 349
    player_name "Okay..."
    show sis 109
    show player 348
    sis "First, I want to hear you {b}beg{/b} for it."
    show sis 167
    show player 349
    player_name "What do you mean?"
    show sis 166
    show player 348
    sis "Which part of that didn't you understand?"
    show sis 164
    sis "... I'm not doing it, unless you {b}beg{/b} for it!"
    show sis 167
    show player 349
    player_name "Beg... for what exactly?"
    show sis 109
    show player 348
    sis "I want you to {b}beg{/b} to see my pussy."
    show sis 108
    menu:
        "Leave.":
            show player 349
            show sis 167
            player_name "I think I'll just leave..."
            show player 348
            sis "???"
            show sis 166
            sis "You wont do it?"
            show player 349
            show sis 165
            player_name "No, sorry."
            show player 354
            show sis 164
            sis "You think you're {b}too good{/b} for this?!"
            show player 349
            show sis 165
            player_name "It's not like-"
            show player 354
            show sis 164
            sis "Shut up and {b}GET OUT{/b}!!" with hpunch
            hide sis
            hide player
            with dissolve
            $ playSound()
            jump hallway_dialogue

        "Beg." if not sister.known(sis_shower_cuddle03):
            show player 349
            show sis 108
            player_name "Can... you show me your pussy?"
            show player 348
            show sis 109
            sis "I didn't hear a {b}please{/b}."
            show player 349
            show sis 167
            player_name "Can you please show me your pussy, {b}[sis]{/b}?"
            show player 348
            show sis 166
            sis "You know what..."
            sis "I don't think you deserve this, even if you begged for it."
            sis "You're too pathetic, anyway."
            show player 349
            show sis 167
            player_name "But, I thought you needed help-"
            show player 348
            show sis 166
            sis "Maybe later... if you treat your {b}older sister{/b} a little better..."
            show sis 164
            show player 354
            sis "Now, {b}GET OUT{/b}!!" with hpunch
            hide sis
            hide player
            with dissolve
            $ playSound()
            jump hallway_dialogue

        "Beg." if sister.known(sis_shower_cuddle03):
            if not sister.known(sis_couch03):
                $ sister.add_event(sis_couch03)
            $ sis_shower_cuddle03.finish()
            show player 349
            show sis 108
            player_name "Can... you show me your pussy?"
            show sis 109
            show player 348
            sis "I didn't hear a {b}please{/b}."
            show sis 108
            show player 349
            player_name "Can you please show me your pussy, {b}[sis]{/b}?"
            show player 348
            show sis 109
            sis "Alright..."
            show sis 127
            show player 344b
            with fastdissolve
            sis "Let's wash this part of my body... right here..."
            show sis 124_125_126_123
            pause 8
            sis "Hmm..."
            show sis 127
            sis "You know what?"
            sis "I can't reach back there so... I might need some help after all..."
            show player 349 at Position(xpos=60)
            show sis 123
            player_name "...My help?"
            show player 348
            show sis 109 at Position(xpos=1024) with fastdissolve
            sis "Not exactly..."
            sis "First, put some soap on it."
            show sis 167
            show player 349
            player_name "On it?"
            show player 348
            show sis 166
            sis "On your {b}dick{/b}, you idiot!"
            show sis 111 with fastdissolve
            sis "Here, take it!"
            show sis 108
            show player 356
            with fastdissolve
            pause
            show player 350 with fastdissolve
            pause
            show player 348 with fastdissolve
            show sis 109
            sis "Now, you know what to do..."
            show sis 108
            show player 349
            player_name "I don't know..."
            show sis 109
            show player 348
            sis "I want to hear you {b}beg{/b} for it, but for {b}REAL{/b} this time..."
            show sis 108
            menu:
                "Leave.":
                    show player 349
                    show sis 167
                    player_name "I think I'll just leave..."
                    show player 348
                    sis "???"
                    show sis 166
                    sis "You wont do it?"
                    show player 349
                    show sis 165
                    player_name "No, sorry."
                    show player 354
                    show sis 164
                    sis "You think you're {b}too good{/b} for this?!"
                    show player 349
                    show sis 165
                    player_name "It's not like-"
                    show player 354
                    show sis 164
                    sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                    hide sis
                    hide player
                    with dissolve
                    $ playSound()
                    jump hallway_dialogue

                "Beg." if not sister.known(sis_shower_cuddle04):
                    show player 349
                    show sis 167
                    player_name "Can I... please help you, {b}[sis]{/b}?"
                    show sis 164
                    show player 354
                    sis "WRONG!!" with hpunch
                    show sis 109
                    show player 348
                    sis "I want you to call me {b}princess{/b}..."
                    show sis 167
                    show player 349
                    player_name "Can I please help you, {b}princess{/b}?"
                    show player 348
                    show sis 166
                    sis "You know what..."
                    sis "I don't think you deserve this, even if you begged for it."
                    sis "You're too pathetic anyway."
                    show player 349
                    show sis 167
                    player_name "But, I thought you needed help-"
                    show player 348
                    show sis 166
                    sis "Maybe later... if you treat your {b}older sister{/b} a little better..."
                    show sis 164
                    show player 354
                    sis "Now, {b}GET OUT{/b}!!" with hpunch
                    hide sis
                    hide player
                    with dissolve
                    $ playSound()
                    jump hallway_dialogue

                "Beg." if sister.known(sis_shower_cuddle04):
                    if not sister.known(sis_final):
                        $ sister.add_event(sis_final)
                    $ sis_shower_cuddle04.finish()
                    show sis 167
                    show player 349
                    player_name "Can I... please help you, {b}[sis]{/b}?"
                    show player 354
                    show sis 164
                    sis "WRONG!!" with hpunch
                    show sis 109
                    show player 348
                    sis "I want you to call me {b}princess{/b}..."
                    show sis 108
                    show player 349
                    player_name "Can I please help you, {b}princess{/b}?"
                    show player 354
                    show sis 164
                    sis "LOUDER!!" with hpunch
                    show player 355
                    show sis 108
                    player_name "Can..."
                    player_name "{b}CAN I PLEASE HELP YOU, PRINCESS{/b}?!!" with hpunch
                    show player 348
                    show sis 109
                    sis "MUCH better!"
                    sis "Sure."
                    sis "I'll let you help me..."
                    show sis 166
                    sis "... but, {b}NO TOUCHING{/b} with your hands!!"
                    hide player
                    hide sis
                    show sissex 96
                    with fastdissolve
                    sis "Understood?!"
                    show sissex 95 at Position(xpos=511)
                    player_name "Yes, {b}[sis]{/b}..."
                    show sissex 92_93_94_95 at Position(xpos=511)
                    pause 8
                    show sissex 96 at Position(xpos=512)
                    sis "You like that, you little pervert?"
                    show sissex 93 at Position(xpos=534)
                    pause
                    show sissex 94 at Position(xpos=513)
                    pause
                    show sissex 95 at Position(xpos=511)
                    menu:
                        "Put it inside." if not sister.known(sis_shower_cuddle05) or pStats.dex() < 7:
                            hide sissex
                            show sis 129 zorder 1 at Position(xpos=443)
                            show player 351 zorder 2 at Position(xpos=260)
                            sis "[dex_warn]Not so fast, pervert!!" with hpunch
                            sis "[dex_warn]Just what are you trying to do here?!"
                            show sis 128
                            player_name "!!!"
                            show sis 130
                            sis "Didn't I tell you {b}NO HANDS{/b}??"
                            show player 351b
                            show sis 131
                            player_name "Sorry... I couldn't resist..."
                            show sis 132
                            show player 351
                            sis "You're lucky I let you go this far!"
                            show sis 131
                            show player 351b
                            player_name "I..."
                            player_name "I'm sorry!!"
                            show sis 130
                            show player 351
                            sis "Shut up and {b}GET OUT{/b}!!" with hpunch
                            hide sis
                            hide player
                            with dissolve
                            $ playSound()
                            jump hallway_dialogue

                        "Put it inside." if sister.known(sis_shower_cuddle05) and pStats.dex() >= 7:
                            $ sis_shower_cuddle05.finish()
                            $ anim_toggle = False
                            $ xray = False
                            show sissex 98
                            sis "Ahh!!!" with hpunch
                            show sissex 97
                            sis "What are you DOING?!!"
                            show sissex 101 at Position(xpos=476)
                            player_name "I want you, {b}Sis{/b}!!!"
                            label sis_shower_sex_loop:
                                show sissex 101 at Position(xpos=476)
                                show screen shower_sex_buttons
                                pause
                                if anim_toggle == True:
                                    hide sissex 101
                                    hide screen shower_sex_buttons
                                    show sissex 98_99_100_101 at Position(xpos = 511)
                                    pause 8
                                    hide sissex 98_99_100_101
                                else:
                                    $ animcounter = 0
                                    while animcounter < 3:
                                        hide screen shower_sex_buttons
                                        show sissex 98 at Position(xpos = 511)
                                        pause
                                        show sissex 99 at Position(xpos = 518)
                                        pause
                                        show sissex 100 at Position(xpos = 497)
                                        pause
                                        show sissex 101 at Position(xpos = 476)
                                        pause
                                        $ animcounter += 1
                                show sissex 98 at Position(xpos=511)
                                pause
                                show sissex 99 at Position(xpos=518)
                                pause
                                show sissex 100 at Position(xpos=497)
                                pause                                
                                show sissex 101 at Position(xpos=476)
                                sis "Don't you dare cum inside me..."
                                show sissex 97 at Position(xpos=511)
                                sis "... I swear, I'll {b}KILL YOU{/b}!!"
                                menu:
                                    "Keep going.":
                                        jump sis_shower_sex_loop

                                    "Cum inside." if pStats.str() < 7:
                                        show sissex 101 at Position(xpos=476)
                                        pause
                                        show sissex 98 at Position(xpos=511)
                                        pause
                                        show sissex 99 at Position(xpos=518)
                                        pause
                                        show sissex 100 at Position(xpos=497)
                                        pause                                
                                        show sissex 101 at Position(xpos=476)
                                        pause                                       
                                        hide sissex
                                        $ xray = False
                                        show sis 130 zorder 1 at Position(xpos=443)
                                        show player 351 zorder 2 at Position(xpos=260)
                                        sis "[str_warn]What the {b}FUCK{/b}??" with hpunch
                                        sis "[str_warn]Were you about to cum {b}INSIDE{/b} me!?"
                                        show sis 131
                                        show player 351b
                                        player_name "No..."
                                        show sis 130
                                        show player 351
                                        sis "What's wrong with you?!"
                                        sis "You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!"
                                        show sis 131
                                        show player 351b
                                        player_name "I..."
                                        player_name "I'm sorry!!"
                                        show sis 130
                                        show player 351
                                        sis "Yeah right! We're done here! {b}GET OUT{/b}!!" with hpunch
                                        hide sis
                                        hide player
                                        with dissolve
                                        $ playSound()
                                        jump hallway_dialogue

                                    "Cum inside." if pStats.str() >= 7:
                                        show sissex 101 at Position(xpos=476)
                                        pause
                                        show sissex 98 at Position(xpos=511)
                                        pause
                                        show sissex 99 at Position(xpos=518)
                                        pause
                                        show sissex 100 at Position(xpos=497)
                                        pause                                
                                        show sissex 101 at Position(xpos=476)
                                        pause                                             
                                        show white
                                        show sissex 102 at Position(xpos=516)
                                        sis "{b}Aahhh!!!!{/b}" with hpunch
                                        hide white with dissolve
                                        pause
                                        show sissex 103 at Position(xpos=511) with fastdissolve
                                        pause
                                        show sissex 102_103 at Position(xpos = 516)
                                        pause 2.5
                                        show sissex 103 at Position(xpos=511)
                                        $ xray = False
                                        sis "{b}*Panting*{/b}"
                                        sis "Oh god..."
                                        hide sissex
                                        show sis 134 zorder 1 at Position(xpos=600)
                                        show player 353 zorder 2 at Position(xpos=260)
                                        with dissolve
                                        sis "What the FUCK?!"
                                        sis "I felt that!!!"
                                        show player 352
                                        sis "You just kept shooting cum deep inside!!"
                                        show sis 133
                                        show player 349 at Position(xpos=254)
                                        player_name "It was a reflex!"
                                        player_name "I... I couldn't stop..."
                                        show sis 134
                                        show player 348
                                        sis "Don't you get it, you idiot?!"
                                        sis "If you keep cumming inside me like that every time, I could get {b}PREGNANT{/b}!!"
                                        show sis 133
                                        show player 349
                                        player_name "I..."
                                        player_name "I'm sorry!!"
                                        show sis 134
                                        show player 353 at Position(xpos=260)
                                        sis "Sh-Shut up and {b}GET OUT{/b}!!" with hpunch
                                        hide sis
                                        hide player
                                        with dissolve
                                        $ playSound()
                                        jump hallway_dialogue