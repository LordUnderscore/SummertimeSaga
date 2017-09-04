label library_dialogue:
    $ location_count = "Library"
    if getPlayingSound("<loop 9 to 83>audio/ambience_library.ogg"):
        $ playSound("<loop 9 to 83>audio/ambience_library.ogg", 1.0)

    if aunt.started(aunt_breeding_guide):
        scene library with None
        show player 10 with dissolve
        player_name "( Maybe this place would have a book that would help {b}Aunt Diane{/b} make more milk. )"
        show player 11
        pause
        show player 35
        player_name "( Where do I even start? )"
        show player 10
        player_name "( I suppose I could ask the librarian for help. )"
        hide player with dissolve

    elif library_count == 0:
        scene library with None
        show player 1 at left
        show jane 2 at right
        with dissolve
        jan "Hi!"
        show player 14
        show jane 1
        player_name "Oh, hi!"
        player_name "I'm looking for some school {b}textbooks{/b}."
        show player 1
        show jane 2
        jan "Do you have a membership subscription?"
        show jane 1
        menu:
            "No.":
                show player 10 at left
                show jane 1 at right
                player_name "Umm... I don't think I have one."
                show player 13
                show jane 3
                jan "Oh. That's okay!"
                show jane 2
                jan "Would you like to get one?"
                show jane 3
                show player 11
                jan "Membership subscriptions are {b}$20{/b}, and you get access to all of our selections!"
                show jane 1
                show player 2
                player_name "Uhh... I guess I have no choice. Haha."
                show jane 3
                show player 13
                jan "Knowledge is priceless, right?"
                show jane 2
                jan "Would you like to subscribe right now?"
                show jane 1
                menu:
                    "Sure." if inventory.money >= 20:
                        show player 4 at left
                        show jane 1 at right
                        player_name "Hmm..."
                        show player 174b at Position(xoffset=38) with fastdissolve
                        player_name "All right. Here's {b}$20.{/b}"
                        play audio coins2
                        $ inventory.money -= 20
                        $ library_subscription = True
                        show player 1 with fastdissolve
                        show jane 3
                        jan "Thank you!"
                        show jane 2
                        jan "If you're looking for a specific {b}book{/b}, just come to the front desk."
                        jan "I'll look them up and find 'em for ya!."
                        show jane 1
                        show player 2
                        player_name "That sounds great! Thanks!"
                        hide player 2
                        hide jane 1
                        with dissolve
                        $ library_count = 1
                        $ callScreen(location_count)
                    "I'll pass.":

                        show player 4 at left
                        show jane 1 at right
                        player_name "Hmm..."
                        show player 35
                        player_name "Actually, I think I'll pass..."
                        show jane 2
                        show player 1
                        jan "Oh... alright then."
                        show jane 1
                        show player 2
                        player_name "I might come by another time!"
                        show jane 2
                        show player 1
                        jan "Okay, have a good day!"
                        hide player 1
                        hide jane 2
                        with dissolve
                        $ library_count = 0
                        $ location_count = "Town Map"
                        $ callScreen(location_count)

    elif homework_count == 1 and not janice_thankyou:
        scene library with None
        show jane 6 at right
        show player 1 at left
        with dissolve
        jan "Hey!"
        jan "Just wanted to thank you for getting me the {b}new webcam{/b}!"
        show jane 1
        show player 2
        player_name "You're welcome!"
        show jane 3
        show player 1
        jan "People are loving it so far..."
        jan "The frame rate is great and the resolution is phenomenal..."
        jan "...They can't get enough of it!"
        show jane 1
        show player 17
        player_name "I guess I should thank you for the {b}textbook{/b} as well!"
        show player 14
        player_name "It helped me a lot, I was able to finish my {b}homework{/b}."
        show jane 3
        show player 1
        jan "I'm glad we found a partnership we can both gain from!"
        show jane 2
        jan "I'll be at the desk if you need anything."
        $ janice_thankyou = True
        $ library_desk_count = 1
        hide player
        hide jane
    $ callScreen(location_count)

label library_desk_dialogue:
    if library_desk_count == 0:
        scene librarydesk with None
        show jane 10
        show player 1f at right
        with dissolve
        jan "Hi! How can I help you?"
        show player 2f
        show jane 9
        player_name "Hi, I'm looking for a {b}book{/b}."
        show player 1f
        show jane 10
        jan "Sure thing! Do you know the book's name?"
        show player 1f
        show jane 9
        menu:
            "French Grammar - Volume 1" if textbook1 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Yeah, I need the book \"{b}French Grammar - Volume 1{/b}\""
                show player 1f
                show jane 11
                jan "Oh, we don't have it here..."
                jan "... but, it is available to order online."
                show player 14f
                show jane 9
                player_name "That's great, but how long will it take for it to get here?"
                show player 11f
                show jane 11
                jan "Actually, I can't make any new orders at the moment."
                show player 12f
                show jane 9
                player_name "What??"
                show player 5f
                show jane 11
                jan "Unfortunately, the library's had a huge cut in funding last year..."
                jan "There's just no budget to order new books..."
                show player 10f
                show jane 9
                player_name "So... What am I supposed to do now?"
                show player 5f
                show jane 10
                jan "Well, you could wait and see if we can afford to make an order at a later time?"
                show player 12f
                show jane 9
                player_name "I can't do that! I have to finish my {b}homework{/b} before the {b}Finals{/b}!"
                show player 11f
                show jane 10
                jan "Feel free to {b}look around{/b} the library. I'm sure there's a few old edition {b}textbooks{/b} laying around."
                show jane 11
                jan "Oh! And try to avoid the {b}back room{/b}... I need to uh... clean it - it's not ready yet."
                show player 12f
                show jane 9
                player_name "Okay..."
                hide player 12f
                hide jane 9
                with dissolve
                $ backroom_blocked_count = 1

            "French Grammar - Volume 2" if textbook2 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Yeah, I need the book \"{b}French Grammar - Volume 2{/b}\""
                show player 11f
                show jane 11
                jan "Oh, sorry... That book is out of stock right now."
                show player 5f
                show jane 10
                jan "Come back another time and I can check again for you..."
                show player 10f
                show jane 9
                player_name "Alright, thanks."
                hide player 10f
                hide jane 9
                with dissolve

            "French Grammar - Volume 3" if textbook3 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Yeah, I need the book \"{b}French Grammar - Volume 3{/b}\""
                show player 11f
                show jane 11
                jan "Oh, sorry... That book is out of stock right now."
                show player 5f
                show jane 10
                jan "Come back another time and I can check again for you..."
                show player 10f
                show jane 9
                player_name "Alright, thanks."
                hide player 10f
                hide jane 9
                with dissolve
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished with dissolve

            "Milk production book." if aunt.started(aunt_breeding_guide):
                show jane 9 at left
                show player 14f at right
                player_name "This may sound weird, but do you have anything in the library about increasing milk production?"
                show player 13f
                pause
                show jane 11
                jan "Um... Why? I don't think you'll ever be able to breastfeed."
                show jane 10
                jan "Oh! Whoops! You probably meant for farming, right?"
                show jane 9
                show player 10f
                player_name "Ummm... Actually, I'm interested in learning about either topic, I guess..."
                show player 13f
                show jane 11
                jan "Check the bookshelf over there. We should have something."
                show jane 9
                show player 14f
                player_name "Thank you!"
                show player 13f
                show jane 10
                jan "You're welcome!"
                hide player
                hide jane
                with dissolve
                $ aunt_breeding_guide.finish()

    elif library_desk_count == 1:
        scene librarydesk with None
        show jane 10
        show player 1f at right
        with dissolve
        jan "Hi! How can I help you?"
        show player 2f
        show jane 9
        player_name "Hi, I'm looking for a book."
        show player 1f
        show jane 10
        jan "Sure thing, do you know its name?"
        show jane 9
        menu:
            "French Grammar - Volume 1" if textbook1 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Yeah, I need \"{b}French Grammar - Volume 1{/b}\""
                show player 1f
                show jane 11
                jan "Did you get me what I asked you for?"
                show jane 9
                menu:
                    "Here's the webcam." if supersaga_webcam in inventory.items:
                        show player 12f at right
                        show jane 9
                        player_name "Yeah... Here's the {b}webcam{/b}."
                        show player 239_240f
                        pause
                        show player 54 at Position(xoffset=-38) with fastdissolve
                        pause
                        show player 1f with fastdissolve
                        $ inventory.items.remove(supersaga_webcam)
                        show jane 13
                        jan "Thank you!"
                        show player 16f
                        show jane 9
                        player_name "..."
                        show player 12f
                        player_name "What about my {b}textbook{/b}?"
                        show player 11f
                        show jane 13
                        jan "Oh! Right..."
                        show player 11f
                        jan "It came in earlier today, I put it on the {b}shelf{/b} over there."
                        jan "Go ahead and take it."
                        $ completed_quests.append(quest06)
                        show player 1f
                        show jane 13
                        jan "See you next time!"
                        $ library_desk_count = 0
                        hide player 1f
                        hide jane 13 with dissolve
                    "I don't have it.":

                        show player 24f at right
                        show jane 9
                        player_name "I don't have it yet..."
                        show player 5f
                        show jane 10
                        jan "I can't get that {b}textbook{/b} order for you then, you know that."
                        jan "Come back when you have the {b}webcam{/b}, and we'll talk."
                        hide player 5f
                        hide jane 10
                        with dissolve

            "French Grammar - Volume 2" if janice_thankyou:
                if not webcam_quest:
                    show player 14f at right
                    show jane 9
                    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
                    show player 1f
                    show jane 10
                    jan "You know how it is..."
                    jan "I still can't make any new orders at this moment."
                    show player 12f
                    show jane 9
                    player_name "Still??"
                    show player 5f
                    show jane 11
                    jan "I would love to get that for you... But our funds are still low."
                    show player 10f
                    show jane 9
                    player_name "What do you mean? I thought the new {b}webcam{/b} was helping??"
                    show player 5f
                    show jane 11
                    jan "Don't get me wrong: It's helping..."
                    jan "but people are getting tired of the same stuff!"
                    show player 10f
                    show jane 9
                    player_name "So... What can we do?"
                    show player 5f
                    show jane 11
                    jan "Well, our viewers want more variety..."
                    show player 11f
                    show jane 13
                    jan "...and I maybe you could help with that!"
                    show player 12f
                    show jane 9
                    player_name "But, how?"
                    show player 11f
                    show jane 10
                    jan "Don't you go to school?"
                    show player 12f
                    show jane 9
                    player_name "Yeah?"
                    show player 11f
                    show jane 13
                    jan "Well, just hide one of my remote controlled {b}webcams{/b} in the school!"
                    show jane 9
                    player_name "..."
                    show player 12f
                    player_name "Are you crazy?!"
                    player_name "What if I got caught!"
                    show jane 13
                    show player 90f
                    jan "Relax! Just go at night, when no one is around."
                    show player 37f
                    show jane 9
                    player_name "Ugh... I can't believe I have to do this..."
                    show jane 10
                    jan "Do you want those books, or not?"
                    show player 24f
                    show jane 9
                    player_name "I'll see what I can do..."
                    $ inventory.items.append(supersaga_webcam)
                    $ quest_list.append(quest11)
                    $ webcam_quest = True
                    hide jane
                    hide player
                else:

                    show player 14f at right
                    show jane 9
                    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
                    show player 1f
                    show jane 11
                    jan "Well? Did you do it?"
                    menu:
                        "I placed it." if webcam_planted:
                            show jane 9
                            show player 12f at right
                            player_name "Yeah. I placed it in the {b}lockeroom{/b}..."
                            player_name "It's in the ceiling {b}air vent{/b}..."
                            show player 1f
                            show jane 13
                            jan "Thank you!"
                            show player 16f
                            show jane 9
                            player_name "..."
                            show player 12f
                            player_name "What about my {b}textbook{/b}?!"
                            show player 11f
                            show jane 13
                            jan "Oh! Right..."
                            show player 11f
                            show jane 15
                            jan "Here it is!"
                            $ inventory.items.append(textbook2)
                            show player 30f
                            show jane 9
                            player_name "Thanks!"
                            show player 1f
                            show jane 13
                            jan "See you next time!"
                            $ library_desk_count = 0
                            $ completed_quests.append(quest11)
                            hide player 1f
                            hide jane 13 with dissolve
                        "Not yet.":

                            show player 24f at right
                            show jane 11
                            player_name "I didn't do it yet..."
                            show player 5f
                            show jane 10
                            jan "I can't get that {b}textbook{/b} order for you, then. You know that."
                            jan "Come back when you placed the {b}webcam{/b} at school."
                            hide player 5f
                            hide jane 10
                            with dissolve

            "French Grammar - Volume 3" if quest11 in completed_quests:
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished with dissolve
    $ callScreen(location_count)

label kamasutra:
    scene libraryshelf with None
    show book_02_c at truecenter with dissolve
    player_name "Woa..."
    player_name "This book has all sorts of sex...positions?"
    player_name "It must be what she asked for..."
    hide book_02_c with dissolve
    $ inventory.items.append(kamasutra)
    jump library_dialogue

label breeding_guide:
    scene libraryshelf with None
    player_name "( The book should be here somewhere... )"
    show book_01_c at truecenter with dissolve
    player_name "( This looks like it! )"
    player_name "Hmm..."
    player_name "( Looks simple enough. )"
    player_name "( It should work with {b}Aunt Diane{/b} too. )"
    player_name "( I'm just not sure if she would want to get {b}pregnant{/b}, though. )"
    player_name "( Let's just see what she says... )"
    hide book_01_c with dissolve
    $ inventory.items.append(breeding_guide)
    jump library_dialogue