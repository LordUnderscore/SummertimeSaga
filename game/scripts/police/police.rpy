default police_lobby_first_visit = True
default police_office_first_visit = True
default police_basement_first_visit = True
default police_earl_first_visit = True

label police_lobby_dialogue:
    $ location_count = "Police Lobby"
    if police_lobby_first_visit == True:
        scene police_lobby_b
        show player 11
        with dissolve
        player_name "( The Police station... Man, I'm sure glad I never had to come here before. )"
        hide player with dissolve
        $ police_lobby_first_visit = False

    if M_mia.get_state() == S_mia_clues:
        scene police_lobby_b
        show player 35 with dissolve
        player_name "Hmm... Where to start."
        player_name "I should {b}question his partners{/b} first."
        player_name "They may know where he could be..."
        hide player with dissolve
    $ callScreen(location_count)

label police_board:
    scene police_board
    with dissolve
    player_name "( This looks like the info board... )"
    pause
    $ callScreen(location_count)

label police_harolds_desk:
    scene police_c_2
    show player 109
    show harold_desk at right
    with dissolve
    pause
    show player 108
    player_name "Nothing much here."
    show player 108f with dissolve
    player_name "I was hoping to find some notes and some-"
    player_name "Huh... Is that an old picture of him?"
    call screen harolds_desk
    scene police_office_picture
    player_name "Is that... {b}Helen{/b} and {b}Harold{/b}?!"
    player_name "Wow... They look SO different...and much happier!"
    player_name "..."
    player_name "Where is that location?"
    player_name "It looks like...{b}Raven Hill{/b}?"
    player_name "Huh."
    player_name "They probably used to hangout there a lot..."
    $ M_mia.trigger(T_harold_photo_clue)
    $ callScreen(location_count)

label police_office_dialogue:
    $ location_count = "Police Office"
    if police_office_first_visit == True and is_here("harold"):
        scene police_office_b
        show yumi 2f at left
        show harold 1 at right
        with dissolve
        yum "Thank you so much for this opportunity, sir!"
        yum "I've been looking forward to this moment every since I entered the academy."
        show harold 2
        show yumi 1f
        harold "That's great, {b}Yumi{/b}."
        harold "It feels good to have a new partner."
        show yumi 2f
        show harold 1
        yum "I have to get back to cell duty."
        show yumi 1f
        show harold 2
        harold "Oh. Alright then. See you later."
        show harold 1
        hide yumi with dissolve
        pause
        show player 1 at left with dissolve
        show harold 2
        harold "Hey! What are you doing here?"
        harold "Aren't you one of {b}Mia's{/b} classmates?"
        show harold 1
        show player 14
        player_name "Hi, I just had some questions."
        show player 1
        menu:
            "Where's {b}Mia{/b}?":
                show player 14 at left
                show harold 1 at right
                player_name "I was just wondering: do you know where {b}Mia{/b} is?"
                show player 11
                show harold 2
                harold "I'm sorry, I can't help you right now; we're busy with a new case..."
                harold "But, she should be at school or at home."
                show harold 1
                show player 14
                player_name "Okay. Thanks, Sir!"
                hide player
                hide harold
                hide ui
                with dissolve
                $ police_office_first_visit = False

    elif M_mia.is_set('questioned yumi') and M_mia.is_set('questioned earl'):
        scene police_office_b
        show player 35 with dissolve
        player_name "Okay, so he's taking time off and took off for a drive this morning..."
        player_name "...And he's drunk."
        show player 12
        player_name "Hmm... I need more {b}clues{/b}."
        player_name "Maybe I should check his {b}desk{/b}..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.get_state() == S_mia_harold_gift:
        scene police_c_2
        show player 13 at left
        show harold 2 at right
        with dissolve
        harold "Hey there!"
        show harold 1
        show player 14
        player_name "Hi, sir!"
        player_name "Emm... I have something for you."
        show player 13
        show harold 3
        harold "Something for me?"
        show harold 1
        show player 12
        player_name "Well, it's from {b}Mia{/b}..."
        player_name "...She said she found this at home and wanted you to have it."
        show player 239_240 with dissolve
        pause
        show player 447 with dissolve
        show harold 4
        harold "!!!"
        show harold 33 at Position (xpos=1017)
        show player 13
        with dissolve
        harold "My old aviators..."
        show harold 32
        show player 14
        player_name "She thought you should have them."
        show player 13
        show harold 35
        harold "Thanks, I... It's been a while..."
        show harold 34
        show player 14
        player_name "I think you should wear them again!"
        show player 13
        show harold 33
        harold "I'll think about it."
        show harold 34
        show player 14
        player_name "Well, I better get going."
        show player 13
        show harold 33
        harold "Umm... Would you do something quick for me before you leave?"
        show harold 34
        show player 14
        player_name "Sure, what is it?"
        show player 13
        show harold 33
        harold "Just tell {b}Yumi{/b} that we need a status update on an inmate transfer..."
        harold "...She should be in the basement."
        show harold 34
        show player 14
        player_name "Okay, I'll tell her."
        show player 13
        show harold 35
        harold "Thanks again, kiddo."
        hide player
        hide harold
        with dissolve
        $ inventory.items.remove(aviators)
        $ ui_lock_count = 1
        $ M_mia.trigger(T_harold_glasses)

    elif M_mia.get_state() == S_mia_convince_harold:
        scene police_c_2 with fade
        show player 14 at left
        show earl 3 at right
        with dissolve
        player_name "Hello, officer {b}Earl{/b}!"
        show player 13
        show earl 2 with dissolve
        ear "Hello... What was your name again?"
        show earl 1
        show player 10
        player_name "{b}[firstname]{/b}, I'm in your daughter's class."
        show player 5
        show earl 4
        ear "Oh, yeeeeeeah."
        show earl 2
        ear "What do you need?"
        show earl 3 with dissolve
        show player 12
        player_name "Well, I was hoping to find {b}Harold{/b} here. Is he around?"
        show player 13
        show earl 2 with dissolve
        ear "He just went out on patrol but should be back soon."
        ear "I can hardly finish my donut box and he's back at his desk..."
        ear "...and I eat FAST!"
        ear "Anyway... The guy hasn't cracked a case in a long time. I'm not sure he has it in him anymore."
        show earl 3 with dissolve
        show player 12
        player_name "Really?"
        show player 5
        show earl 6 with dissolve
        ear "I think when I got promoted instead of him...it took the wind out of his sails."
        show earl 5
        pause
        show earl 6
        ear "Hey... I'm all out of donuts!"
        show player 13
        ear "Listen, kid. I gotta make a quick trip and resupply. If my blood sugar dips I get feisty."
        ear "And you don't want to meet feisty {b}Earl{/b}."
        ear "{b}Harold{/b} should be back soon. Stick around!"
        hide earl with dissolve
        show player 12
        player_name "Huh..."
        player_name "{b}Harold{/b} hasn't been doing well at work...and lost a promotion..."
        show player 10
        player_name "He's getting grief at home and at work."
        show player 5
        pause
        show player 13
        show harold 2 at Position (xpos=762) with dissolve
        harold "Well, hello there, {b}[firstname]{/b}."
        harold "What are up to today?"
        show harold 1
        show player 14
        player_name "{b}Mia{/b} wanted me to ask you to join {b}Helen{/b} and her for dinner on the weekend."
        show player 13
        show harold 29
        harold "..."
        show harold 30 at right with dissolve
        harold "Well... I would love to see them..."
        harold "I wish I had the time too...but..."
        show player 5
        hide harold
        show harold 26 at Position (xpos=762)
        with dissolve
        harold "I have a lot of...work. I've got a lot of cases to solve lately."
        harold "My oldest case is starting to stand out to my chief."
        harold "I was assigned the notorious night bandit case."
        harold "I've been catching heat lately for my lack of results on the whereabouts of the missing goods..."
        show harold 25

        if erik.over(erik_thief):
            show harold 26
            harold "...and {b}Larry{/b} isn't giving up the location of the goods either..."
            show harold 25
            show player 12
            player_name "I'll talk with him. His son is my best friend."
            player_name "If I can't get the location out of him, maybe I can get {b}Erik{/b} to help us."
        else:

            show player 12
            player_name "I've heard the news. I've actually seen the thief around my house a lot lately."
            show harold 29
            player_name "He is always sneaking into my neighbor's, {b}Mrs. Johnson{/b}, yard."
            show player 5
            show harold 3
            harold "Really? If you notice him again give me a call directly."
            show harold 1
            show player 12
            player_name "Of course! I'll keep an eye out for him."
            show player 5
            show harold 6
            harold "There have also been reports of him near the park as well. If you happen to notice him there, keep me in the loop."
            show harold 1
            show player 12
            player_name "Okay, I'll check there for clues as well."


        show player 13
        show harold 2
        harold "Thanks, {b}[firstname]{/b}."
        show harold 6
        harold "I better get back to work, if I ever want to solve some cases and free up some time away from work."
        show harold 1
        show player 14
        player_name "Talk to you later, {b}Harold{/b}."
        hide harold with dissolve

        if erik.over(erik_thief):
            show player 12
            player_name "Sounds like I need to help him find where {b}Larry{/b} hid the stolen goods."
            show player 10
            player_name "Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}."
            show player 12
            player_name "I should stop down to the jail cells and see him."
            player_name "Maybe he'll tell me where the stolen goods are."
        else:

            show player 12
            player_name "Sounds like I need to help him find the thief's stolen goods."
            show player 10
            player_name "Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}."
            show player 12
            player_name "I better keep an eye on {b}Mrs. Johnson's{/b} backyard at night."
            player_name "{b}Harold{/b} also mentioned the theif was spotted in the park too."
        show player 5
        pause
        show player 30
        player_name "{b}Earl{/b} is still not back."
        show player 33
        player_name "I wonder how many donuts he goes through each day."
        hide harold
        hide player
        with dissolve
        $ M_mia.trigger(T_harold_find_goods)

    elif M_mia.get_state() == S_mia_return_goods:
        scene police_c_2 with fade
        show player 453 at right
        show harold 2f at left
        with dissolve
        harold "Hi, {b}[firstname]{/b}."
        show harold 1f
        show player 454
        player_name "Hey, {b}Harold{/b}!"
        show player 453
        show harold 3f
        harold "What's with the big bag you got with you?"
        show harold 1f
        show player 454
        player_name "It's something I found in the park..."
        player_name "...I think you might want to see this."
        show player 453
        show harold 4f
        harold "Oh, yeah?"
        show harold 1f
        show player 454
        player_name "Have a look!"
        show player 13f
        show harold 47
        with dissolve
        harold "!!!"
        show harold 49 with dissolve
        harold "...Those are...all the stolen items!!"
        show harold 48

        if erik.over(erik_thief):
            show player 17f
            player_name "It was right where you said it would be!"
            show player 13f
            show harold 49
            harold "It was?"
            show harold 48
            show player 14f
            player_name "You mentioned the burglar was sighted in the park a lot."
            player_name "I did some checking around and found it tucked away behind some bushes next to a white tree."
        else:

            show player 14f
            player_name "{b}Larry{/b} actually told me where it was."
            player_name "He said he had been stashing all the stolen goods in the park."
        show player 13f
        show harold 49
        harold "I'm impressed {b}[firstname]{/b}. You did a great job!"
        show harold 48
        show player 17f
        player_name "Oh don't thank me. I wouldn't have found it if you didn't collect the clues..."
        show player 14f
        player_name "If anyone asks me about it, it was officer {b}Harold{/b} that made the find!"
        show player 13f
        show harold 49
        harold "Oh, you're too generous."
        show harold 48
        show earl 5 at Position (xpos=500)
        show yumi 11 at Position (xpos=700)
        with dissolve
        yum "What do you have there partner?"
        show yumi 10
        show earl 6
        ear "Looks like his dirty laundry bag."
        ear "*Snort* Hee-uck-uck-uck"
        show earl 5
        show harold 49
        harold "Not quite, {b}Earl{/b}. Those are all the stolen goods from the night burglar!"
        show harold 48
        show earl 6
        ear "Shiiieeeeet!"
        show earl 5
        show yumi 11
        yum "Congratulations, sir!"
        show yumi 10
        show earl 6
        ear "I...I knew I could always count on you, {b}Harold{/b}!"
        show earl 5
        show harold 49
        harold "Thanks guys. I really didn't do much though-"
        show harold 48
        show player 14f
        player_name "{b}Harold's{/b} just being modest!"
        show player 13f
        show earl 6
        ear "So, what are all the retrieved items?"
        show earl 5
        show harold 49
        harold "Lots of valuables... I think everything that was reported stolen is in here."
        hide harold
        show earl 7 at left
        with dissolve
        ear "Wow! I didn't think you had it in you lately, {b}Harold{/b}!"
        ear "But you solved one of the most high profile cases in a recent years!"
        show earl 8
        ear "You'll surely get a promotion out of finding all the stolen items. Heck, you deserve a promotion!"
        show earl 7
        "*Grumble* *Gurgle*"
        show earl 8
        ear "Woah... My belly is growling... All this excitement made me extra hungry."
        ear "I need to find me a donut."
        hide earl
        show harold 48 at left
        with dissolve
        show yumi 11
        yum "Congratulations again, {b}Harold{/b}."
        show yumi 10
        show harold 49
        harold "Thanks, {b}Yumi{/b}."
        show harold 50
        hide yumi
        show player 11f
        with dissolve
        harold "!!!"
        show harold 48
        show yumi 12 at Position (xpos=500)
        with dissolve
        yum "..."
        show yumi 13 at Position (xoffset=12) with dissolve
        yum "Well... I...uh...better get back to my cell duties."
        hide yumi with dissolve
        show harold 2f at Position (xpos=9) with dissolve
        show player 13f
        harold "That...felt great."
        harold "I haven't felt this appreciated in a long time..."
        harold "Thank you, {b}[firstname]{/b}, for helping me out with this."
        show harold 1f
        show player 14f
        player_name "It was mostly luck, really."
        show player 13f
        show harold 2f
        harold "Ahhh..."
        harold "I think I'm going to start spending more time on my patrols now."
        harold "You know...actually try and solve my other cases instead of trying to just make it through the day."
        show harold 1f
        show player 14f
        player_name "Good for you {b}Harold{/b}. I'm glad you feel better."
        player_name "I know I always feel good after accomplishing something at school."
        show player 17f
        player_name "{b}Mia{/b} and {b}Helen{/b} will be proud to hear you solved the case too!"
        show player 13f
        show harold 25f
        pause
        show harold 2f
        harold "Tell you what. I'll attend that dinner after all."
        harold "I feel like a weights been lifted my shoulders now that people's valuables have been found."
        harold "I'll call them shortly and make dinner plans... I'll actually have something to tell them about!"
        show harold 1f
        show player 14f
        player_name "I'm glad it all worked out in the end, {b}Harold{/b}."
        show player 13f
        pause
        show player 36f with dissolve
        player_name "Well, I'll see you later."
        show player 13f with dissolve
        show harold 2f
        harold "Goodbye, {b}[firstname]{/b}."
        hide harold
        hide player
        with dissolve
        $ M_mia.trigger(T_harold_promotion)
    $ callScreen(location_count)

label police_basement_dialogue:
    $ location_count = "Police Basement"
    if police_basement_first_visit == True:
        scene police_basement_b
        pause .4
        scene police_c_3
        show player 1
        with dissolve
        player_name "( This must be the \"drunk tank\" people talk about... )"
        hide player with dissolve
        $ police_basement_first_visit = False

    elif M_mia.is_set('questioned yumi') and M_mia.is_set('questioned earl'):
        scene police_basement_b
        show player 35 with dissolve
        player_name "Okay, so he's taking time off and took off for a drive this morning..."
        player_name "...And he's drunk."
        show player 12
        player_name "Hmm... I need more {b}clues{/b}."
        player_name "Maybe I should check his {b}desk{/b}..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.get_state() == S_mia_inmate_status:
        scene police_basement_empty_b
        show player 4 at Position (xoffset=6) with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "I don't see {b}Yumi{/b} anywhere, maybe I should-"
        "*Shouting*" with hpunch
        show player 11
        player_name "..."
        show player 10
        player_name "Is that coming from one of the cells?!"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_harold_backup:
        scene police_basement_empty_b
        show player 10 with dissolve
        player_name "Quick, I have to find {b}Harold{/b}..."
        hide player with dissolve
    $ callScreen(location_count)

label inmate_transfer_block:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "There's people shouting."
    player_name "I should check what's happening in those cells..."
    hide player with dissolve
    $ callScreen(location_count)

label police_cell_dialogue:
    if M_mia.get_state() == S_mia_inmate_status:
        scene police_cell_inside_fight1
        yum "Hey, stop!!!!"
        scene police_cell_inside_fight2
        crys "Arhh!!"
        scene police_cell_inside_fight1
        yum "...Help!! Get some backup!!"
        player_name "!!!"
        scene police_cell_inside_fight2
        player_name "I'll get {b}Harold{/b}!"
        scene police_cell_inside_fight1
        yum "Go! ...Quick!"
        $ M_mia.trigger(T_yumi_backup_request)

    elif M_mia.get_state() == S_mia_harold_backup:
        scene police_basement_empty_b
        show player 10 with dissolve
        player_name "Quick, I have to find {b}Harold{/b}..."
        hide player with dissolve

    elif M_mia.get_state() == S_mia_harold_to_the_rescue:
        scene police_cell_inside_cs1
        with fade
        show text "{b}Harold{/b} and I rushed to the basement.\nWhen {b}Harold{/b} walked into the cell, he froze for a moment...\n...But realized he had to find the courage to step in and help {b}Yumi{/b}." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause

        scene police_cell_inside_cs2
        with fade
        show text "Inside the cell was {b}Crystal{/b}...\n...{b}Roxxy's{/b} mom, notorious for causing trouble when drunk.\nIt turns out, she is quite a fighter after a few drinks..." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause

        scene police_cell_inside_cs3
        with fade
        show text "{b}Harold{/b} had quite a bit of trouble at first...\n...But he soon found his old form.\nI could tell that despite the trouble, he enjoyed getting some action." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        hide police_cell_inside_cs1
        hide police_cell_inside_cs2
        hide police_cell_inside_cs3

        scene police_cell_c_02 with fade
        show harold 39 at Position (xpos=158)
        show yumi 5 at Position (xpos=855)
        harold "Now, STAY there!!"
        show harold 38
        show yumi 7
        yum "..."
        show harold 37
        harold "Are you okay?"
        show harold 36
        show yumi 6
        yum "Yeah, I just... I've never seen you like this before."
        show yumi 5
        show harold 37
        harold "Oh, it's just, you know... These type of people get on your nerves..."
        show harold 36
        show yumi 6
        yum "No, I meant like... Taking action like this."
        yum "It was really nice! It's a side of you I haven't seen before."
        show yumi 5
        show harold 37
        harold "You know what, I kind of missed that. The action."
        show harold 36
        show yumi 6
        yum "Thanks for having my back..."
        show yumi 5
        show harold 37
        harold "Oh, come on. I would do anything for my partner!"
        show harold 36
        show yumi 6
        yum "Ugh! I should have been more careful..."
        yum "...It was stupid of me and everyone at work will find out, I'm sure..."
        show yumi 5
        show harold 37
        harold "Well, {b}Yumi{/b}..."
        harold "I wouldn't worry to much about it..."
        show harold 42 at Position (xoffset=32) with dissolve
        pause
        show harold 43 at Position (xpos=195) with dissolve
        pause
        scene police_cell_inside_zoom
        pause
        scene police_cell_inside_splash with flash
        pause
        scene police_cell_c_02
        show harold 41 at Position (xpos=158)
        show yumi 7 at Position (xpos=855)
        with fade
        harold "...Because I'll take care of it."
        harold "Now, let's get out of here!"
        hide harold
        hide yumi
        with dissolve
        scene black with fade
        pause
        scene police_basement_empty_b
        show player 10f at right
        show harold 40 at left
        show yumi 5f at Position (xpos=550)
        with dissolve
        player_name "...{b}Harold{/b}?"
        show player 11f
        show harold 41
        harold "Hey, kid."
        show harold 40
        show player 10f
        player_name "Are you okay? Your shirt...it's ripped?"
        show player 11f
        show harold 41
        harold "It's fine, just a scratch."
        show harold 40
        show player 12f
        player_name "Looks like your partner had a rough time as well..."
        show player 11f
        show yumi 6f
        yum "Oh, yeah... MY hair is a mess."
        show yumi 5 with dissolve
        show harold 41
        harold "Actually, I kind of like your hair this way. Keep it."
        show player 13f
        show harold 40
        show yumi 7
        yum "..."
        show harold 41
        harold "How about we go for a drive?"
        show harold 40
        show yumi 8
        yum "You mean, now?!"
        show yumi 9
        show harold 41
        harold "Yeah, it's nice out...and I'm thirsty."
        show harold 40
        show yumi 8
        yum "Ha ha, alright... If you insist."
        show yumi 9
        show harold 41
        harold "Hop in the car, I'll meet you outside."
        show harold 40
        hide yumi with dissolve
        show player 14f
        player_name "I should let you go then."
        show player 13f
        show harold 41
        harold "Wait..."
        show harold 40
        show player 11f
        player_name "..."
        show harold 41
        harold "Thanks for all your...help."
        show harold 40
        show player 14f
        player_name "Oh, I... It's nothing, sir."
        show player 13f
        show harold 41
        harold "See ya, kiddo!"
        hide harold
        hide player
        with dissolve
        $ ui_lock_count = 0
        $ M_mia.trigger(T_harold_backup)
    else:

        scene police_cell
        show xtra 13 zorder 1 at left
        show player 10f zorder 2
        with dissolve
        player_name "I wouldn't want to end up in there. Sheesh!"
        hide player with dissolve
    $ callScreen(location_count)

label police_cell_larry_dialogue:
    scene police_cell
    if not erik.known(erik_father_forgive):
        show larry 15 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 5f at right with dissolve
        larry "Hey! You!"
        show larry 14
        show player 11f
        player_name "!!!"
        show player 12f
        player_name "Umm...Yeah?"
        player_name "What do you want?"
        show player 16f
        show larry 15
        larry "Listen, I'm not mad at you for what you did."
        larry "It's actually nice knowing there is someone keeping watch out for my family."
        show larry 14
        show player 5f
        player_name "..."
        show larry 15
        larry "I know what I was doing was bad, okay?."
        larry "I just... I need you to give {b}Erik{/b} a message from me."
        show larry 14
        show player 10f
        player_name "I'm not sure he would want that..."
        show player 5f
        show larry 15
        larry "I need you to tell him that I'm sorry!"
        larry "I'm sorry for everything..."
        show larry 14
        show player 12f
        player_name "I don't know if I should."
        show player 5f
        show larry 15
        larry "Please!"
        larry "I...I can help you!"
        show larry 14
        show player 10f
        player_name "Huh?"
        show player 11f
        show larry 15
        larry "I stashed a bag full of stolen things I took."
        larry "I'll tell you where they are if you tell my son that everything I did was to help him."
        larry "I was trying to get back on top, you know?"
        larry "I just...did it the wrong way, and I'm sorry for that..."
        show larry 14
        show player 34f
        player_name "..."
        show larry 15
        show player 5f
        larry "You can return the stolen goods to the police, or keep them! I don't care."
        larry "Can you just tell {b}Erik{/b} I'm sorry...and that I love him."
        larry "Hopefully, he can forgive me one day and...perhaps we can see each other again?"
        show larry 14
        show player 35f
        player_name "Hmm..."
        show player 12f
        player_name "I suppose I could. I'll see what I can do."
        show player 5f
        show larry 15
        larry "Thanks, kid!"
        $ erik.add_event(erik_father_forgive)

    elif erik.started(erik_father_forgive):
        show larry 14 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 12f at right with dissolve
        player_name "What did you want me to do again for you?"
        show player 5f
        show larry 15
        larry "Talk to {b}Erik{/b} and tell him I love him and that I'm sorry..."
        larry "If you do, I'll tell you where I hid all the goods I stole."
        show larry 14
        show player 10f
        player_name "I'll see what I can do."

    elif erik.completed(erik_father_forgive) and not erik.known(erik_father_treasure):
        show larry 15 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 5f at right with dissolve
        larry "Hey! It's you again!"
        larry "Did you get a chance to speak to {b}Erik{/b} like I asked?"
        show larry 14
        show player 12f
        player_name "Yeah. I did."
        show player 5f
        show larry 15
        larry "And what...what did he say?!"
        show larry 14
        show player 12f
        player_name "He'll think about it."
        show player 10f
        player_name "You need to give him some time, I guess..."
        show player 5f
        show larry 15
        larry "Thanks, kid."
        larry "You did the right thing..."
        larry "...Alright."
        larry "About those stolen goods I stashed."
        larry "They're {b}behind a bush in the park, next to a white tree{/b}."
        show larry 14
        show player 34f
        player_name "Hmm..."
        show player 12f
        player_name "Okay, I'll go have a look."
        show player 5f
        show larry 15
        larry "Listen! I'm going to try and turn my life around!"
        larry "You'll see!"
        larry "And...and maybe, someday you can even convince {b}Erik{/b} to come visit me?"
        show larry 14
        show player 12f
        player_name "We'll see."
        show player 5f
        show larry 15
        larry "Thanks..."
        $ erik.add_event(erik_father_treasure)

    elif erik.known(erik_father_treasure):
        show larry 14 at Position (xpos=351)
        show cell_bars at left
        show larry_hands at Position (xpos=400,ypos=658)
        show player 12f at right with dissolve
        player_name "Where did you hide the stolen goods?"
        show player 5f
        show larry 15
        larry "They're {b}behind a bush in the park, next to a white tree{/b}."
        show larry 14
        show player 12f
        player_name "Okay, I'll go have a look."
    hide player
    hide larry
    hide cell_bars
    hide larry_hands
    with dissolve
    $ callScreen(location_count)

label police_harold_dialogue:
    scene police_c_2
    if M_mia.is_set('mia route'):
        show harold 1 at right
        show player 14 at left
        with dissolve
        player_name "Hey, {b}Harold{/b}!"
        show player 13
        show harold 2
        harold "There's my man!"
        show harold 1
        show player 14
        player_name "How are things going lately?"
        show player 13
        show harold 2
        harold "Never been better! Our family is the happiest it's ever been."
        harold "{b}Helen{/b} has really changed. Really...changed."
        harold "Things are red hot in the bedr-"
        show harold 4
        harold "Anyway, you know what I mean."
        show harold 1
        show player 21
        player_name "Heh heh... Yeah, I suppose..."
        show player 13
        show harold 2
        harold "I should get back to work."
        harold "Feel free to stop by the house anytime, kiddo!"
        show harold 1
        show player 14
        player_name "Thanks, {b}Harold{/b}!"
        player_name "See you later."
        hide player
        hide harold
        with dissolve

    elif M_helen.get_state() in [S_helen_route_split, S_helen_mia_breakdown]:
        show player 22f at right
        show harold 51 at left
        with dissolve
        pause
        show harold 52
        show yum 12f at Position (xpos=395)
        with dissolve
        yum "!!!"
        show player 5f
        yum "Oh, I didn't see you there..."
        show yum 14f at Position (xpos=382) with dissolve
        show harold 53
        harold "Oh don't worry, {b}Yumi{/b}, it's just my daughter's little buddy."
        show harold 52
        show player 10f
        player_name "Hello..."
        show player 5f
        show yum 13f
        yum "Hi... Oh! I forgot I have something I...need to take care of in my office."
        hide yum
        show harold 54
        with dissolve
        harold "..."
        show harold 55
        harold "Sorry you had to see that, kiddo."
        harold "{b}Yumi{/b} is more of a hands on partner..."
        harold "Thought I'd try and teach her a couple things..."
        show harold 54
        show player 11f
        player_name "..."
        show player 10f
        player_name "So you and {b}Helen{/b}..."
        show player 5f
        show harold 55
        harold "Look. That ship has sailed, kiddo. {b}Helen{/b} seems to have accepted our separation."
        harold "I figured I better move on too."
        harold "To tell you the truth."
        harold "I've never been happier, and I've started seeing someone else."
        show harold 54
        show player 12f
        player_name "I wonder who..."
        show player 10f
        player_name "At least you're happy..."
        show player 5f
        pause
        show player 10f
        player_name "But how is {b}Mia{/b} handling this? Is she going to be alright?"
        show player 5f
        show harold 55
        harold "I'm not giving up on {b}Mia{/b}."
        harold "I visit her every day. She's my tough little girl."
        harold "She always has been after having to put up with {b}Helen{/b} and I."
        harold "She'll be alright."
        show harold 54
        show player 12f
        player_name "Good."
        show player 5f
        show harold 55
        harold "You're a good kid, {b}[firstname]{/b}. Thanks again for caring about my daughter."
        harold "I appreciate you and her trying to get me back with {b}Helen{/b}..."
        harold "It's just some things don't work out..."
        show harold 54
        show player 21f
        player_name "Heh heh..."
        player_name "You're welcome."
        show player 5f
        show harold 55
        harold "Don’t be afraid to visit me if there is anything you need help with."
        show harold 54
        show player 36f with dissolve
        player_name "Will do. Goodbye, {b}Harold{/b}."
        hide player
        hide harold
        with dissolve
        $ M_helen.trigger(T_harold_new_girl)
        $ callScreen(location_count)

    elif M_mia.get_state() == S_mia_harold_backup:
        show harold 1 at Position (xpos=762)
        show player 23 at left
        with dissolve
        player_name "{b}Harold{/b}!!"
        show player 22
        show harold 6
        harold "What's going on?? Did you find {b}Yumi{/b}?"
        show harold 1
        show player 38 with dissolve
        player_name "Yes! But she needs your help, now!!"
        show player 3 with dissolve
        show harold 3
        harold "What?!"
        show harold 1
        show player 10 with dissolve
        player_name "In the cell! {b}Yumi{/b}... She's struggling with an inmate!!"
        show player 5
        show harold 29
        harold "!!!"
        show harold 30 at right with dissolve
        harold "I... I should call for more backup... Maybe I should tell {b}Earl{/b} first-"
        show player 12
        player_name "{b}Harold{/b}! There's no time!"
        hide harold
        show harold 25 at Position (xpos=762)
        with dissolve
        player_name "You have to take control of the situation."
        show player 11
        show harold 26
        harold "But I should tell {b}Earl{/b} first..."
        harold "...I haven't dealt with inmates in a long time and-"
        show harold 25
        show player 15
        player_name "{b}Yumi{/b}'s your partner and needs your help!"
        player_name "You have to go, NOW!!!"
        show player 16
        show harold 24
        harold "..."
        show harold 6
        harold "You're right... I should take action."
        harold "Let's go."
        hide player
        hide harold
        with dissolve
        $ M_mia.trigger(T_harold_grows_a_pair)
        $ callScreen(location_count)

    elif M_mia.get_state() == S_mia_harolds_thoughts:
        show harold 1 at right
        show player 36 at left
        with dissolve
        player_name "Hi, {b}Harold{/b}."
        show player 13 with dissolve
        show harold 2
        harold "Hello again, kiddo."
        show harold 1
        show player 14
        player_name "Thought I'd stop by and see how dinner was with {b}Mia{/b} and {b}Helen{/b}."
        show player 13
        show harold 6
        harold "Oh... Umm... It was alright I guess. The food was really good."
        show harold 1
        show player 10
        player_name "Do you think things have...gotten better between {b}Helen{/b}...and you?"
        show player 5
        show harold 4
        harold "..."
        show harold 6
        harold "I know {b}Mia{/b} is trying to get {b}Helen{/b} and I back together."
        harold "You've been helping her too... You're a good kid."
        show harold 1
        harold "..."
        show harold 6
        harold "I suppose things between {b}Helen{/b} and I are better than when you saw us erupt at each other."
        show harold 4
        pause
        harold "I...just don't know though..."
        show harold 1
        pause
        show player 10
        player_name "Why don't you know?"
        show player 5
        show harold 26
        harold "Oh, kiddo."
        harold "We may be on good terms now, but we could be at each other's throats again."
        harold "For once, I'm thinking I might be happier on my own."
        harold "My marriage might be better left behind me."
        harold "Maybe...if {b}Helen{/b} really changed for good."
        harold "It might be possible for us to get back together."
        show harold 1
        show player 14
        player_name "I...understand."
        show player 13
        show harold 6
        harold "I better get back to work. I just had another breakthrough on a case."
        show harold 2
        harold "See you later, {b}[firstname]{/b}."
        show harold 1
        show player 14
        player_name "Bye, {b}Harold{/b}."
        show player 13
        hide harold with dissolve
        pause
        show player 14
        player_name "Sounds like {b}Harold's{/b} telling me there's a chance he'd get back with {b}Helen{/b}."
        show player 35
        player_name "Maybe {b}Sister Angelica{/b}s training is actually helping her and {b}Harold{/b}."
        show player 10
        player_name "But...he sure seems happy right now without {b}Helen{/b}..."
        player_name "{b}Mia{/b} would be devastated if he didn't get back with {b}Helen{/b}."
        show player 5
        player_name "..."
        show player 12
        player_name "I guess it's not really up to me at this point..."
        player_name "Might as well finish helping {b}Sister Angelica{/b}."
        show player 35
        player_name "What did she want again?"
        hide player with dissolve
        $ M_mia.trigger(T_harold_indecisiveness)
        $ callScreen(location_count)
    else:

        show player 1 at left
        show harold 2 at right
        with dissolve
        harold "Oh, hey, it's you again. Need something?"
        show harold 1
        show player 14
        player_name "Hi, I just had some questions."
        show player 1
    menu:
        "Where's Mia?":
            show player 14 at left
            show harold 1 at right
            player_name "I was just wondering: do you know where Mia is?"
            show player 11
            show harold 2
            harold "I'm sorry, I can't help you right now; we're busy with a new case..."
            harold "But, she should be at school or at home."
            show harold 1
            show player 14
            player_name "Okay. Thanks, Sir!"

        "{b}Larry{/b}." if M_mia.get_state() == S_mia_stolen_goods and erik.over(erik_thief):
            show player 10
            player_name "What did you need me to ask {b}Larry{/b}?"
            show player 5
            show harold 6
            harold "{b}Larry{/b} isn't giving up the location of the goods."
            show harold 1
            show player 33
            player_name "Oh yeah!"
            show player 12
            player_name "I'll talk with him. His son is my best friend."
            player_name "If I can't get the location out of him, maybe I can get {b}Erik{/b} to help us."
            show player 5
            show harold 2
            harold "Thanks, {b}[firstname]{/b}."
            hide harold
            hide player
            with dissolve

        "Thief." if M_mia.get_state() == S_mia_stolen_goods and not erik.over(erik_thief):
            show player 10
            player_name "What did you need me to do if I see the thief again?"
            show player 5
            show harold 6
            harold "If you notice him, give me a call directly."
            show harold 1
            show player 12
            player_name "Of course! I'll keep an eye out for him."
            player_name "He is always sneaking into my neighbor's, {b}Mrs. Johnson's{/b}, yard at night."
            show player 5
            show harold 6
            harold "There have also been reports of him near the park as well. If you happen to notice him there, keep me in the loop."
            show harold 1
            show player 12
            player_name "Okay, I'll check there for clues as well."
            show player 5
            show harold 2
            harold "Thanks, {b}[firstname]{/b}."
            hide harold
            hide player
            with dissolve

        "Donuts." if M_mia.get_state() == S_mia_impress_harold and donuts_correct not in inventory.items and donuts_fail not in inventory.items:
            show harold 1 at right
            show player 14 at left
            player_name "What kiiind of... donuts, err... do you like?"
            show player 11
            show harold 3
            harold "Excuse me?"
            show player 14
            show harold 1
            player_name "Just wondering!"
            show player 11
            show harold 2
            harold "Look, I don't have time to chat right now, I'm swamped with work..."
            harold "... Why don't you run off to school, okay?"
            show player 10
            show harold 1
            player_name "But-"
            show player 5
            show harold 2
            harold "I have to go, sorry."

        "Donuts." if M_mia.get_state() == S_mia_impress_harold and donuts_fail in inventory.items:
            show harold 1 at right
            show player 437 at left with fastdissolve
            player_name "I err, got you something."
            show player 1
            show player 436
            harold "..."
            show player 437
            player_name "It's for you!"
            show harold 8
            show player 1
            with fastdissolve
            harold "You brought me a box of... donuts?!"
            show player 14
            show harold 7
            player_name "Yeah! I thought maybe you'd like to snack on them at work..."
            show player 1
            show harold 9
            harold "Oh..."
            harold "I'm not a big fan of that kind, to be honest."
            show player 11
            show harold 10
            player_name "..."
            show harold 11
            harold "But I err... I appreciate the thought!"
            harold "I'm sure that {b}Earl{/b} will be more than happy to have them..."
            show player 10
            show harold 10
            player_name "Alright."

            show player 5
            hide harold with dissolve
            pause
            show player 10
            player_name "Damn!"
            player_name "I must of bought the wrong kind."
            player_name "I have to make sure I get the right ingredients..."
            $ inventory.items.remove(donuts_fail)

        "Donuts." if M_mia.get_state() == S_mia_impress_harold and donuts_correct in inventory.items:
            show harold 1 at right
            show player 437 at left with fastdissolve
            player_name "I err, got you something."
            show player 1
            show player 436
            harold "..."
            show player 437
            player_name "It's for you!"
            show harold 8
            show player 1
            with fastdissolve
            harold "You brought me a box of... donuts?!"
            show player 14
            show harold 7
            player_name "Yeah! I thought maybe you'd like to snack on them at work..."
            show player 1
            show harold 9
            harold "Let me see..."
            harold "Holy... [harold_glaze]... with... [harold_topping]?!"
            show player 14
            show harold 7
            player_name "I thought you'd like those!"
            show player 1
            show harold 8
            harold "These are my favourite... How did you..."
            show player 17
            show harold 44
            player_name "I got lucky, I suppose."
            show player 1
            show harold 45
            harold "*Nom nom*"
            show harold 46
            harold "Well, kid, you did well."
            show player 17
            show harold 45
            player_name "Glad you like them!"
            show player 1
            harold "..."
            show player 11
            show harold 46
            harold "Wait, before you go..."
            show player 1
            harold "I know that you and {b}Mia{/b} like to... hang out, and all that stuff."
            harold "You seem like a good kid, so I'll talk to my wife and see if she can lay off a bit."
            show player 14
            show harold 45
            player_name "You mean, I can visit her now?"
            show player 1
            show harold 46
            harold "Not too fast!"
            harold "I didn't say that... but... You could probably sneak in like before and I'll try and keep my wife distracted, alright?"
            show player 14
            show harold 45
            player_name "Really?"
            show player 1
            show harold 46
            harold "I said I'll try, I can't promise you anything."
            show player 14
            show harold 45
            player_name "Thanks, {b}Harold{/b}."
            show player 1
            show harold 46
            harold "Alright, now get out of here before my boss sees us with these donuts!"
            show player 17
            show harold 45
            player_name "Ha ha."
            $ inventory.items.remove(donuts_correct)
            $ M_mia.trigger(T_harold_donuts)
    hide player
    hide harold
    with dissolve
    $ callScreen(location_count)

label police_earl_dialogue:
    scene police_c_1 with None
    if police_earl_first_visit == True:
        show earl 2 at right
        show player 11 at left
        with dissolve
        ear "What'chu doing in here?!"
        show earl 3
        ear "Is it another one of those \"Bring your kids to work\" days?"
        show earl 1
        show player 14
        player_name "Oh, no, I'm just passing by, Sir."
        player_name "I wanted to speak with {b}Harold{/b}."
        show earl 2
        show player 1
        ear "Wait a minute... Don't you go to school with my daughter?"
        show earl 3
        show player 14
        player_name "Oh, right! You're {b}Rhonda's{/b} dad!"
        show earl 2
        show player 1
        ear "Shiiiiiiiiiiieeeeeet!"
        show player 11
        ear "You better watch yourself around my baby girl, or I'll have to put surveillance on {b}you{/b}."
        show earl 4
        ear "Got it?!"
        show earl 1
        show player 29
        player_name "Uhh... of course, Sir!"
        player_name "I would never-"
        show earl 2
        show player 13 at left
        ear "Relax, I'm just messing with ya! Move along now."
        $ police_earl_first_visit = False
    else:

        show earl 2 at right
        show player 1 at left
        with dissolve
        ear "Hey, what's up?"
        show player 14
        show earl 3
        if M_mia.get_state() == S_mia_impress_harold:
            menu:
                "Donuts.":
                    show earl 1 at right
                    show player 14 at left
                    player_name "This might seem like a silly question, but what kind of donuts does {b}Harold{/b} like?"
                    show player 1
                    show earl 2
                    ear "Hah!"
                    ear "{b}Harold{/b} only eats them if they're {b}[harold_glaze]{/b}..."
                    show earl 3
                    ear "... But I ain't sure what else he puts on them."
                    show player 14
                    show earl 1
                    player_name "I see."
                    show player 11
                    show earl 2
                    ear "Why do you ask?"
                    show player 17
                    show earl 1
                    player_name "Oh, no reason."
                    show player 11
                    show earl 4
                    ear "Wait, shouldn't you be at school? What are you doing here-"
                    show player 14
                    show earl 3
                    player_name "Errr..."
                    show player 17
                    player_name "Thanks, bye!"

        elif M_mia.get_state() == S_mia_clues:
            menu:
                "{b}Harold{/b}.":
                    show player 10
                    player_name "Do you know where {b}Harold{/b} could be?"
                    player_name "I need to err...return something to him!"
                    show player 11
                    show earl 2
                    ear "I'm not sure where he went, but I saw him yesterday in the office..."
                    ear "...He looked in a bad shape, that's for sure!"
                    ear "For a second I thought he was quitting..."
                    ear "...So I told him to take some time off."
                    show earl 1
                    show player 12
                    player_name "Did he mention where he would be while off duty?"
                    show player 5
                    show earl 2
                    ear "I didn't want to ask too many questions, you know?"
                    ear "Sometimes guys just need some alone time..."
                    show earl 1
                    show player 14
                    player_name "Alright, thanks."
                    hide player
                    hide earl
                    with dissolve
                    $ M_mia.set('questioned earl', True)
                    jump police_office_dialogue
        else:

            player_name "Just passing by, Sir."
            show earl 2
            show player 1
            ear "Alright then."
    hide earl
    hide player
    with dissolve
    $ callScreen(location_count)

label police_yumi_dialogue:
    scene police_c_3 with None
    show yumi 2 at right
    show player 1 at left
    with dissolve
    yum "Hello, are you a visitor or are you here to post bail?"
    show yumi 1
    menu:
        "Donuts." if M_mia.get_state() == S_mia_impress_harold:
            show player 14 at left
            show yumi 1 at right
            player_name "I know you only recently started working with him..."
            show yumi 3
            player_name "... But would you happen to know what kind of donuts {b}Harold{/b} likes?"
            show player 1
            show yumi 4
            yum "Huh?"
            yum "Why do you ask?"
            show yumi 1
            show player 14
            player_name "Oh, I'm... trying to get him to like me."
            show player 1
            show yumi 2
            yum "Huh. That's... strange."
            show player 14
            show yumi 1
            player_name "I know, but I'm friends with his daughter and-"
            show player 11
            show yumi 2
            yum "You don't need to explain. I think I got the picture."
            show player 1
            yum "Well, every time we visit the donut shop... he puts {b}[harold_topping]{/b} on the top of his donuts."
            show player 14
            show yumi 1
            player_name "Really?"
            show player 1
            show yumi 2
            yum "Yeah, he always gets that topping."
            show player 17
            show yumi 1
            player_name "Okay, thanks for helping me!"
            show player 1
            show yumi 2
            yum "No problem!"

        "{b}Harold{/b}." if M_mia.get_state() == S_mia_clues:
            show player 12
            player_name "Do you know where {b}Harold{/b} could be?"
            player_name "I need to err...return something to him!"
            show player 5
            show yumi 4
            yum "You know, I saw him just this morning!"
            yum "He looked...off...and smelled like alcohol..."
            show yumi 3
            show player 10
            player_name "Alcohol?!"
            show player 11
            show yumi 4
            yum "Yeah, but don't tell anyone!"
            yum "The poor guy's been having problems with his wife."
            yum "I just don't get it, you know? He's such a nice guy..."
            yum "...I think he deserves better, that's for sure!"
            show yumi 3
            show player 12
            player_name "You don't know where he went after this morning do you?"
            show player 5
            show yumi 4
            yum "Hmm... I'm not sure, but he took his car."
            show yumi 3
            show player 35
            player_name "So he went for a drive somewhere..."
            show player 14
            player_name "...Alright, thanks!"
            hide player
            hide yumi
            with dissolve
            $ M_mia.set('questioned yumi', True)
            jump police_basement_dialogue
        "Just visiting.":

            show player 14 at left
            show yumi 1 at right
            player_name "I'm just here to visit someone."
            show yumi 2
            show player 1
            yum "Sure. Make sure you leave your backpack in the bin, and stay behind the line."
            yum "There's no touching allowed."
    hide player
    hide yumi
    with dissolve
    $ callScreen(location_count)