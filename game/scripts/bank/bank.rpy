label bank_dialogue:
    $ location_count = "Bank"
    if bank_count == 0:
        scene bank
        show player 1 at left with dissolve
        show liu 2 at right with dissolve
        liu "Welcome to {b}Saga Financial Bank{/b}!"
        show liu 1 at right
        show player 14 at left
        player_name "Hi!"
        show liu 3 at right
        show player 1 at left
        liu "Please, feel free to use our {b}ATM machines{/b} for {b}deposits{/b}!"
        liu "Or we can also assist you with any questions you may have at our {b}help desk{/b}!"
        show liu 1 at right
        show player 14 at left
        player_name "Okay, sure!"
        hide player 14 at left with dissolve
        hide liu 1 at right with dissolve
        $ bank_count = 1
    $ callScreen(location_count)

label bank__tellerdialogue:
    if bank_teller_count == 0:
        scene bank
        show liu 10 at right
        show player 14 at left with dissolve
        window hide
        pause
        show player 11 at left
        player_name "..."
        show liu 9 at right
        show player 12 at left
        player_name "Excuse me?"
        show liu 5 at right
        show player 1 at left
        liu "Oh! I'm sorry!"
        liu "How can I help you today, sir?"
        menu:
            "Check my account.":
                show liu 4 at right
                show player 2 at left
                player_name "Can you tell me how my account is doing?"
                show liu 5 at right
                show player 1 at left
                liu "I see that you have a family joint account with us!"
                liu "You recently created a savings account which has..."
                liu "... {b}[inventory.savings]{/b} dollars in it!"
                show liu 4 at right
                show player 17 at left
                player_name "Yeah, that's my savings for college starting in the fall."
                show liu 5 at right
                show player 1 at left
                liu "Anything else I can do for you?"
                menu:
                    "More information." if more_account_info == 0:
                        show liu 4 at right
                        show player 4 at left
                        player_name "Hmmm..."
                        show player 30 at left
                        player_name "Can you tell me a bit more about the savings from other primary accounts?"
                        show liu 5 at right
                        show player 1 at left
                        liu "Well you also have your family's accounts, which has..."
                        show liu 9 at right
                        show player 11 at left
                        liu "Oh..."
                        show player 10 at left
                        player_name "What's wrong?"
                        show liu 6 at right
                        show player 23 at left
                        liu "Well... It seems like your primary family account has been frozen..."
                        show liu 11 at right
                        show player 10 at left
                        player_name "How can that be?"
                        show liu 6 at right
                        show player 5 at left
                        liu "A large number of loans have not been paid and the bank had to intervene."
                        show liu 11 at right
                        liu "..."
                        show liu 6 at right
                        show player 22 at left
                        liu "I have... other bad news..."
                        show player 11 at left
                        liu "It also seems like your family has not paid their {b}mortgage payments{/b}..."
                        liu "...The last one was over 6 months ago..."
                        show liu 11 at right
                        show player 22 at left
                        player_name "..."
                        show player 23 at left with hpunch
                        player_name "What?!?"
                        show liu 6 at right
                        show player 5 at left
                        liu "I'm afraid the only outcome will surely be {b}foreclosure{/b}..."
                        show liu 11 at right
                        show player 10 at left
                        player_name "I can't believe this..."
                        show liu 6 at right
                        show player 5 at left
                        liu "From your reaction... I assume you didn't know about this."
                        show liu 11 at right
                        show player 24 at left
                        player_name "Well... I knew my {b}Dad{/b} had some problems... but never this bad."
                        show liu 6 at right
                        liu "I'm sorry to say, but there's not much I can do in this situation."
                        show liu 11 at right
                        show player 25 at left
                        player_name "It's fine. I just wanted to know..."
                        player_name "I have to go now..."
                        hide player 25 at left
                        hide liu 11 at right
                        with dissolve
                        $ more_account_info = 1
                    "Thanks, I have to go.":

                        show liu 4 at right
                        show player 14 at left
                        player_name "I have to go. But I'll come back another time!"
                        show liu 5 at right
                        show player 1 at left
                        liu "Thanks for doing business with us!"
                        liu "Come back soon!"
                        hide player 1 at left
                        hide liu 5 at right
                        with dissolve

            "Chat." if bankteller_chat == 0:
                show liu 9 at right
                show player 10 at left
                player_name "This might sound a bit personal, but..."
                player_name "Is everything alright?"
                show liu 6 at right
                show player 13 at left
                liu "Em... Of course!"
                liu "What makes you think that?"
                show liu 9 at right
                show player 2 at left
                player_name "I dunno, you just seemed like you've had a terrible day at work..."
                show liu 6 at right
                show player 13 at left
                liu "Ohh... It's not that... Work is fine, really..."
                show liu 10 at right
                liu "{b}*sigh*{/b}"
                show player 11 at left
                liu "It's just... You know, problems at home sometimes..."
                show liu 6 at right
                liu "...It gets to you like-"
                show liu 8 at right
                liu "Wait... Why am I telling you this?"
                show liu 4 at right
                show player 29 at left
                player_name "Oh, I'm sorry! I didn't mean to make you uncomfortable."
                player_name "Sometimes when I have problems at home..."
                show liu 9 at right
                show player 33 at left
                player_name "I just have to tell someone about it. You know, let it out!"
                show liu 5 at right
                show player 13 at left
                liu "Well... Yeah, I guess you're right."
                show liu 7 at right
                show player 13 at left
                liu "I have to get back to work though..."
                show liu 10 at right
                liu "..."
                show liu 5 at right
                show player 11 at left
                liu "What's your name again?"
                show liu 4 at right
                show player 17 at left
                player_name "Oh, my name is {b}[firstname]{/b}!"
                show liu 7 at right
                show player 2 at left
                liu "Nice to meet you {b}[firstname]{/b}, I'm {b}Liu Wang{/b}!"
                $ liu = Character('Liu Wang', color="#c8ffc8")
                show liu 4 at right
                show player 14 at left
                player_name "I'll see you next time, {b}Liu{/b}!"
                show liu 8 at right
                show player 1 at left
                liu "Bye!"
                hide player 1 at left
                hide liu 8
                with dissolve
                $ bankteller_chat = 1
    $ callScreen(location_count)