default player_mail = []
default seen_garage_locked = False
default attic_key_taken = False
default shovel_taken = False
default stool_taken = False
default fishing_rod_taken = False
default ring_taken = False
default cheerleader_outfit_taken = False
default mom_helped = 0
default mrs_johnson_visit = False

label home_front:
    $ location_count = "Home Front"
    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if gTimer.is_dark():
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
        $ map_enter = False
        $ callScreen(location_count)
    else:


        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    if gTimer.gameDay() > 1 and not gTimer.is_dark() and not mrs_johnson_visit:
        scene home_front with None
        show mom 61f zorder 2 at left
        show erikmom 17 at right
        with dissolve
        if mom.name.lower() in ["mom", "mother",]:
            erimom "Hi!"
        else:
            erimom "Hey, {b}[mom]{/b}!"
        show mom 62f
        show erikmom 14
        mom "Oh, hello."
        show mom 61f
        show erikmom 17
        erimom "I wanted to stop by and give my condolences for your loss..."
        show mom 62f
        show erikmom 14
        mom "Oh, thank you. That's very... thoughtful of you."
        show mom 125f
        show erikmom 19
        erimom "I just want you to know that me and my son are right next door if you ever need something."
        erimom "Or if you just need someone to talk to."
        show mom 63f
        show erikmom 14
        mom "That's very generous."
        show mom 125f
        show erikmom 17
        erimom "I know this is a completely different situation for you, but I can relate, you know?"
        show mom 63f
        show erikmom 14
        mom "You mean, because of your husband?"
        show mom 125f
        show erikmom 17
        erimom "Of course!"
        show erikmom 20
        erimom "I mean, my husband left me... so its a bit different."
        show erikmom 18
        erimom "But I had to be on my own for a long time!"
        show mom 63f
        show erikmom 14
        mom "Don't you feel lonely?"
        mom "Is it tough with just you and your son at home?"
        show mom 125f
        show erikmom 20
        erimom "Yeah... {b}Erik{/b} was sad when I had to tell him his dad wasn't coming home..."
        show erikmom 17
        erimom "... but don't worry!"
        erimom "There's ways to cheer boys up, you know? I've got some tricks for that too..."
        show mom 63f
        show erikmom 14
        mom "Oh, yeah? Like what?"
        show mom 125f
        show erikmom 17
        erimom "Girls like to talk and get emotional attention, but boys..."
        show mom 59f
        erimom "... you need to give them {b}physical{/b} attention!"
        show mom 125f
        erimom "You know... like hugs, cuddles and more motherly love!"
        show mom 63f
        show erikmom 14
        mom "I see..."
        show mom 125f
        show erikmom 18
        erimom "{b}Erik{/b} has been SO much better ever since I started catering to his... needs."
        show mom 63f
        show erikmom 14
        mom "I just don't know If I'm strong enough to get through all of this..."
        show mom 125f
        show erikmom 17
        erimom "Listen, honey. If I could do it, so can you."
        erimom "Focus on your children, that's what i did!"
        erimom "You have to think of what they want."
        show mom 63f
        show erikmom 14
        mom "I suppose you're right."
        show mom 125f
        pause
        show player 1 zorder 1 at Position(xpos=300) with dissolve
        show mom 62f
        mom "Oh! Hi, Sweetie!"
        show player 14
        player_name "Hey, {b}Mom{/b}... Hi, {b}Mrs. Johnson{/b}!"
        show player 1
        show erikmom 17
        erimom "Hello, {b}[firstname]{/b}."
        erimom "Your mom was just telling me how much she cares about you..."
        show erikmom 14
        show player 14
        player_name "Oh, heh..."
        show erikmom 17
        show player 13
        erimom "She loves you very much, so you better take good care of her!"
        show erikmom 14
        show player 14
        player_name "Uhh... Of course."
        show player 1
        show erikmom 17
        erimom "..."
        erimom "Well, I'll let you two head back home..."
        show erikmom 14
        mom "You sure you don't want to come in?"
        show erikmom 17
        erimom "No, it's fine! I should really get home. {b}Erik{/b} needs help with... something."
        show erikmom 14
        mom "Well, in any case, thanks for the chat! Come back any time!"
        show erikmom 17
        erimom "Oh, I will honey! Hang in there..."
        $ mrs_johnson_visit = True
        hide player
        hide mom
        hide erikmom

    elif quest14 in quest_list and quest14_1 and not quest14_2 and quest14 not in completed_quests and not player.known(lawn_mowed):
        $ player.add_event(lawn_mowed)
        scene black
        with Pause(0.5)
        show cutting_grass_01 with dissolve
        show text "This is a lot harder than I expected. I should've paid more attention to dad when he used to do it." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show cutting_grass_02 with dissolve
        show text "It doesn't look half bad. I Hope {b}Mom{/b} thinks the same." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        show cutting_grass_03 with dissolve
        show text "Huh, she's been standing there. I was so focused on cutting the grass, I didn't notice her come out." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        hide cutting_grass_01
        hide cutting_grass_02
        hide cutting_grass_03 with dissolve
        scene black with dissolve
        with Pause(0.5)

        scene home_front
        show player 2 at left
        show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
        show mom 1 at right
        with dissolve
        player_name "{b}Mom{/b}, I'm finished with the lawn."
        show player 203
        show mom 2
        mom "Wow! I don't know what to say, Sweetie!"
        show mom 3
        mom "The yard looks amazing!"
        show mom 2
        mom "You looked so grown up handling the lawnmower, too. It was really nice to see."
        show player 2
        show mom 1
        player_name "I was just doing it the way I thought dad would."
        show player 11
        show mom 2
        mom "And you did it as quickly and nicely as he used to."
        mom "You’ve gotten really strong, Sweetie."
        show player 21
        show mom 1
        player_name "I'm just glad I was able to do it. I want to be able to help you, mom."
        show player 2
        player_name "Should we go inside now?"
        show mom 1
        mom "Sure!"
        scene home_front with None
        show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
        show player 10 zorder 1
        with dissolve
        player_name "{b}*Panting*{/b}"
        show player 14
        player_name "Wow, that was a lot of work!"
        show player 24
        player_name "Man, I really got my clothes dirty..."
        show player 4 at Position(xoffset=5)
        player_name "I think {b}Mom's{/b} doing the laundry in the basement, maybe I can bring down my dirty clothes."
        hide player with dissolve

    elif mom_count >= 6 and henchmen_count == 1 and map_enter and mom_revealing_tommorow:

        scene home_front_car
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        show player 11 at left with dissolve
        player_name "!?"
        player_name "Whose car is that?"
        player_name "I've never seen it before..."
        hide player
        $ playSound()
        scene henchman_cs2 1
        with dissolve
        show text "I looked through the window, and saw the same man from last week.\n It looks like he brought a friend with him this time." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        scene henchman_cs2 2 with dissolve
        show text "I couldn't hear what they were saying, but {b}Mom{/b} looked terrified." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        play audio smack
        scene henchman_cs2 3 with hpunch
        show text "Suddenly, one of them hit her, knocking her to the floor..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "There was no way I could just stand there and watch...\nI {b}had{/b} to do something!" at Position (xpos= 512, ypos = 700)
        pause
        scene home_entrance_fight
        show mom 40 at Position(xpos=156,ypos=768)
        show henchman2 1 at right
        with dissolve
        player_name "{b}MOM{/b}!!"
        show player 205 at Position(xpos=350,ypos=768) with dissolve
        player_name "Are you okay??"
        show player 204
        mom "Yes, I’m fine..."
        show player 205
        player_name "What are you guys doing in our house?!"
        show player 204
        show henchman2 2
        henchman2 "Step aside, kid. This doesn't concern you."
        show player 205
        show henchman2 1
        player_name "If you touch her again I'm going to-"
        show player 204
        show henchman2 3
        henchman2 "I wouldn’t do that if I were you."
        show henchman2 1
        player_name "..."
        show player 205
        player_name "I'm calling the cops and you can deal with-"
        show player 204
        show henchman2 3
        hide mom with dissolve
        henchman2 "I don't think so."
        show henchman2 1
        hide player
        show henchman1 7 at Position(xpos=350,ypos=768) with hpunch
        player_name "Get off me!"
        show henchman1 8
        hide henchman2
        show henchman2 3 at right
        henchman2 "Easy, kid."
        henchman2 "Your family owes us a {b}LOT{/b} of money..."
        henchman2 "...And we're still waiting to get paid!"
        show henchman2 2
        henchman2 "As for the police..."
        show henchman1 9
        show henchman2 5
        with hpunch
        mom "{b}[firstname]{/b}!!!"
        show henchman2 3
        show henchman1 10 at Position(xpos=340,ypos=768)
        henchman2 "Call them, and we'll know..."
        show henchman2 2
        henchman2 "...long before they can do anything about it."
        henchman2 "Do what's best for your family and get us the money..."
        show henchman2 4
        henchman2 "Because there won't be another chance. {b}Got it{/b}?"
        show player 184
        show henchman1 6f at left
        show henchman2 2
        with vpunch
        henchman2 "Let's get out of here."
        $ playMusic()
        hide henchman1
        hide henchman2
        with dissolve
        pause
        hide player
        show mom 41 at left
        with dissolve
        mom "Easy, Sweetie. I've got you."
        show mom 44 at left
        show sis 39 at right
        with dissolve
        sis "What the hell is going on?"
        sis "I heard screams and-"
        show sis 40
        sis "!!!"
        sis "Oh my god, are you hurt??"
        show mom 43
        show sis 43
        mom "Don't worry. It's nothing..."
        mom "They left..."
        show mom 44
        show sis 39
        sis "Shouldn't we call someone??"
        show sis 43
        show mom 43
        mom "No... We can't..."
        show mom 44
        show sis 39
        sis "What do you mean?"
        sis "I think we could-"
        show sis 43
        show mom 45
        mom "NOT right now, {b}[sis]{/b}!"
        show mom 43
        mom "Just..."
        mom "Go upstairs. I'll deal with this."
        show mom 44
        show sis 39
        sis "I... Okay..."
        hide sis
        with dissolve
        show mom 41
        mom "Are you okay, Sweetie?"
        show mom 42
        player_name "Sorry. I couldn't stop them, {b}Mom{/b}..."
        show mom 41
        mom "That's okay. You were very brave!"
        mom "You wanted to protect us."
        show mom 42
        player_name "What do we do?"
        show mom 41
        mom "Don't worry about that; we'll be okay."
        show mom 42
        mom "..."
        show mom 41
        mom "How's your face?"
        show mom 42
        player_name "My nose hurts..."
        player_name "...and I made a mess."
        show mom 41
        mom "Come on, let's get you cleaned up."
        hide mom with dissolve
        $ henchmen_count = 2
        $ mother.add_event(mom_cuddling)
        $ mom_cuddling.finish()
        scene shower2
        show mom 39f at left
        show player 209f at right
        with dissolve
        mom "Looks like the bleeding stopped..."
        show mom 63f
        mom "You should take a shower, Sweetie."
        mom "It'll help with the swelling."
        show player 210
        mom "I'll go fetch you some clean clothes."
        show mom 38f
        hide mom
        hide player
        scene hallway
        show mom 38
        with fade
        mom "..."
        mom "( I feel like I should be in there with him... make sure he's okay. )"
        mom "( Maybe he just needs privacy... )"
        mom "( I'll just leave his clothes outside the door. )"
        pause
        show mom 125 with fastdissolve
        mom "( I can't believe he stood up to those men... for me. )"
        mom "( He's grown so quickly lately... )"
        mom "( ...in more ways than one. )"
        mom "( Maybe I should go in and check up on him. )"
        mom "( See if he needs any help... )"
        scene shower_closeup
        show moms 26 zorder 2
        with fade
        player_name "Shit... So that's what getting punched in the face feels like..."
        show moms 27 with dissolve
        pause
        show moms_b zorder 1 at Position(xpos=350,ypos=768) with dissolve
        pause
        hide moms_b
        show moms 28 at Position(xpos=487,ypos=768)
        with dissolve
        pause
        show moms 29 at Position(xpos=492,ypos=768)
        player_name "Man... Is my nose supposed to be this soft?"
        show moms 31 at Position(xpos=484,ypos=768) with vpunch
        player_name "{b}Mom{/b}??"
        player_name "Why are you-"
        show moms 30
        mom "It's okay, Sweetie..."
        mom "I'll help you wash."
        show moms 34
        mom "You deserve it, after what you did back there."
        show moms 37_36
        pause 4
        show moms 34
        mom "Have you been working out?"
        show moms 35
        player_name "Yeah."
        show moms 34
        mom "I never got the chance to see..."
        mom "You really have grown."
        show moms 36
        show moms 76 with dissolve
        show moms 41_76
        pause 4
        show moms 42 with dissolve
        mom "You need to wash down below as well, Sweetie."
        show moms 72
        player_name "{b}Mom{/b}, are you sure about this?"
        show moms 43
        mom "You're not the first man I showered with."
        show moms 44
        mom "Just relax..."
        show moms 45 with dissolve
        mom "I'll take care of it..."
        show moms 74
        player_name "Okay..."
        show moms 73_74
        pause 4
        show moms 73
        player_name "{b}Mom{/b}, I'm gonna..."
        show moms 46
        mom "It's okay, Sweetie, just let it go!"
        show moms 47 at Position(xpos=498,ypos=768)
        player_name "!!!"
        show white zorder 4 with dissolve
        show moms 47 at Position(xpos=498,ypos=768)
        show playersex 33 zorder 3 at Position(xpos=521,ypos=508)
        hide white with dissolve
        pause
        show moms 48
        hide playersex
        with dissolve
        mom "Wow, you had a lot in you..."
        show moms 44 at Position(xpos=484,ypos=768) with dissolve
        mom "There..."
        show moms 34 at Position(xpos=447,ypos=768) with dissolve
        mom "Isn't that better?"
        show moms 35 at Position(xpos=447,ypos=768)
        player_name "Yeah, thanks {b}Mom{/b}."
        show moms 34
        mom "Come on. I still see some blood on your face."
        scene shower2
        with fade
        show player 21 at left
        show mom 34 at right
        with dissolve
        player_name "Hey, {b}Mom{/b}..."
        player_name "Can we do this again later?"
        show player 1
        show mom 37 with dissolve
        pause
        show mom 36
        mom "Sure."
        show mom 35
        mom "But you {b}HAVE{/b} to make sure your sister doesn't see us."
        mom "I have to go clean up the mess downstairs..."
        show mom 36
        mom "Wait a minute or two before coming out of the bathroom."
        mom "I don't want her to suspect something..."
        show mom 32
        show player 33
        player_name "Don't worry about it."
        hide mom
        hide player
        with dissolve
        $ gTimer.tick()
        jump hallway_dialogue
    $ map_enter = False
    $ callScreen(location_count)

label home_entrance:
    $ location_count = "Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.started(erik_bullying):
        scene home_entrance
        show erikmom 19c at right with dissolve
        show player 10 at left with dissolve
        player_name "Is everything ok, {b}Mrs. Johnson{/b}?"
        show player 5
        show erikmom 19
        erimom "Sorry to disturb you this morning."
        show erikmom 52
        erimom "It's just... it's about {b}Erik{/b}."
        erimom "Has {b}Erik{/b} been having trouble lately at school?"
        show erikmom 19c
        show player 12
        player_name "Huh?"
        show player 35
        player_name "Not that I know of?"
        show player 10
        player_name "He usually does well at school..."
        show player 5
        show erikmom 20
        erimom "No. I'm not talking about grades."
        show erikmom 52
        erimom "Have the other kids in school been giving {b}Erik{/b} a hard time?"
        erimom "He's been asking to stay home instead of going to class."
        show erikmom 20
        erimom "I... I even saw him come home last week with bruises."
        show erikmom 19c
        show player 23
        player_name "!!!" with hpunch
        show player 12
        player_name "{b}Erik{/b} is pretty quiet at school."
        player_name "I've never seen him get involved in any kind of bad stuff."
        show player 5
        show erikmom 19
        erimom "Maybe, if a close friend stopped over to him see him, he'd be more willing to talk..."
        show erikmom 19c
        show player 10
        player_name "You want me to ask him?"
        show player 5
        show erikmom 19
        erimom "I just want what's best for him, and you're his only friend."
        show erikmom 19c
        show player 12
        player_name "Okay. I'll go see him."
        hide player
        hide erikmom
        with dissolve
        $ ui_lock_count = 0
        $ erik_bullying.finish()

    elif player.started(lawn_mowed):
        scene home_entrance
        show player 11 zorder 1 at left
        show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
        show sis 9 at right
        with dissolve
        sis "Eugh, what's that smell?!"
        show player 14
        show sis 10
        player_name "I was just outside mowing the lawn and-"
        show player 11
        show sis 9
        sis "That's disgusting! You're getting grass everywhere, you slob!"
        show player 12
        show sis 10
        player_name "I'm sorry. I was just trying to help {b}Mom{/b}."
        show player 11
        show sis 9
        sis "What's with you and doing things around the house all of a sudden?"
        sis "Are you trying to be {b}Mom's{/b} \"special boy\" or something?"
        show player 10
        show sis 10
        player_name "No! I'm just-"
        show player 11
        show sis 9
        sis "Don't act stupid! I know what you're doing!"
        hide sis with dissolve
        pause
        show player 12
        player_name "What's with her lately? She's so tense all the time..."
        show player 10
        player_name "Anyway... I should head down to the {b}basement{/b} to get all of this off me..."
        $ lawn_mowed.finish()
        hide player with dissolve

    elif player_room_count == 1 and not mom_phone_event01:
        scene expression gTimer.image("home_entrance{}")
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "Is that {b}Mom{/b} on the phone?"
        show player 12
        player_name "...She sounds like she's mad. Is she yelling?"
        show player 10
        player_name "I should go see if she's okay."
        hide player 5 with dissolve
        $ ui_lock_count = 1
        $ mom_phone_event01 = True

    elif mom_count == 3 and not mom_dialogue_advance and not gTimer.is_night() and henchmen_count == 0:
        scene home_entrance
        if not doorbell_rang:
            show player 1
            player_name "( Doorbell's ringing, someone's at the door. )"
            player_name "( Must be {b}Erik{/b} or something... )"
            hide player with dissolve
        scene henchman_cs1 2 with fade
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        show text "I was expecting to see {b}Erik{/b}, instead I saw a strange man...\nHe was wearing an all black suit coupled with a stern look that would put coach Bridget's to shame." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
        scene henchman_cs1 1
        show player 2 at left
        show henchman2 1 at right
        with dissolve
        player_name "Hi?"
        show henchman2 2
        show player 1
        henchman2 "Where's your {b}mother{/b}?"
        show henchman2 1
        show player 11
        player_name "..."
        show player 12
        player_name "Who's asking?"
        show player 11
        show henchman2 3
        henchman2 "It's personal matters, kid."
        show henchman2 1
        show player 12
        player_name "Well, she's kind of busy at the moment, so why don't you come another time."
        show henchman2 2
        show player 11
        henchman2 "Just give her this message will ya..."
        show henchman2 3
        henchman2 "She has one week left, or else."
        show henchman2 1
        show player 11
        player_name "..."
        show player 12
        player_name "Or else, what?"
        show player 11
        show henchman2 3
        henchman2 "Just give her the message."
        henchman2 "We'll be back..."
        show henchman2 1
        player_name "..."
        $ playMusic()
        hide henchman2
        with dissolve
        scene home_entrance
        show player 10 at left
        with fade
        player_name "( What was {b}that{/b} all about... )"

        show player 5
        show mom 62 at right with dissolve
        mom "Was someone at the door, Sweetie?"
        show player 10
        show mom 61
        player_name "Yeah, some strange guy in a black suit came by..."
        show player 5
        show mom 59
        mom "!!!"
        show player 11
        show mom 60
        mom "...What did he want?"
        show mom 59
        show player 10
        player_name "He said you had one week left, but refused to say why."
        show player 11
        show mom 60
        mom "It must be about..."
        mom "But I already paid off all the-"
        show mom 59
        mom "..."
        show player 10
        player_name "What is it?"
        show player 11
        show mom 60
        mom "It's nothing, Sweetie."
        show player 1
        show mom 62
        mom "They must've gotten the wrong address, that's all."
        $ henchmen_count = 1
        $ ui_lock_count = 0
        hide player
        hide mom
        with dissolve

    elif mom_count == 9 and not mom_dialogue_advance and gTimer.is_evening() and mom_revealing:
        scene home_entrance_night with None
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( There're weird voices coming from the kitchen... )"
        show player 12
        player_name "( ...I don't remember {b}Mom{/b} or {b}[sis]{/b} inviting anyone over... )"
        show player 10
        player_name "( I should go see if everything is okay. )"
        hide player 5 with dissolve

    elif sister.started(sis_couch01) and gTimer.is_evening():
        scene home_entrance_night with None
        show player 11
        with dissolve
        player_name "( What's that sound? )"
        player_name "( It sounds like the TV is on. )"
        show player 4 at Position(xpos=518)
        player_name "( Who could be watching TV this late? )"

    elif sister.started(sis_couch01) and gTimer.is_evening():
        scene home_entrance_night with None
        show player 26 with dissolve
        player_name "( That porno {b}Sis{/b} was watching was hot! I kind of feel like watching it, too... )"
        show player 33
        player_name "Hmm... Maybe {b}another night{/b}."
        hide player with dissolve

    elif sister.started(sis_couch03) and gTimer.is_evening():
        scene home_entrance_night with None
        show player 11
        with dissolve
        player_name "( What was that sound? )"
        jump home_livingroom_dialogue
    $ callScreen(location_count)

label home_garage:
    $ location_count = "Garage"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")
    $ callScreen(location_count)

label player_mailbox:
    $ location_count = "Mailbox"
    $ callScreen(location_count, False)

label player_mailbox_dialogue:
    $ location_count = "Mailbox"
    scene expression gTimer.image("player_mailbox{}")

    if erik.completed(erik_orcette) and orcette not in inventory.items and not erik.known(erik_orcette_2) and orcette_mail_lock:
        player_name "( Sweet! It looks like I'm the first one to get the mail! )"
        menu:
            player_name "The package is addressed to me. This must be Erik's toy."
            "Leave it alone.":
                pause
            "Open it.":


                show mailbox_item04_c at truecenter
                with dissolve
                pause
                player_name "( So this is what he's been waiting for... )"
                player_name "( The {b}Orcette{/b}. )"
                player_name "( I better put this back in the box. )"

        show unlock38 at truecenter with dissolve
        $ inventory.items.append(orcette)
        $ player_mail = []
        pause
        hide unlock38
        hide mailbox_item04_c
        with dissolve
        player_name "( Time to get this to {b}Erik{/b} before someone catches me carrying this thing around. )"

    elif m_pizza_pamphlet in player_mail:
        player_name "( This is probably junk mail.)"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza? I haven't been to that place in a while. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True

    elif m_newspaper in player_mail:
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The thief is still on the loose? You'd think they would've caught him by now... )"
        player_name "( I better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
    $ callScreen(location_count, False)

label lawnmower_dialogue:
    $ location_count = "Garage"
    scene expression gTimer.image("home_garage{}")
    if quest14 in quest_list and quest14 not in completed_quests and gas_can not in inventory.items:
        show player 2
        player_name "( I haven’t used a lawn mower in years... do I even remember how to use one? )"
        player_name "( {b}Dad{/b} used to pull the cord and it would start. Let me try that. )"
        scene home_garage_closeup
        show player 197
        with dissolve
        $ renpy.pause()
        show player 200 at Position (xpos=566)
        $ renpy.pause()
        show player 197 at center
        scene home_garage
        show player 35
        with dissolve
        player_name "( It must be out of gas. It barely started, so at least I know it’s running. )"
        show player 2
        player_name "( Well it’s not going to start without gas. I should probably get some from {b}CONSUM-R{/b}. )"
    elif quest14 in quest_list and quest14 not in completed_quests and gas_can in inventory.items:
        scene home_garage_closeup
        show player 202 at Position (xpos=521) with dissolve
        player_name "( I finally have some gas for the mower. )"
        show player 201 at Position (xpos=509)
        player_name "( That should be enough. )"
        show player 196 at Position (xpos=521)
        player_name "Hope this works. I don’t know what else to do after this..."
        show player 197 at center
        $ renpy.pause()
        show player 200 at Position (xpos=566)
        $ renpy.pause()
        show player 197 at center
        $ renpy.pause()
        show player 200 at Position (xpos=566)
        $ renpy.pause()
        show player 199 at center
        player_name "Hmm... it's not working. I'll try pulling it a bit harder..."
        show player 200 at Position (xpos=566)
        $ renpy.pause()
        show player 198 at center
        player_name "It worked!"
        $ ui_lock_count = 1
        $ inventory.items.remove(gas_can)
        $ quest14_1 = True
        jump home_front
    else:

        show player 35 with dissolve
        player_name "( Why would I use the lawn mower? The grass looks fine... )"
        hide player 35 with dissolve
    $ callScreen(location_count)

label car_dialogue:
    $ location_count = "Garage"
    scene expression gTimer.image("home_garage{}") with None

    if quest16 in quest_list and quest16 not in completed_quests and not mother.known(mom_broken_engine):
        $ location_count = "Car Engine"
        show player 4 with dissolve
        player_name "( She's right. The car doesn't even try to start. )"
        show player 5
        player_name "( I'd better check the engine. )"
        if gTimer.is_dark():
            player_name "( It sure is dark in here. )"
        $ callScreen(location_count)
    else:

        if seen_garage_locked:
            show player 34 at left with dissolve
            player_name "Hmm..."
            show player 35
            player_name "I don't need to use {b}Mom's{/b} car."
            hide player 35 with dissolve
        else:

            show player 2 at left with dissolve
            player_name "{b}Mom's{/b} car ... wish I had a reason to drive it..."
            $ seen_garage_locked = True
            hide player 2 at left with dissolve
    $ callScreen(location_count)

label engine_broken_dialogue:
    scene expression gTimer.image("home_garage{}") with None

    show player 23 with dissolve
    player_name "!!!"
    show player 22
    player_name "The engine's a wreck! What happened?"
    pause
    show player 16
    player_name "( I wonder if this has something to do with those guys coming around the house... )"
    player_name "( It looks like someone hit it with a crowbar. )"
    show player 11
    player_name "( There's no way I can fix this. We have to get a whole new engine or something. )"
    player_name "( I should probably tell {b}Mom{/b} about this. She won't be happy! )"
    $ mother.add_event(mom_broken_engine)
    jump home_garage

label attic_dialogue:
    $ location_count = "Attic"
    $ callScreen(location_count)

label ring:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( That looks like an expensive ring! )"
    player_name "( What was it doing all the way up there? )"
    hide expression "objects/closeup_ring.png" with dissolve
    show expression "boxes/popup_ring.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_ring.png" with dissolve
    jump attic_dialogue

label cheerleader_outfit:
    scene expression gTimer.image("attic{}")




    show expression "boxes/popup_item_outfit1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_outfit1.png" with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "That's {b}Dad{/b}'s old {b}fishing rod{/b}!!"
    player_name "( I remember when we used to go fishing by the {b}pier{/b}, when I was little. )"
    player_name "{b}*Sigh*{/b}"
    player_name "I miss {b}Dad{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    show expression "boxes/popup_item_rod1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_rod1.png" with dissolve
    jump attic_dialogue

label painting:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}Mom{/b} used to love painting farm animals..."
    hide expression "objects/closeup_painting01.png" with dissolve
    jump attic_dialogue

label attic_key:
    scene expression gTimer.image("home_entrance{}")
    show expression "objects/closeup_key.png" with dissolve
    player_name "( I've never seen this key before. )"
    player_name "( It's rather small... )"
    hide expression "objects/closeup_key.png" with dissolve
    show expression "boxes/popup_key.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_key.png" with dissolve
    jump home_entrance

label shovel:
    scene expression gTimer.image("home_garage{}")
    show expression "boxes/popup_item_shovel1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_shovel1.png"
    jump home_garage

label stool:
    scene expression gTimer.image("home_garage{}")
    show expression "boxes/popup_item_stool1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_stool1.png"
    jump home_garage

label vacuum_dialogue:
    $ location_count = "Entrance"
    scene location_home_entrance_fight
    show mom 94 at right with dissolve
    pause
    show mom 95
    pause
    show mom 94
    pause
    show mom 95
    pause
    show mom 94
    show player 1 at left with dissolve
    pause
    show mom 95
    pause
    show mom 97 with dissolve
    mom "Oh!!"
    mom "You startled me..."
    show mom 98
    show player 17
    player_name "Sorry, {b}Mom{/b}."
    show player 14
    player_name "I didn't mean to!"
    show mom 97
    show player 1
    mom "Sorry about the noise."
    mom "It's taking me a while to clean up, but I should be done soon."
    mom "My poor old back is killing me..."
    show mom 98
    menu:
        "Let me help.":
            show mom 98 at right
            show player 14 at left
            player_name "Here, {b}Mom{/b}, pass me the vacuum."
            show player 1
            show mom 96
            mom "..."
            show mom 97
            mom "You want the vacuum?"
            show mom 96
            show player 14
            player_name "Yeah, I'll take over from here."
            player_name "You deserve a rest, {b}Mom{/b}."
            show player 10
            player_name "I don't like seeing you hurting like this..."
            show mom 97
            show player 11
            mom "It's okay, Sweetie. You don't have-"
            show mom 98
            show player 10
            player_name "No, {b}Mom{/b}!"
            player_name "I want to do it."
            show mom 97
            show player 1
            mom "Well, if you insist..."
            show player 257
            show mom 100
            with dissolve
            mom "Thanks for helping... It's very sweet of you."
            show player 259
            show mom 99
            player_name "No problem!"
            hide player
            hide mom
            with dissolve
            scene help_mom_mc_home_cutscene with fade
            show text "I felt bad {b}Mom{/b} was having a hard time with her back pain. \nI was glad I could help, even if it took a while to finish. \nI have to say, doing the stairs was harder than I thought... \nAt least {b}Mom{/b} kept me company until I finished both floors." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            $ mom_helped += 1
        "It's too loud.":

            show mom 96 at right
            show player 10 at left
            player_name "Can you please finish cleaning another time?"
            player_name "I can't study with all the noise..."
            show mom 97
            show player 11
            mom "I'm sorry, Sweetie!"
            mom "I didn't mean to bother you like this."
            show mom 96
            show player 14
            player_name "It's okay, {b}Mom{/b}."
            show mom 97
            show player 1
            mom "I guess I could rest my back for a while..."
            show mom 96
            show player 17
            player_name "Thanks!"
            hide player
            hide mom
            with dissolve
    $ mom_vacuuming = False
    $ callScreen(location_count)

label lawn_mower_dirty:
    if location_count == "Home Front":
        scene home_front with None

    elif location_count == "Entrance":
        scene home_entrance with None

    elif location_count == "Living Room":
        scene home_livingroom_b with None
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 11 zorder 1
    with dissolve
    player_name "( I should get my clothes cleaned up before I do that... )"
    hide player
    hide xtra
    with dissolve
    $ callScreen(location_count)

label mom_dinner_outfit:
    if location_count == "Entrance":
        scene home_entrance with None

    elif location_count == "Living Room":
        scene home_livingroom_b with None
    show player 10 with dissolve
    player_name "{b}Mom{/b} called for me, I should check up on her..."
    hide player with dissolve
    $ callScreen(location_count)

label erik_bullying_3:
    $ location_count = "Entrance"
    scene home_entrance_evening
    show erikmom 19c at Position (xpos=700)
    show mom 13 at right
    with dissolve
    show player 5 at left with dissolve
    mom "Sweetie!! Are you okay?!"
    show mom 14b
    show player 10
    player_name "I'm fine, {b}Mom{/b}. The nurse said I just had a small concussion."
    show player 11
    show mom 13
    mom "You had a concussion!"
    show mom 14b
    show player 10
    player_name "Everything is fine. I'll be okay, {b}Mom{/b}."
    show player 5
    show mom 13
    mom "I didn't even know you were in the hospital!"
    mom "Oh, I'm the worst mother in the world!"
    show mom 14b
    show player 10
    player_name "{b}Mom{/b}, it's alright. I'm really fine! Calm down."
    show player 11
    show mom 13
    mom "I left the house this morning and when I got back I realized you still weren't home yet!"
    mom "Then {b}Mrs. Johnson{/b} stopped over and..."
    show mom 14b
    show erikmom 19
    erimom "I got a hold of your mother when I saw she was home and filled her in on your scuffle at school."
    erimom "I told her you were on your way back from the hospital with {b}Erik{/b}."
    erimom "You did a good thing standing up for {b}Erik{/b}."
    show erikmom 38
    show mom 13
    mom "Yes, it was really brave of you to stand up for your friend at school."
    mom "But, be please be careful!"
    show mom 14b
    show player 24
    player_name "I know {b}Mom{/b}..."
    show player 25
    player_name "I promise I'll try and stay out of trouble."
    show player 24
    show mom 13
    mom "Come here."
    hide player
    hide mom
    hide erikmom
    with dissolve
    show erikmom 14 at right
    show mom 4
    with dissolve
    mom "I'm so glad your safe."
    mom "I love you."
    player_name "I love you too, {b}Mom{/b}."
    hide mom
    hide erikmom
    with dissolve
    show erikmom 14 at Position (xpos=700)
    show mom 1 at right
    show player 13 at left
    with dissolve
    show erikmom 17
    erimom "Thanks again, [firstname]."
    erimom "You're always welcome to stop over and visit."
    show erikmom 14
    show player 14
    player_name "It's fine. Just helping a friend."
    show player 13
    show erikmom 17
    erimom "Thank you."
    show erikmom 14
    show player 36 with dissolve
    player_name "Good night {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show erikmom 17
    erimom "Good night."
    hide erikmom with dissolve
    show mom 2
    mom "Now hurry up to bed and get some rest."
    hide player
    hide mom
    with dissolve
    $ erik.add_event(erik_bullying_3)
    $ callScreen(location_count)