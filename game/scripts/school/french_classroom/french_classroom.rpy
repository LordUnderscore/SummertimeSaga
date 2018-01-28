label classroom_dialogue:
    $ location_count = "French Classroom"
    if classroom_count == 0:
        scene classroom
        show player 1 at left with dissolve
        show teacher 2 at right with dissolve
        bis "There you are!"
        show player 2 at left
        show teacher 1 at right
        player_name "Hi, {b}Mrs. Bissette{/b}!"
        show player 2 at left
        show teacher 5 at right
        bis "Listen, {b}[firstname]{/b}, I know you've had some personal matters to take care of, and that's why you've been absent lately..."
        bis "...But is everything okay?"
        show player 24 at left
        show teacher 4 at right
        player_name "Yeah. I think I should be okay..."
        show player 5 at left
        show teacher 6 at right
        bis "Your grades have been declining recently, but I'll give you extra time to hand in your {b}homework{/b}..."
        show teacher 5 at right
        show player 87 at left
        bis "Just complete it at home on your {b}computer{/b}, and give it back to me when it's done!"
        show player 13 at left
        show teacher 1 at right
        player_name "Thank you, {b}Mrs. Bissette{/b}!"
        player_name "Your class is my favorite! I'll do my best!"
        show player 1 at left
        show teacher 3 at right
        bis "It's no problem at all, {b}[firstname]{/b}!"
        bis "...And visit the {b}library{/b} to pick up some {b}school books{/b} that'll help you complete your {b}homework{/b}! Every little trick helps!"
        hide player 1 at left with dissolve
        hide teacher 1 at right with dissolve

        $ inventory.items.append(homework)
        if quest01 not in completed_quests:
            $ quest_list.append(quest01)

        show unlock18 at truecenter
        $ renpy.pause()
        hide unlock18 with dissolve

        show unlock5 at truecenter
        $ renpy.pause()
        hide unlock5 with dissolve
        $ loc_library_unlocked = True

        show evedesk 1 at left with dissolve
        eve "Wow... I thought you were dead for sure!"
        show evedesk 2 at left
        player_name "What?... What do you mean?"
        show evedesk 1 at left
        eve "I dunno... You've been missing all month, and people started making up rumours about how your family had been murdered or something..."
        show evedesk 3 at left
        player_name "Ugh... It's nothing like that!"
        show evedesk 4 at left
        eve "I figured. People just like to talk, and this school is just a big joke."
        eve "I'm glad our last year is almost over..."
        show evedesk 5 at left
        player_name "Yeah, I know what you mean."
        show evedesk 6 at left
        eve "You should hang out with us at the {b}park{/b} sometime... Avoid all these idiots around school and chill, you know?"
        show evedesk 5 at left
        eve "Make sure you come by at {b}night{/b}... it's usually when we go out there."
        player_name "Ehh... I guess I could come by one night."
        show evedesk 6 at left
        eve "It's up to you. Do whatever you want!"
        hide evedesk 6 at left with dissolve

        show unlock2 at truecenter
        $ renpy.pause()
        hide unlock2 with dissolve
        $ loc_park_unlocked = True

        $ classroom_count = 1
        $ stairs_count = 3
        $ left_hall_count = 0
        $ map_talk_count = 1
        $ unlock_ui()
        $ bed_locked = 1
        $ event_outside_school_count = 1
        $ erik_door_count = 1
        $ gTimer.tick()
        jump map_dialogue
    $ callScreen(location_count)

label teacher_button_dialogue:
    scene location_classroom_closeup
    show player 1 at left with dissolve
    show teacher 2 at right with dissolve
    bis "Hi, {b}[firstname]{/b}!"
    show player 17 at left
    show teacher 1 at right
    player_name "Hi, {b}Mrs. Bissette{/b}!"
    show player 1 at left
    show teacher 2 at right
    bis "Have you been able to catch up on your studies?"
    bis "I hope you're catching up on your studies!"
    bis "Now, is there something you wanted to talk about?"
    show teacher 1
    menu:
        "Not really.":
            show player 14
            player_name "No. I just wanted to say hello."
            show teacher 2
            show player 13
            bis "Well, take a seat. Class will be starting soon!"
            show teacher 3
            bis "I've got an exciting lesson planned for today!"
            show teacher 1
            show player 2
            player_name "Sounds good, {b}Mrs. Bissette{/b}."

        "I'm done!" if homework1 in inventory.items or homework_handed:
            if homework_handed:
                show player 14 at left
                show teacher 1 at right
                player_name "Now that I gave you my {b}homework{/b}, Is there anything I should do?"
                show teacher 3
                show player 1
                bis "I mark it during class, and give it to you after!"
                show teacher 2
                bis "Take a seat, and {b}stay for the class{/b}. I'll come see you later..."
                hide teacher 2 at right with dissolve
                hide player 1 at left with dissolve
            else:

                show player 17 at left
                show teacher 1 at right
                player_name "I just finished your first {b}homework{/b}!"
                show player 239_240
                pause
                show player 86 at left
                player_name "Here it is!"
                show teacher 6 at right
                show player 13 at left
                bis "Already? That was fast! It usually takes students much longer!"
                show teacher 3 at right
                show player 29 at left
                player_name "I told you I liked your class!!"
                bis "You're so sweet!"
                show teacher 2 at right
                bis "...If only I had more students like you..."
                show teacher 11 at right
                show player 13 at left
                bis "Hmm..."
                show teacher 12 at right
                show player 11 at left
                bis "Why don't you stay {b}after class{/b}? I can give you back your graded {b}homework{/b}!"
                show teacher 13 at right
                show player 14 at left
                player_name "Uhm... Sure, {b}Mrs. Bissette{/b}!"
                show teacher 12 at right
                show player 1 at left
                bis "Take a seat and {b}stay for the class{/b}. I'll come see you after..."
                $ inventory.items.remove(homework1)
                $ homework_handed = True
                hide teacher 12 at right with dissolve
                hide player 1 at left with dissolve
        "Working on it.":

            show player 10 at left
            show teacher 12 at right
            player_name "I'm not done yet, but I'm working on it!"
            show player 5 at left
            show teacher 2 at right
            bis "That's all right, take as much time as you need..."
            show teacher 3 at right
            show player 13 at left
            bis "...And remember to visit the {b}Library{/b}!"
            bis "You can find useful {b}school books{/b} there!"
            show teacher 1 at right
            show player 2 at left
            player_name "Thank you, {b}Mrs. Bissette{/b}!"
            hide teacher 1 at right with dissolve
            hide player 2 at left with dissolve
        "Chat.":

            show player 29 at left
            show teacher 1 at right
            player_name "{b}Mrs. Bissette{/b}, I just wanted to say that I really appreciate the help with catching up on my school work!"
            show player 13 at left
            show teacher 3 at right
            bis "It's my pleasure! All I want is to make sure that you are motivated to perform..."
            show teacher 12 at right
            bis "...And I love rewarding hard working students!"
            show teacher 13 at right
            show player 10 at left
            player_name "I'll do my best. I really want to get into a good college..."
            show teacher 2 at right
            show player 13 at left
            bis "That's what I like to hear!"
            bis "I can review your {b}homework{/b} with you when you hand it in, if you want!"
            show teacher 1 at right
            show player 17 at left
            player_name "That sounds good, {b}Mrs. Bissette{/b}! Thank you!"
            hide teacher 1 at right with dissolve
            hide player 17 at left with dissolve
    $ callScreen(location_count)

label class_started:
    scene classroom
    show player 12 with dissolve
    player_name "( Classes have already started! There's only a few hours left... )"
    show player 35
    player_name "( I should sit in class in the morning so I can follow the lecture! )"
    hide player 35 with dissolve
    $ callScreen(location_count)

label school_closing_dialogue:
    scene classroom
    show player 1 with dissolve
    player_name "( I should go home, school is closing soon. )"
    hide player
    $ callScreen(location_count)

label class_study01:
    if class_study_count == 0:
        show studyclass01 with dissolve
        show text "It felt good to be back in class after a month off." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass02 with dissolve
        show text "I spent the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass03 with dissolve
        show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass04 with dissolve
        show text "It's hard to keep focus when I've had little sleep lately." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass05
        show text "But I always can count on my classmates to keep me awake..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass06
        show text "They have been picking on me lately...\nProbably because I just came back and now I'm the center of attention..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass07
        show text "Don't get me wrong though. I can stand my ground..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass08 with hpunch
        show text "...but I guess this is just how school goes.\nWell, at least the day is over and I can go home now..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        $ class_study_count = 1

        hide studyclass01
        hide studyclass02
        hide studyclass03
        hide studyclass04
        hide studyclass05
        hide studyclass06
        hide studyclass07
        hide studyclass08 with dissolve

        if homework_handed == True:
            jump homework_handed_dialogue
        scene black with dissolve
        show unlock21 at truecenter with dissolve
        $ renpy.pause()
        hide unlock21 with dissolve
        $ gTimer.tick()
        $ pStats.increase("int")
        if gTimer.is_evening():
            jump night_closed_school
        $ callScreen(location_count)
    else:

        show studyclass01 with dissolve
        show text "I sit down at my desk and begin another day in class..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass02 with dissolve
        show text "I spend the whole day trying to catch up to my studies..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass03 with dissolve
        show text "...until the bell rang." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass04 with dissolve
        show text "It's hard to keep focus when I've had little sleep lately.\nAt least the day is over and I can go home now..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        if homework_handed == True:
            jump homework_handed_dialogue

        hide studyclass01
        hide studyclass02
        hide studyclass03
        hide studyclass04 with dissolve
        scene black with dissolve
        with Pause(0.5)
        $ pStats.increase("int")
        $ gTimer.tick()
        if gTimer.is_dark():
            jump night_closed_school
        $ callScreen(location_count)

label homework_handed_dialogue:
    if homework_count == 0:
        scene classroom_night
        show desk 1 at Position (xpos = 400, ypos = 768) with dissolve
        show teacher 7 at right with dissolve
        bis "Thanks for staying after class!"
        show teacher 8 at right
        show desk 2
        bis "I just wanted to give you back your {b}homework{/b}, and talk about your progress..."
        show teacher 9 at right
        show desk 4
        player_name "Did I do bad?"
        show desk 3
        $ inventory.items.append(homework2)
        $ homework_done = False
        player_name "..."
        show desk 6
        player_name "I got a {b}C+{/b}..."
        show desk 5
        show teacher 10 at right
        bis "Don't worry!"
        bis "You did fine, considering you were behind everyone else!"
        show teacher 9 at right
        show desk 6
        player_name "I'm not sure I can do it {b}Mrs. Bissette{/b}..."
        show teacher 10 at right
        show desk 5
        bis "Don't say that!"
        hide teacher
        show desk 7 at Position (xpos = 450, ypos = 768)
        bis "You have to keep working at it."
        show desk 8 at Position (xpos = 371, ypos = 768)
        bis "...you're such a strong student..."
        player_name "..."
        show desk 9 at Position (xpos = 373, ypos = 768)
        bis "...There's nothing I like more..."
        show desk 10
        bis "...than to {b}motivate{/b} my students..."
        bis "...and I'm very good at it..."
        show desk 11
        player_name "...Yeah..."
        show desk 8 at Position (xpos = 371, ypos = 768)
        bis "Very good!"
        show desk 12 at Position (xpos = 450, ypos = 768)
        bis "Now finish more of your {b}homework{/b} at home and come back to me when you're done..."
        bis "...I'm sure you can do better than a {b}C+{/b}!"
        show desk 13
        player_name "Y... Yes! {b}Mrs. Bissette{/b}!"
        show desk 12
        bis "Good boy..."
        $ gTimer.tick(3)
        $ homework_handed = False
        $ homework_count = 1
        $ M_mia.trigger(T_mc_homework)
        hide desk 12 with dissolve

    elif homework_count == 1:
        scene classroom_night
        show desk 1 at Position (xpos = 400, ypos = 768) with dissolve
        show teacher 7 at right with dissolve
        bis "Thanks for staying after class with me again..."
        show teacher 8 at right
        show desk 2
        bis "I just wanted to give you back your {b}homework{/b} and talk about your progress..."
        show teacher 9 at right
        show desk 4
        player_name "How did I do this time?"
        show desk 21
        $ inventory.items.append(homework3)
        player_name "..."
        show desk 22
        player_name "I got a {b}B+{/b}!"
        hide teacher
        show desk 7 at Position (xpos = 450, ypos = 768)
        bis "That's right!"
        show desk 12
        bis "You did better than the average in the class!"
        show desk 13
        player_name "Wow... That's great news,{b}Mrs. Bissette{/b}!"
        show desk 12
        bis "That's right!"
        bis "And..."
        show desk 14 at Position (xpos = 458, ypos = 768)
        bis "I'm really proud of you, {b}[firstname]{/b}."
        bis "You're showing so much improvement..."
        show desk 15
        player_name "...Oh, y-yeah?"
        show desk 16
        bis "Yeah!"
        bis "And... I'm always willing to..."
        show desk 17 at Position (xpos = 457, ypos = 768)
        bis "...{b}reward{/b}..."
        show desk 18 at Position (xpos = 458, ypos = 768)
        bis "...students with straight {b}A{/b}'s."
        player_name "!!!"
        show desk 16
        bis "Just..."
        bis "Keep on showing me your desire to succeed..."
        show desk 19
        bis "And..."
        show desk 20
        bis "I'll make sure to return the favor..."
        player_name "..."
        show desk 12 at Position (xpos = 450, ypos = 768)
        bis "Would you like that?"
        show desk 13
        player_name "Y... Yes! {b}Mrs. Bissette{/b}!"
        show desk 12
        bis "Good boy..."
        hide desk with dissolve
        $ gTimer.tick(3)
        $ homework_handed = False
        $ homework_count = 2
    else:

        scene classroom_night
        show popup_unfinished at truecenter with dissolve
        $ renpy.pause()
        hide popup_unfinished with dissolve
        $ callScreen(location_count)
    jump night_closed_school