label erik_button_dialogue:
    if not erik.known(erik_card_hunt):
        jump erik_card_hunt
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        jump erik_orcette
    if is_here("june"):
        scene expression "backgrounds/location_erik_house_bedroom_bed_june.jpg" with hpunch
        player_name "!!!"
        $ location_count = "Erik's House Entrance"
        $ erik_funky = True
        jump erik_funky_block
    if location_count == "Erik's Basement":
        scene location_erik_basement01_closeup
    elif location_count == "Erik's Room":
        if erik.started(erik_gf):
            scene expression gTimer.image("erik_house_bedroom{}_b")
            show player 14
            with dissolve
            player_name "He looks so happy now."
            show player 17
            player_name "I should go tell {b}Mrs. Johnson{/b} the good news!"
            hide player with dissolve
            $ callScreen(location_count)

        elif erik.in_progress(erik_gf_stolen):
            scene expression gTimer.image("erik_house_bedroom{}_b")
            show player 10
            with dissolve
            player_name "He's probably not in the best mood right now..."
            player_name "I'll talk to him tomorrow."
            hide player with dissolve
            $ callScreen(location_count)
        scene expression gTimer.image("eriks_room{}_c")
    show player 2 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Hey {b}Erik{/b}!"
    show player 1 at left
    show erik 5 at right
    eri "Hey {b}[firstname]{/b}! What's up?"
    label erik_talk:
        menu:
            "Cards." if erik.started(erik_card_hunt):
                jump erik_cards

            "Cock Crown of Thorns." if erik.started(erik_crown_card):
                jump erik_crown_card

            "The package." if erik.started(erik_orcette) or erik.started(erik_orcette_2):
                jump erik_package

            "VR Headset." if erik.started(erik_vr):
                jump erik_vr_game

            "Sex education." if mrsj.started(mrsj_sex_ed):
                show erik 1 at right
                show player 12 at left
                player_name "What did your mom want us to get again?"
                show player 5
                show erik 5
                eri "Hmm... I think she wants us to get {b}pills so she won't get pregnant{/b}."
                eri "And that book? The one about sex positions..."
                show erik 1
                show player 35
                player_name "Yeah, something about {b}Kama Sutra{/b}?"
                show player 34
                show erik 5
                eri "I think so."
                show erik 1
                show player 14
                player_name "Alright."
                hide player
                hide erik
                with dissolve

            "Girlfriend." if June.completed(june_erik_help) and not erik.known(erik_gf):
                show player 14
                player_name "Dude, I got some great news for you!"
                show player 1
                show erik 5
                eri "Huh?"
                show player 14
                show erik 1
                player_name "So, I spoke to {b}June{/b}..."
                show erik 4
                eri "Oh yeah?"
                show player 14
                show erik 1
                player_name "Apparently, she likes to play this game called Orc Bork..."
                player_name "... and she's been looking to play it with someone!"
                show player 1
                show erik 4
                eri "Really?"
                show player 17
                show erik 1
                player_name "Yup!"
                show player 14
                player_name "I even told her about you!"
                player_name "I mentioned your name and how you could help her beat the game she's been playing."
                show player 1
                show erik 4
                eri "Woah..."
                show erik 1
                show player 17
                player_name "You should go to school and talk to her!"
                show player 1
                show erik 4
                eri "Yeah... I should!"
                show player 14
                show erik 1
                player_name "Anyway, It's going to be great, you'll see!"
                show player 1
                show erik 4
                eri "Thanks, [firstname]."
                show player 14
                show erik 1
                player_name "I'll talk to you later, then."
                hide player
                hide erik
                $ erik.add_event(erik_gf)

            "Girlfriend." if June.completed(june_mc_help) and not erik.known(erik_gf_stolen):
                show erik 1 at right
                show player 10 at left
                player_name "{b}Erik{/b}, about {b}June{/b}..."
                show player 5
                show erik 5
                eri "Yeah?"
                show player 10
                show erik 2
                player_name "Well, I don't think it's going to work out..."
                show player 5
                show erik 3b
                eri "Why? What happened?"
                show player 10
                show erik 3c
                player_name "Well, we spoke for a while..."
                show player 5
                show erik 3
                eri "And?"
                show player 10
                show erik 3c
                player_name "I just don't think she's that interested..."
                show player 5
                show erik 3
                eri "Oh..."
                show erik 3b
                eri "It's alright."
                eri "I knew she wouldn't want to anyway..."
                show player 10
                show erik 3b
                player_name "She, uh... she might be coming over to my house later."
                show player 5
                show erik 5
                eri "What?!"
                show player 10
                show erik 3c
                player_name "I'm sorry!"
                player_name "While I was talking to her, one thing led to another..."
                player_name "We're just going to hang out..."
                show player 5
                eri "..."
                player_name "..."
                show player 10
                player_name "I'll, uh, talk to you later, then."
                hide player
                hide erik
                with dissolve
                $ erik.add_event(erik_gf_stolen)
                $ erik_gf_stolen.finish()

            "Girlfriend." if June.completed(june_intro) and not June.known(june_intro_2):
                show player 14 at left
                show erik 1 at right
                player_name "Hey, who's that girl you said you like again?"
                show erik 4
                show player 1
                eri "{b}June{/b}?"
                show player 14
                show erik 1
                player_name "Yeah, where does she hang around?"
                show player 1
                show erik 4
                eri "She usually spends her time at {b}school{/b} in the {b}computer room{/b} on the second floor..."
                show player 14
                show erik 1
                player_name "Ah, okay!"
                player_name "I'll see what I can do."
                show player 1
                $ June.add_event(june_intro_2)
                jump erik_talk

            "Message from your Dad." if erik.started(erik_father_forgive):
                show erik 52 at right
                show player 10 at left
                player_name "I was at the Police station not too long ago..."
                show player 5
                show erik 5
                eri "Oh yeah?"
                show erik 52
                show player 10
                player_name "I saw your dad."
                show player 11
                show erik 3b
                eri "Ugh. I don't really want to think about him..."
                show erik 52
                show player 10
                player_name "Well, he's still locked up, and he actually saw me when I was there..."
                show player 5
                show erik 53
                eri "Oh yeah? Did he say anything to you?"
                show erik 52
                show player 10
                player_name "He wants you to know that he's sorry about everything..."
                player_name "...And hopefully, you will forgive him so he can see you again one day."
                show player 11
                show erik 2
                eri "..."
                show erik 3
                show player 5
                eri "I see..."
                show erik 3b
                show player 13
                eri "Thanks for telling me that, {b}[firstname]{/b}."
                show erik 52
                show player 14
                player_name "No problem, {b}Erik{/b}."
                hide player
                hide erik
                with dissolve
                $ erik_father_forgive.finish()

            "Your Mom." if erik.over(erik_breastfeeding_2) and not erik.completed(erik_path_split):
                if mrsj.completed(mrsj_poker_night_2) and not erik.known(erik_path_split):
                    show player 14 at left
                    show erik 1 at right
                    player_name "Hey, you know that thing we did with your mom after the poker game?"
                    show erik 3
                    show player 11
                    eri "Oh, yeah..."
                    show erik 3b
                    eri "I hope you don't think my mom is crazy or anything..."
                    show erik 1
                    show player 14
                    player_name "No, of course not!"
                    show player 17
                    player_name "I think she's awesome!"
                    show player 14
                    player_name "But... I just wanted to be sure that you were okay with it, you know?"
                    show erik 7
                    show player 1
                    eri "It's fine, really."
                    show erik 5
                    eri "She's always been very touchy with me."
                    eri "I've never been close to other girls."
                    show player 4
                    eri "I think she does it because she feels bad about me being alone all the time..."
                    show erik 1
                    show player 14
                    player_name "How about a girlfriend?"
                    show erik 3
                    show player 11
                    eri "Who would want to hook up with me?"
                    show erik 3b
                    eri "I'm terrible at talking to girls..."
                    show erik 2
                    show player 5
                    eri "*Sigh*"
                    show player 14
                    player_name "Maybe someone from school you have things in common with?"
                    show erik 3b
                    show player 1
                    eri "I guess..."
                    show erik 1
                    show player 14
                    player_name "Would you prefer do stuff with your mom?"
                    show erik 5
                    show player 1
                    eri "Like what?"
                    show erik 1
                    show player 14
                    player_name "Like... sex? Have you thought about it?"
                    show erik 5
                    show player 1
                    eri "Seems easier... she already gives me lots of attention."
                    show erik 1
                    show player 14
                    player_name "Oh, yeah? What do you mean?"
                    show erik 5
                    show player 11
                    eri "Like touching me... letting me play with her..."
                    eri "Something like what we did after the poker game."
                    show erik 1
                    show player 10
                    player_name "I knew you were breastfeeding, but I didn't know you were going that far."
                    show erik 4
                    show player 11
                    eri "I think she likes it."
                    show erik 1
                    show player 14
                    player_name "Do you think she would do more with us?"
                    show erik 5
                    show player 4
                    eri "I don't know... Maybe?"
                    show erik 1
                    show player 14
                    player_name "We could always talk to your mom about it?"
                    show erik 5
                    show player 1
                    eri "I don't know if we should..."
                    show erik 1
                    show player 14
                    player_name "Why not?"
                    player_name "Maybe she wants to..."
                    show erik 5
                    show player 1
                    eri "Maybe?"
                    show erik 1
                    show player 4
                    player_name "Hmm..."
                    show erik 4
                    show player 1
                    eri "Do you think you could ask her?"
                    show erik 1
                    show player 23
                    player_name "Me?!"
                    show erik 4
                    show player 11
                    eri "Yeah!"
                    eri "It's pretty awkward for me to ask, you know?"
                    show erik 1
                    show player 29 at Position(xoffset=8)
                    player_name "I'll' try to bring it up and see what she says..."
                    show player 1
                    $ erik.add_event(erik_path_split)
                    jump erik_talk

                elif erik.started(erik_path_split):
                    show player 14 at left
                    show erik 1 at right
                    player_name "What should I ask your mom again?"
                    show erik 5
                    show player 1
                    eri "Find out if she wants to do more stuff with us?"
                    show player 14 at left
                    show erik 1
                    player_name "Oh, right."
                    player_name "I'll let you know once I talk to her."
                    show player 1
                    show erik 1
                    jump erik_talk
                else:

                    show erik 1 at right
                    show player 10 at left
                    player_name "I didn't know you and your mom were...so close."
                    show player 5
                    show erik 3
                    eri "It's weird, I know..."
                    show erik 2 with dissolve
                    show player 12
                    player_name "No, not at all!"
                    show player 10
                    player_name "I...I think it's cool!"
                    show player 13
                    show erik 3b with dissolve
                    eri "..."
                    show player 29 with dissolve
                    player_name "I mean...your mom is like...really hot!"
                    player_name "I think you're kind of lucky..."
                    show player 13 with dissolve
                    show erik 3
                    eri "I guess so."
                    show player 12
                    player_name "You guys do...anything else together?"
                    show player 11
                    show erik 5
                    eri "...NO!!"
                    show erik 3
                    eri "She just, you know, let's me touch her a lot..."
                    show erik 3b
                    show player 23
                    player_name "Really?!"
                    player_name "Like...her whole body?"
                    show player 14
                    show erik 5
                    eri "Well, sort of."
                    show erik 50
                    show player 12
                    player_name "Don't you like it?"
                    show player 13
                    show erik 5
                    eri "Of course!"
                    eri "It's just that...it's my mom, you know?"
                    show erik 50
                    show player 33
                    player_name "I guess, yeah."
                    show player 13
                    show erik 5
                    eri "Just...please don't tell anyone alright?"
                    show erik 50
                    show player 14
                    player_name "{b}Erik{/b}, you're my best friend."
                    player_name "I'll keep this between us."
                    player_name "I was just a little...surprised, you know?"
                    show player 13
                    show erik 5
                    eri "Thanks, [firstname]. You're a good friend."
                    hide player
                    hide erik
                    with dissolve

            "I have the game!" if erik.completed(erik_favor) and game in inventory.items and not erik.known(erik_favor_2):
                show erik 1 at right
                show player 17 at left
                player_name "I have it!"
                show erik 4 at right
                show player 1 at left
                eri "Oh yeah?"
                show erik 1 at right
                show player 33 at left
                player_name "A band new copy of {b}Sea Dogs SAGA{/b}!"
                show player 239_240
                pause
                show erik 4 at right
                show player 72 at left
                eri "No way!"
                show erik 8 at right
                show player 1 at left
                eri "Thanks, {b}[firstname]{/b}!"
                show erik 9 at right
                show player 14 at left
                player_name "Sooo... Are you gonna talk to Kevin?"
                show erik 10 at right
                show player 1 at left
                eri "Yeah. I'll take over his cafeteria duties."
                show erik 9 at right
                show player 36 at left
                player_name "Great! Thanks {b}Erik{/b}!"
                $ inventory.items.remove(game)
                $ erik.add_event(erik_favor_2)
                jump erik_talk

            "I need a favor." if erik.started(erik_favor):
                show erik 1 at right
                show player 29 at left
                player_name "I need a favor favor, actually!"
                show erik 5 at right
                show player 13 at left
                eri "Oh yeah?"
                eri "What is it?"
                show erik 1 at right
                show player 14 at left
                player_name "Well, you know {b}Kevin{/b} from {b}school{/b}?"
                show erik 5 at right
                show player 1 at left
                eri "Sort of..."
                show erik 1 at right
                show player 17 at left
                player_name "Ok, well. He's on cafeteria duty for another two months..."
                player_name "...And he really needs a replacement."
                show erik 2 at right
                show player 11 at left
                eri "Ugh. I {b}HATE{/b} cafeteria duty..."
                show erik 3 at right
                show player 10 at left
                player_name "Look, you don't have to do it..."
                show player 14 at left
                player_name "...But if you do, I'll get you whatever you want!"
                player_name "Is there anything at all?"
                show erik 1 at right
                show player 1 at left
                eri "Hmm..."
                show erik 4 at right
                show player 11 at left
                eri "Well, you could get me this new game that just came out I guess..."
                show erik 1 at right
                show player 2 at left
                player_name "What's it called?"
                show erik 4 at right
                show player 1 at left
                eri "It's called: {b}Sea Dogs SAGA{/b}"
                eri "...it's in store at {b}COSMIC CUMICS{/b} already..."
                show erik 1 at right
                show player 18 at left
                player_name "Ok! So if I get it, you'll do it?"
                show erik 3 at right
                show player 2 at left
                eri "Yeah... I guess."
                show erik 1 at right
                show player 14 at left
                player_name "Awesome!!!"
                $ erik_favor.finish()
                jump erik_talk
            "Where's your mom?":

                show erik 1 at right
                show player 35 at left
                player_name "Where's your mom?"
                show erik 5 at right
                show player 34 at left
                eri "My mom? ...Eh, she is normally at home except for during the afternoon.."
                show player 1 at left
                show erik 1 at right
                show player 14 at left
                player_name "Ah, I see."
                jump erik_talk
            "Not much.":

                show erik 1 at right
                show player 2 at left
                player_name "Oh, not much."
                show player 17 at left
                player_name "Just dropping by to say hi!"
                show erik 5 at right
                show player 1 at left
                eri "Is everything ok at home with you family?"
                show erik 1 at right
                show player 10 at left
                player_name "{b}Mom's{/b} been getting {b}weird phone calls{/b} but she say's everything's fine so..."
                show player 24 at left
                player_name "I think we'll be alright..."
                show erik 5 at right
                show player 13 at left
                eri "That's odd..."
                show erik 5 at right
                show player 24 at left
                player_name "Yeah, I know..."
                show player 36 at left
                player_name "Anyway, I better get going."
                show erik 7 at right
                eri "Alright, then. See ya!"
                hide player 36 at left with dissolve
                hide erik 7 at right with dissolve
                hide erik_indoors

            "I need help." if webcam_quest and not erik_helped_with_camera:
                show player 29 at left
                show erik 1 at right
                player_name "By the way... I need help with something tonight..."
                show erik 5
                eri "Oh yeah? What is it?"
                show player 21
                show erik 1
                player_name "It's gonna sound a bit crazy, but I need help sneak into school tonight..."
                show player 13
                show erik 5
                eri "What?"
                eri "...But why?"
                show player 10
                show erik 1
                player_name "All you need to know is this will help me catch up with school..."
                show player 108f
                player_name "...And I can't afford to fail, I really need to do it."
                show player 5
                show erik 3
                eri "Hmm..."
                eri "I don't know about this... Sounds like trouble."
                show player 10
                show erik 1
                player_name "Please?"
                show player 13
                show erik 5
                eri "I guess I can help..."
                show player 17
                show erik 1
                player_name "Sweet!!!"
                show player 14
                player_name "Alright, meet me at school tonight!"
                show player 1
                show erik 4
                eri "Okay."
                $ webcam_erik_help = True
                hide erik
                hide player
        $ callScreen(location_count)