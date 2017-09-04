label consumr:
    $ location_count = "Consumr"
    if quest10 in quest_list and quest10 not in completed_quests:
        scene consumr
        show player 4 with dissolve
        player_name "( There must quite a few types of pesticides in here. )"
        show player 10
        player_name "( I'm not sure what kind I need. )"
        player_name "( I should probably ask the {b}store clerk{/b} like {b}Aunt Diane{/b} suggested. )"
        hide player
    $ callScreen(location_count)

label veronica_dialogue_button:
    scene location_consumr_closeup
    show player 1 at left with dissolve
    show veronica 2 at right with dissolve
    vero "Welcome to {b}CONSUM-R{/b}! My name is {b}Veronica{/b}."
    show veronica 4
    vero "Is there anything I can help you with today?"
    menu:
        "I'm fine.":
            show player 2
            show veronica 1
            player_name "Uhm..."
            show player 17
            player_name "I think I'm fine, thanks!"
            show veronica 4
            show player 1
            vero "No problem!"
            show veronica 2
            vero "Just let me know if you need anything."

        "Bug spray?" if quest10 in quest_list and quest10 not in completed_quests:
            show veronica 1
            show player 4
            player_name "Uh..."
            show player 12
            player_name "I'm looking for pesticide?"
            show veronica 4
            show player 1
            vero "Ah, yes! We have a variety of pest repellent products!"
            show veronica 1
            show player 2
            player_name "Hmm... How about for insects?"
            show veronica 3
            show player 1
            vero "Well... There are many types of pesticides for insects..."
            show veronica 2
            show player 11
            vero "Do you know what type of bug you're dealing with?"
            show veronica 1
            show player 10
            player_name "I'm not quite sure what kind it is..."
            show veronica 3
            show player 13
            vero "Well, what does it {b}look like{/b}?"
            menu:
                "Large wings.":
                    show veronica 1
                    show player 35
                    player_name "It had a set of large wings..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Could be {b}grasshoppers{/b}..."
                    show veronica 4
                    show player 1
                    vero "Get the spray can with a {b}red cap{/b}. It's called the {b}Bug Exterminator{/b}."
                    show veronica 2
                    vero "It should do the trick!"
                    show veronica 1
                    show player 17
                    player_name "Alright, thanks!"
                "Pincers on back.":

                    show veronica 1
                    show player 35
                    player_name "It had large pincers..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Could be {b}earwigs{/b}... Nasty buggers!"
                    show veronica 4
                    show player 1
                    vero "Get the spray can with a {b}green cap{/b}. It's called the {b}Bug Annihilator{/b}."
                    show veronica 2
                    vero "It should do the trick!"
                    show veronica 1
                    show player 17
                    player_name "Alright, thanks!"
                "White spots.":

                    show veronica 1
                    show player 35
                    player_name "It had white spots on its shell..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Could be {b}beetles{/b}..."
                    show veronica 4
                    show player 1
                    vero "Get the spray can with a {b}blue cap{/b}. It's called the {b}Bug Eradicator{/b}."
                    show veronica 2
                    vero "It should do the trick!"
                    show veronica 1
                    show player 17
                    player_name "Alright, thanks!"
    $ callScreen(location_count)