label cafeteria_dialogue:
    $ location_count = "Cafeteria"
    if quest09 in quest_list and quest09 not in completed_quests and quest09_1 == False and quest09_2 == False and quest09_3 == False:
        scene cafeteria_b
        show player 163 at left with dissolve
        show annie 3 at right with dissolve
        ann "What's going on here??"
        show annie 1
        show player 164
        player_name "Hi {b}Annie{/b}! I uh..."
        show annie 9
        player_name "Well, I'm supposed to drop this off here in the cafeteria."
        player_name "It's a {b}milk{/b} delivery!"
        show annie 4
        show player 163
        ann "I know what it is. I have eyes."
        ann "What I don't understand, is why you're the one delivering it."
        show annie 1
        show player 164
        player_name "Oh, it's actually from my {b}Aunt{/b}..."
        player_name "She couldn't do it herself, so she asked me to do it for her."
        player_name "Here's the {b}receipt{/b}!"
        show annie 12
        show player 163
        ann "Hmm..."
        show annie 13
        ann "I can't accept this."
        ann "You'll have to give it to principal {b}Smith{/b} in her {b}office{/b}."
        show annie 6
        show player 164
        player_name "But-"
        show player 163
        show annie 5
        ann "I can't trust someone who's unauthorized for deliveries!"
        ann "If {b}Mrs. Smith{/b} approves it, I'll take it from you."
        show annie 6
        show player 164
        player_name "All right, then..."
        $ quest09_1 = True
        $ lock_ui()

    elif quest09 in quest_list and quest09 not in completed_quests and quest09_2 == True:
        scene cafeteria_b
        show player 164 at left with dissolve
        show annie 1 at right with dissolve
        player_name "All done!"
        show annie 9
        show player 163
        ann "..."
        show annie 3
        ann "{b}Mrs. Smith{/b} took the {b}receipt{/b}?"
        show annie 1
        show player 164
        player_name "Yeah, she was... kind of... busy. But she said I should give it to you."
        show annie 5
        show player 163
        ann "I see..."
        show annie 15
        show player 1
        ann "I'll take these from you, then."
        show annie 14
        show player 17
        player_name "Thanks, {b}Annie{/b}!"
        hide player
        hide annie
        with dissolve
        $ inventory.items.remove(milk_carton)
        $ quest09_2 = False
        $ quest09_3 = True
        $ unlock_ui()

    elif not erik.known(erik_favor):
        scene cafeteria_b
        show player 2 at left with dissolve
        show kevin 1 at right with dissolve
        player_name "Hey, {b}Kevin{/b}!"
        show player 1 at left
        show kevin 2 at right
        kev "Hey, dude..."
        show kevin 1 at right
        show player 10 at left
        player_name "You're on cafeteria duties huh..."
        show kevin 2 at right
        show player 13 at left
        kev "Yep! I got two more months of this crap."
        show kevin 1 at right
        show player 17 at left
        player_name "That sucks."
        show kevin 2 at right
        show player 1 at left
        kev "Yeah but what can I do?"
        kev "By the way, was {b}Dexter{/b} giving you guys a hard time in the hallway?"
        show kevin 1 at right
        show player 24 at left
        player_name "Yeah, he and {b}Roxxy{/b} are always on our case..."
        show player 26 at left
        player_name "But it's nothing. I don't really care about what they say."
        show kevin 3 at right
        show player 11 at left
        kev "Dude. You gotta stand up for yourself."
        show kevin 1 at right
        show player 10 at left
        player_name "I'd rather just avoid him, you know?"
        player_name "There's no point in getting into a fight with a guy twice my size."
        show kevin 3 at right
        show player 11 at left
        kev "You can't let him walk all over you. How're you going to survive college like that?"
        show kevin 1 at right
        show player 24 at left
        player_name "Well, I'm just too weak to do anything about it."
        show kevin 4 at right
        show player 11 at left
        kev "Hmm... Maybe we could work something out."
        show kevin 1 at right
        show player 10 at left
        player_name "What do you mean?"
        show kevin 4 at right
        show player 1 at left
        kev "Well, I could help you work out at the {b}Gym{/b}..."
        kev "Like spotting you when you're lifting, and show you some tricks."
        show kevin 2 at right
        show player 34 at left
        kev "But you'll have to {b}find someone to take my spot{/b} in the cafeteria."
        kev "I can't take any more of this."
        show player 34 at left
        show kevin 1 at right
        player_name "Alright! I can try and find someone who could swap with you."
        show kevin 2 at right
        show player 1 at left
        kev "Alright man. I have to get back to work. Catch you later!"
        show kevin 1 at right
        show player 36 at left
        player_name "See you later, {b}Kevin{/b}!"
        hide player
        hide kevin
        with dissolve
        $ erik.add_event(erik_favor)

    elif erik.known(erik_favor) and not erik.completed(erik_favor_2):
        scene cafeteria_b
        show player 2 at left with dissolve
        show kevin 1 at right with dissolve
        player_name "Hey, {b}Kevin{/b}!"
        show kevin 2 at right
        show player 1 at left
        kev "Hey, dude..."
        kev "Were you able to find someone to take over my cafeteria duties?"
        menu:
            "I think so!" if erik.known(erik_favor_2):
                show player 14 at left
                show kevin 1 at right
                player_name "I think I found a replacement!"
                show kevin 2 at right
                show player 1 at left
                kev "No way, man! That's awesome!"
                kev "Who's taking my spot?"
                show kevin 1 at right
                show player 17 at left
                player_name "It's {b}Erik{/b}... And I had to bribe him..."
                show kevin 2 at right
                show player 1 at left
                kev "Haha! Well, thanks, dude!"
                kev "Now I can spend more time at the {b}Gym{/b}!"
                show kevin 6 at right
                show player 11 at left
                kev "...And I won't be needing this anymore!"
                show kevin 5 at right
                show player 12 at left
                player_name "That thing is nasty..."
                show kevin 12 at right
                show player 1 at left
                kev "Hey! If you're looking for a Gym BRO, you'll know where to find me!"
                show kevin 5 at right
                show player 14 at left
                player_name "Alright! I'll come by!"
                $ erik_favor_2.finish()
            "Not yet.":

                show kevin 1 at right
                show player 26 at left
                player_name "Not yet, But I'll keep looking!"
                show kevin 3 at right
                show player 1 at left
                kev "All right..."
        hide player
        hide kevin
        with dissolve

    elif is_here("erik") and erik.completed(erik_favor_2):
        scene cafeteria_b
        show player 36 at left with dissolve
        show erik 11 at right with dissolve
        player_name "Hey, {b}Erik{/b}!"
        show erik 12 at right
        show player 1 at left
        eri "Hey, {b}[firstname]{/b}!"
        show erik 11 at right
        show player 21 at left
        player_name "Soo... How's the cafeteria duties?"
        show erik 12 at right
        show player 13 at left
        eri "It could be worse, I guess."
        eri "I usually don't do much during lunch at school, anyway..."
        show erik 11 at right
        show player 17 at left
        player_name "I'm glad you're okay with it."
        show erik 12 at right
        show player 1 at left
        eri "I get to go home and play {b}Sea Dogs SAGA{/b}!"
        show erik 11 at right
        show player 14 at left
        player_name "Cool! Well, I'll let you go back to your duties..."
        show erik 11 at right
        show player 1 at left
        eri "See ya later!"
        hide erik
        hide player
        with dissolve
    $ callScreen(location_count)