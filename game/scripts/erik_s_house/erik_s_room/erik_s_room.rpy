label erik_room_dialogue:
    $ location_count = "Erik's Room"
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( Huh, {b}Erik{/b} isn't here. He must be in the basement... )"
        hide player with dissolve
    elif erik.completed(erik_bullying) and not erik.known(erik_bullying_2):
        jump erik_bullying
    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 30 with dissolve
        player_name "Huh?"
        player_name "( {b}Erik{/b} is usually at his computer. )"
        show player 12
        player_name "( He must be in the basement... )"
        hide player with dissolve
    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        jump erik_sex_ed
    elif June.started(june_intro):
        jump june_intro
    elif erik.started(erik_breastfeeding):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( No one here? )"
        show player 14
        player_name "( He must be in the basement... )"
        show player 11
        pause
        show player 10
        player_name "Huh?"
        player_name "( I think I can hear some voices coming from {b}Mrs. Johnson{/b}'s room. )"
        show player 12
        player_name "( I should ask her where {b}Erik{/b} is... )"
        hide player with dissolve
        $ erik_breastfeeding.finish()

    if is_here("erik"):
        if not erik.started(erik_card_hunt) and not is_here("june"):
            $ playSound("<loop 3>audio/ambience_erikroom.ogg")
    $ callScreen(location_count)

label june_intro:
    scene expression gTimer.image("erik_house_bedroom{}_b")
    show player 1 at left
    show erik 4 at right
    with dissolve
    eri "Hey, man."
    eri "Did you end up talking to my mom?"
    show player 14
    show erik 1
    player_name "Yeah, she thinks it might be a good idea to meet other girls..."
    show player 1
    show erik 5
    eri "Oh, really?"
    show player 14
    show erik 1
    player_name "Yeah, I agree with her!"
    show erik 3c
    player_name "I can try and help you..."
    show player 11
    show erik 3b
    eri "I don't know, {b}[firstname]{/b}."
    show erik 3
    eri "I don't think I'll ever find someone who's right for me..."
    show player 10
    show erik 2
    player_name "What?"
    show player 11
    show erik 3b
    eri "Someone who's like me!"
    show player 10
    show erik 3c
    player_name "What do you mean?"
    show erik 3b
    show player 11
    eri "I'm out of shape, I'm not good at talking to people..."
    show player 5
    eri "... Face it, man, I'm just a klutz..."
    show erik 3
    eri "... The only thing I'm good at is playing games!"
    show player 10
    show erik 3c
    player_name "So?"
    show player 14
    player_name "What if we found you a gamer girl?"
    show player 1
    show erik 5
    eri "A gamer girl..."
    show erik 4
    eri "I... I guess so?"
    show player 4
    show erik 1
    player_name "Hmm..."
    show player 14
    player_name "Do you know a girl at school who likes video games?"
    show player 11
    show erik 4
    eri "Well... There's this one girl from another class... She's kind of cute."
    show player 14
    show erik 1
    player_name "There's a girl at school that you like?"
    show player 1
    show erik 5
    eri "I don't know... she just seems... nice!"
    show player 14
    show erik 1
    player_name "What's her name?"
    show player 1
    show erik 4
    eri "I think her name is {b}June{/b}."
    show player 14
    show erik 1
    player_name "Have you ever talked to her?"
    show player 1
    show erik 14
    eri "Well this one time..."
    eri "... We, uh, I asked her about..."
    show player 11
    show erik 3
    eri "No, not really."
    show erik 3b
    eri "I think she borrowed one of my pencils, once..."
    show player 14
    show erik 3c
    player_name "Why don't you speak to her more?!"
    show player 11
    show erik 3
    eri "I can't!"
    show erik 3b
    eri "I'm WAY too shy..."
    eri "... and I don't even know what I would say to her."
    show player 35
    show erik 3c
    player_name "Okay, well, this might just be harder than I thought."
    show player 11
    show erik 3
    eri "Maybe we should just give up..."
    show erik 2
    eri "*Sigh*"
    show player 10
    player_name "What?!"
    show player 14
    show erik 3c
    player_name "Come on, {b}Erik{/b}!"
    player_name "You'll see! I think she might like you..."
    player_name "Where does she usually hang out?"
    show player 1
    show erik 1
    eri "Hmm..."
    show erik 5
    eri "I've seen her in the computer room many times before."
    show player 14
    show erik 1
    player_name "The {b}computer room{/b} at {b}school{/b}?"
    show player 1
    show erik 4
    eri "Yeah. It's on the second floor..."
    show player 14
    show erik 1
    player_name "I'll go see her, maybe I can try and set something up for you."
    show player 1
    show erik 4
    eri "Okay, thanks, man."
    show erik 1
    $ june_intro.finish()
    jump erik_talk

label erik_sex_ed:
    scene expression gTimer.image("eriks_room{}_c")
    show player 13 at left
    show erik 5 at right
    with dissolve
    eri "Hey, {b}[firstname]{/b}!"
    eri "Did you end up talking to my mom?"
    show erik 1
    show player 14
    player_name "Yeah, she said she needed to think about it..."
    show player 13
    show erik 5
    eri "Maybe we shouldn't have said-"
    show erik 1b
    show player 11
    erimom "Boys?"
    erimom "Can you come over here, please?"
    show erik 1
    show player 10
    player_name "Was that your mom?"
    show player 5
    show erik 5
    eri "Yeah... I think she's in her room."
    show erik 1
    show player 14
    player_name "She wants us to come over..."
    show player 13
    show erik 5
    eri "Why?"
    show erik 1
    show player 14
    player_name "We'll have to see..."
    hide player
    hide erik
    with dissolve
    $ erik_sex_ed.finish()
    $ callScreen(location_count)

label erik_bullying:
    scene expression gTimer.image("eriks_room{}_c")
    show player 13 at left with dissolve
    show erik 5 at right with dissolve
    eri "Hey, {b}[firstname]{/b}."
    eri "How've you been?"
    show erik 1
    show player 14
    player_name "I've been doing pretty good."
    show player 12
    player_name "How about you?"
    player_name "Have you been missing classes lately or something?"
    show player 5
    show erik 2 with dissolve
    eri "..."
    show player 10
    player_name "Is everything alright?"
    show player 5
    show erik 5 with dissolve
    eri "My mom sent you up here, huh?"
    show erik 3b
    show player 10
    player_name "Just checking up on you, that's all."
    show player 5
    show erik 5
    eri "Well... {b}Dexter{/b} has been on my case ever since you left..."
    eri "It's just been hard to attend school knowing he'll be there too. Waiting..."
    show erik 3b
    show player 12
    player_name "What happened while I was away?"
    show player 5
    show erik 5
    eri "A few weeks ago, I was sitting in the cafetaria and he came up to me..."
    show erik 3
    eri "...He said he wanted a copy of my homework for {b}Mrs. Bissette{/b}'s class."
    show player 12
    player_name "What did you do?"
    show player 11
    show erik 5
    eri "I told him no!"
    eri "But, he said he'd stick me into a locker If I didn't do what he asked..."
    show erik 3b
    player_name "..."
    show erik 5
    eri "Anyway, I ended up giving him my homework and have been until recently."
    show erik 3b
    show player 38 with dissolve
    player_name "What happened?"
    show player 11 with dissolve
    show erik 5
    eri "I told him he can't push me around all the time."
    eri "And then... He hit me in front of everyone..."
    show erik 2 with dissolve
    show player 16
    pause
    show player 12
    player_name "Hey, {b}Erik{/b}..."
    show erik 3 with dissolve
    show player 10
    player_name "I'm glad you told me."
    show player 30
    player_name "Let me know if he bothers you again."
    player_name "And hopefully he can focus his attention on someone else!"
    show player 13
    show erik 5
    eri "Alright, thanks {b}[firstname]{/b}."
    show erik 3b
    show player 14
    player_name "Ready to go to school now?"
    show player 13
    show erik 5
    eri "Yeah, I guess..."
    eri "But, can you please not tell my mom I'm being bullied at school?"
    eri "I don't want her to worry so much..."
    show erik 3b
    show player 2
    player_name "Okay."
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_bullying_2)
    $ callScreen(location_count)

label erik_cards:
    if eriks_cards in inventory.items:
        show erik 1 at right
        show player 14 at left
        player_name "I found your cards, {b}Erik{/b}!"
        show player 239_240
        pause
        show player 374 with dissolve
        player_name "Here you go..."
        show player 5 with dissolve
        show erik 36 at Position (xpos=1014) with dissolve
        eri "Awesome!"
        eri "Here, you have to see this new card I got."
        eri "There's no way I can lose in the upcoming tournament with this one..."
        show erik 38
        eri "..."
        eri "Where is it?"
        pause
        show player 11
        eri "No! It's not in here!"
        show player 12
        player_name "What card was it?"
        show player 11
        show erik 37
        eri "It was the {b}Cock Crown of Thorns{/b}!"
        show erik 2 at right with dissolve
        eri "No way..."
        eri "I'm totally going to lose, now."
        show erik 3
        eri "It was my... Precious..."
        show player 34
        player_name "Hmm..."
        show player 33
        player_name "I think I got an idea."
        show player 13
        show erik 5
        eri "Really?"
        show erik 3b
        show player 17
        player_name "Don't worry, {b}Erik{/b}. I'll find you that card."
        show player 13
        show erik 5
        eri "How are you going to do that?"
        show erik 3b
        show player 35
        player_name "I think I saw that card at {b}Cosmic Cumics{/b} a few weekends ago."
        show player 13
        show erik 5
        eri "But... Isn't it expensive?"
        show erik 5b
        eri "And I don't have much cash on me..."
        show erik 3b
        pause
        show player 14
        player_name "It's fine! I've been making some money helping my {b}Aunt Diane{/b}."
        show player 13
        show erik 4
        eri "You're the best, man!"
        show erik 1
        show player 14
        player_name "It's no problem, {b}Erik{/b}! I don't mind helping you out..."
        show player 17
        player_name "...And you have to win that tournament!"
        $ inventory.items.remove(eriks_cards)
        $ erik_card_hunt.finish()
        $ erik.add_event(erik_crown_card)
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Where did you see your cards last?"
        show player 11
        show erik 5
        eri "Hmm... I think that the last time I took them out was down here."
        eri "I was playing in the basement... But, my mom must've put them somewhere..."
        show erik 1
        show player 14
        player_name "I'll help you find them."
        show player 13
        show erik 5
        eri "Thanks."
        show erik 3
        eri "I really have to find them before the tournament next weekend..."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_crown_card:
    if card02 in inventory.items:
        show erik 1 at right
        show player 14 at left
        player_name "I got that card you wanted."
        show player 13
        show erik 4
        eri "The {b}Cock Crown of Thorns{/b}!?"
        show erik 1
        show player 2
        player_name "Yup!"
        show player 239_240
        pause
        show player 372 with dissolve
        player_name "Here you go..."
        show player 13 with dissolve
        show erik 40 at Position (xpos=1014) with dissolve
        eri "You're awesome! Thank you so much!"
        eri "With this card my victory is assured!"
        eri "I will be unstoppable! Peasants will bow before me..."
        show erik 39
        show player 17
        player_name "Ha ha."
        show player 13
        pause
        show erik 41
        eri "Hold on a second."
        show erik 36 with dissolve
        eri "I want you to have one of my cards..."
        show erik 30 at Position (xpos=1025) with dissolve
        show player 10
        player_name "A card?"
        show player 11
        show erik 31
        eri "It's one of my favorites... But I have a few copies..."
        show erik 1 with dissolve
        show player 371 with dissolve
        player_name "Huh..."
        hide player
        hide erik
        with dissolve
        show card_03_c at Position (ypos=650) with dissolve
        pause
        hide card_03_c with dissolve
        show erik 1 at right
        show player 370 at left
        with dissolve
        player_name "...Thanks!"
        show player 13 with dissolve
        show erik 4
        eri "Don't worry about it!"
        eri "It's to thank you for getting me that card."
        eri "Plus, I know you'll take care of her properly."
        show erik 1
        show player 14
        player_name "Well, thanks man!"
        show player 13
        show erik 5
        eri "Just... Make sure you keep it out of the sunlight so it doesn't fade."
        show erik 1
        show player 17
        player_name "Ha ha, I promise..."
        $ inventory.items.remove(card02)
        show unlock37 at truecenter with dissolve
        $ inventory.items.append(card03)
        pause
        hide unlock37 with dissolve
        $ erik_crown_card.finish()
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Which card is missing again?"
        show player 11
        show erik 5
        eri "Hmm... It's called the {b}Cock Crown of Thorns{/b}."
        eri "You said you might find it at {b}Cosmic Cumics{/b}?"
        show erik 1
        show player 14
        player_name "Oh, right!"
        player_name "I'll see if it's there..."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_package:
    if orcette in inventory.items:
        show erik 1 at right
        show player 376 at left with dissolve
        player_name "Here's your new toy!"
        show player 378
        show erik 4
        eri "What? You got it already?"
        show erik 1
        show player 376
        player_name "Yup!"
        show player 13 with dissolve
        show erik 43 at Position (xpos=1014) with dissolve
        eri "Sweet!"
        eri "This thing looks... Awesome!"
        eri "They even got the colors just right..."
        show player 14
        player_name "You ever used one of these before?"
        show player 13
        show erik 44
        eri "No, but I've always wanted to try it out!"
        eri "It's just... My mom would freak of she ever found out."
        show erik 42
        show player 12
        player_name "Uhh... You'd be suprised, your mom seems pretty cool!"
        show player 13
        show erik 44
        eri "Maybe..."
        show erik 42
        show player 12
        player_name "Is that thing... easy to clean?"
        show player 13
        show erik 43
        eri "I think it came with instructions, but I should just have to rinse it out."
        show erik 42
        pause
        show erik 43
        pause
        show player 18
        player_name "..."
        show player 17
        player_name "Oh {b}Erik{/b}..."
        show player 18
        show erik 44
        eri "What?!"
        show erik 42
        show player 14
        player_name "Nothing."
        show player 13
        show erik 43
        pause
        show player 33
        player_name "Well, I should probably leave you two alone..."
        show player 13
        show erik 44
        eri "{b}[firstname]{/b}, thanks again."
        show erik 43
        show player 14
        player_name "It's fine..."
        player_name "...Just be sure to lock the door!"
        $ inventory.items.remove(orcette)
        $ erik_orcette_2.finish()
        $ event_wait_till = gTimer.gameDay() + 2
    else:
        show erik 1 at right
        show player 12 at left
        player_name "What item did you want again?"
        show player 13
        show erik 5
        eri "It's like a rubber tube... It's called the {b}Orcette{/b}..."
        eri "You can find it online."
        eri "Just make sure it's delivered at your house so my mom doesn't see it."
        show erik 1
        show player 14
        player_name "Alright, got it."
        show player 13
        show erik 4
        eri "Thanks, [firstname]."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_vr_game:
    if game02 in inventory.items and virtualsaga in inventory.items:
        show erik 1 at right with dissolve
        show player 14 at left with dissolve
        player_name "I got it!"
        show player 239_240
        pause
        show player 400
        player_name "I got the headset!"
        show player 399
        show erik 4
        eri "Oh yeah?!"
        show player 13 with dissolve
        show erik 46 with dissolve
        eri "Wow... That must of been expensive..."
        show erik 47
        eri "How much was it?!"
        show erik 45
        show player 17
        player_name "Ehh, don't worry about it."
        show player 14
        player_name "I've been saving up some money."
        show player 13
        show erik 46
        eri "That's... Awesome."
        show erik 45
        show player 12
        player_name "Oh, here's the game, too!"
        show player 13
        show erik 47
        eri "Thanks, {b}[firstname]{/b}."
        eri "I've mentioned having people over to the basement to my mom."
        eri "She didn't seem to mind us using it."
        eri "She always bugs me about never having friends over..."
        show erik 45
        show player 14
        player_name "Great!"
        show player 33
        player_name "Hmm... I'll have to think about who we could invite over."
        show player 13
        show erik 47
        eri "I don't really know anyone, but I'll go with whoever you find!"
        show erik 45
        show player 14
        player_name "Ok!"
        show player 13
        show erik 46
        eri "Thanks again for the headset! I can't wait to try it out!"
        show erik 49 with dissolve
        show player 14
        player_name "You're welcome."
        eri "Awesome..."
        show erik 49
        pause
        player_name "See you later, {b}Erik{/b}."
        $ inventory.items.remove(game02)
        $ inventory.items.remove(virtualsaga)
        $ erik_vr.finish()
    else:
        show erik 1 at right
        show player 10 at left
        with dissolve
        player_name "What did you want in exchange for using the basement?"
        show player 5
        show erik 5
        eri "Hmm... The VR headset {b}Virtual Saga X{/b}..."
        show erik 4
        eri "...And that new game, called {b}World of Orcette{/b}..."
        show erik 1
        show player 10
        player_name "Where did you say they sold it?"
        show player 5
        show erik 5
        eri "At {b}Cosmic Cumics{/b}."
        show erik 1
        show player 14
        player_name "Ok. I'll see if I can find it there.."
        show player 13
        show erik 4
        eri "Thanks, {b}[firstname]{/b}!"
    hide player
    hide erik
    with dissolve
    $ callScreen(location_count)