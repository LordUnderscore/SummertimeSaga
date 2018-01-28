label erik_indoors:
    $ location_count = "Erik's House Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.over(erik_gf) and not erik.known(erik_gf_2):
        scene expression gTimer.image("erik_inside{}_b")
        show player 14 at left
        show june 2 at Position (xpos=700)
        show erik 1 at right
        with dissolve
        player_name "Oh, hey guys!"
        show player 1
        show erik 4
        eri "Hey, {b}[firstname]{/b}!"
        show june 3
        show erik 1
        june "Hi!"
        show player 14
        show june 2
        player_name "I didn't know you two were already hanging out!"
        show player 1
        show erik 4
        eri "Yeah, we've been playing Ork Bork a lot..."
        show erik 1
        show june 6
        june "Ha ha. Yeah, we're totally addicted!"
        show june 2
        show player 14
        player_name "So, you two have been getting along fine, huh?"
        show player 1
        show erik 4
        eri "Yeah, actually we have to do something... in my err... room."
        show erik 1
        show player 11
        show june 3
        june "Yeah we have to, uhm... look over something?"
        show player 14
        show june 2
        player_name "Oh... I see!"
        show player 17
        player_name "It's alright, I'll come over another time then."
        show player 14
        player_name "I'll see you guys later!"
        show player 1
        show erik 4
        eri "Later, man."
        hide player
        hide june
        hide erik
        with dissolve
        $ erik.add_event(erik_gf_2)
        $ erik_gf_2.finish()

    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        $ lock_ui()
        label erik_sex_ed_block:
            scene expression gTimer.image("erik_inside{}_b")
            show player 14
            with dissolve
            player_name "I should go see if {b}Erik{/b} is in his room..."
            hide player with dissolve

    elif mrsj.over(mrsj_poker_night) and not mrsj.known(mrsj_poker_night_2):
        scene expression gTimer.image("erik_inside{}_b")
        show erikmom 17 at right
        show player 1 at left
        with dissolve
        erimom "{b}[firstname]{/b}!"
        show player 11
        erimom "Can I have a quick word with you before you go see {b}Erik{/b}?"
        show erikmom 14
        show player 14
        player_name "Sure, {b}Mrs. Johnson{/b}."
        show erikmom 20
        show player 11
        erimom "I... I don't remember much of last night."
        show erikmom 19
        erimom "Whatever happened, I want to apologize."
        show player 13
        erimom "I drank too much, and I shouldn't have done those things with you boys."
        show erikmom 19c
        show player 10
        player_name "Oh, it's fine, Mrs. Johnson..."
        show erikmom 19
        show player 13
        erimom "You don't resent me, right?"
        show erikmom 19c
        show player 14
        player_name "Of course not."
        player_name "I think it was fun!"
        show erikmom 19
        show player 1
        erimom "What about {b}Erik{/b}?"
        erimom "Did he have fun too?"
        show player 14
        show erikmom 14
        player_name "I... I think so?"
        show erikmom 17
        show player 1
        erimom "Well... as long as you boys didn't find it too strange..."
        show erikmom 19c
        show player 14
        player_name "Did you talk to him about it?"
        show erikmom 19
        show player 11
        erimom "No! God no."
        show erikmom 20
        erimom "I don't want to make this more awkward than it already is."
        show erikmom 19
        erimom "But... Could you do me a favour and talk to him about it?"
        erimom "I just want to make sure he's not mad at me about it."
        show erikmom 14
        show player 14
        player_name "Sure, {b}Mrs. Johnson{/b}. I'll talk to him."
        show erikmom 18
        show player 1
        erimom "Thanks, you're so sweet."
        hide player
        hide erikmom
        with dissolve
        $ mrsj.add_event(mrsj_poker_night_2)
        $ mrsj_poker_night_2.finish()

    elif erik.over(erik_thief_2) and not mrsj.known(mrsj_poker_night):
        scene expression gTimer.image("erik_inside{}_b")
        show player 14 at left
        show erik 1 zorder 1 at right
        with dissolve
        player_name "Hey, {b}Erik{/b}."
        show erik 4
        show player 1
        eri "Hey, did you find anyone?"
        show erik 1
        show player 10
        player_name "Not much so far, everyone is either busy or just doesn't want to come over."
        show erik 5
        show player 11
        eri "Even {b}Mia{/b}?"
        show erik 1
        show player 10
        player_name "I think she's busy with homework."
        show erik 3
        show player 5
        eri "Aww man, who else is gonna play cards with us?"
        show player 1
        show erik 1b at Position(xpos=870)
        show erikmom 17b zorder 2 at right
        with dissolve
        erimom "Is something wrong, Pumpkin?"
        show erik 4b
        show erikmom 14b
        eri "Oh, it's nothing, {b}Mom{/b}."
        show erik 1b
        show erikmom 18
        erimom "Oh, come on! I heard you guys talking about inviting friends over."
        show erik 5b
        show erikmom 14b
        eri "Well, we can't find anyone to play Poker with us."
        show erik 1b
        show erikmom 17
        erimom "Ooh, that sounds fun!"
        show erik 5b
        show erikmom 14b
        eri "It would be more fun if we had other players..."
        show erik 1b
        show player 11
        show erikmom 17
        erimom "What about me?"
        show player 13
        show erikmom 18
        erimom "I'd like to play..."
        show player 1
        show erik 4b
        show erikmom 14b
        eri "Really?"
        show erik 1b
        show erikmom 17
        erimom "Yeah! It's not fair that a couple of good boys like you can't find someone to play with..."
        erimom "Tell you what, if you need another player, let me know, I'm always up for a nice poker night!"
        show erik 1
        show player 14
        show erikmom 14
        player_name "That sounds awesome!"
        show player 17
        player_name "Thanks {b}Mrs. Johnson{/b}."
        show player 1
        show erik 1 at right
        hide erikmom
        with dissolve
        pause
        show player 14
        player_name "Dude!! I can't believe your mom is going to play with us."
        show erik 4
        show player 1
        eri "Well, I guess we found someone..."
        hide player
        hide erik
        with dissolve
        $ mrsj.add_event(mrsj_poker_night)

    elif erik.over(erik_thief) and not erik.known(erik_thief_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 19 at right
        show player 13 at left
        with dissolve
        erimom "{b}[firstname]{/b}!"
        erimom "I just wanted to say thank you so much for, you know, protecting us."
        show erikmom 20
        erimom "It's pretty embarrassing you had to see my ex husband like that..."
        show erikmom 19c
        show player 33
        player_name "I just wanted to make sure you didn't get your house broken into."
        show player 13
        show erikmom 17
        erimom "I'm lucky to have such a wonderful neighbor..."
        show erikmom 14
        show player 17
        player_name "Oh, thanks!"
        show player 13
        show erikmom 49
        erimom "I should... reward you with something special, for what you've done for us..."
        show erikmom 50
        show player 4 with dissolve
        player_name "..."
        show player 29 with dissolve
        player_name "Uhh, you don't have to, {b}Mrs. Johnson{/b}!"
        show player 13 with dissolve
        show erikmom 49
        erimom "Oh, no. I insist!"
        erimom "I'll think of something and I'm sure you're going to like it..."
        show erikmom 50
        show player 17
        player_name "Ha ha, alright."
        hide player
        hide erikmom
        with dissolve
        $ erik.add_event(erik_thief_2)
        $ erik_thief_2.finish()

    elif mrsj.over(mrsj_yoga_help_2) and not erik.known(erik_breastfeeding):
        scene expression gTimer.image("erik_inside{}_b")
        show player 10 with dissolve
        player_name "( It's quiet, is anyone home? )"
        player_name "( Maybe {b}Erik{/b} is in his room. )"
        show player 17
        player_name "( I hope he's not sleeping... or doing something else. )"
        hide player with dissolve
        $ erik.add_event(erik_breastfeeding)
        $ lock_ui()

    elif mrsj.started(mrsj_yoga_help_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 17 at right
        show player 17 at left
        with dissolve
        erimom "{b}[firstname]{/b}!!"
        erimom "How did your first time instructing a yoga class go?"
        show erikmom 14
        show player 14
        player_name "I think I did ok?"
        show player 13
        show erikmom 17
        erimom "Was {b}Anna{/b} able to help you?"
        show erikmom 14
        show player 14
        player_name "Yeah, she was there."
        player_name "She is really good at yoga..."
        show player 17
        player_name "...and flexible!"
        show player 13
        show erikmom 18
        erimom "Ha ha ha!"
        show erikmom 49
        erimom "{b}Anna{/b} can get into any position I put her in."
        erimom "I've had her twisted up like a pretzel, once."
        show erikmom 50
        show player 12
        player_name "Really?"
        show player 11
        show erikmom 49
        erimom "Oh yeah. She's very good in tight... situations."
        erimom "And a little baby oil doesnt hurt either..."
        show erikmom 50
        show player 13
        player_name "..."
        show erikmom 19
        erimom "Umm... Anyway, so you think you'd do it again?"
        show erikmom 14
        show player 14
        player_name "Well, she invited me to do more yoga with her at the gym at night."
        show player 13
        show erikmom 18
        erimom "You should go!"
        show erikmom 49
        erimom "{b}Anna{/b} can teach you a lot of things..."
        show erikmom 50
        show player 17
        player_name "I'm sure, ha ha."
        show player 13
        show erikmom 19
        erimom "Thank you for helping me. Again."
        show erikmom 17
        erimom "And dont think I've forgot how much you've done for our family."
        show erikmom 49
        erimom "I owe you... a lot."
        show erikmom 50
        show player 33
        player_name "Don't worry about it. It's no problem."
        hide player
        hide erikmom
        with dissolve
        $ mrsj_yoga_help_2.finish()

    elif erik.over(erik_vr) and not mrsj.known(mrsj_yoga_help):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 17 at right
        show player 13 at left
        with dissolve
        erimom "Oh, good!"
        show erikmom 19
        erimom "{b}[firstname]{/b}, I hate to bother you, but are you available tonight?"
        show erikmom 19c
        show player 10
        player_name "Huh?"
        show player 11
        show erikmom 19
        erimom "I need someone to go and teach my yoga class for me tonight. I have another appointment I need to attend."
        show erikmom 14
        show player 12
        player_name "Me?!"
        show player 5
        show erikmom 49
        erimom "Do you think you could help your... favorite neighbor??"
        show erikmom 50
        show player 38 with dissolve
        player_name "Uhh... I... guess I could try?"
        show player 29 with dissolve
        player_name "But I don't know much about yoga..."
        show player 11 at left with dissolve
        show erikmom 17
        erimom "It's a beginners class!"
        erimom "You'll do fine!"
        show erikmom 57 with dissolve
        erimom "Here is a list of the yoga moves to do in front of the class."
        show erikmom 58
        pause
        show erikmom 14
        show player 386
        with dissolve
        player_name "Thanks."
        show player 380
        pause
        show player 384
        player_name "Umm... These moves look pretty complicated..."
        show player 385
        show erikmom 17
        erimom "My friend {b}Anna{/b} will be there to assist you during the class."
        show erikmom 18
        erimom "She's my little eager beaver. Always willing to help and to please."
        show erikmom 14
        show player 386
        player_name "Oh. Okay... I'll try my best."
        show player 385
        show erikmom 49
        erimom "You're so sweet. I'll make sure to pay you back one day!"
        show erikmom 17
        erimom "I gotta go, so study those moves!"
        erimom "Bye!"
        show erikmom 14
        show player 386
        player_name "Bye, {b}Mrs. Johnson{/b}."
        show player 385
        hide erikmom with dissolve

        show unlock41 at truecenter with dissolve
        $ inventory.items.append(instructions1)
        pause
        $ mrsj.add_event(mrsj_yoga_help)
        hide unlock41 with dissolve

        show player 381
        player_name "I should have a look at those instructions before I go to yoga class tonight..."
        hide player with dissolve

    elif mrsj.started(mrsj_intro) and not gTimer.is_morning():
        scene expression gTimer.image("erik_entrance{}_c")
        show player 1 at left
        show erikmom 17 at right
        with dissolve
        erimom "Hello, {b}[firstname]{/b}!"
        show erikmom 14
        show player 36 with dissolve
        player_name "Hi, {b}Mrs. Johnson{/b}."
        show player 13 with dissolve
        show erikmom 17
        erimom "It's been a while since your last visit!"
        show erikmom 14
        show player 10
        player_name "Yeah, I've been a bit busy lately."
        player_name "I've been trying to catch up on school work and save up a little money for college."
        show player 13
        show erikmom 17
        erimom "It's nice to hear of a young man, such as yourself, acting so responsibly."
        show erikmom 49
        erimom "Just make sure you save yourself some time to chase after girls, Honey."
        show erikmom 50
        show player 21
        player_name "Yeah..."
        show player 13
        pause
        show erikmom 17
        erimom "Well, I'm really happy to see you again!"
        show erikmom 18
        erimom "You're probably here to see {b}Erik{/b}, not little ol' me."
        show erikmom 17
        erimom "It's been so quiet around here..."
        show erikmom 14
        show player 10
        player_name "What do you mean?"
        show player 5
        show erikmom 19
        erimom "I mean, it's just that {b}Erik{/b} doesn't get many visitors and you are his best and only friend."
        show erikmom 17
        show player 13
        erimom "You are always welcome in this house day or night."
        show erikmom 49
        erimom "You're a good kid."
        show erikmom 50
        show player 2
        player_name "Thanks, {b}Mrs. Johnson{/b}."
        show player 13
        pause
        show player 12
        player_name "Do you know where I could find {b}Erik{/b}?"
        show player 5
        show erikmom 17
        erimom "I think I saw him just a bit ago making a rare appearance outside his room."
        erimom "He's probably down in the basement right now."
        if not gTimer.is_dark():
            erimom "Anyway, I should probably get going."
            show player 13
            erimom "I have to teach yoga lessons in the afternoon down at the gym."
            erimom "I've got some new students and I better hurry up so I'm not late!"
            show erikmom 14
            show player 14
            player_name "Okay, have fun!"
            show player 13
            show erikmom 17
            erimom "You too! Tell {b}Erik{/b} I'll be back with dinner and not to eat too many sweets."
            show erikmom 49
            erimom "I want him nice and hungry for me tonight!"
        else:


            show erikmom 18
            erimom "Well, it's getting a bit late for me."
            show erikmom 17
            show player 13
            erimom "I'm off to bed, so you have fun. But remember to keep the volume to a respectable level if you play some video games."
            show erikmom 14
            show player 14
            player_name "Will do. Have a good night {b}Mrs. Johnson{/b}!"
        $ mrsj_intro.finish()
        hide erikmom
        hide player
        with dissolve

    elif erik.completed(erik_orcette) and orcette in inventory.items and not erik.known(erik_orcette_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show player 375 at left
        show erikmom 17 at right
        with dissolve
        erimom "Hello, {b}[firstname]{/b}!"
        erimom "Are you looking for {b}Erik{/b}?"
        show erikmom 14
        show player 377
        player_name "!!!"
        show player 376
        player_name "H... Hi, {b}Mrs. Johnson{/b}."
        show player 378
        erimom "..."
        show erikmom 17
        erimom "So, what're you two up to..."
        show erikmom 14
        show player 376
        player_name "Oh, nothing!"
        show player 377
        show erikmom 49
        erimom "What is it that you're holding anyway?"
        erimom "Something new you and {b}Erik{/b} are going to play with, huh?"
        show erikmom 50
        player_name "!!!"
        show player 379
        player_name "Uh.... Yeah something like that."
        show player 377
        show erikmom 17
        erimom "I just love surprises! What is it? It has to be some new game."
        erimom "That's all my little pumpkin does these days..."
        show erikmom 14
        show player 379
        player_name "Yeah... Um... It's not... Well..."
        show player 377
        show erikmom 17
        erimom "Let me see!"
        show player 23 with dissolve
        show erikmom 43 with dissolve
        player_name "Wait!"
        show player 22
        erimom "!!!"
        show erikmom 44
        erimom "What... is it?"
        show erikmom 46
        show player 10
        player_name "It's..."
        show player 11
        show erikmom 43
        erimom "Is this one of those fake sex things they advertise online?"
        show erikmom 46
        show player 10
        player_name "Uh..."
        show player 24
        show erikmom 44
        erimom "Did {b}Erik{/b} put you up to this?"
        erimom "I've seen it flash across his computer screen when I entered his room one time."
        show erikmom 46
        show player 25
        player_name "No. No. It's... Um... Mine."
        show player 24
        player_name "I... Uh... Was going to... Just show him?"
        show erikmom 45
        erimom "Ha ha."
        erimom "Boys and their toys!"
        show erikmom 46
        player_name "..."
        show player 25
        show erikmom 44
        erimom "Oh Honey... It's alright!"
        erimom "Young men exploring their sexuality is a good thing!"
        erimom "Maybe playing with your new toy will motivate him to... get out of his room?"
        erimom "The real thing is... even better, young man."
        show erikmom 46
        show player 22
        player_name "{b}*Gulp*{/b}"
        show erikmom 44
        erimom "{b}Erik{/b} is upstairs, Honey."
        erimom "Oh, and make sure to use lube with that thing."
        erimom "You don't want to get friction burns on your... parts."
        hide erikmom with dissolve
        show player 377 with dissolve
        pause
        show player 376
        player_name "( Wow... I thought she was going to get mad at me for this... )"
        player_name "( But she seemed pretty open about it? )"
        player_name "( {b}Erik{/b} sure has a cool mom... )"
        $ erik.add_event(erik_orcette_2)
        hide player with dissolve
    $ callScreen(location_count)

label mrsj_sex_ed:
    scene erik_house_upstairs_n_c01
    show erik 5f at Position (xpos=300)
    show player 13 at left
    show erikmom 14 at right
    with dissolve
    eri "Hi, {b}Mom{/b}!"
    eri "You...needed something from us?"
    show erik 1f
    show erikmom 19
    erimom "Listen, boys."
    erimom "I know you two have been talking about this, so..."
    erimom "I've thought this over, and since you two are okay with this..."
    show erikmom 49
    erimom "I'll agree to give you two private...sex education lessons."
    show erikmom 50
    show player 23
    player_name "!!!"
    show erik 5f
    eri "M...{b}Mom{/b}, are you sure?"
    show erik 1f
    show erikmom 49
    show player 18
    erimom "Of course, Pumpkin!"
    erimom "I don't have a problem with it, as long as this stays between us!!"
    show erikmom 50
    show player 14
    player_name "I...I don't have a problem with that, {b}Mrs. Johnson{/b}..."
    show player 11
    show erikmom 52
    erimom "But!!" with hpunch
    erimom "Before we start with these lessons... I'll need something from you two."
    show player 5
    show erikmom 14
    show erik 4f
    eri "What do you need, {b}Mom{/b}?"
    show erik 1f
    show erikmom 19
    show player 13
    erimom "...I've actually never had sex with two guys before."
    show erikmom 49
    erimom "I'd like a book that shows sexual positions for more than two partners."
    erimom "I've heard a book called {b}Karma Sutra{/b} describes ancient eastern positions."
    erimom "See if you can find me that book."
    show erikmom 52
    erimom "And there's one more thing..."
    show erikmom 14
    show erik 5f
    eri "Oh, yeah?"
    show erik 1f
    show erikmom 49
    erimom "Well, if we're going to have sex, I have to make sure I don't get pregnant!"
    show erikmom 50
    player_name "..."
    show erikmom 49
    erimom "I'll have to take {b}birth control pills{/b}..."
    show erikmom 50
    show erik 5f
    eri "Can't we use condoms?"
    show erik 1f
    show erikmom 52
    erimom "Even with condoms, there's always a risk!!"
    show erikmom 49
    erimom "And if I use the pill, we can do it raw..."
    show erikmom 50
    show player 83
    show erik 58f
    player_name "!!!"
    show player 82
    show erikmom 20
    pause
    erimom "..."
    show erikmom 18
    erimom "Ha ha!"
    show player 81
    player_name "!!!" with hpunch
    show player 78
    show erikmom 49
    erimom "I can see you two are very excited about starting those sex lessons with me..."
    show erikmom 50
    show erik 56f
    eri "Sorry, {b}Mom{/b}."
    show erik 57f
    show erikmom 49
    erimom "It's fine, Pumpkin."
    show player 80
    erimom "The sooner you two help me get what I need, the sooner we can start!"
    show erikmom 50
    show erik 58f
    eri "Okay, {b}Mom{/b}!"
    show erik 57f
    show player 83
    player_name "We will find you what you need, {b}Mrs. Johnson{/b}!"
    hide player
    hide erikmom
    hide erik
    with dissolve
    scene black with fade
    pause

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show erik 4 at right
    show player 13 at left
    with dissolve
    eri "I can't believe {b}Mom{/b} is okay with having sex with us..."
    show erik 1
    show player 17
    player_name "I think we're lucky..."
    show player 13
    show erik 3
    eri "I've never had sex before..."
    show erik 3c
    show player 14
    player_name "Well, your mom plans on teaching us how. And it's going to be awesome!"
    show player 13
    show erik 5
    eri "But how are we going to get that stuff she asked for?"
    show erik 1
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "I think I got an idea."
    show player 13
    show erik 5
    eri "Oh, yeah?"
    show erik 1
    show player 14
    player_name "I'm sure the hospital has the pills your mom talked about..."
    show player 33
    player_name "And we can always find the Kama Sutra book at the library!"
    show player 13
    show erik 5
    eri "I hope you're right."
    show erik 1
    show player 14
    player_name "I'll come back when I find something..."
    hide player
    hide erik
    with dissolve
    $ erik.complete_events(erik_sex_ed)
    $ mrsj.add_event(mrsj_sex_ed)
    $ unlock_ui()
    $ callScreen(location_count)

label mrsj_sex_ed_2:
    scene erik_house_upstairs_n_c01
    show erik 4f at Position (xpos=300)
    show player 13 at left
    show erikmom 14 at right
    with dissolve
    eri "Hey, {b}Mom{/b}."
    show erik 1f
    show erikmom 17
    erimom "Hi, boys!"
    erimom "How are you two doing?"
    show erikmom 14
    show erik 4f
    eri "We found some things that may help you...with our lessons."
    show erik 1f
    show player 239_240 with dissolve
    pause
    show player 425 with dissolve
    player_name "Here's what I found, {b}Mrs. Johnson{/b}!"
    show player 13
    show erikmom 63
    with dissolve
    erimom "Oh, wonderful!"
    erimom "I'll have to prepare for our little lessons together..."
    erimom "Maybe you two should visit me at night in my room...Or, should I call it, our classroom!"
    erimom "Ha ha."
    hide player
    hide erikmom
    hide erik
    with dissolve
    scene black with fade
    pause

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "When should we visit my mom?"
    show erik 1
    show player 14
    player_name "I'll try and stop back over as soon as I can..."
    player_name "But you should do it with her whenever you want!"
    show player 13
    show erik 4
    eri "I guess you're right..."
    eri "Thanks for helping me with this, {b}[firstname]{/b}."
    hide player
    hide erik
    with dissolve
    $ inventory.items.remove(kamasutra)
    $ inventory.items.remove(birth_control_pills)
    $ mrsj_sex_ed.finish()
    $ callScreen(location_count)

label erik_breastfeeding:
    scene erik_house_cs01_01b with fade
    show text "This was the first time i had ever been in {b}Mrs. Johnson{/b}'s room.\nEven if I always knew {b}Erik{/b}'s mom was very close to him...\nI didn't expect to see him... breastfeeding..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene erik_house_cs02 with fade
    show text "The look on their faces said everything...\n...I was not supposed to be there. Everything would've been fine...\n...If only I had knocked first.\nInstinctively, I closed the door and decided I should leave." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show player 22 at left with dissolve
    show erik 2 at Position (xpos=750)
    show erikmom 52 at right
    with dissolve
    erimom "{b}[firstname]{/b}?!"
    erimom "I... What are doing here?"
    show erikmom 38
    show player 37 with dissolve
    player_name "{b}Erik{/b}?!"
    show erik 3b with dissolve
    player_name "I... um... was just trying to find you."
    show player 24 with dissolve
    show erik 3
    eri "{b}[firstname]{/b}..."
    show erik 2 with dissolve
    show player 25
    player_name "I heard voices and I thought..."
    show player 11
    show erik 3b
    eri "I...I just want to be in my room right now."
    show erik 2
    show erikmom 19b
    erimom "It's fine I-"
    hide erik with dissolve
    show erikmom 19c
    show player 22
    erimom "..."
    show erikmom 20
    erimom "Listen, what you saw just now is something... normal!"
    show player 5
    show erikmom 19
    erimom "He's my baby boy..."
    show erikmom 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}."
    player_name "I didn't mean to walk in on you guys like that..."
    show player 5
    pause
    show player 10
    player_name "Can you just tell {b}Erik{/b} that I'm sorry?"
    show player 5
    show erikmom 19
    erimom "Don't worry about him. He'll be fine..."
    erimom "It's just... {b}Erik{/b} doesn't seem to see or talk about many girls, so I try and..."
    show player 11
    erimom "...I give him a little womanly attention!"
    erimom "I thought I could get him off his computer if he could just... have a little taste!"
    show erikmom 19c
    show player 5
    player_name "..."
    show erikmom 19
    erimom "Can you just... you know. Keep this between us?"
    erimom "I don't think he would want the other kids at school to find out."
    show erikmom 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}. I won't tell anyone."
    hide player
    hide erikmom
    with dissolve
    $ erik.complete_events(erik_breastfeeding)
    $ erik.add_event(erik_breastfeeding_2)
    $ erik_breastfeeding_2.finish()
    $ unlock_ui()
    $ callScreen(location_count)

label erik_funky_block:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Well... I guess I should leave Erik alone for a while."
    hide player with dissolve
    $ callScreen(location_count)

label mrsj_room_locked_dialogue:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Oops! Mrs. Johnson must be keeping her door locked..."
    hide player with dissolve
    $ callScreen(location_count)

label mrsj_filled_block:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10
    with dissolve
    player_name "I should let {b}Mrs. Johnson{/b} rest."
    player_name "Besides, I don't think I can handle two of those lessons in one day..."
    hide player with dissolve
    $ callScreen(location_count)