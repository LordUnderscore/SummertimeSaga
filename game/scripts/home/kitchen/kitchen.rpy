default first_revealing = True

label home_kitchen_dialogue:
    $ location_count = "Kitchen"
    if mom_count == 3:
        $ mom_door_count = 1

    if not gTimer.is_dark():
        if quest18 in quest_list and not mother.known(mom_dinner_outfit):
            scene homekitchen with None
            show player 1 at left
            show mom 62 at right
            with dissolve
            mom "{b}[firstname]{/b}, do you have a minute? I need some help."
            show player 14
            show mom 61
            player_name "Of course, {b}Mom{/b}. What do you need?"
            show player 1
            show mom 62
            mom "I want you to tell me what you think of the outfit I plan on wearing to dinner with {b}Aunt Diane{/b}."
            mom "Give me a moment, I gotta head to {b}my room{/b} so I can put it on."
            hide mom with dissolve
            scene home_livingroom_b
            show player 14
            player_name "{b}Mom{/b} hasn't dressed up for an occasion in a long time..."
            show player 11
            mom "Sweetie!"
            mom "Could you come in here for a second?"
            show player 2
            player_name "I should go check up on her."
            hide player with dissolve
            $ ui_lock_count = 1
            $ mother.add_event(mom_dinner_outfit)
            jump home_livingroom_dialogue

        elif gTimer.is_morning() and sister.over(sis_telescope01) and not sister.known(sis_breakfast):
            scene homekitchen with None
            show player 1 at left
            show mom 2 at right
            with dissolve
            mom "Hey, Sweetie!"
            mom "Hungry for some breakfast?"
            show mom 51 at Position(xpos=1025)
            show player 10
            player_name "I don't know If I have time, {b}Mom{/b}."
            if gTimer.is_weekend():
                player_name "I have to meet {b}Erik{/b} at his house..."
            else:
                player_name "I'm running late for school."
            show player 11
            show mom 52
            mom "Honey, you have to eat!"
            show player 11
            if gTimer.is_weekend():
                mom "I don't care if your friend {b}Erik{/b} has to wait all day..."
            else:
                mom "I don't care if your school calls me to complain about being late..."
            show player 1
            mom "You can't just go out on an empty stomach!"
            show player 14
            show mom 51
            player_name "I guess I could take a few minutes to eat something..."
            show player 1
            show mom 2
            mom "I prepared some cereal for you in the {b}dining room{/b}."
            hide player
            hide mom
            with dissolve
            $ ui_lock_count = 1
            $ sister.add_event(sis_breakfast)
            $ callScreen(location_count)

        elif mom_count == 0 and not mom_dialogue_advance:
            scene homekitchen with None
            show player 1 at left with dissolve
            show mom 2 at right with dissolve
            mom "Good morning, Sweetie! I made you some breakfast!"
            mom "I thought you'd like something special for your first day back at school."
            show player 2 at left
            show mom 1 at right
            player_name "Thanks, {b}Mom{/b}, but I'm not really hungry, and I see that I'm running late for school, so..."
            show player 1 at left
            show mom 2 at right
            mom "Aren't you waiting for {b}Erik{/b}?"
            show player 2 at left
            show mom 1 at right
            player_name "Nah, he's still sleeping. I'll probably meet him at his house on the way."
            show player 1 at left
            show mom 3 at right
            mom "Oh! By the way: I spoke with {b}Aunt Diane{/b}, and she's willing to pay you, if you {b}help her clean her garden{/b} this summer!"
            mom "It could be a good way to {b}earn{/b} some money for college, don't you think?"
            show player 4 at left
            show mom 1 at right
            player_name "Hmm... Yeah, I could do that. I should go visit her to see what she needs."
            hide player 4
            show mom 4 at right
            mom "Come here, Sweetie..."
            mom "I know it's been hard without your {b}Dad{/b} around..."
            mom "We'll get through this. I promise things will get better."
            show mom 5 at right
            player_name "I know, {b}Mom{/b}..."
            hide mom 5 at right with dissolve

            show unlock14 at truecenter
            $ renpy.pause()
            hide unlock14 with dissolve

            show unlock12 at truecenter
            $ renpy.pause()
            hide unlock12 with dissolve

            call screen mom_name_input
            if mom_name != "":
                $ mom = Character('[mom_name]', color="#ff6df0")

            $ mom_dialogue_advance = True
            $ ui_lock_count = 0
            $ callScreen(location_count)

        elif mom_count == 3 and not mom_dialogue_advance and quest17 not in quest_list and not gTimer.is_morning() or mom_count == 3 and not mom_dialogue_advance and quest17 not in quest_list and shower != "mom":
            scene homekitchen with None
            show player 2 at left with dissolve
            show mom 1 at right with dissolve
            player_name "Hey, {b}Mom{/b}, anything I can do to help around the house?"
            show player 1
            show mom 2
            mom "Yes! The pipe under the {b}bathroom sink{/b} is leaking."
            show mom 3
            mom "I was going to call a repair man, but if you could fix it, that'd be great!"
            show mom 1
            show player 2
            player_name "Sure! I'll try to fix it."
            show mom 2
            show player 1
            mom "Anything else you wanted to talk about?"
            show mom 1
            hide mom
            hide player
            $ ui_lock_count = 1
            $ quest_list.append(quest17)

        elif mom_count == 5 and not mom_dialogue_advance and gTimer.is_afternoon() or mom_count == 5 and not mom_dialogue_advance and gTimer.is_morning() and shower != "mom":
            scene location_home_kitchen_blur with None
            show player 1 at left
            show mom 2 at right
            with dissolve
            mom "Hey, Sweetie!"
            show mom 1
            show player 2
            player_name "Hi, {b}Mom{/b}."
            player_name "Anything I can help you with?"
            show mom 2
            show player 1
            mom "No. I just..."
            mom "...You seem to be out a lot lately."
            show mom 1
            show player 2
            player_name "I am?"
            show mom 2
            show player 1
            mom "Yeah... I don't see you at home as much..."
            mom "Which is a good thing!!"
            mom "I was hoping you'd move on, and keep your mind busy."
            mom "But I like to make sure you're okay."
            show mom 1
            show player 2
            player_name "I'm fine, {b}Mom{/b}."
            player_name "Just trying to keep busy with school stuff, you know?"
            player_name "I'm also enjoying the work with {b}Aunt Diane{/b}... and going to the gym..."
            show mom 2
            show player 1
            mom "What about spending time with friends?"
            show mom 1
            show player 2
            player_name "I hang out with {b}Erik{/b} a lot... And other friends from school."
            show mom 2
            show player 11
            mom "Are any of those friends... girls?"
            show mom 1
            show player 10
            player_name "{b}Mom{/b}..."
            show mom 2
            show player 11
            mom "What?"
            mom "You are a handsome young man! I'm sure girls are giving you some attention at school..."
            show player 10
            show mom 1
            player_name "I don't know. I guess?"
            show mom 2
            show player 11
            mom "What's her name?"
            show mom 1
            show player 10
            player_name "{b}Mom{/b}!!"
            show mom 52
            show player 11
            mom "Are you guys dating or something? You can tell me, you know..."
            show mom 51
            show player 10
            player_name "It's not like that, {b}Mom{/b}."
            show mom 52
            show player 11
            mom "Have you kissed her?"
            show mom 51
            player_name "..."
            show mom 52
            mom "Do you know how?"
            show mom 51
            show player 10
            player_name "Not really."
            show mom 3
            show player 11
            mom "It's okay, Sweetie."
            show mom 2
            mom "I could... teach you, if you'd like..."
            show mom 1
            player_name "!!!" with hpunch
            show player 10
            player_name "{b}Mom{/b}, this is awkward..."
            show mom 2
            show player 11
            mom "Why? It's fine!"
            mom "If anyone is going to teach you the right way, it may as well be me."
            mom "You want to make a good first impression, right?"
            show mom 1
            show player 14
            player_name "I... I guess it could help..."
            player_name "You want to teach me right now?"
            show mom 3
            show player 1
            mom "Better now, than later."
            show mom 51
            show player 14
            player_name "What do I do?"
            show mom 52
            show player 1
            mom "Here. Come closer."
            show player 227 at Position(xpos=200)
            show mom 77 at Position(xpos=650)
            with dissolve
            player_name "..."
            mom "Now place your hands around my hips and close your eyes..."
            mom "...then press your lips gently against mine..."

            hide player
            show mom 79
            with hpunch
            pause
            show mom 80
            pause
            show mom 79
            pause
            show mom 80
            pause
            show mom 79
            pause
            show player 11 at left
            show mom 87 at right
            with dissolve
            mom "!!!"
            show mom 88
            mom "Oh my..."
            show player 10
            show mom 87
            player_name "Did I do something wrong??"
            show mom 63
            show player 11
            mom "You don't always have to use your tongue."
            show mom 61
            show player 10
            player_name "I, I didn't know."
            show mom 62
            show player 1
            mom "It's okay. You were... Quite good."
            show mom 61
            show player 21
            player_name "Oh yeah?"
            show mom 62
            show player 1
            mom "I think there's a lucky girl out there waiting to find out!"
            show mom 61
            show player 2
            player_name "Thanks, {b}Mom{/b}."
            show mom 87
            show player 11
            mom "..."
            show mom 62
            mom "Uhh, you must have things to attend to."
            show player 1
            mom "Have a good day, Sweetie!"
            hide mom
            hide player
            with dissolve
            $ learn_kissing = True
            $ mom_dialogue_advance = True

        elif (mom_count == 7 and not mom_dialogue_advance and quest16 not in quest_list and gTimer.is_afternoon()) or (mom_count == 7 and not mom_dialogue_advance and quest16 not in quest_list and is_here("mom")):
            scene homekitchen with None
            show player 203 at left with dissolve
            show mom 2 at right with dissolve
            mom "Hey Sweetie I need you to do another thing for me."
            show player 2
            show mom 1
            player_name "What is it?"
            show player 1
            show mom 13
            mom "Can you look at the car and see why it's not starting?"
            show mom 1
            show player 10
            player_name "I thought you just had it out a couple weeks ago?"
            show player 1
            show mom 13
            mom "I did. For some reason it won't even start now."
            show mom 1
            show player 2
            player_name "Maybe you left the lights on and the battery's dead. I'll give it a try."
            show mom 2
            show player 1
            mom "Thanks! I left the keys in the car so you can try to start it."
            show mom 1
            show player 14
            player_name "Okay!"
            $ quest_list.append(quest16)

        elif (mom_count == 7 and not mom_dialogue_advance and mother.started(mom_broken_engine) and gTimer.is_afternoon()) or (mom_count == 7 and not mom_dialogue_advance and mother.started(mom_broken_engine) and is_here("mom")):
            scene homekitchen with None
            show player 10 at left with dissolve
            show mom 61 at right with dissolve
            player_name "I found out why the car wont start..."
            show player 5
            show mom 63
            mom "Oh?! Did you fix it already?"
            show mom 61
            pause
            show player 25
            player_name "It's pretty bad, {b}Mom{/b}... I don't think I can fix it."
            show player 5
            show mom 39
            mom "Oh."
            show mom 38
            show player 10
            player_name "The engine is completely busted... I think we might have to replace it."
            player_name "It could be expensive..."
            show player 5
            pause
            show mom 60
            mom "Well. We do have insurance. Try and see what the car dealership will do for us."
            mom "Hopefully, they'll cover most of the repairs, otherwise..."
            show mom 39
            mom "I don't know what we'll do, Sweetie."
            show mom 38
            pause
            show player 10
            player_name "It'll be alright, {b}Mom{/b}. I'll see if the {b}dealership{/b} can help us."
            show player 5
            pause
            show player 14
            player_name "I'll get it fixed."
            player_name "One way or another."
            show mom 61
            show player 13
            pause
            show mom 62
            mom "It's good to have your support, Sweetie."
            mom "Thank you."
            show expression "boxes/popup_car.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_car.png"
            $ mom_broken_engine.finish()
            $ loc_dealership_unlocked = True

        elif mom_count == 8 and not mom_dialogue_advance and mom_revealing and shower != "sister" and henchmen_count > 1:
            scene location_home_kitchen_blur with None
            show mom 2 at right with dissolve
            show player 1 at left with dissolve
            mom "Hey, Sweetie..."
            show player 14
            show mom 1
            player_name "Hi, {b}Mom{/b}."
            show player 1
            show mom 2
            mom "Are you busy right now?"
            show player 14
            show mom 1
            player_name "Not really."
            player_name "Do you need something?"
            show player 1
            show mom 2
            mom "Well..."
            mom "Your sister is in her room right now and.."
            mom "I thought maybe we could take a quick shower together..."
            show player 11
            show mom 1
            player_name "..."
            show player 21
            player_name "Oh... Sure!"
            show player 1
            show mom 2
            mom "I... I have a little something to show you..."
            show player 11
            show mom 1
            player_name "!!!"
            show player 29
            player_name "I’d love to find out."
            player_name "You want to... Do it now?"
            show player 1
            show mom 3
            mom "I’ll meet you in the shower, Sweetie."
            hide player
            hide mom
            scene location_home_kitchen
            with dissolve
            $ mom_dialogue_advance = True
            jump mom_shower_question

        elif mom_count == 10 and not mom_dialogue_advance and quest18 not in quest_list and quest18 not in completed_quests and shower != "mom":
            scene location_home_kitchen_blur with None
            show mom 2 at right with dissolve
            show player 203 at left with dissolve
            mom "Hey Sweetie I’m glad you’re here."
            show mom 3
            mom "Diane’s going to be over tonight."
            show mom 2
            show player 11
            mom "I don't know why, but she was very persistent about it."
            mom "Anyway, I need you to pick up some {b}sea trout{/b} at the {b}pier{/b}."
            mom "It’s {b}Diane's{/b} favorite fish, and I want to give her something special with the dinner."
            show mom 1
            show player 2
            player_name "{b}Aunt Diane{/b} is coming over? That’s a surprise!"
            player_name "It’ll be good for her to be here; she doesn’t do much at her home."
            player_name "The family hasn’t been together since the funeral, either."
            player_name "I’ll make sure to get that {b}sea trout{/b}, so the dinner's great for aunt Diane."
            show expression "boxes/popup_pier.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pier.png"
            $ loc_pier_unlocked = True
            $ quest_list.append(quest18)

    if mom_count == 1 and not mom_dialogue_advance:
        scene expression gTimer.image("homekitchen{}") with None
        show mom 6 at right with dissolve
        mom "I've told you already! I don't {b}KNOW{/b} where the money is..."
        mom "My husband... He never said anything to us!"
        show mom 7 at right
        mom "But-"
        show mom 6 at right
        mom "We don't have anything!!"
        show mom 7 at right
        mom "..."
        show mom 6 at right
        mom "Is this a {b}threat{/b}?!"
        mom "If you call us again, I-"
        show mom 8 at right with hpunch
        mom "Just leave us {b}ALONE!!!{/b}"
        show mom 9 at right
        show player 10 at left with dissolve
        player_name "..."
        player_name "...{b}Mom{/b}?"
        player_name "...Are you okay?"
        show player 5 at left
        show mom 11 at right
        mom "It's okay, Sweetie."
        show mom 10 at right
        show player 10 at left
        player_name "Are you sure? It sounded pretty bad..."
        show player 5 at left
        show mom 11 at right
        mom "It's nothing to worry about..."
        show mom 10 at right
        show player 5 at left
        player_name "..."
        show player 10 at left
        player_name "I could try and find another job. Maybe I can come up with some money for you."
        show player 5 at left
        show mom 11 at right
        mom "Don't."
        mom "This has nothing to do with us."
        show mom 10 at right
        show player 10 at left
        player_name "As long as you're okay, {b}Mom{/b}."
        hide player 10 at left
        show mom 12 at right
        with dissolve
        mom "We'll be allright. I promise."
        hide mom 12 at right with dissolve
        $ mom_dialogue_daily = True
        $ mom_dialogue_advance = True
        $ ui_lock_count = 0
        $ bed_locked = 1
        $ player_room_count = 3
        $ door20_locked_count = 1
        $ callScreen(location_count)

    elif mom_count == 9 and mom_dialogue_advance == False and gTimer.is_evening() and mom_revealing:
        scene homekitchen_secret with None
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        dia "Well, it's good that he's been helping you around the house."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "I know, it's just..."
        mom "He's so... affectionate towards me lately..."
        show aunt 122 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "He's your only son!"
        show aunt 121
        dia "He probably feels like he needs to protect you..."
        dia "Especially after all that's been happening with you guys."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 17f at Position(xpos=0.3318,ypos=1.1130)
        mom "It's not that... I feel like, the way he looks at me you know?"
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        dia "..."
        show aunt 121
        dia "What do you mean?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "Well, a little while ago I.. I started noticing things..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "...Like?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "Like, asking me to teach him how to kiss..."
        mom "And... touching me in certain ways..."
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "..."
        show mom 60f
        mom "And the other day, I find him, on my bed... playing with himself!"
        mom "With my underwear!"
        show aunt 121
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        dia "What did you do?!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "I left!"
        mom "And I told him to not do that kind of stuff in my room, but..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "But, what?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f at Position(xpos=0.3318,ypos=1.000)
        mom "He did it again! And then said that he had urges - that he just couldn't control it..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "...So?"
        show aunt 124
        show mom 17f at Position(xpos=0.3318,ypos=1.1130)
        mom "So I let him do it... as I watched."
        show aunt 121
        show mom 20f at Position(xpos=0.3318,ypos=1.1130)
        dia "You watched him masturbate?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f at Position(xpos=0.3318,ypos=1.000)
        mom "What else was I supposed to do..."
        mom "I was just trying to help him get it over with..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "You're naughty..."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "There's more..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "Really?!"
        dia "What else?!"
        show aunt 124
        show mom 60f
        mom "We've been... taking showers together..."
        show aunt 121
        show mom 59f
        dia "Wow..."
        show aunt 125
        dia "How is he?"
        show aunt 124
        show mom 60f
        mom "Diane!!"
        show aunt 122
        show mom 59f
        dia "What?!"
        show aunt 123
        dia "Oh, come on! You can tell me!"
        show aunt 124
        show mom 60f
        mom "... What do you want to know?"
        show aunt 125
        show mom 59f
        dia "Did you... touch him?"
        show aunt 126
        show mom 60f
        mom "I washed him..."
        show aunt 125
        show mom 59f
        dia "All the way?"
        show aunt 126
        show mom 60f
        mom "Well, yeah..."
        show aunt 125
        show mom 59f
        dia "How was he?"
        show aunt 126
        show mom 60f
        mom "What do you mean by that?"
        show aunt 125
        show mom 59f
        dia "Was he... big?"
        show aunt 126
        show mom 60f
        mom "!!!"
        mom "He was... actually quite... large."
        show aunt 125
        show mom 59f
        dia "Oh, my!"
        dia "I bet you liked it."
        show aunt 126
        show mom 16f at Position(xpos=0.3318,ypos=1.1130)
        mom "He's a young and handsome boy, but he's also my son."
        show aunt 125
        show mom 15f
        dia "Wait, have you guys... had sex?"
        show aunt 126
        show mom 16f
        mom "No!! Of course not..."
        show aunt 122
        show mom 15f
        dia "You could have! He obviously wants to!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "I can't do that!"
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "I was just asking..."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "Please tell me that I'm not doing something terribly wrong here..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "It's your decision, but..."
        dia "I think you should let go! Enjoy the intimacy with your son!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "Really? You don't think this is wrong?"
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "You both seem to be enjoying it. What's the wrong in it?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "I suppose..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "If he's going to learn it from somewhere, might as well do it at home! Haha!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "You're laughing, but this is serious, {b}Diane{/b}."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "Just see how it goes. Maybe it's just a phase that he'll grow out of."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 62f at Position(xpos=0.3318,ypos=1.000)
        mom "You might be right..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 61f
        dia "Anyway, I'd better go home. It's getting late."
        dia "We'll continue this another time. I think we still have lots to discuss!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 62f
        mom "Haha. You're becoming my new therapist!"
        show mom 61f
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        dia "See you later, honey."
        scene home_entrance_night
        show player 5
        player_name "( That... was a lot to take in. )"
        player_name "( {b}Mom{/b} seemed really conflicted about all of this... )"
        show player 203
        player_name "( She said she's enjoying it, though. )"
        player_name "( Either way, I have to thank {b}Aunt Diane{/b} for making it seem normal. )"
        $ mom_dialogue_advance = True
        jump home_entrance
    $ mom_dialogue_daily = True
    $ callScreen(location_count)

label mom_button_dialogue:
    if mom_count == 0 and mom_dialogue_advance:
        scene location_home_kitchen_closeup with None
        show player 1 at left with dissolve
        show mom 2 at right with dissolve
        mom "Hey Sweetie! Shouldn't you get going?"
        show player 2 at left
        show mom 1 at right
        player_name "Yeah. I was on my way."
        hide player 2 at left with dissolve
        hide mom 1 at right with dissolve

    elif not gTimer.is_dark() and not mom_masturbating:


        scene expression gTimer.image("location_home_kitchen{}") with None
        if mom_revealing:
            show momobj 2 at Position(xpos=590,ypos=768)
            if first_revealing:
                show player 5 at left with dissolve
                player_name "!!!"
                player_name "( {b}Mom{/b} is so hot... )"
                player_name "( And her ass is sticking out like that... )"
                show player 1
                player_name "( Should I... )"
                $ first_revealing = False
            menu:
                "Feel Ass" if mom_count < 9:
                    player_name "( I want to touch her so bad... )"
                    player_name "( But what if she gets mad? )"
                    player_name "( I really shouldn't. )"
                    hide momobj 2 with dissolve

                "Feel Ass" if mom_count >= 9:
                    scene location_home_kitchen_closeup
                    show mom 47 at Position(xpos=656,ypos=768)
                    with dissolve
                    pause
                    show mom 48 at Position(xpos=660,ypos=768) with dissolve
                    player_name "( Did she notice? )"
                    hide mom 48
                    show moms 49_50 at Position(xpos=660,ypos=768)
                    pause 4
                    mom "Sweetie, you shouldn't be doing this..."
                    hide moms 49_50
                    show mom 50 at Position(xpos=665,ypos=768)
                    mom "Not here..."
                    scene homekitchen
                    show player 1 at left
                    show mom 52 at right
                    with dissolve
                    mom "{b}*whispers*{/b} What if your {b}sister{/b} sees us?"
                    show mom 51 at right
                    show player 21
                    player_name "Sorry. It was too tempting..."
                    show player 1
                    show mom 52
                    mom "I don't really mind it..."
                    mom "...but, these things {b}must{/b} stay in the bedroom, okay?"
                    mom "We can't get caught doing this."
                    show mom 2
                    mom "Now, is there something you wanted to talk about?"
                    show mom 1
                    jump mom_options
                "Talk":

                    scene location_home_kitchen_closeup
                    hide momobj
                    show mom 1 at right
                    show player 2 at left
                    with dissolve
                    player_name "Hey {b}Mom{/b}, got a minute?"
                    show mom 2
                    show player 1
                    mom "Need something, {b}[firstname]{/b}?"
                    show mom 1
                    jump mom_options

        show player 1 at left with dissolve
        show mom 2 at right with dissolve
        mom "Hi Sweetie!"
        mom "Is everything okay at school?"
        show player 14 at left
        show mom 1 at right
        player_name "Yeah..."
        show player 13 at left
        show mom 13 at right
        mom "I'm sorry you fell behind at your school after what happened..."
        show mom 14 at right
        show player 14 at left
        player_name "It's okay, {b}Mom{/b}, I'm doing fine!"
        show player 13 at left
        show mom 13 at right
        mom "I'm just checking on my beautiful son, to make sure he's okay!"
        show player 21 at left
        show mom 14 at right
        player_name "Okay, {b}Mom{/b}..."
        player_name "I gotta go."
        show player 13 at left
        show mom 3 at right
        mom "Don't stay out too late!"
        show mom 1
        label mom_options:
            menu:
                "Ask about dad.":
                    show player 10 at left
                    show mom 1 at right
                    player_name "{b}Mom{/b}... What happened to {b}Dad{/b}?"
                    show player 11
                    show mom 60
                    mom "Oh... Sweetie, I..."
                    show mom 59
                    show player 10
                    player_name "Please! I want to know..."
                    show player 11
                    show mom 60
                    mom "I'm sorry... I don't know."
                    mom "The investigation came up with nothing..."
                    mom "They couldn't find any evidence, so they put the case on hold..."
                    show mom 59
                    show player 10
                    player_name "They have to find something eventually, right?"
                    show player 11
                    show mom 60
                    mom "We can only hope."
                    show mom 59
                    pause
                    show mom 60
                    mom "Sweetie..."
                    mom "I want closure as much as you and your {b}sister{/b}..."
                    mom "But we can't let ourselves get dragged down by this."
                    show mom 63
                    mom "You're still a teenager. Live your life."
                    mom "It's what he would've wanted."
                    show player 10
                    show mom 59
                    player_name "Okay. I think I understand..."
                    show player 14
                    show mom 61
                    player_name "Thanks, {b}Mom{/b}."
                    show player 1
                    show mom 2
                    mom "Anything else you wanted to talk about?"
                    show mom 1
                    show player 1
                    jump mom_options

                "Ask about money problems." if mom_count > 1 and henchmen_count < 2:
                    show mom 1
                    show player 10
                    player_name "{b}Mom{/b}, about what you said on the phone back there..."
                    show mom 13
                    show player 11
                    mom "I told you earlier, it's not a big deal."
                    mom "We'll be alright!"
                    show mom 14
                    show player 14
                    player_name "But... What if... I wanted to help you?"
                    player_name "What if I got a real job?"
                    show player 10
                    player_name "I don't like seeing you so stressed out by this..."
                    show mom 52
                    show player 11
                    mom "You're still in school!"
                    mom "I don't think it's wise for you to take up full time work..."
                    mom "Your education is what's most important right now."
                    show mom 51
                    show player 10
                    player_name "I'll work after school, and on weekends!"
                    show mom 53
                    show player 13
                    mom "*sigh* Stubborn like your father..."
                    show mom 59
                    mom "Hmm..."
                    show mom 63
                    mom "You could always check the {b}mail box{/b}!"
                    mom "There should be some job postings in there..."
                    mom "Maybe There's something in there you'll like?"
                    show mom 61
                    show player 18
                    player_name "Thanks {b}mom{/b}, I'll take a look."
                    show mom 62
                    show player 1
                    mom "Anything else you wanted to talk about, Sweetie?"
                    show mom 1
                    jump mom_options

                "Ask about the men in suits." if mom_count > 2 and henchmen_count < 2:
                    show player 10
                    player_name "{b}Mom{/b}, about what that gangster said..."
                    show mom 59
                    player_name "Did you know about {b}Dad{/b}?"
                    show player 11
                    show mom 53
                    mom "{b}*Sigh({/b} I can't keep you in the dark forever..."
                    mom "It was going fine, until a few years ago..."
                    mom "Then your father started gambling, and eventually built up a lot of debt..."
                    mom "He told me he was able to pay it off, so I didn't press the issue too much."
                    mom "Suddenly, the accident happened..."
                    show mom 60
                    mom "And now, they're trying to get the money from us..."
                    show player 10
                    show mom 59
                    player_name "Are you sure we can't tell the police about this?"
                    show player 11
                    show mom 60
                    mom "If what that man said is true... I can't risk them harming you or {b}[sis]{/b}."
                    show player 10
                    show mom 59
                    player_name "Are we going to pay them?"
                    show player 11
                    show mom 60
                    mom "We don't have the money, Sweetie."
                    show mom 53
                    mom "{b}*Sigh({/b} Maybe we should just move away and start fresh..."
                    show player 1
                    show mom 63
                    mom "We'll figure something out."
                    show mom 51
                    show player 2
                    player_name "I'm sure we will, {b}Mom{/b}."
                    show mom 2
                    show player 1
                    mom "Now... Is there something else you wanted to talk about?"
                    show mom 1
                    jump mom_options

                "Help around the house" if mom_count == 2 and not mom_dialogue_advance and quest14 not in quest_list:
                    show player 2
                    player_name "Hey, {b}Mom{/b}, anything I can do to help around the house?"
                    show player 1
                    mom "Hmm..."
                    show mom 2
                    mom "Now that you mention it, the lawn hasn't been mowed in weeks."
                    mom "You can start there, the {b}lawn mower{/b} should be in the {b}garage{/b}."
                    show mom 1
                    show player 2
                    player_name "All right. I'll get on it."
                    show player 1
                    show mom 2
                    mom "Anything else you wanted to talk about?"
                    show mom 1
                    $ quest_list.append(quest14)
                    jump mom_options

                "Help around the house." if mom_count == 2 and not mom_dialogue_advance and quest14 in quest_list:
                    show player 4
                    player_name "( I still have to {b}mow the lawn{/b}. )"
                    show player 1
                    jump mom_options

                "Help around the house." if mom_count == 3 and not mom_dialogue_advance and quest17 in quest_list:
                    show player 4
                    player_name "( I gotta fix the {b}bathroom sink{/b} somehow... )"
                    show player 1
                    jump mom_options

                "Help around the house." if mom_count == 7 and not mom_dialogue_advance and quest16 in quest_list:
                    show player 4
                    player_name "( I have to visit the {b}car dealership{/b}. Maybe they can fix mom's car... )"
                    show player 1
                    jump mom_options

                "Help around the house." if mom_count > 7:
                    show player 2
                    player_name "Hey, {b}Mom{/b}, anything I can do to help around the house?"
                    show player 1
                    mom "Hmm..."
                    show mom 2
                    mom "Nothing I can think of right now, no."
                    show mom 1
                    show player 2
                    player_name "Cool. Let me know if something comes up."
                    show player 1
                    jump mom_options

                "Shower." if henchmen_count == 2:
                    show player 2
                    show mom 1
                    player_name "Hey, {b}Mom{/b}!"
                    player_name "I was wondering..."
                    show player 21
                    player_name "Would you like to take a shower with me?"
                    show player 14
                    show mom 2
                    mom "It is getting pretty hot in the house..."
                    show mom 3
                    mom "Sure! A shower sounds lovely right now."
                    show mom 2
                    mom "Give me a minute. I'll join you after I'm done here."
                    scene shower_closeup
                    show moms 27
                    with dissolve
                    pause
                    show moms 28 at Position(xpos=487,ypos=768) with dissolve
                    pause
                    show moms 34 with dissolve
                    mom "Sorry to keep you waiting, Sweetie..."
                    jump mom_shower_question

                "I fixed the car." if quest16_1 and quest16 not in completed_quests:
                    show player 2
                    show mom 1
                    player_name "Hey {b}Mom{/b} I got the car fixed."
                    show player 203
                    show mom 3
                    mom "Thank you so much, {b}[firstname]{/b}!"
                    show mom 2
                    mom "I'm glad there's a man in the house who can take care of my problems."
                    show player 2
                    show mom 1
                    player_name "No problem, {b}Mom{/b}! I’ll always be here for you."
                    $ completed_quests.append(quest16)
                    $ mom_dialogue_advance = True
                    jump mom_options

                "I have the fish" if quest18 in quest_list and quest18 not in completed_quests and seatrout in inventory.items:
                    player_name "Hey {b}Mom{/b} I have the {b}fish{/b}."
                    show player 2
                    mom "Good job, Sweetie! Now I can finish dinner"
                    show mom 2
                    mom "You can join us in the dining room, when it's done. {b}Aunt Diane{/b} would really like to see you."
                    show player 203
                    $ inventory.items.remove(seatrout)
                    $ completed_quests.append(quest18)
                    $ mom_dialogue_advance = False
                    $ mom_count = 11
                    $ gTimer.tick(3)
                    scene home_entrance_evening
                    show aunt 137 at right
                    show mom 91f
                    with fade
                    dia "I'm so glad to see you!"
                    dia "I don't remember the last time I came over for dinner."
                    show aunt 136
                    show mom 93f
                    mom "I know!"
                    mom "I was starting to think you hated my cooking."
                    show aunt 138
                    show mom 91f
                    dia "Haha."

                    show player 203 at left with dissolve
                    show aunt 137
                    show mom 92f
                    dia "There he is..."
                    dia "The man of the house."
                    show aunt 136
                    show player 14
                    player_name "Good evening, {b}Aunt Diane{/b}."
                    show player 17
                    player_name "You look really nice in that dress!"
                    show aunt 138
                    show player 203
                    dia "Your son really knows how to greet a lady!"
                    show player 13
                    show aunt 136
                    show mom 93f
                    mom "Well, he's always been a charmer..."
                    show aunt 137
                    show mom 91f
                    dia "Well thank you, Handsome!"
                    dia "Is your {b}sister{/b} joining us tonight?"
                    show player 10
                    show aunt 136
                    player_name "She's getting ready, I think."
                    show player 12
                    player_name "She's always in her room. She comes down at the last minute to eat..."
                    show player 203
                    show aunt 138
                    dia "Still a princess, I see."
                    show aunt 137
                    dia "She never changes..."
                    show mom 92f
                    show aunt 136
                    mom "So..."
                    show mom 93f
                    mom "I think you will be pleased to know that we prepared your favorite dish!"
                    show mom 91f
                    show aunt 138
                    dia "Ohh... I can smell it!"
                    show mom 93f
                    show aunt 136
                    mom "Please, come in and sit at the table!"
                    show mom 92f
                    mom "Dinner is ready!"
                    hide mom
                    hide aunt
                    with dissolve
                    show player 24
                    player_name "I should join them in the {b}dining room{/b}."
                    player_name "I'm getting hungry..."
                    hide player
                    with dissolve
                    $ ui_lock_count = 1
                    $ location_count = "Entrance"
                    $ callScreen(location_count)

                "Learn to kiss." if learn_kissing:
                    show player 21 at left
                    show mom 1 at right
                    player_name "I was wondering if you could teach me again..."
                    show player 1
                    show mom 51
                    mom "!!!"
                    show player 14
                    player_name "Teach me how to kiss... Like we did last time."
                    show player 1
                    show mom 52
                    mom "Oh."
                    mom "I don't know if we should."
                    show player 14
                    show mom 51
                    player_name "I really like doing it with you, though."
                    show player 1
                    show mom 52
                    mom "I know, Sweetie..."
                    show player 11
                    mom "But you should try and find a nice girl to do this with."
                    show player 10
                    show mom 51
                    player_name "I'm trying to..."
                    show player 1
                    show mom 52
                    mom "Okay, then. But just one kiss!"
                    show mom 51
                    show player 14
                    player_name "Thanks, {b}Mom{/b}."
                    show player 1
                    show mom 2
                    mom "Step closer to me."
                    show player 227 at Position(xpos=200)
                    show mom 77 at Position(xpos=650)
                    with dissolve
                    player_name "..."
                    hide player
                    show mom 105 at Position(xpos=650)
                    with dissolve
                    mom "Now place your hands around my hips like this..."
                    mom "...Close your eyes..."
                    mom "...Then press your lips gently against mine..."

                    hide player
                    show mom 79
                    with hpunch
                    pause 0.5
                    show mom 80_79
                    pause 3
                    show mom 75 at Position(xpos=650)
                    show player 231 at Position(xpos=234)
                    with dissolve
                    mom "You're becoming quite good at this..."
                    show player 232 at Position(xpos=234)
                    show mom 72
                    player_name "Your lips are so soft, {b}Mom{/b}."
                    show player 231
                    show mom 74
                    mom "..."
                    show player 233
                    show mom 73
                    mom "Oh, my!!!"
                    show player 230 with hpunch
                    show mom 72
                    player_name "!!!"
                    show player 269 at Position(xpos=243)
                    player_name "Sorry..."
                    show mom 73
                    mom "Are you..."
                    mom "Maybe this is going too far."
                    show mom 72
                    player_name "..."
                    show mom 73
                    mom "Perhaps that's enough for today."
                    show mom 59 at right
                    show player 83 at left
                    with dissolve
                    player_name "I didn't mean to, {b}Mom{/b}!"
                    show mom 60
                    show player 82
                    mom "I know..."
                    mom "But It shouldn't have this effect on you..."
                    show mom 59
                    player_name "..."
                    show mom 63
                    mom "We can talk about this later..."
                    show mom 125
                    hide player with dissolve
                    pause
                    show mom 39
                    mom "I should stop these private kissing lessons..."
                    mom "He got... so hard!"
                    show mom 60
                    mom "{b}*Sigh*{/b} Maybe it's just a phase..."
                    show mom 62
                    mom "He's still young and has all these urges..."
                    mom "I suppose it's just natural."
                    show mom 61
                    pause
                    show mom 59 with dissolve
                    pause
                    show mom 53 at Position(xoffset=10) with fastdissolve
                    mom "It was pressing so {b}hard{/b} against my stomach..."
                    show mom 88 with fastdissolve
                    mom "I still can't belive it's that long..."
                    show mom 87
                    pause
                    show mom 61 with fastdissolve
                    pause
                    show mom 53 at Position(xoffset=10) with fastdissolve
                    mom "No."
                    mom "Clear those thoughts out of your mind, {b}[mom_name]{/b}. He's your {b}son{/b}!"
                    show mom 59 with fastdissolve
                    pause
                    show mom 60
                    mom "Does he think about me while he touches himself?"
                    show mom 53 at Position(xoffset=10) with fastdissolve
                    mom "{b}*Sigh*{/b}"
                    mom "I do hope he finds a girlfriend soon. He'll enjoy having her help him out."
                    show mom 59 with fastdissolve
                    pause
                    show mom 53 at Position(xoffset=10) with fastdissolve
                    mom "Now that I think about it, I don't have anyone to help relieve my needs either..."
                    show mom 59 with fastdissolve
                    pause
                    show mom 63
                    mom "Well, it's nice to know I'm not the only one that's going to be sexually frustrated in this house..."
                    mom "Misery sure loves company..."
                    scene bedroom
                    show player 83
                    with fade
                    player_name "Great, now {b}Mom{/b} probably thinks I'm weird..."
                    show player 82
                    pause
                    show player 83
                    player_name "It got so hard when I thought about her naked..."
                    player_name "Lately, it feels like she is the only thing I want to think about."
                    show player 82
                    pause
                    show player 83
                    player_name "I should find something to do, clear my head a little..."
                    hide player with dissolve
                    jump bedroom_dialogue
                "Nevermind.":

                    show player 2
                    player_name "Actually, nevermind, see you later, {b}Mom{/b}."
        $ mom_door_count = 1
        $ mom_dialogue_daily = True
        hide player
        hide mom
        with dissolve
    $ mom_dialogue_daily = True
    $ callScreen(location_count)

label dishes_dialogue:
    $ location_count = "Kitchen"
    scene location_home_kitchen_closeup with None
    show mom 116 at right
    with dissolve
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 116 at right
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 116 at right
    show player 1 at left with dissolve
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 119 at Position(xpos=1014)
    mom "Oh, hey Sweetie!"
    show mom 120
    show player 14
    player_name "Hey, {b}Mom{/b}!"
    show mom 119
    show player 1
    mom "If you need something, it'll have to wait."
    mom "I need to finish drying these dishes."
    show mom 120
    menu:
        "Let me help.":
            show mom 118
            show player 14
            player_name "Take a break, {b}Mom{/b}."
            player_name "I'll take it from here."
            show mom 119
            show player 1
            mom "Sweetie, you know you don't have to."
            show mom 118
            show player 14
            player_name "No, it's fine. I'm kind of bored anyway."
            show mom 119
            show player 1
            mom "Well... Okay."
            show player 272
            show mom 62
            mom "Put the dishes away in the cupboard after you're finished."
            show player 273
            show mom 61
            player_name "Will do."
            show mom 63
            show player 272
            mom "Thanks for helping out, Sweetie!"
            show player 274
            show mom 61
            player_name "No problem, {b}Mom{/b}!"
            scene location_home_kitchen
            with dissolve
            scene help_mom_kitchen_cutscene with fade
            show text "{b}Dad{/b} was usually the one helping {b}Mom{/b} with dishes... \nBut, I didn't mind being the one to help her now. \nShe stayed with me in the kitchen and we talked the whole time... \nIt was nice seeing {b}Mom{/b} happy for once." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            $ mom_helped += 1
        "Nevermind.":

            show player 14 at left
            show mom 120 at Position(xpos=1014)
            player_name "Okay. I'll come back later, then."
            scene location_home_kitchen
            with dissolve
    $ mom_vacuuming = False
    $ callScreen(location_count)

label sis_breakfast_force:
    scene homekitchen with None
    show player 11 at left
    show mom 2 at right
    with dissolve
    mom "Where are you going? Your breakfast is ready in the {b}dining room{/b}, Sweetie..."
    show player 14
    show mom 1
    player_name "Sorry, {b}Mom{/b}! I'll go eat now."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)

label sis_breakfast_force_mom:
    scene homekitchen with None
    show player 11 at left
    show mom 2 at right
    with dissolve
    mom "Your breakfast is ready in the {b}dining room{/b}, Sweetie..."
    show player 14
    show mom 1
    player_name "Thanks, {b}Mom{/b}! I'll go eat now."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)