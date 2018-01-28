label garden_dialogue:
    default aunt_count = 0
    default in_garden = False
    default shed_dialogue = 0
    default aunt_dialogue_advance = False
    default after_minigame = False
    default drunk_dialogue = False
    default shed_unlocked = False
    default aunt_shed_scene = False
    default drank_milk = False
    default drink_milk_offer = False
    default pump_quest_active = False
    default aunt_drink_active = False
    default aunt_drink_made = False
    default aunt_extra_shot = False
    default aunt_drink_offered = False
    default garden_firsttime = False
    default infestation_done = False
    default aunt_masturbating_seen = False
    default seen_shed_locked = False
    default xray_toggle = False
    default xray = 0
    default aunt_had_sex = False
    default condom_on = True
    default shed_sex_angle = 0
    default shed_cow_outfit = True
    default cow_outfit = 0
    default shed_xray_toggle = False
    default shed_cum = False
    default shed_had_sex = False
    default shed_sex_count = 0
    default aunt_apology_seen = False
    default milking_unlocked = False
    default garden_done = 0
    default shed_sex_action = 0

    $ location_count = "Diane's Garden"
    $ tick_skip_active = True
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if not gTimer.is_dark():
        if aunt_shed_scene and not aunt.known(aunt_drunken_splur):
            scene location_garden_close_blur with None
            show player 11 at left
            show aunt 99 at right
            with dissolve
            dia "Yoo-hooo! Theeere's my handsome nephew!"
            show player 5
            dia "How are you-hic doing today?"
            dia "Come to till my garden with your shovel?"
            show aunt 95
            show player 12
            player_name "{b}Aunt Diane{/b}? Are you okay?"
            show player 11
            show aunt 162 at Position (xpos = 973)
            dia "Who, Me?"
            dia "I'm-{b}*hic*{/b}- fine."
            show aunt 161
            pause
            show aunt 162
            dia "It's a bit hot outside, so I had to make myself something to cool off..."
            show aunt 161
            show player 22
            pause
            show player 10
            player_name "{b}Aunt Diane{/b}, your clothes... they um... slipped."
            show player 11
            show aunt 162
            dia "Huh? What are you..."
            show aunt 163
            dia "Oh!!"
            show aunt 164
            dia "Hahaha!"
            show player 21
            show aunt 165
            player_name "Heh..."
            show player 13
            show aunt 166
            dia "That's what happens when you start drinking before you get dressed, my sweet nephew."
            dia "It doesn't help having these... massive udders flopping around!!"
            show aunt 164
            dia "Haha!"
            show aunt 165
            pause
            show player 11
            show aunt 163
            dia "Oops! It's still poking out!"
            show aunt 164
            dia "Haha!"
            show player 1
            show aunt 94 at right with fastdissolve
            dia "There."
            show aunt 99
            dia "Have I ever told you you're my favorite nephew?"
            show player 14
            show aunt 98
            player_name "Uh... a few times?"
            show player 11
            show aunt 97
            dia "I mean, your sister is such a... bitch, you know?"
            show aunt 99
            show player 13
            dia "But I like you a lot more..."
            show aunt 98
            show player 11
            pause
            show aunt 94
            dia "I wish I had young looking breasts like your sister though..."
            show aunt 95
            pause
            show aunt 99
            dia "What?"
            dia "You don't think she's got a nice pair?"
            show aunt 98
            show player 24
            player_name "I... Uh..."
            show aunt 96
            show player 11
            dia "You're telling me you haven't noticed them?"
            show aunt 98
            show player 10
            player_name "Well... I don't know."
            show aunt 99
            show player 11
            dia "Here."
            show player 22
            show aunt 167 at Position (xpos = 973) with fastdissolve
            pause
            show aunt 169
            show player 11
            dia "I mean, don't you think they look better than your {b}auntie's{/b} old boobs?"
            show aunt 167
            show player 21
            player_name "No.. Yours look really good."
            show aunt 168
            show player 13
            dia "Awww!"
            dia "You're so sweet..."
            dia "And that's why you're my favorite nephew!"
            show aunt 167
            pause
            show aunt 166 with fastdissolve
            show player 11
            dia "I..."
            dia "I'm... so sorry."
            dia "I really shouldn't be talking like this in front of you."
            show player 21
            show aunt 165
            player_name "It's alright..."
            show player 5
            show aunt 166
            dia "You must think your {b}aunt{/b} is just an easy lush."
            show aunt 165
            show player 21
            player_name "No, I don't. It's fun seeing you this way... I mean you're even funnier when you're tipsy."
            show player 13
            show aunt 166
            dia "You're cute, sweetheart, but I think I'm going to lay down for a bit."
            show aunt 97 at right with fastdissolve
            dia "I think I've had a little too much to drink..."
            hide aunt with dissolve
            pause
            show player 35
            player_name "Man, I can't remember the last time I've seen her that drunk before."
            player_name "I should probably make sure she made it to her bed."
            hide player with dissolve
            $ ui_lock_count = 1
            $ aunt.add_event(aunt_drunken_splur)

        elif quest09_3 and not aunt.known(aunt_mouse_attack):
            scene garden with None
            show player 1f with dissolve
            pause
            show player 32f at Position(xoffset=-69)
            player_name "Huh. Where's {b}Aunt Diane{/b}?"
            player_name "She's usually out here working on her garden..."
            show player 31 at Position(xoffset=68)
            pause
            show player 30
            player_name "It doesn't look like she's in her shed either."
            show player 12
            player_name "She must be inside. It's really hot outside today."
            show player 5
            player_name "..."
            show player 10
            player_name "Maybe I should check up on her before I start working."
            hide player with dissolve
            $ ui_lock_count = 1
            $ aunt.add_event(aunt_mouse_attack)

        elif aunt_count == 0 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            if quest20 not in quest_list:
                scene garden
                show player 1 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Look at that handsome young man..."
                show aunt 3 at right
                show player 13 at left
                dia "You've grown so much, I can hardly recognize you!"
                show aunt 1 at right
                show player 17 at left
                player_name "Hi, {b}Aunt Diane{/b}!"
                show aunt 7 at right
                show player 2 at left
                player_name "Wow! You look so much like {b}Mom{/b}..."
                show aunt 6 at right
                show player 1 at left
                dia "Oh, she was always the prettier {b}twin{/b}..."
                show aunt 7 at right
                show player 33 at left
                player_name "Well, I think you look great, {b}Aunt Diane{/b}!"
                show aunt 12 at right
                show player 1 at left
                dia "Well, you sure know how to talk to the ladies..."
                show aunt 13 at right
                show player 11 at left
                dia "..."
                show aunt 5 at right
                dia "Anyway, let's talk about my garden!"
                show aunt 2 at right
                show player 1 at left
                dia "I'm guessing, your mom told you I was looking to pay a strong, young man to help me take care of my garden?"
                show aunt 1 at right
                show player 2 at left
                player_name "Yeah, I could use the money for College, starting in the fall, and I don't have any other jobs yet, so..."
                show aunt 2 at right
                show player 5 at left
                dia "Well, I was hoping you could start today but I have some bad news."
                show aunt 139 with dissolve
                dia "My old shovel finally gave up on me today."
                show aunt 141
                show player 10
                player_name "Oh! Yeah... That looks pretty bad."
                show aunt 140
                show player 1
                dia "We may have to wait until I replace it..."
                dia "I'm sorry, {b}[firstname]{/b}."
                show aunt 141
                show player 2
                player_name "It's okay, Aunt Diane."

                $ quest_list.append(quest20)
                if shovel not in inventory.items:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "Is there any way we can continue the work without it?"
                    show aunt 2
                    show player 1
                    dia "We really need to dig up the garden so... I'm afraid not."
                    show aunt 8
                    show player 11
                    dia "Unless..."
                    show player 10
                    show aunt 1
                    player_name "Unless?"
                    show player 11
                    show aunt 2
                    dia "...You wouldn't happen to have one at home?"
                    show player 4
                    show aunt 1
                    player_name "Hmm..."
                    show player 2
                    player_name "We might have a {b}shovel{/b} in our garage!"
                    player_name "I'll go check, and come back if I find something."
                    show player 203
                    show aunt 3
                    dia "That's wonderful!"
                    show aunt 2
                    dia "Thank you so much for trying to help! Come back if you find some tools!"
                else:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "I think I actually have something in my backpack..."
                    label have_shovel:
                        show player 239_240
                        player_name "Hmm..."
                        show player 241
                        $ renpy.pause()
                        show player 242
                        $ renpy.pause()
                        show player 243
                        $ renpy.pause()
                        show player 244
                        player_name "Here it is!"
                        show player 243
                        show aunt 3
                        dia "Ohh! Wonderful!"
                        show aunt 2
                        dia "I knew I you'd be able to get one!"
                        dia "Alright! But before you start, I have to tell you what to do..."
                        show aunt 14 at right
                        show player 11 at left with dissolve
                        dia "Make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
                        show aunt 14 at right
                        show player 11 at left
                        dia "Take out everything else... Especially those pesky rats and bugs! ...Got it?"
                        show aunt 1 at right
                        show player 14 at left
                        player_name "Got it!!"
                        show aunt 2 at right
                        show player 1 at left
                        dia "Oh! ...And remember to place all your earned money in the {b}Bank{/b}, when you're done!"
                        show aunt 1 at right
                        show player 4 at left
                        player_name "Umm... sure. I guess I could do that..."
                        show aunt 3 at right
                        show player 1 at left
                        dia "Thanks for the help, Handsome!"
                        hide aunt 3 at right
                        hide player 1 at left
                        show aunt 11 at left
                        player_name "..."
                        hide aunt 11 at left with dissolve
                        show unlock6 at truecenter
                        $ renpy.pause()
                        hide unlock6 with dissolve
                        $ loc_bank_unlocked = True
                        show expression "boxes/popup_garden.png" at truecenter with dissolve
                        $ renpy.pause()
                        hide expression "boxes/popup_garden.png" with dissolve
                        $ aunt_dialogue_advance = True
                        $ map_status_count = 3
                        $ completed_quests.append(quest20)
                        $ callScreen(location_count)

        elif aunt_count == 1 and quest21 not in completed_quests and garden_done >= 3:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            scene location_garden_blur
            if quest21 in quest_list:
                show player 203 at left
                show aunt 2 at right
                dia "There you are!!"
                dia "I was hoping you'd show up."
                show player 14
                show aunt 1
                player_name "Hi, Aunt Diane."
                show player 203
                show aunt 8
                dia "You think you can help your old Aunt with the wheelbarrow this time?"
                show player 14
                player_name "It's no problem, Aunt Diane!"
                player_name "Let me give it another try!"
                show player 251 with dissolve
                player_name "Hmm..."
                show player 252
                player_name "This shouldn't be too hard."
            else:

                show player 203 at left with dissolve
                show aunt 2 at right with dissolve
                dia "There you are!!"
                dia "I was hoping you would show up today."
                show player 2
                show aunt 1
                player_name "Hi, Aunt Diane!"
                player_name "Is there something wrong?"
                show aunt 2
                show player 203
                dia "Everything's great! You've been doing such a great job, so far..."
                dia "In fact, you're doing so well, that we have a ton of leftover waste!"
                show aunt 1
                show player 17
                player_name "Sorry about that. Haha."
                show aunt 2
                show player 203
                dia "I've been trying to get rid of it all with the {b}wheelbarrow{/b}..."
                dia "But it's too heavy, and your poor old Aunt's back hurts!"
                dia "You think you could help her?"
                show player 14
                show aunt 1
                player_name "Of course!"
                player_name "That's why I'm here!"
                show player 10
                player_name "But... Where do you want me to dump it all?"
                show player 203
                show aunt 2
                dia "I was thinking behind the house, right by the edge of the woods."
                dia "There's a small ditch where I usually put all the garden waste..."
                dia "It's a bit far, but I'm sure you'll manage!"
                show player 2
                show aunt 1
                player_name "It's no problem, Aunt Diane!"
                player_name "I'll take care of it!"
                show player 251 with dissolve
                player_name "Hmm..."
                show player 252
                player_name "This shouldn't be too hard."
                $ quest_list.append(quest21)

            if pStats.str() >= 2:
                show player 255 at left
                show aunt 1 at right
                player_name "There we go."
                player_name "It's not so bad, after all!"
                show player 254
                show aunt 5
                dia "!!!" with hpunch
                dia "Wow... You lifted it like it was nothing!"
                show player 255
                player_name "Well, I've been training at the gym lately..."
                show player 254
                show aunt 2
                dia "Ohh! Someone's becoming nice and strong, I see!"
                show player 255
                show aunt 1
                player_name "Haha. I guess so."
                show player 254
                show aunt 8
                dia "Flex those muscles, and follow me behind the yard... Handsome..."

                hide location_garden_blur
                hide player
                hide aunt
                scene location_garden_cutscene04
                show text "The ditch behind her house was so far!\n I barely made it; the wheelbarrow kept slipping out of my hands. \n I was just happy showing Aunt Diane that I was strong enough to do it..." at Position (xpos= 512, ypos = 700)
                with fade
                $ renpy.pause()
                hide text
                hide location_garden_cutscene04
                scene location_garden_blur
                show aunt 5 at right
                show player 18 at left
                with dissolve
                dia "I can't believe you did it with such ease!"
                show player 17
                show aunt 1
                player_name "It was pretty hard, actually. Haha!"
                show player 203
                show aunt 2
                dia "Well, I just hope you don't hate me for it..."
                show player 2
                show aunt 1
                player_name "It's fine."
                player_name "It had to be done, and I didn't mind the exercise!"

                show player 203
                show aunt 8
                dia "Tell me..."
                dia "...how do you stay in shape like this?"
                show aunt 9
                show player 11
                player_name "..."
                show player 21
                player_name "What do you mean?"
                show aunt 3
                show player 13
                dia "Staying nice and fit like that!"
                show aunt 6
                show player 11
                dia "I try to stay active all the time... But I always feel fat."
                show aunt 1
                show player 10
                player_name "Fat?"
                show aunt 7
                show player 29
                player_name "I think you look fine, {b}Aunt Diane{/b}."
                show aunt 12
                show player 13
                dia "You say that now, but if you saw me without clothes on..."
                show aunt 13
                show player 11
                player_name "..."
                show aunt 5
                dia "Err... Anyway!"
                show aunt 8
                dia "So what's your trick?"
                dia "Have you been working out?"
                show aunt 9
                show player 21
                player_name "A little."
                show player 35
                player_name "I try going to the gym sometimes."
                show aunt 2
                show player 13
                dia "Really?!"
                dia "That's great!"
                show aunt 14
                dia "You know, there are many good advantages to staying in shape."
                show aunt 8
                show player 11
                dia "Women love guys who are strong, flexible and have great... Stamina."
                show aunt 9
                player_name "..."
                show aunt 10
                dia "Let me see your abs!"
                show aunt 9
                show player 22
                player_name "!!!" with hpunch
                show player 21
                player_name "You want to see my..."
                show aunt 10
                show player 11
                dia "Your muscles! Yes."
                dia "Let's see them!"
                show aunt 9
                show player 10
                player_name "Okay..."
                show aunt 7
                show player 249
                show aunt 12
                dia "Wow!!"
                show aunt 10
                dia "Sexy body!"
                show aunt 8
                dia "You must be popular with the girls at school..."
                show aunt 9
                show player 250
                player_name "Not really."

                show aunt 7
                show player 108f
                player_name "There are guys much bigger than me at school."
                player_name "I'm definitely not one of the cool guys..."
                show player 109f
                show aunt 8
                dia "That's okay, you know."
                show aunt 6
                show player 13
                dia "Girls don't always want the cool guys."
                show aunt 5
                dia "And just give it some time!"
                show aunt 4
                show player 17
                player_name "Thanks, {b}Aunt Diane{/b}."
                show aunt 2
                show player 203
                dia "Thank you so much for helping me with this wheelbarrow!"
                dia "Now, we can get back to work on the garden!"
                show player 2
                show aunt 1
                player_name "Sure! Let me get the tools and get started..."
                $ completed_quests.append(quest21)
                $ aunt_dialogue_advance = True
            else:

                show player 253 at left with dissolve
                $ renpy.pause()
                show player 256 at Position(xpos=0.0322,ypos=1.0000) with dissolve
                show aunt 1 at right
                player_name "[str_warn]Ughhh!!..."
                player_name "[str_warn]...Ghhh..."
                show player 27 with dissolve
                player_name "[str_warn]I... I can't do it, {b}Aunt Diane{/b}..."
                player_name "[str_warn]I'm sorry..."
                show player 3
                show aunt 2
                dia "Oh..."
                dia "It's... okay. I didn't realize it was so full..."
                dia "But don't worry, I can probably find someone else who could do it for me."
                show player 23
                player_name "Wait... I can do it!"
                show player 256 with dissolve
                dia "..."
                show player 10 with dissolve
                player_name "I must be tired today, that's all..."
                player_name "Let me rest and get some {b}strength{/b}. I'll come back and do it, I promise."
                show aunt 1
                show player 3
                dia "..."
                show aunt 3
                show player 5
                dia "You're so persistent!"
                show aunt 2
                show player
                dia "Alright, then. I'll see you again soon!"
                show player 2
                show aunt 1
                player_name "Thanks, Aunt Diane!"
                hide player with dissolve
                hide aunt with dissolve

        elif aunt_count == 2 and quest08 not in quest_list:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 1 at left with dissolve
            show aunt 2 at right with dissolve
            dia "Hey there!"
            show player 14 at left
            show aunt 1 at right
            player_name "Hi {b}Aunt Diane{/b}!"
            show aunt 3 at right
            show player 1 at left
            dia "Ready for some vegetable landscaping?"
            show aunt 4 at right
            show player 17 at left
            player_name "Yup!"
            show aunt 14 at right
            show player 1 at left
            dia "Oh! Before you get started..."
            show aunt 2 at right
            dia "Could you do me a favor and get me my {b}pump{/b} from the {b}shed{/b}?"
            show aunt 1 at right
            show player 12 at left
            player_name "A {b}pump{/b}?"
            show aunt 2 at right
            show player 1 at left
            dia "Yeah! It should be on the shelf somewhere..."
            show aunt 1 at right
            show player 14 at left
            player_name "Uhh.. Okay, I'll look for it."
            show aunt 3 at right
            show player 1 at left
            dia "Thanks, {b}handsome{/b}!"
            $ shed_unlocked = True
            $ quest_list.append(quest08)
            hide player 1 at left with dissolve
            hide aunt 3 at right with dissolve

        elif aunt_count == 3 and not aunt_dialogue_advance and quest09 not in quest_list:
            if not gTimer.is_weekend():
                if in_garden:
                    $ in_garden = False
                    $ callScreen(location_count)
                scene garden
                show player 106 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Oh, {b}[firstname]{/b}!"
                show player 23
                dia "I'm so glad you're here..."
                show player 24
                player_name "You need me for something?"
                show player 3
                dia "Yes!!"
                dia "I'm running late, and I need a huge favor."
                show player 1
                player_name "Sure, {b}Aunt Diane{/b}! Anything you need!"
                show player 2
                dia "Great!"
                dia "I just need you to make a {b}small delivery{/b} for me."
                show player 3
                dia "The {b}package{/b} has to be dropped off at the {b}school{/b}, today!"
                show player 1
                player_name "Wait. You need something dropped off... At {b}my{/b} school?"
                show player 3
                dia "Yeah! It's {b}fresh milk{/b}!"
                show aunt 1
                player_name "..."
                player_name "You... make milk?"
                show aunt 6
                dia "I know..."
                dia "I started not too long ago."
                show aunt 108
                dia "Anyway, I don't have time to explain. Here's the {b}receipt{/b}."
                show aunt 1
                player_name "But, {b}Aunt Diane{/b}, where's the package? And where do I drop it off?"
                show aunt 22
                dia "Right! I'm sorry..."
                show aunt 23
                dia "The package is in the {b}shed{/b}. Just drop it off at the {b}cafeteria{/b}."
                show aunt 24
                player_name "Okay, I can do that."
                show aunt 2
                dia "Thank you so much, {b}[firstname]{/b}."
                show aunt 14
                dia "Oh! And don't take too long! We don't want the milk to go bad!."
                $ quest_list.append(quest09)
                $ ui_lock_count = 1
            else:

                scene garden
                show player 106 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Oh, {b}[firstname]{/b}!"
                show player 23
                dia "I'm so glad you're here..."
                show player 24
                player_name "You need me for something?"
                show player 3
                dia "Yes!!"
                dia "I'm running late, and I need a huge favor."
                show player 1
                player_name "Sure, {b}Aunt Diane{/b}! Anything you need!"
                show player 2
                dia "Great!"
                dia "I just need you to make a {b}small delivery{/b} for me."
                show player 3
                dia "The {b}package{/b} has to be dropped off at the {b}school{/b}, so come back during the school week."
                show player 1
                player_name "Okay."

        elif aunt_count == 4 and not aunt_dialogue_advance and quest10 not in quest_list:
            if quest10 in quest_list and quest10 not in completed_quests:
                scene garden_dead with None
            else:

                scene garden with None
            show player 11 at left with dissolve
            show aunt 106 at right with dissolve
            dia "{b}[firstname]!!!{/b}"
            show player 10
            show aunt 107
            player_name "{b}Aunt Diane{/b}?"
            player_name "Is everything okay??"
            show player 11
            show aunt 23
            dia "My poor vegetables!!"
            show player 23
            show aunt 22
            dia "They're all {b}destroyed{/b}!"
            show player 10
            player_name "What do you mean? How?"
            show player 11
            show aunt 106
            dia "There's some kind of... {b}Bug{/b}... It's an infestation!"
            show player 22
            dia "It took over my whole garden!!"
            show player 10
            show aunt 107
            player_name "What?!"
            show player 5
            show aunt 23
            dia "I have to do something quick before I lose everything..."
            show player 10
            show aunt 24
            player_name "Can I help in any way?"
            show player 5
            show aunt 2
            dia "I was thinking maybe you could {b}have a look{/b} at the bugs up close, first..."
            show aunt 3
            dia "I hate those things! I can't get close to them! They give me the creeps!"
            show player 14
            show aunt 4
            player_name "Sure, {b}Aunt Diane{/b}, I can have a look."
            show player 13
            show aunt 14
            dia "Oh! Do you think you could {b}find some pesticide{/b} to use on them?"
            show player 10
            show aunt 9
            player_name "Uhh... I don't mind..."
            show player 12
            player_name "But I'm not sure where I could find that kind of stuff."
            show player 11
            show aunt 6
            dia "You should try the {b}CONSUM-R{/b} at the mall."
            show aunt 10
            dia "Just {b}ask someone{/b} working there. Tell them what kind of bugs we have..."
            show player 10
            dia "I'm sure they'll help you find the right stuff."
            show player 21
            show aunt 9
            player_name "Alright, I'll see what I can find!"
            show player 13
            show aunt 3
            dia "Thanks so much!"
            show aunt 10
            dia "I don't know what I'd do without you..."
            hide player
            show aunt 11 at Position (xpos = 584, ypos = 768)
            with dissolve
            player_name "..."
            $ quest_list.append(quest10)

        elif aunt_count == 5 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 127 with dissolve
            player_name "Where's {b}Aunt Diane{/b}?"
            show player 12
            player_name "She's usually outside around this time..."
            show player 56
            player_name "She must be home somewhere."
            hide player 56 with dissolve
            $ ui_lock_count = 1

        elif aunt_count == 6 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 1 at left with dissolve
            show aunt 19 at right with dissolve
            dia "Heyyyy there, Mr. Handsooome!"
            show player 1 at left
            show aunt 17 at right
            player_name "Hi {b}Aunt Diane{/b}!"
            show player 11 at left
            player_name "..."
            show aunt 52 at right
            show player 21 at left
            player_name "Umm... You're not wearing a shirt, {b}Aunt Diane{/b}..."
            show player 13 at left
            dia "Oh! You're right! Haha!"
            show aunt 19 at right
            dia "I don't remember what happened to it!"
            show aunt 17 at right
            show player 21 at left
            player_name "...You lost it?"
            show aunt 19 at right
            show player 13 at left
            dia "It's probably all those margaritas, messing with my head again!"
            show aunt 17 at right
            show player 17 at left
            player_name "Haha, I see."
            show player 1 at left
            show aunt 18 at right
            dia "You know what?"
            dia "I think we should take a day off from the garden today... And just relax!"
            show aunt 19 at right
            show player 11 at left
            dia "What do you think?"
            menu:
                "Sure!":
                    show player 17 at left
                    show aunt 17 at right
                    player_name "Sure! I guess we could..."
                    show aunt 18 at right
                    show player 1 at left
                    dia "Let's just lay in the sun this afternoon!"
                    show aunt 19 at right
                    dia "There's nothing like a little sunbathing on a hot day!"
                    show aunt 17 at right
                    show player 1 at left
                    player_name "Umm... I could use a tan."
                    show aunt 20 at right
                    show player 11 at left
                    dia "First, you have to give me a hand with... a little something!"
                    show aunt 21 at right
                    window hide
                    pause
                    show aunt 20 at right
                    window hide
                    pause
                    show aunt 21 at right
                    window hide
                    pause
                    show aunt 20 at right
                    window hide
                    pause
                    show player 21 at left
                    player_name "You need help?... With... The sunscreen?"
                    show aunt 19 at right
                    show player 13 at left
                    dia "Well, of course!"
                    show aunt 18 at right
                    dia "How else am I going to do my back?"
                    dia "You don't want your poor Aunt to burn, do you?"
                    show aunt 17 at right
                    show player 21 at left
                    player_name "Okay. I guess I can help with that..."
                    show aunt 19 at right
                    show player 11 at left
                    dia "Let me just get the lawn chair... You just wait riiight here!"
                    hide player
                    scene garden_close
                    show aunt 25
                    with dissolve
                    player_name "( Hmmm... Okay... )"
                    player_name "( How am I going to do this... )"
                    show aunt 26
                    player_name "( Those straps are in the way... )"
                    player_name "( ...Maybe if I just... )"
                    show aunt 27
                    player_name "( ...Remove them like this... )"
                    show aunt 28
                    player_name "( There we go! )"
                    player_name "( Now, for the cream... )"
                    show aunt 29
                    window hide
                    pause
                    show aunt 30
                    window hide
                    pause
                    show aunt 31
                    player_name "Woah..."
                    player_name "( I can't believe I'm touching {b}Aunt Diane{/b}'s naked back... )"
                    show aunt 30
                    window hide
                    pause
                    show aunt 31
                    window hide
                    pause
                    show aunt 30
                    player_name "( It's so warm... And soft... )"
                    show aunt 31
                    window hide
                    pause
                    show aunt 30
                    window hide
                    pause
                    show aunt 32
                    player_name "..."
                    show aunt 32
                    window hide
                    pause
                    show aunt 33
                    window hide
                    pause
                    show aunt 34 with hpunch
                    player_name "( What the- )"
                    player_name "( She just lowered her pants... )"
                    player_name "( She wants me to go lower?? )"
                    player_name "..."
                    show aunt 35
                    window hide
                    pause
                    show aunt 36
                    window hide
                    pause
                    show aunt 35
                    window hide
                    pause
                    show aunt 36
                    player_name "( Maybe I can reach... Just a little... Further... )"
                    show aunt 36
                    window hide
                    pause
                    show aunt 37
                    window hide
                    pause
                    show aunt 36
                    window hide
                    pause
                    show aunt 37 with hpunch
                    player_name "( Oh shit! I went too far! )"
                    show aunt 38
                    player_name "( She's getting up... )"
                    show aunt 39 at Position (xpos = 484, ypos = 768)
                    with dissolve
                    player_name "I'm so sorry {b}Aunt Diane{/b}!!"
                    player_name "I know, I shouldn't have!"
                    show aunt 40
                    dia "What are you sorry for?"
                    dia "You did a veeery good job..."
                    show aunt 41
                    dia "..."
                    show aunt 42
                    dia "Why aren't you looking at me?"
                    player_name "Well... You're naked, {b}Aunt Diane{/b}!"
                    show aunt 46
                    dia "So? ...You've never seen a naked woman before?"
                    dia "...It's completely natural..."
                    show aunt 43
                    window hide
                    pause
                    show aunt 43
                    player_name "..."
                    show aunt 44
                    player_name "Uhh! Let me get you a towel!"
                    show aunt 45
                    dia "{b}Wait just a second!!{/b}"
                    dia "We're not quite done yet..."
                    dia "Aren't you going to do my front, first?"
                    show aunt 47
                    player_name "..."
                    show aunt 48
                    window hide
                    pause
                    show aunt 49 with hpunch
                    window hide
                    pause
                    show aunt 50
                    player_name "...Oh, crap! Not again!"
                    dia "Oh! Wow!"
                    player_name "I'm so sorry! I have to go now!"
                    show aunt 51
                    with dissolve
                    dia "Hey, wait a second!"
                    hide aunt 51
                    with dissolve
                    $ drunk_dialogue = True
                    $ aunt_dialogue_advance = True
                    jump map_dialogue
                "I'd rather not.":

                    show player 17 at left
                    show aunt 53 at right
                    player_name "I'd love to, but I should really get working on the garden..."
                    show player 1 at left
                    dia "You gotta have fun sometimes, you know..."
                    show aunt 18 at right
                    dia "But, I understand..."
                    show aunt 17 at right
                    show player 14 at left
                    player_name "Maybe next time!"
                    hide aunt 17 at right with dissolve
                    hide player 14 at left with dissolve
                    $ callScreen(location_count)

        elif aunt_count == 6 and aunt_dialogue_advance and drunk_dialogue:
            scene townmap
            player_name "I should visit {b}Aunt Diane{/b} another time..."
            jump map_dialogue

        elif aunt_count == 7 and not aunt_apology_seen:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            if drunk_dialogue:
                scene garden
                show player 5 at left with dissolve
                show aunt 23 at right with dissolve
                dia "Hey {b}[firstname]{/b}..."
                show aunt 24 at right
                show player 10 at left
                player_name "Hi {b}Aunt Diane{/b}..."
                player_name "..."
                show player 24 at left
                player_name "Umm... I wanted to apologize for the other day..."
                show player 17 at left
                show aunt 23 at right
                show player 5 at left
                dia "Stop."
                dia "It's me who should be sorry."
                show aunt 22 at right
                dia "I had too much to drink... And... I was clearly out of line."
                show player 21 at left
                player_name "It's okay Aunt Diane..."
                show aunt 23 at right
                show player 13 at left
                dia "Can we keep it between us?"
                show aunt 24 at right
                show player 29 at left
                player_name "Don't worry... I won't tell {b}Mom{/b}."
                player_name "It wasn't a big deal anyway."
                hide player
                show aunt 11 at left
                dia "Aw! Thanks hun. That's why you're my favourite nephew!"
                hide aunt 11 at left
                $ aunt_apology_seen = True
                $ callScreen(location_count)
        else:

            if aunt_count < 8 and aunt_count != 5:
                if in_garden:
                    $ in_garden = False
                    $ callScreen(location_count)

                if quest10 in quest_list and quest10 not in completed_quests:
                    scene garden_dead
                else:

                    scene garden
                show player 1 at left with dissolve
                show aunt 5 at right with dissolve
                dia "Hey Handsome! You came back to help your poor old Aunt pick her favourite vegetables?"
                show player 14 at left
                show aunt 7 at right
                player_name "I don't think you look old at all, {b}Aunt Diane{/b}."
                show player 1 at left
                show aunt 7 at right
                dia "Aw... You are such a sweetheart!"
                hide player 1
                show aunt 11 at left
                player_name "..."
                hide aunt 11 at left with dissolve
            $ callScreen(location_count)
    else:

        if quest09 in completed_quests and not aunt_shed_scene and aunt_count < 8:
            if quest10 in quest_list and quest10 not in completed_quests:
                scene garden_dead_night
            else:

                scene garden_night
            show player 12 with dissolve
            player_name "That's strange..."
            show player 30
            player_name "Aunt Diane's shed is {b}still open{/b}..."
            hide player 30 with dissolve
        else:

            if aunt_count < 8:
                jump night_closed_garden
    $ callScreen(location_count)

label aunt_button_dialogue:
    if aunt_drink_made:
        $ aunt_drink_made = False
        $ aunt_drink_offered = False
        scene location_garden_close_blur
        if aunt_extra_shot:
            $ aunt_extra_shot = False
            show player 136 at left with dissolve
            show aunt 100 at right with dissolve
            player_name "Here's your {b}drink{/b}!"
            show aunt 94
            show player 1
            dia "My favourite refreshment!"
            show aunt 97
            show player 18
            dia "You sure know how to please your {b}Aunt{/b}... And that is very sweet of you..."
            show player 11
            show aunt 95
            dia "..."
            show player 13
            show aunt 94
            dia "That was yummy..."
            show player 33
            show aunt 98
            player_name "I'm glad you like it!"
            show player 11
            show aunt 96
            dia "Wow... It has a strong kick to it, haha!"
            dia "I'm feeling a little... {b}Woozy{/b}!"
            show aunt 98
            show player 21
            player_name "Are you okay?"
            show player 13
            show aunt 97
            dia "Oh, I'm fiiiine..."
            show player 11
            show aunt 99
            dia "Just get me my {b}lawn chair{/b}, so I can lay down a little..."
            hide player
            scene garden_close
            show aunt 65 at Position (xpos = 490, ypos = 768)
            with dissolve
            player_name "Is that alright?"
            show aunt 66
            dia "Oh, yesss... This is wonderful!"
            show aunt 65
            player_name "Should I... get back to work?"
            show aunt 67
            dia "I think we should relax and have fun..."
            show aunt 68
            player_name "Haha! Okay."
            show aunt 65
            player_name "Umm... What are we doing for fun, then?"
            show aunt 67
            dia "I think we should continue where we left off."
            player_name "..."
            show aunt 65
            player_name "Wh- What do you mean?"
            show aunt 67
            dia "You know exactly what I mean, young man..."
            show aunt 69
            show aunt 70
            show aunt 71 with hpunch
            player_name "!!!"
            show aunt 72
            dia "What are you waiting for?"
            show aunt 73
            player_name "I don't know if I should..."
            show aunt 72
            dia "I know you want to {b}feel them{/b} with your hands..."
            show aunt 74
            dia "They're nice and soft..."
            dia "That's it..."
            show aunt 75
            dia "Jussst like that..."
            show aunt 77
            window hide
            pause
            show aunt 78
            window hide
            pause
            show aunt 75
            dia "Go slowly..."
            dia "...and squeeze the end of it gently..."
            show aunt 77_78_76
            pause 4
            dia "..."
            show aunt 75
            dia "Could you get up for me... Handsome?"
            show aunt 79 with hpunch
            player_name "!!!"
            dia "As I suspected..."
            dia "You seem to enjoy playing with your {b}Aunt{/b}'s body..."
            show aunt 80
            player_name "I... I can't control it..."
            show aunt 81
            player_name "!!!"
            dia "I haven't seen such a strong erection in a very long time..."
            dia "...And yours is... Truly exceptional..."
            show aunt 83_82
            pause 4
            show aunt 81
            dia "Does that feel good?"
            show aunt 83_82
            pause 4
            show aunt 84 with hpunch
            player_name "Oh, crap!"
            show aunt 85
            dia "Well... That didn't last very long!"
            player_name "I'm sorry, {b}Aunt Diane{/b}!"
            dia "Don't be!"
            dia "Let's clean you up in the {b}kitchen{/b}..."
            scene dianekitchen
            with dissolve
            show player 138 at left
            show aunt 86 at right
            with dissolve
            dia "Here, use this!"
            show player 140
            show aunt 91
            player_name "Thanks..."
            show player 139
            show aunt 92
            dia "Listen to me, {b}[firstname]{/b}."
            dia "Let's be honest with each other here..."
            show aunt 87
            dia "...You're obviously having strong desires for {b}my body{/b}..."
            show aunt 92
            dia "...and your {b}Aunt{/b} hasn't had any attention from a man in a very long time..."
            show aunt 89
            dia "...So why don't we keep this situation just {b}between us{/b}?"
            show aunt 91
            show player 140
            player_name "What do you mean?"
            show player 139
            show aunt 87
            dia "Well... You just let me know if you want some \"special attention\" from your {b}Aunt{/b}..."
            show aunt 89
            dia "...and we don't tell anyone about it!"
            show player 140
            show aunt 88
            player_name "I guess... We could do that."
            show player 139
            show aunt 90
            dia "Your mom definitely cannot know about this, or she'll kill me!!"
            show player 140
            show aunt 91
            player_name "Don't worry. I won't tell her."
            show player 139
            show aunt 90
            dia "That's my handsome boy!"
            show aunt 89
            dia "We're gonna have a lot of {b}fun{/b} together..."
            hide player
            show aunt 93 at left
            with dissolve
            window hide
            pause
            $ ui_lock_count = 0
            $ in_garden = True
            $ aunt_drink_active = False
            $ aunt_dialogue_advance = True
            jump garden_dialogue

    elif aunt_count < 8:
        scene location_garden_close_blur
        show player 1 at left with dissolve
        show aunt 5 at right with dissolve
        dia "Hey Handsome! You came back to help your poor old {b}Aunt{/b} pick her favourite vegetables?"
        show player 14 at left
        show aunt 7 at right
        player_name "I don't think you look old at all, {b}Aunt Diane{/b}."
        show player 1 at left
        show aunt 5 at right
        dia "Aw... You're such a sweetheart!"
        show aunt 10 at right
        dia "Is there anything else I can do for you before you get started?"
        label dia_default_dialogue_options:
            menu:
                "Talk.":
                    show aunt 1 at right
                    show player 17 at left
                    player_name "I just wanted to say how much we miss your visits at the house!"
                    show aunt 7
                    show player 10
                    player_name "You used to come by a lot more in the past, and hang out with {b}Mom{/b}..."
                    show aunt 22
                    show player 13
                    dia "I..."
                    show aunt 23
                    dia "I guess your {b}Aunt{/b} just likes to have some alone time, lately."
                    show aunt 24
                    show player 10
                    player_name "Is everything okay?"
                    show aunt 3
                    show player 13
                    dia "Of course!"
                    show aunt 23
                    dia "I just..."
                    show aunt 6
                    dia "Well... After my last divorce..."
                    dia "I guess... I don't see the point in trying to meet people, anymore."
                    show aunt 14
                    dia "So I just don't go out as much!"
                    show aunt 1
                    show player 108f
                    player_name "Oh. I see..."
                    show aunt 14
                    show player 13
                    dia "You might not know this, but I used to go out with your mom all the time!"
                    show aunt 8
                    show player 11
                    dia "We were known around town as the {b}Slinky Twins{/b}..."
                    show aunt 3
                    dia "We we partying all the time!"
                    show aunt 4
                    show player 21
                    player_name "Really?"
                    show aunt 2
                    show player 13
                    dia "You bet!"
                    show aunt 10
                    dia "We would go out on dates, and dance all night together."
                    show aunt 6
                    show player 11
                    dia "That's how your mom met your father, and I met all my stupid, ex husbands."
                    show aunt 12
                    show player 5
                    dia "That's what I get for drinking too much, and making poor decisions! Haha..."
                    show aunt 13
                    player_name "..."
                    show aunt 10
                    show player 11
                    dia "But you're not like those guys!"
                    dia "You're a nice, handsome, young man..."
                    show aunt 7
                    dia "..."
                    show aunt 22
                    dia "What am I saying? You don't want to hear about your old Aunt's problems!"
                    show aunt 24
                    show player 21
                    player_name "It's okay. I don't mind hearing about your stories."
                    show aunt 3
                    show player 13
                    dia "You're so sweet!"
                    show aunt 10
                    dia "Is there anything else you want to talk about?"
                    jump dia_default_dialogue_options

                "I found a shovel" if quest20 in quest_list and quest20 not in completed_quests and shovel in inventory.items:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "I found a {b}shovel{/b} in my garage!"
                    jump have_shovel

                "The garden." if quest20 in completed_quests:
                    show aunt 1 at right
                    show player 29 at left
                    player_name "About the garden... What exactly do I need to do?"
                    show aunt 2
                    show player 13
                    dia "I need you to clean it up and remove all the unwanted stuff from it."
                    show aunt 14 at right
                    show player 11 at left
                    dia "Make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
                    show aunt 14 at right
                    show player 11 at left
                    dia "Take out everything else... Especially those pesky rats and bugs! ...Got it?"
                    show aunt 1 at right
                    show player 14 at left
                    player_name "Got it!!"
                    show player 1
                    show aunt 2
                    dia "Is there anything else you want to talk about?"
                    jump dia_default_dialogue_options

                "The pump." if quest08 in quest_list and quest08 not in completed_quests:
                    show aunt 1
                    show player 29
                    player_name "Uhm... About that pump."
                    show aunt 2
                    show player 13
                    dia "Oh, right. Were you able to find it?"
                    menu:
                        "Where is it?":
                            show aunt 1 at right
                            show player 14 at left
                            player_name "Where did you say I could find it?"
                            show aunt 2 at right
                            show player 1 at left
                            dia "I told you earlier."
                            dia "It should be on the {b}shelf{/b}, in the {b}shed{/b}!"
                            show aunt 1 at right
                            show player 14 at left
                            player_name "Uhh... Okay. I'll look for it."
                            jump dia_default_dialogue_options
                        "Not yet.":

                            show player 10 at left
                            show aunt 1 at right
                            player_name "I haven't found it yet..."
                            show aunt 2 at right
                            show player 13 at left
                            dia "That's all right!"
                            show aunt 3 at right
                            dia "Just bring it to me when you find it."
                            show aunt 1 at right
                            show player 17 at left
                            player_name "Will do!"
                            hide player 17 at left with dissolve
                            hide aunt 1 at right with dissolve
                            jump dia_default_dialogue_options

                        "I found it!" if pump in inventory.items:
                            show player 17 at left
                            show aunt 1 at right
                            player_name "Yeah, it wasn't too hard to find!"
                            show player 239_240
                            pause
                            show aunt 2 at right
                            show player 103 at left
                            player_name "Here..."
                            $ inventory.items.remove(pump)
                            show player 1 at left
                            show aunt 54 at right
                            dia "Thank you!"
                            show player 21 at left
                            show aunt 1 at right
                            player_name "I wanted to ask you something..."
                            show aunt 2 at right
                            show player 13 at left
                            dia "Sure! What is it?"
                            show aunt 7 at right
                            show player 35 at left
                            player_name "What's that big {b}thing{/b} in the {b}shed{/b}? It has all sorts of chains hooked to it..."
                            player_name "...And some strange looking tubes and containers?"
                            show aunt 5 at right
                            show player 13 at left
                            dia "Oh, that thing..."
                            dia "It's a {b}milker{/b}!"
                            show aunt 7 at right
                            show player 21 at left
                            player_name "Like... To make milk?"
                            show aunt 6 at right
                            show player 13 at left
                            dia "Yeah I... Umm... Used to have a cow! That's right!"
                            show aunt 7 at right
                            show player 21 at left
                            player_name "In your {b}shed{/b}?"
                            show aunt 5 at right
                            show player 13 at left
                            dia "Hmm... Well I couldn't let it eat my garden!"
                            show aunt 9 at right
                            show player 35 at left
                            player_name "I see..."
                            show player 17 at left
                            player_name "Anyway, I should get back to work!"
                            $ quest_complete(quest08)
                            $ aunt_dialogue_advance = True
                            hide player 17 at left with dissolve
                            hide aunt 9 at right with dissolve

                "Milk delivery." if quest09 in quest_list and quest09 not in completed_quests:
                    show aunt 1
                    show player 14
                    player_name "Those milk cartons you asked me to deliver."
                    show aunt 3
                    show player 1
                    dia "Oh right!"
                    show aunt 2
                    dia "How is it going? Did you drop them off at the school?"
                    menu:
                        "Where at school?":
                            show aunt 1
                            show player 29
                            player_name "Where did you want me to drop them off at school? I forgot..."
                            show aunt 2
                            show player 13
                            dia "At the {b}cafeteria{/b}!"
                            show aunt 3
                            dia "It's where all deliveries go."
                            show aunt 1
                            show player 17
                            player_name "Got it!"
                            show aunt 14
                            show player 11
                            dia "Hurry up before it gets too warm!"
                            show aunt 1
                            show player 17
                            player_name "Will do! Thanks."
                            jump dia_default_dialogue_options
                        "Not yet.":

                            show aunt 1
                            show player 29
                            player_name "I still have to go to school to drop it off."
                            show aunt 2
                            show player 13
                            dia "No problem."
                            show aunt 14
                            show player 11
                            dia "But don't wait too long! The milk will get warm..."
                            show aunt 1
                            show player 17
                            player_name "Will do! Thanks."
                            jump dia_default_dialogue_options

                        "I delivered them!" if quest09_3 == True:
                            show aunt 1 at right
                            show player 2 at left
                            player_name "I've got some great news, {b}Aunt Diane{/b}!"
                            player_name "My principal wants to double the school's order!"
                            show player 13
                            show aunt 2
                            dia "What? Really?"
                            show aunt 1
                            show player 17
                            player_name "She says people really like it!"
                            show player 13
                            show aunt 6
                            dia "Well, that will definitely keep me busy..."
                            show aunt 10
                            dia "I may even need an extra hand to help me pump it all."
                            show aunt 8
                            dia "I just hope I can produce enough..."
                            show player 2
                            show aunt 9
                            player_name "Whatever you need, I can help!"
                            show player 1
                            show aunt 8
                            dia "I'll keep that in mind."
                            show aunt 9
                            pause
                            show aunt 10
                            dia "Oh, before you go..."
                            dia "I don't think I ever offered you some of the {b}fresh milk{/b} I make!"
                            show aunt 9
                            show player 11
                            player_name "..."
                            show aunt 55 with fastdissolve
                            dia "Would you like to try some?"
                            show aunt 56
                            show player 12
                            player_name "It's fresh? As in it was collected this morning??"
                            show aunt 55
                            show player 11
                            dia "Of course!"
                            show aunt 56
                            show player 21
                            player_name "Did you get a new cow or something?"
                            show aunt 55
                            show player 13
                            dia "Err.. No. I... got it from the farmer's market earlier!"
                            dia "I just package it here."
                            show aunt 56
                            show player 17
                            player_name "That's cool..."
                            show aunt 55
                            show player 11
                            dia "So? You wanna try it?"
                            show aunt 56
                            menu:
                                "Sure!":
                                    show player 17 at left
                                    show aunt 55 at right
                                    player_name "Sure! I'll try it..."
                                    show aunt 10 at right
                                    show player 105 at left
                                    dia "Have as much as you want!"
                                    show aunt 9 at right
                                    window hide
                                    pause
                                    show player 104 at left
                                    player_name "..."
                                    show player 34 at left
                                    show aunt 10 at right
                                    dia "So? How is it?"
                                    show aunt 9 at right
                                    show player 35 at left
                                    player_name "It's warm..."
                                    show player 30 at left
                                    player_name "...And sort of.. creamy?"
                                    show aunt 3 at right
                                    show player 11 at left
                                    dia "Haha!"
                                    show aunt 10 at right
                                    dia "Did you like it, at least?"
                                    show aunt 9 at right
                                    show player 21 at left
                                    player_name "...Yeah it's not bad!"
                                    show aunt 10 at right
                                    show player 13 at left
                                    dia "Alright, I might get you more later, then..."
                                    show aunt 4 at right
                                    show player 21 at left
                                    player_name "Sure, {b}Aunt Diane{/b}! Thank you!"
                                    $ drink_milk_offer = True
                                    $ drank_milk = True
                                    hide player 21 at left with dissolve
                                    hide aunt 4 at right with dissolve
                                "I don't like milk.":

                                    show aunt 4 at right
                                    show player 21 at left
                                    player_name "No thank you... I'm not a big fan of milk..."
                                    show aunt 8 at right
                                    show player 13 at left
                                    dia "Really?"
                                    show aunt 14 at right
                                    dia "That's too bad... You don't know what you're missing out on!"
                                    show aunt 1 at right
                                    show player 26 at left
                                    player_name "Yeah, I bet..."
                                    show player 17 at left
                                    player_name "Anyway, I should get back to work!"
                                    $ drink_milk_offer = True
                                    hide player 17 at left with dissolve
                                    hide aunt 1 at right with dissolve
                            $ gTimer.tick()
                            $ completed_quests.append(quest09)
                            $ aunt_dialogue_advance = True
                            $ quest09_3 = False

                "Bug infestation." if quest10 in quest_list and quest10 not in completed_quests:
                    show aunt 1
                    show player 14
                    player_name "The bug problem in the garden..."
                    show player 1
                    show aunt 23
                    dia "Oh yeah, those damn {b}bugs{/b}."
                    dia "Were you able to {b}find a way{/b} to get rid of them yet?"
                    menu:
                        "What should I do?":
                            show aunt 24
                            show player 29
                            player_name "I'm not sure how I to get rid of them..."
                            show aunt 14
                            show player 13
                            dia "Well, if I were you, I'd try and find some kind of {b}pesticide{/b}."
                            show aunt 6
                            dia "Maybe ask someone at the {b}store{/b}? They'll {b}help{/b} you get the right stuff."
                            show aunt 1
                            show player 21
                            player_name "Alright, I'll go have a look at the mall. Thanks!"
                            show aunt 2
                            show player 13
                            dia "See you soon!"
                            jump dia_default_dialogue_options
                        "Not Yet.":

                            show aunt 24
                            show player 29
                            player_name "I haven't found a solution yet."
                            show player 21
                            player_name "But don't worry, Aunt Diane! I'll find a way!"
                            show player 13
                            show aunt 3
                            dia "Haha."
                            dia "I'm sure you will!"
                            show aunt 2
                            dia "Come back to me when you've made some progress."
                            jump dia_default_dialogue_options

                        "I got rid of them!" if infestation_done == True:
                            show aunt 24
                            show player 33
                            player_name "I think I did it!"
                            show aunt 7
                            show player 2
                            dia "You did?!"
                            show player 162
                            player_name "Yeah, I just applied this {b}pesticide{/b} I bought at the store and it did the trick!"
                            show aunt 1
                            show player 12
                            player_name "Took me a while, but they should be leaving you alone, now!"
                            show aunt 3
                            show player 2
                            dia "That's amazing!"
                            show aunt 10
                            show player 11
                            dia "I'm so lucky to have such a... {b}handy Nephew{/b}..."
                            show aunt 9
                            show player 29
                            player_name "Oh, it's nothing. I'm just glad I could help!"
                            show aunt 23
                            show player 11
                            dia "Did the pesticide cost you anything?"
                            dia "I should really pay you back for that."
                            show aunt 24
                            show player 21
                            player_name "It's okay. It didn't cost me much, anyway."
                            show aunt 14
                            show player 11
                            dia "Well, if you don't let me pay you back, I'll just have to pay you more for your working in my garden!"
                            show aunt 4
                            player_name "..."
                            show aunt 10
                            show player 13
                            dia "Your Aunt can also play this game!"
                            show aunt 9
                            show player 21
                            player_name "Are you sure?"
                            show aunt 10
                            show player 13
                            dia "Of course! You've been such a great help around here!"
                            show aunt 3
                            dia "You deserve it!"
                            show aunt 4
                            show player 21
                            player_name "Heh... Thanks."
                            $ upgrade_garden()
                            $ aunt_dialogue_advance = True
                            $ completed_quests.append(quest10)

                "Make a drink." if aunt_count == 6 and not aunt_dialogue_advance or aunt_count == 7 and not aunt_dialogue_advance:
                    if pStats.chr() >= 5:
                        $ aunt_drink_offered = True
                        show aunt 1 at right
                        show player 14 at left
                        player_name "Hey, I got an idea!"
                        show player 17
                        show aunt 7
                        player_name "Let's make you a nice, refreshing, {b}drink{/b}!"
                        show player 1
                        show aunt 5
                        dia "Oh... I'm not sure I should have that! Haha!"
                        show player 17
                        show aunt 7
                        player_name "I think it would do you some good!"
                        show player 14
                        player_name "You deserve it!"
                        show player 1
                        show aunt 12
                        dia "I guess you're right... It has been a long day, after all!"
                        show player 14
                        show aunt 13
                        player_name "Where do you keep your margaritas?"
                        show player 1
                        show aunt 5
                        dia "You can make them in the {b}kitchen{/b}..."
                        show aunt 14
                        dia "...And I'll make myself comfortable while I wait..."
                        show player 17
                        show aunt 9
                        player_name "I'll be right back!!"
                        hide player 17 with dissolve
                        $ aunt_drink_active = True
                    else:

                        show aunt 1 at right
                        show player 29 at left
                        player_name "[chr_warn]Hey, I umm..."
                        show aunt 7
                        player_name "[chr_warn]...Was wondering if you'd like a {b}drink{/b}?"
                        show player 3
                        show aunt 5
                        dia "Oh... I don't think now is a good time."
                        show player 24
                        player_name "[chr_warn]I... Thought you liked those..."
                        show aunt 22
                        show player 13
                        dia "I... Tend to make bad decisions when I drink..."
                        show player 24
                        show aunt 24
                        player_name "[chr_warn]I see..."
                        show player 21
                        player_name "[chr_warn]Maybe another time, then."
                        hide player 21 with dissolve
                        hide aunt 24 with dissolve
                "I have to work.":

                    show aunt 1 at right
                    show player 17 at left
                    player_name "I'm just get started on the garden..."
                    dia "Eager to get those muscles working, I see!"
                    show player 11
                    show aunt 10
                    dia "Come here, and give your {b}Aunt{/b} a nice {b}kiss{/b}!"
                    hide player 11
                    show aunt 11 at left
                    player_name "..."
                    hide aunt 11 at left with dissolve
        $ callScreen(location_count)

    elif aunt_count >= 8:
        scene location_diane_kitchen_closeup
        show player 1 at left with dissolve
        show aunt 89 at right with dissolve
        dia "Hey there, Handsome..."
        if not gTimer.is_weekend():
            dia "Dropping by your {b}Aunt{/b}'s house on the way back from school?"
        else:

            dia "Bored at home, and felt like seeing your Aunt?"
        show aunt 88
        show player 29
        player_name "Is that... Okay?"
        show aunt 90
        show player 13
        dia "Of course!"
        show aunt 89
        dia "I was hoping you'd come by my house for some {b}secret fun{/b}..."
        show aunt 88
        show player 21
        player_name "Do you want to... Do something?"
        show aunt 89
        show player 13
        dia "What do you have in mind?"
        label dia_default_dialogue_options_kitchen:
            menu:
                "Talk.":
                    show aunt 109 at Position (xpos=947)
                    show player 21
                    player_name "I just wanted to tell you how much I've been thinking about visiting you..."
                    show aunt 89 at right
                    show player 13
                    dia "You've been missing your {b}Auntie{/b}?"
                    show aunt 89
                    show player 21
                    player_name "Yeah."
                    show aunt 87
                    show player 13
                    dia "Well, I've also been thinking about your daily visits... And watching you work hard..."
                    show aunt 88
                    show player 29
                    player_name "Really?"
                    show aunt 92
                    show player 5
                    dia "I haven't had a man around... In quite some time."
                    show aunt 88
                    show player 2
                    player_name "I appreciate everything you've been doing for me, {b}Aunt Diane{/b}..."
                    player_name "I've never had someone give me that kind of... Attention, before..."
                    show aunt 109 at Position (xpos=947)
                    show player 108f
                    player_name "...And you're so pretty..."
                    show aunt 90 at right
                    show player 13
                    dia "You're so sweet!"
                    show aunt 88
                    show player 108f
                    player_name "I also like that we can meet here... In secret."
                    show aunt 89
                    show player 13
                    dia "I suppose there's something exciting about doing things together, in private."
                    dia "That's why you're my favourite. I can trust you to keep this between us!"
                    show aunt 88
                    show player 17
                    player_name "Yeah... I don't want it to stop..."
                    show aunt 89
                    show player 13
                    dia "Your {b}Auntie{/b} will always have her... Door open for you."
                    show aunt 88
                    show player 17
                    player_name "Thanks..."
                    show aunt 89
                    show player 1
                    dia "Is there anything else you have in mind?"
                    jump dia_default_dialogue_options_kitchen
                "Talk about Mom.":

                    show aunt 109 at Position (xpos=947)
                    show player 24
                    player_name "I worry about {b}Mom{/b}..."
                    show aunt 92 at right
                    show player 5
                    dia "What do you mean?"
                    show aunt 91
                    show player 10
                    player_name "She seems really stressed out, after all that happened with {b}Dad{/b}..."
                    show aunt 92
                    show player 13
                    dia "Hmmm... Well, my {b}Sister{/b} is a strong woman, just like me."
                    show aunt 87
                    dia "She'll be fine!"
                    show aunt 91
                    show player 24
                    player_name "I just want to protect her! I want to... Hold her and make her feel safe."
                    show aunt 109 at Position (xpos=947)
                    show player 13
                    dia "..."
                    show aunt 89 at right
                    show player 11
                    dia "Do you... have feelings for your mom, as well?"
                    show aunt 88
                    show player 29
                    player_name "Well... I love my mom, of course."
                    show aunt 89
                    show player 3
                    dia "You know what I mean..."
                    dia "Do you {b}fantasize{/b} about her? Do you want to do things to her, like you do with me?"
                    menu:
                        "Yes.":
                            show aunt 88
                            show player 24
                            player_name "Yeah... I do."
                            show player 21
                            player_name "I've been thinking about her... And I get all excited when I see her..."
                            show aunt 109 at Position (xpos=947)
                            show player 108f
                            player_name "Like when I catch her in the shower, and stare at her naked..."
                            show aunt 110 at Position (xpos=950)
                            show player 13
                            dia "Oh {b}wow{/b}..."
                            show aunt 89 at right
                            show player 11
                            dia "Does she know?"
                            show aunt 88
                            show player 10
                            player_name "I don't think so..."
                            show aunt 89
                            show player 11
                            dia "You must've been quite horny."
                            show aunt 109 at Position (xpos=947)
                            show player 29
                            player_name "I know. I have these urges, and I keep thinking about doing stuff with {b}Mom{/b}... And {b}You{/b}."
                            show aunt 90 at right
                            show player 13
                            dia "My goodness! You must have something for twins!"
                            show aunt 89
                            show player 11
                            dia "Have you tried giving her {b}hints{/b}?"
                            show aunt 87
                            dia "You never know... She might like it."
                            show aunt 88
                            show player 21
                            player_name "What do you mean?"
                            show aunt 89
                            show player 13
                            dia "Well, she's lonely... She could use a man around her."
                            show aunt 87
                            dia "Someone to take care of her, and satisfy... Whatever needs she has!"
                            show aunt 88
                            show player 108f
                            player_name "I guess so..."
                            show aunt 89
                            show player 11
                            dia "You should try."
                            dia "See what she does..."
                            show aunt 88
                            show player 21
                            player_name "I'll think about it."
                            show aunt 89
                            show player 13
                            dia "Is there anything else you have in mind?"
                            jump dia_default_dialogue_options_kitchen
                        "No.":

                            show aunt 91
                            show player 24
                            player_name "No... Not really."
                            show player 10
                            player_name "I just care a lot about her."
                            show aunt 89
                            show player 13
                            dia "I see..."
                            show aunt 87
                            dia "Well, you're doing just fine!"
                            show aunt 89
                            dia "And she's lucky to have such a caring {b}Son{/b}."
                            show aunt 88
                            show player 21
                            player_name "Thanks..."
                            show aunt 89
                            show player 13
                            dia "Is there anything else you have in mind?"
                            jump dia_default_dialogue_options_kitchen

                "Milk production." if not aunt.known(aunt_breeding_guide):
                    show aunt 91
                    show player 14
                    player_name "How's your milk business going?"
                    show player 13
                    show aunt 90
                    dia "Wonderful!"
                    dia "The market is growing, and everybody is loving my milk!"
                    show aunt 89
                    dia "Having your school double its order is helping a lot."
                    show aunt 88
                    show player 14
                    player_name "That's awesome!"
                    show player 13
                    show aunt 89
                    dia "Yeah."
                    show aunt 91
                    pause
                    show aunt 92
                    show player 11
                    dia "Unfortunately though, my {b}thermal tank{/b} failed on me today."
                    dia "I don't have any way of keeping my milk chilled."
                    show aunt 91
                    show player 4
                    pause
                    show player 17
                    player_name "I can probably get you a new one, if you'd like?"
                    show player 18
                    pause
                    show aunt 110 at Position (xpos = 950)
                    dia "You could?"
                    show aunt 92 at right
                    dia "That would be really nice of you to do!"
                    show player 34
                    dia "I'm just not sure where you could find one..."
                    show aunt 91
                    show player 35
                    player_name "Hmm... I could check the {b}mall{/b} for one."
                    show aunt 92
                    show player 13
                    dia "Sure. That could work."
                    dia "But that's the easy part..."
                    show aunt 91
                    pause
                    show player 10
                    player_name "Is something else wrong?"
                    show aunt 92
                    show player 11
                    dia "I'm not sure yet."
                    dia "It seems that I'm reaching my limit on how much milk I can produce."
                    dia "I don't think I'll be able to meet future demands."
                    dia "I really need to find a way to increase production."
                    show aunt 91
                    show player 10
                    player_name "Oh? Any ideas on how to do that?"
                    show player 11
                    show aunt 92
                    dia "Nothing easy springs to mind."
                    show aunt 87
                    dia "It's not like I can go advertising for more cows!"
                    show player 17
                    show aunt 90
                    dia "Hahaha!"
                    pause
                    show aunt 88
                    show player 29
                    player_name "Maybe I can help with that, too!"
                    show aunt 89
                    show player 13 at left
                    dia "Really?"
                    show aunt 88
                    show player 14
                    player_name "Yeah. We can use the {b}library{/b} for {b}research{/b}."
                    player_name "Maybe I can find some information about {b}milk production{/b} there."
                    show player 13
                    show aunt 90
                    dia "Oh, you're the best nephew in the whole world!"
                    show aunt 87
                    dia "Let me know if you find anything!"
                    show aunt 89
                    dia "I'll be sure to {b}reward{/b} you!"
                    hide aunt
                    hide player
                    with dissolve
                    $ quest_list.append(quest12)
                    $ aunt.add_event(aunt_breeding_guide)

                "The milk jug." if quest12 in quest_list and quest12 not in completed_quests and milkjug not in inventory.items:
                    show aunt 88
                    show player 10
                    player_name "What should I do about keeping the milk chilled?"
                    show aunt 87
                    show player 5
                    dia "We need to find a {b}thermal jug{/b} to keep the milk chilled."
                    show aunt 89
                    dia "They're usually made of {b}stainless steel, with a lid{/b}."
                    dia "I'm sure we can find something like that somwehere in the {b}mall{/b}."
                    show aunt 88
                    show player 10
                    player_name "Okay! I'll try to find something."

                "The milk jug." if quest12 in quest_list and quest12 not in completed_quests and milkjug in inventory.items:
                    show player 239_240
                    pause
                    show aunt 88
                    show player 173
                    player_name "I found a large {b}milk jug{/b}!"
                    show aunt 90
                    show player 172
                    dia "Oh, that's wonderful!"
                    show aunt 118
                    show player 1
                    dia "Thank you so much, {b}[firstname]{/b}."
                    dia "You really saved me a lot of work!"
                    show aunt 88
                    show player 17
                    player_name "It's nothing, {b}Aunt Diane!{/b}"
                    show player 14
                    player_name "I'm glad I can keep all that milk chilled now."
                    $ inventory.items.remove(milkjug)
                    $ completed_quests.append(quest12)

                "Milk production book." if aunt.known(aunt_breeding_guide) and breeding_guide in inventory.items and not aunt.known(aunt_breeding_bull):
                    $ inventory.items.remove(breeding_guide)
                    show player 239_240
                    pause
                    show player 369
                    player_name "Here, I found this {b}book{/b} at the {b}library{/b}!"
                    show player 14
                    show aunt 158 at Position(xpos=985)
                    with fastdissolve
                    player_name "It has information and detailed illustrations on how to increase milk production..."
                    show aunt 159
                    show player 10
                    player_name "It's... meant for farming animals, but I believe it could work with you."
                    show player 5
                    show aunt 157
                    dia "Huh?"
                    dia "I see..."
                    show aunt 159
                    player_name "..."
                    show aunt 160
                    dia "Hmm... Finding a bull?"
                    show aunt 159
                    dia "..."
                    show player 11
                    show aunt 160
                    dia "Pair the {b}bull{/b} with a {b}fertile female{/b} for... {b}breeding{/b}?!"
                    show aunt 159
                    dia "..."
                    show aunt 160
                    dia "Once the cow has been {b}impregnated{/b}, her udders expand for increased lactation..."
                    show aunt 159

                    show player 5
                    player_name "..."
                    show aunt 158
                    show player 10
                    player_name "So what do you think, {b}Aunt Diane{/b}?"
                    show player 5
                    show aunt 160
                    dia "I... don't..."
                    show aunt 157
                    dia "I guess I'm just a little surprised."
                    show aunt 160
                    dia "That's just not something I was planning to do."
                    dia "I mean, I've been able to produce decent amounts of milk..."
                    show player 14
                    show aunt 159
                    player_name "But this could double your supply!"
                    show player 13
                    show aunt 158
                    dia "..."
                    show aunt 157
                    dia "I'll have to think about it."
                    dia "This comes with... consequences, you know..."
                    show aunt 158
                    show player 21
                    player_name "I just thought this could help you solve your problems..."
                    show player 13
                    show aunt 160
                    dia "It's great! Thank you for your help."
                    show aunt 157
                    dia "You've been very good lately."
                    show aunt 158
                    show player 14
                    player_name "You're welcome, {b}Aunt Diane{/b}!"
                    show player 13
                    pause
                    show player 29
                    player_name "Well, I guess I'll get back to gardening then."
                    show player 1
                    show aunt 157
                    dia "Sure. I'll catch up with you later..."
                    show aunt 159
                    hide player with dissolve
                    dia "..."
                    show aunt 110 at Position(xpos=950)
                    dia "Getting {b}pregnant{/b}?"
                    dia "It's been a while since I thought of having a kid."
                    dia "My exes never wanted any..."
                    show aunt 91 at Position(xpos=1024)
                    dia "..."
                    show aunt 92
                    dia "But I'm not too old, yet..."
                    show aunt 89
                    dia "I can't believe my nephew is suggesting farming manuals..."
                    show aunt 88
                    pause
                    show aunt 92
                    dia "Even if I did, who would I even find to... {b}breed{/b} with?"
                    dia "{b}Breeding{/b}..."
                    show aunt 89
                    dia "It sounds so... primal! So... Animalistic! So... naughty!"
                    show aunt 88
                    dia "Hmm."
                    show aunt 87
                    dia "The only person I can think of is... my nephew."
                    show aunt 92
                    dia "No! I can't..."
                    show aunt 89
                    dia "... but he has such a nice cock, like a {b}bull{/b}..."
                    show aunt 110 at Position(xpos=950)
                    dia "Come on, {b}Diane{/b}! You're thinking about fucking your sister's son {b}raw{/b}!"
                    dia "What would I say to my sister if I had a kid with her son?"
                    show aunt 91 at Position(xpos=1024)
                    dia "..."
                    show aunt 92
                    dia "Who else do I have though? I'm just becoming an old lady with her vegetables..."
                    dia "He probably wouldn't even want to do this with me..."
                    show aunt 88
                    pause
                    show aunt 92
                    dia "But, I have to do something, if I'm going to expand this milk business."
                    dia "Doing nothing won't help any."
                    show aunt 89
                    dia "He's done nothing BUT help... satisfy me, lately."
                    show aunt 88
                    pause
                    show aunt 87
                    dia "God, I keep thinking about his huge cock!"
                    show aunt 89
                    dia "I love feeling it inside me."
                    show aunt 88
                    dia "..."
                    show aunt 89
                    dia "I... I have to clear my head, and think about all of this."
                    show aunt 92
                    dia "This has to be a purely business decision, {b}Diane{/b}."
                    hide aunt with dissolve
                    $ aunt.add_event(aunt_breeding_bull)
                    jump garden_dialogue

                "Breeding." if aunt.over(aunt_breeding_bull) and not aunt.known(aunt_breeding_help):
                    show player 10
                    player_name "Any luck finding a... bull to breed with, {b}Aunt Diane{/b}?"
                    show player 5
                    show aunt 87
                    dia "Oh... You know me..."
                    show aunt 92
                    dia "I hardly leave the house these days..."
                    dia "I've got the garden, and my milking operation to keep me quite busy."
                    dia "It's hard meeting people, you know?"
                    show aunt 91
                    show player 14
                    player_name "I suppose, yeah..."
                    show player 13
                    show aunt 89
                    dia "Why are you asking, anyway? Do you have someone in mind?"
                    show aunt 88
                    menu:
                        "Me!" if pStats.chr() < 7:
                            show player 10
                            player_name "[chr_warn]Would you... I mean... do you think..."
                            show player 24
                            show aunt 110 at Position (xpos = 950)
                            player_name "[chr_warn]Nevermind."
                            show player 5
                            show aunt 92 at right
                            dia "What were you going to say?"
                            show aunt 91
                            show player 10
                            player_name "[chr_warn]It's nothing. I just... um..."
                            show player 24
                            player_name "[chr_warn]I promise I'll keep looking, and find someone... I mean I'll find a suitable bull for you."
                            show player 5
                            show aunt 92
                            dia "Thanks sweetheart!"
                            dia "Don't ever be afraid to speak your mind."
                            show aunt 91
                            show player 10
                            player_name "[chr_warn]Sure, {b}Aunt Diane{/b}."
                            show player 5
                            show aunt 92
                            dia "Anything else you want to talk about?"
                            show aunt 91
                            jump dia_default_dialogue_options_kitchen

                        "Me!" if pStats.chr() >= 7:
                            show player 14
                            player_name "Well... Why couldn't I do it?"
                            show player 13
                            show aunt 109 at Position (xpos = 950)
                            dia "!!!" with hpunch
                            show aunt 110 at Position (xpos = 953)
                            dia "What? Really?"
                            show player 17
                            show aunt 91 at Position(xpos=1027)
                            player_name "Yeah! I mean, we already... do stuff together..."
                            show player 13
                            show aunt 87
                            dia "Yes... we do, but..."
                            show aunt 89
                            dia "You're my sister's kid!"
                            show aunt 88
                            show player 21
                            player_name "I'm sorry, I thought maybe you'd want to."
                            show player 5
                            show aunt 91
                            dia "..."
                            show player 11
                            show aunt 89
                            dia "I... I do!"
                            show aunt 92
                            dia "I figured you'd think I'm too old for you!"
                            show aunt 91
                            show player 33
                            player_name "I don't think you're old at all!"
                            show player 1
                            pause
                            show aunt 89
                            dia "I would love to have you {b}breed me{/b}."
                            show aunt 88
                            show player 11
                            player_name "!!!"
                            show player 1
                            show aunt 89
                            dia "You know, I actually thought about you as a potential partner, but thought you would never want to {b}breed{/b} with {b}me{/b}."
                            show aunt 90
                            dia "I thought you just liked to fool around, you know?"
                            show aunt 88
                            show player 21
                            player_name "No, I... I really like doing those things with you {b}Aunt Diane{/b}!"
                            player_name "When can we start? I'm up to doing it right now!"
                            show player 13
                            show aunt 90
                            dia "Not too fast, my young, horny bull!"
                            show aunt 89
                            dia "We have to make something clear, first."
                            dia "Your mother can never know about this, okay?"
                            show aunt 88
                            show player 14
                            player_name "Okay, I won't say a word. I promise!"
                            show player 13
                            show aunt 87
                            dia "Alright."
                            dia "If you still feel like you want to do this with me..."
                            show aunt 89
                            dia "... meet me in my shed at night."
                            dia "I'll have something prepared for us..."
                            show aunt 88
                            show player 21
                            player_name "See you there, {b}Aunt Diane{/b}!"
                            hide player
                            hide aunt
                            with dissolve
                            $ aunt.add_event(aunt_breeding_help)
                        "Not yet.":

                            show player 10
                            player_name "No."
                            show player 14
                            player_name "But I'll keep looking."
                            show player 13
                            show aunt 89
                            dia "Good. Keep an eye out for potential candidates for me!"
                            show aunt 88
                            show player 14
                            player_name "Will do."
                            hide player
                            hide aunt
                            with dissolve
                "Have fun.":

                    show aunt 109 at Position (xpos=947)
                    show player 29
                    player_name "Maybe have some fun?"
                    show aunt 89 at right
                    show player 13
                    dia "Ahhh..."
                    dia "Someone's in the mood for some... Special attention."
                    show aunt 88
                    show player 108f
                    player_name "Y... Yeah."
                    show aunt 87
                    show player 11
                    dia "Very well... Let's get comfortable first..."
                    scene dianekitchen_closeup
                    show auntsex 2 at Position(xpos = 702, ypos = 769)
                    show playersex 1 at Position(xpos = 260, ypos = 768)
                    with dissolve
                    dia "Now..."
                    dia "Take off your pants."
                    show auntsex 1
                    show playersex 1
                    window hide
                    pause
                    show playersex 2 at Position(xpos = 300, ypos = 768)
                    window hide
                    pause
                    show playersex 3 at Position(xpos = 350, ypos = 768)
                    show auntsex 2
                    dia "Very good..."
                    if not aunt_had_sex:
                        show playersex 4 with dissolve
                        show playersex 3 with dissolve
                        window hide
                        pause
                        show auntsex 7
                        window hide
                        pause
                        show playersex 4 with dissolve
                        show playersex 3 with dissolve
                        show auntsex 8
                        dia "Wow... It's... Twitching..."
                        show auntsex 7
                        window hide
                        pause
                        show playersex 4
                        show playersex 3
                        show auntsex 2
                        dia "I want to compare it to my vegetable!"
                        show auntsex 9
                        show playersex 3
                        player_name "..."
                        show auntsex 10 at Position(xpos = 698, ypos = 769)
                        show playersex 3
                        dia "That's... It's amazing!"
                        dia "None of my ex husbands come close to this..."
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "Do you mind if I touch it?"
                        show auntsex 1
                        player_name "It... It's fine."
                        hide playersex
                        show auntsex 11_12 at Position(xpos = 621, ypos = 769)
                        pause 4
                        show playersex 3 at Position(xpos = 350, ypos = 768)
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "So..."
                        dia "Would you like to see me naked?"
                        menu:
                            "Yes.":
                                show auntsex 1
                                show playersex 3
                                player_name "I'd really like that..."
                                show auntsex 2
                                dia "Okay. My turn, then..."
                                show auntsex 3 at Position(xpos = 675, ypos = 769)
                                pause
                                show auntsex 4
                                pause
                                show auntsex 13 at Position(xpos = 709, ypos = 769)
                                player_name "Woa..."
                                show playersex 4
                                pause
                                show playersex 3
                                player_name "You're so pretty, Aunt Diane..."
                                show auntsex 15
                                dia "..."
                                show auntsex 14
                                dia "You keep talking like that and I'm gonna have to invite you for sleep overs."
                                show auntsex 13
                                player_name "Can I... Touch you?"
                                show auntsex 14
                                dia "Of course you can..."
                                dia "But only with the tip..."
                                hide playersex
                                show auntsex 18 at Position(xpos = 626, ypos = 769)
                                dia "Just like that..."
                                show auntsex 19_20 at Position(xpos = 640, ypos = 769)
                                pause 4
                                show auntsex 21 at Position(xpos = 650, ypos = 769)
                                dia "You like that?"
                                show auntsex 20 at Position(xpos = 640, ypos = 769)
                                player_name "Yeah..."
                                show auntsex 15 at Position(xpos = 709, ypos = 769)
                                show playersex 3 at Position(xpos = 350, ypos = 768)
                                player_name "I... Want more..."
                                show auntsex 14
                                dia "What do you mean?"
                                label dia_sex_options:
                                    menu:
                                        "I want you." if pStats.chr() < 7:
                                            show auntsex 15
                                            player_name "[chr_warn]I... I want to be inside you {b}Aunt Diane{/b}."
                                            dia "[chr_warn]..."
                                            show auntsex 14
                                            dia "[chr_warn]Someone's getting excited."
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "[chr_warn]Hmmm..."
                                            show auntsex 17
                                            dia "[chr_warn]Perhaps it's a bit too soon for that."
                                            show auntsex 16
                                            player_name "[chr_warn]..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "[chr_warn]But maybe there's something else we can do."
                                            jump dia_sex_options

                                        "I want you." if pStats.chr() >= 7:
                                            show auntsex 15
                                            player_name "I... I want to be inside you Aunt Diane."
                                            dia "!!!"
                                            show auntsex 17 at Position(xpos = 640, ypos = 769)
                                            dia "Hmm... I don't know if we should..."
                                            show auntsex 15 at Position(xpos = 709, ypos = 769)
                                            player_name "I've always wanted to do it with you..."
                                            player_name "It's all I think about!"
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "Well, I haven't had the real thing in quite some time..."
                                            show auntsex 17 at Position(xpos = 640, ypos = 769)
                                            dia "...But you're my {b}nephew{/b}!"
                                            show auntsex 16
                                            player_name "..."
                                            dia "Hmm..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "Alright."
                                            show auntsex 22 at Position(xpos = 707, ypos = 769)
                                            dia "But we have to use {b}protection{/b}!"
                                            hide playersex
                                            show auntsex 5 at Position(xpos = 522, ypos = 769)
                                            pause
                                            show auntsex 6
                                            window hide
                                            pause
                                            show playersex 3 at Position(xpos = 350, ypos = 768)
                                            show expression "characters/player/char_player_sex_05.png" at Position(xpos = 488, ypos = 601)
                                            show auntsex 14 at Position(xpos = 704, ypos = 769)
                                            dia "All ready?"
                                            show auntsex 24 at Position(xpos = 707, ypos = 769) with dissolve
                                            dia "Now, slide it in nice and slow..."
                                            hide playersex
                                            hide expression "characters/player/char_player_sex_05.png"
                                            show auntsex 29 at Position(xpos = 579, ypos = 769)
                                            dia "There we go..."
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            dia "Deeper..."
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            dia "Yes! Just like that..."
                                            $ M_aunt.set('sex speed', .4)
                                            $ xray = 0
                                            label aunt_sex_loop:
                                                show screen aunt_sex_xray_buttons
                                                pause
                                                if anim_toggle:
                                                    hide screen aunt_sex_xray
                                                    hide screen aunt_sex_xray_buttons
                                                    if xray_toggle:
                                                        hide auntsex
                                                        if condom_on:
                                                            show auntsex_xray 6_9 at Position(xpos = 686, ypos = 769)
                                                        else:

                                                            show auntsex_xray 6_7 at Position(xpos = 686, ypos = 769)
                                                    else:

                                                        hide auntsex_xray
                                                        show auntsex 30_31 at Position(xpos = 592, ypos = 769)
                                                    pause 8
                                                else:

                                                    show screen aunt_sex_xray
                                                    hide auntsex_xray
                                                    hide screen aunt_sex_xray_buttons
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                call screen aunt_sex_options

                                            label aunt_sex_cum_in:
                                                hide auntsex_xray
                                                show auntsex 28 at Position(xpos = 612, ypos = 769)
                                                if xray_toggle:
                                                    if condom_on:
                                                        show expression "characters/player/char_player_sex_10.png" at Position(xpos = 650, ypos = 610)
                                                    else:

                                                        show expression "characters/player/char_player_sex_08.png" at Position(xpos = 650, ypos = 610)
                                                with hpunch
                                                dia "AAahh!"
                                                hide expression "characters/player/char_player_sex_08.png"
                                                hide expression "characters/player/char_player_sex_10.png"
                                                show auntsex 24 at Position(xpos = 707, ypos = 769)
                                                show playersex 11 at Position(xpos = 275, ypos = 768)
                                                if condom_on:
                                                    show expression "characters/player/char_player_sex_12.png" at Position(xpos = 444, ypos = 617)
                                                else:

                                                    show expression "characters/player/char_player_sex_17.png" at Position(xpos = 570, ypos = 640)
                                                dia "..."
                                                show playersex 3
                                                if condom_on:
                                                    hide expression "characters/player/char_player_sex_12.png"
                                                    show expression "characters/player/char_player_sex_13.png" at Position(xpos = 418, ypos = 605)
                                                dia "That's a lot of cum..."
                                                if condom_on:
                                                    dia "Good thing we used protection!"
                                                show auntsex 23
                                                player_name "That felt so... Good!"
                                                show auntsex 24
                                                dia "Let's get cleaned up..."
                                                $ aunt_had_sex = True
                                                jump aunt_sex_end

                                            label aunt_sex_cum_out:
                                                hide auntsex_xray
                                                show auntsex 24 at Position(xpos = 707, ypos = 769)
                                                show playersex 11 at Position(xpos = 275, ypos = 768)
                                                show expression "characters/player/char_player_sex_14.png" at Position(xpos = 525, ypos = 584)
                                                window hide
                                                pause
                                                hide expression "characters/player/char_player_sex_14.png"
                                                show expression "characters/player/char_player_sex_15.png" at Position(xpos = 531, ypos = 584)
                                                window hide
                                                pause
                                                hide expression "characters/player/char_player_sex_15.png"
                                                show expression "characters/player/char_player_sex_16.png" at Position(xpos = 534, ypos = 588)
                                                dia "..."
                                                dia "I love that feeling..."
                                                dia "...Let's get cleaned up."
                                                $ aunt_had_sex = True
                                                jump aunt_sex_end
                                        "Do more.":

                                            show auntsex 13
                                            show playersex 3
                                            player_name "Can we do more?"
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "Hmmm..."
                                            show auntsex 35 at Position(xpos = 709, ypos = 769)
                                            dia "Here. Take this..."
                                            show auntsex 24 at Position(xpos = 707, ypos = 769)
                                            show playersex 18
                                            with dissolve
                                            dia "Go ahead..."
                                            hide playersex
                                            show auntsex 32_33 at Position(xpos = 535, ypos = 769)
                                            pause 2
                                            dia "Keep going..."
                                            pause 2
                                            dia "Faster!"
                                            window hide
                                            pause 2
                                            show auntsex 34 at Position(xpos = 670, ypos = 769)
                                            show playersex 18 at Position(xpos = 350, ypos = 768) with hpunch
                                            dia "!!!"
                                            player_name "..."
                                            player_name "Are you okay?"
                                            show auntsex 24 at Position(xpos = 707, ypos = 769)
                                            dia "{b}*Panting*{/b}"
                                            dia "That was great... {b}[firstname]{/b}."
                    else:

                        show playersex 4 at Position(xpos = 350, ypos = 768)
                        pause
                        show playersex 3
                        pause
                        dia "I love feeling it..."
                        hide playersex
                        show auntsex 11_12 at Position(xpos = 621, ypos = 769)
                        pause 4
                        show playersex 3 at Position(xpos = 350, ypos = 768)
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "My turn."
                        show auntsex 3 at Position(xpos = 675, ypos = 769)
                        pause
                        show auntsex 4
                        pause
                        show auntsex 13 at Position(xpos = 709, ypos = 769)
                        player_name "Woa..."
                        show playersex 4
                        pause
                        show playersex 3
                        player_name "You're so pretty, Aunt Diane..."
                        show auntsex 14
                        dia "So, what would you like to do, now?"
                        $ anim_toggle = False
                        $ xray_toggle = False
                        $ M_aunt.set('sex speed', .4)
                        label dia_sex_options_2:
                            menu:
                                "Play with clit.":
                                    show auntsex 13
                                    player_name "Can I... Touch you?"
                                    show auntsex 14
                                    dia "Of course you can..."
                                    dia "But only with the tip..."
                                    hide playersex
                                    show auntsex 18 at Position(xpos = 626, ypos = 769)
                                    dia "Just like that..."
                                    show auntsex 19_20 at Position(xpos = 640, ypos = 769)
                                    pause 4
                                    show auntsex 21 at Position(xpos = 650, ypos = 769)
                                    dia "You like that?"
                                    show auntsex 20 at Position(xpos = 640, ypos = 769)
                                    player_name "Yeah..."
                                    show auntsex 15 at Position(xpos = 709, ypos = 769)
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    player_name "I... Want more..."
                                    show auntsex 14
                                    dia "What would you like now?"
                                    jump dia_sex_options_2
                                "Play with vegetable.":

                                    show playersex 3
                                    show auntsex 35 at Position(xpos = 709, ypos = 769)
                                    dia "Here. Take this..."
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    show playersex 18
                                    with dissolve
                                    dia "Go ahead..."
                                    hide playersex
                                    show auntsex 32_33 at Position(xpos = 535, ypos = 769)
                                    pause 2
                                    dia "Keep going..."
                                    pause 2
                                    dia "Faster!"
                                    window hide
                                    pause 2
                                    show auntsex 34 at Position(xpos = 670, ypos = 769)
                                    show playersex 18 at Position(xpos = 350, ypos = 768) with hpunch
                                    dia "!!!"
                                    player_name "..."
                                    player_name "Are you okay?"
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    dia "{b}*Panting*{/b}"
                                    dia "That was great... {b}[firstname]{/b}."
                                    dia "Would you like to do something else?"
                                    jump dia_sex_options_2
                                "Fuck raw.":

                                    $ condom_on = False
                                    show auntsex 13
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    player_name "I... I want to be inside you Aunt Diane."
                                    show auntsex 14
                                    dia "Alright."
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    dia "Now, slide it in nice and slow..."
                                    hide playersex
                                    show auntsex 25 at Position(xpos = 579, ypos = 769)
                                    dia "There we go..."
                                    show auntsex 26 at Position(xpos = 592, ypos = 769)
                                    dia "Deeper..."
                                    show auntsex 27 at Position(xpos = 608, ypos = 769)
                                    dia "Yes! Just like that..."
                                    $ xray = 0
                                    label aunt_sex_loop_2:
                                        show screen aunt_sex_xray_buttons
                                        pause
                                        if anim_toggle:
                                            hide screen aunt_sex_xray
                                            hide screen aunt_sex_xray_buttons
                                            if xray_toggle:
                                                hide auntsex
                                                show auntsex_xray 6_7 at Position(xpos = 686, ypos = 769)
                                            else:

                                                hide auntsex_xray
                                                show auntsex 26_27 at Position(xpos = 592, ypos = 769)
                                            pause 8
                                        else:

                                            show screen aunt_sex_xray
                                            hide auntsex_xray
                                            hide screen aunt_sex_xray_buttons
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                        call screen aunt_sex_options
                                "Fuck with condom.":

                                    $ condom_on = True
                                    show auntsex 13
                                    player_name "I... I want to be inside you Aunt Diane."
                                    show auntsex 14
                                    dia "All right."
                                    show auntsex 22 at Position(xpos = 707, ypos = 769)
                                    dia "But we have to use {b}protection{/b}!"
                                    hide playersex
                                    show auntsex 5 at Position(xpos = 522, ypos = 769)
                                    pause
                                    show auntsex 6
                                    window hide
                                    pause
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    show expression "characters/player/char_player_sex_05.png" at Position(xpos = 488, ypos = 601)
                                    show auntsex 14 at Position(xpos = 704, ypos = 769)
                                    dia "All ready?"
                                    show auntsex 24 at Position(xpos = 707, ypos = 769) with dissolve
                                    dia "Now, slide it in nice and slow..."
                                    hide playersex
                                    hide expression "characters/player/char_player_sex_05.png"
                                    show auntsex 29 at Position(xpos = 579, ypos = 769)
                                    dia "There we go..."
                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                    dia "Deeper..."
                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                    dia "Yes! Just like that..."
                                    $ anim_toggle = False
                                    $ xray_toggle = False
                                    $ xray = 0
                                    label aunt_sex_loop_3:
                                        show screen aunt_sex_xray_buttons
                                        pause
                                        if anim_toggle:
                                            hide screen aunt_sex_xray
                                            hide screen aunt_sex_xray_buttons
                                            if xray_toggle == True:
                                                hide auntsex
                                                show auntsex_xray 6_9 at Position(xpos = 686, ypos = 769)
                                            else:

                                                hide auntsex_xray
                                                show auntsex 30_31 at Position(xpos = 592, ypos = 769)
                                            pause 8
                                        else:

                                            show screen aunt_sex_xray
                                            hide auntsex_xray
                                            hide screen aunt_sex_xray_buttons
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                        call screen aunt_sex_options

                    label aunt_sex_end:
                        scene blank with dissolve
                        if not aunt_had_sex:
                            scene dianekitchen with dissolve
                            show player 29 at left with dissolve
                            show aunt 88 at right with dissolve
                            player_name "That was... Really good!"
                            show player 13
                            show aunt 89
                            dia "You liked it?"
                            show aunt 88
                            show player 21
                            player_name "Oh, yes..."
                            show player 29
                            player_name "I did okay?"
                            show aunt 87
                            show player 13
                            dia "You're doing very well, for a young man."
                            show aunt 89
                            dia "I hope you come back soon..."
                            show player 11
                            dia "Especially after school, when you need to release all that stress!"
                            show aunt 88
                            show player 17
                            player_name "I'd love to."
                            show aunt 89
                            show player 13
                            dia "It's getting late. You should probably get going..."
                            show aunt 87
                            dia "You don't want to keep your mom waiting!"
                            show aunt 88
                            show player 17
                            player_name "Yeah."
                            show aunt 89
                            show player 11
                            dia "Remember... We have to keep this our little secret."
                            show aunt 88
                            show player 21
                            player_name "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone."
                            show player 13
                            show aunt 90
                            dia "That's my handsome boy!"
                            hide player
                            show aunt 111 at left
                            dia "We're gonna have a lot of {b}fun{/b} together..."
                            $ gTimer.tick()
                            $ callScreen(location_count)
                            with dissolve
                        else:

                            scene dianekitchen with dissolve
                            show player 29 at left with dissolve
                            show aunt 88 at right with dissolve
                            player_name "That was... Really good!"
                            show player 13
                            show aunt 89
                            dia "You liked it?"
                            show aunt 88
                            show player 21
                            player_name "Oh, yes..."
                            show player 29
                            player_name "I did okay?"
                            show aunt 87
                            show player 13
                            dia "You're doing very well, for a young man."
                            show aunt 89
                            dia "Maybe you could help me with my {b}milking{/b} some day..."
                            show aunt 88
                            show player 17
                            player_name "I'd love to."
                            show aunt 89
                            show player 13
                            dia "Well, I usually work on my milk cartons {b}at night{/b}, in the {b}shed{/b}."
                            dia "You'd have to come visit me then. I'll be waiting for you."
                            show aunt 88
                            show player 17
                            player_name "Sure. I always wanted to know how you made all that milk!"
                            show aunt 89
                            show player 13
                            dia "It's getting late. You should probably get going..."
                            show aunt 87
                            dia "You don't want to keep your mom waiting!"
                            show aunt 88
                            show player 17
                            player_name "Yeah."
                            show aunt 89
                            show player 11
                            dia "Remember... We have to keep this our little secret."
                            show aunt 88
                            show player 21
                            player_name "Don't worry, {b}Aunt Diane{/b}, I won't tell anyone."
                            show player 13
                            show aunt 90
                            dia "That's my handsome boy!"
                            hide player
                            show aunt 111 at left
                            dia "We're gonna have a lot of {b}fun{/b} together..."
                            if milking_unlocked == False:
                                show unlock28 at truecenter with dissolve
                                pause
                                hide unlock28 with dissolve
                                $ milking_unlocked = True
                            $ gTimer.tick()
                            $ callScreen(location_count)
                            with dissolve
                "I should go.":

                    show aunt 88 at right
                    show player 21 at left
                    player_name "I'd love to stay in here with you..."
                    show aunt 91
                    show player 10
                    player_name "But I have to get started on the garden..."
                    show aunt 92
                    show player 13
                    dia "That's too bad."
                    dia "I was looking forward to spending time with you..."
                    show aunt 91
                    show player 10
                    player_name "I'm sorry. Maybe another time?"
                    show aunt 87
                    show player 11
                    dia "Any time. Your {b}Aunt{/b} is always hungry..."
                    show aunt 88
                    show player 17
                    player_name "Oh. Haha..."
                    show aunt 87
                    show player 13
                    dia "I'll be waiting!"
                    hide player 13 at left with dissolve
                    hide aunt 11 at right with dissolve
    $ callScreen(location_count)

label job_done_dialogue:
    $ renpy.checkpoint()
    if quest10 in quest_list and quest10 not in completed_quests and annihilator in inventory.items:
        scene black with dissolve
        with Pause(0.5)

        show garden_event01 with dissolve
        show text "I began to spray the whole lot with green napalm...\n Emptied the entire can of spray on the scattering vermin...\n Until none was spared!" at Position (xpos= 512, ypos = 700) with dissolve
        $ inventory.items.remove(annihilator)
        if exterminator in inventory.items:
            $ inventory.items.remove(exterminator)

        if eradicator in inventory.items:
            $ inventory.items.remove(eradicator)
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        hide garden_event01
        scene black
        with Dissolve(0.5)
        show unlock27 at truecenter with dissolve
        $ renpy.pause()
        $ infestation_done = True
        hide unlock27 with dissolve
        hide black
        $ callScreen(location_count)

    if not garden_firsttime:
        scene black
        with Pause(0.5)

        show garden_firsttime_01 with dissolve
        show text "Aunt Diane went to lay down in the yard and I began to clean up her garden.\n It was so hot outside... And there was so many weeds and bugs!\n But I finally got around doing it all, which took a good while to do...\n Good thing I was holding the shovel the right way!" at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show garden_firsttime_02 with dissolve
        show text "I noticed something odd while I was working...\n I could sense Aunt Diane watching me the whole time!\n She wouldn't say anything, and just look at me in a strange way...\n She must have been tired or something." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        hide garden_firsttime_01
        hide garden_firsttime_02 with dissolve
        scene black with dissolve
        with Pause(0.5)
        $ garden_firsttime = True
    if quest10 in quest_list and quest10 not in completed_quests:
        scene garden_dead
    else:

        scene garden
    if earnings > 0:
        show player 1 at left with dissolve
        show aunt 2 at right with dissolve
        dia "Oh, wow! My garden looks absolutely gorgeous, {b}[firstname]{/b}!"
        show player 1 at left
        show aunt 9 at right
        player_name "Yeah... I had to get rid of a lot of stuff..."
        show aunt 15 at right
        show player 11 at left
        dia "Just look at that big, hard cucumber!"
        show aunt 16 at right
        player_name "..."
        show aunt 5 at right
        show player 13 at left
        dia "Thanks, Handsome! And come back soon!"
        hide player 13 at left with dissolve
        hide aunt 5 at right with dissolve
    else:

        show player 5 at left with dissolve
        show aunt 23 at right with dissolve
        dia "Hmm... There's some room for improvement."
        show aunt 24 at right
        show player 24 at left
        player_name "Yeah... I didn't do too well. Sorry {b}Aunt Diane{/b}!"
        show aunt 3 at right
        show player 13 at left
        dia "It's okay... You're new at this..."
        show aunt 2 at right
        dia "And I'm sure you'll get better at it!"
        dia "Your Aunt always needs fresh vegetables..."
        show aunt 1 at right
        show player 10 at left
        player_name "I guess so..."
        show aunt 14 at right
        show player 11 at left
        dia "Just make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
        show aunt 1 at right
        show player 13 at left
        player_name "I'll do better next time..."
        player_name "Thanks {b}Aunt Diane{/b}!"
        hide player 13 at left with dissolve
        hide aunt 1 at right with dissolve
    $ gTimer.tick()
    $ bad_garden_count = 0
    if earnings < 0:
        $ earnings = 0
    $ inventory.money += earnings
    $ after_minigame = True
    $ garden_done += 1
    show unlock7 at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide unlock7
    with dissolve
    $ in_garden = True
    jump garden_dialogue

label night_closed_garden:
    if quest10 in quest_list and quest10 not in completed_quests:
        scene garden_dead_night
    else:

        scene garden_night
    show player 10 with dissolve
    if aunt_had_sex and not gTimer.is_night():
        player_name "{b}Aunt Diane{/b} said she would be in the {b}barn{/b}."
    else:

        player_name "{b}Aunt Diane{/b} is probably asleep... I don't think I can work on the garden right now."
    hide player 2 with dissolve
    $ callScreen(location_count)

screen garden_minigame:
    timer 0.01 repeat True action If(
        time_count > 0,
        true=SetVariable("time_count", time_count - 0.01),
        false=[Hide("garden_minigame"), Jump("job_done_dialogue")]
    )
    add "backgrounds/minigame01_bg01.jpg"
    $ pos_index = 0
    for Good in t_list:
        $ pic = Good.image
        $ i_passive = Good.passive
        if not Good.passive:
            imagebutton:
                idle pic
                hover pic
                pos valid_pos[pos_index]
                action [If(
                    not Good.status,
                    SetVariable("earnings", earnings + Good.price),
                    [If(
                        earnings - Good.price < 0,
                        SetVariable("earnings", 0),
                        SetVariable("earnings", earnings - Good.price)
                    )]
                 ),
                        Play("audio", "audio/sfx_splat.ogg"),
                        Function(Good.change_passive),
                        If(
                            Good in bad_list or Good in rotten_t_list,
                            SetVariable("bad_garden_count", bad_garden_count + 1),
                            NullAction()
                        ),
                        If(
                            bad_garden_count == bad_garden_number,
                            Jump("job_done_dialogue"),
                            NullAction()
                        )
                ]
        else:
            add Good.passive_pic pos valid_pos[pos_index]
        $ pos_index += 1
    text "[bad_garden_count]"
    text "{b}[earnings]{/b}" pos 155,672 size 35 xalign 0.5
    bar value time_count range timer_range pos 260,685 xmaximum 513 ymaximum 33 style "time_bar"

label garden_listing:
    $ bad_garden_count = 0
    if quest10 in quest_list and quest10 not in completed_quests and not infestation_done:
        $ renpy.random.shuffle(rotten_list)
        $ t_list=[earwig01, earwig02, earwig03, rotten_list[0], rotten_list[1], rotten_list[3]]
        $ bad_garden_number = 5
        $ renpy.random.shuffle(t_list)
        $ renpy.random.shuffle(valid_pos)
        $ time_count = 3
        $ timer_range = 3
        $ style.time_bar.left_bar = "buttons/bar_full.png"
        $ style.time_bar.right_bar = "buttons/bar_empty.png"
        $ rotten_good_reset()
        $ earwig01.passive = False
        $ earwig02.passive = False
        $ earwig03.passive = False
        $ earnings = 0
        call screen garden_minigame
    else:

        $ t_list=item_list[:]
        $ renpy.random.shuffle(t_list)
        $ renpy.random.shuffle(valid_pos)
        $ bad_garden_number = len(bad_list) - 1
        $ time_count = 3
        $ timer_range = 3
        $ style.time_bar.left_bar = "buttons/bar_full.png"
        $ style.time_bar.right_bar = "buttons/bar_empty.png"
        $ good_reset()
        $ earnings = 0
        call screen garden_minigame

label drink_offered:
    scene garden
    if aunt_drink_made:
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "I should give {b}Aunt Diane{/b} her {b}drink{/b} before I get back to work..."
    $ callScreen(location_count)

label aunt_masturbate:
    if not aunt_masturbating_seen:
        show aunt_masturbate 1_2
        player_name "!!!"
        player_name "( ...Aunt Diane... What is she... )"
        window hide
        pause 2
        player_name "( WOW... )"
        player_name "( She's playing with her vegetables... )"
        player_name "( A whole cucumber! )"
        player_name "( ... )"
        player_name "( ...I should leave before I get caught. )"
        scene garden
        with dissolve
        show player 113 with dissolve
        player_name "I can't believe what I just saw..."
        show player 114
        player_name "( I didn't think Aunt Diane would be so... Horny... )"
        show player 113
        player_name "Is that why she wants all those vegetables?"
        show player 109f
        player_name "Hmm..."
        show player 108f
        player_name "I guess she has been lonely lately..."
        player_name "I should get back to work, and pretend as if I didn't see anything..."
        $ ui_lock_count = 0
        $ aunt_masturbating_seen = True
        hide player 108f with dissolve
    $ aunt_dialogue_advance = True
    $ callScreen(location_count)

label before_masturbation:
    scene garden
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "I should find out if Aunt Diane is home first."
    $ callScreen(location_count)

label after_masturbation:
    scene garden
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Maybe not right now."
    $ callScreen(location_count)

label aunt_kitchen_faster_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') - 0.1)
    if not aunt_had_sex:
        jump aunt_sex_loop
    elif aunt_had_sex and not condom_on:
        jump aunt_sex_loop_2
    elif aunt_had_sex and condom_on:
        jump aunt_sex_loop_3

label aunt_kitchen_slower_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') + 0.1)
    if not aunt_had_sex:
        jump aunt_sex_loop
    elif aunt_had_sex and not condom_on:
        jump aunt_sex_loop_2
    elif aunt_had_sex and condom_on:
        jump aunt_sex_loop_3