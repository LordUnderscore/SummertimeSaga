default move_list = []
default move_list_number = 4
default training_tier = 0
default training_skip_payment = False

label training_dialogue:
    $ location_count = "Gym"
    if training_count == 0:
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 35 at left
        player_name "Woah..." with None
        show player 14
        player_name "This place has everything!"
        player_name "It even has all that boxing stuff too!"
        show master 2 at right
        show player 11
        with dissolve
        mas "This is not a boxing gym, but a {b}Muay Thai{/b} training camp!"
        show master 1
        show player 17
        player_name "Oh. I see..."
        show master 3
        show player 11
        mas "Only the toughest and most disciplined students get to learn my teachings!"
        show master 5
        show player 12
        player_name "Hmmm... Couldn't I just, like, lift some weights and just be stronger than everyone?"
        show master 4
        show player 11
        mas "{b}NO!!!{/b}" with hpunch
        show master 3
        show player 1
        mas "Without the mental and physical discipline of Muay Thai..."
        show master 4
        show player 11
        mas "...you are nothing more than sack of meat!"
        show master 3
        mas "By learning to use the eight parts of our body to strike, we become the most efficient weapon!"
        show master 5
        show player 12
        player_name "Oh yeah? What if I had a gun?"
        show master 4
        show player 11
        mas "You {b}FOOL{/b}!!!"
        show player 6
        show master 7
        window hide
        with vpunch
        pause
        show master 1
        show player 38
        player_name "Ouch!!"
        player_name "That hurt!"
        show master 4
        show player 11
        mas "You are slow... and weak! A gun would be of no use for you!"
        show master 2
        mas "This is no good, we will have to work on your {b}Dexterity{/b}."
        show master 5
        show player 12
        player_name "Alright, so, when do we start training?"
        show master 4
        show player 11
        mas "Hah! My lessons are not free, young apprentice."
        show master 3
        mas "I only accept one form of payment..."
        mas "...and it comes in the form of..."
        show player 22
        mas "...a pair of {b}panties{/b}!"
        show player 21
        show master 6
        player_name "A pair of-"
        show master 4
        show player 11
        mas "Must I repeat myself, student?"
        show master 6
        show player 10
        player_name "Uh, no... I'll see what I can find, Sir."
        show master 4
        show player 22
        mas "You have to bow before you leave!"
        show master 1
        show player 40
        player_name "Yes, Sir!"
        show master 4
        show player 22
        mas "And call me, {b}Master Somrak{/b}!!!"
        show master 1
        show player 40
        player_name "Yes, {b}Master Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Good! Now, go!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        if quest07 not in completed_quests:
            $ quest_list.append(quest07)
        $ sis_door_locked_count = 1
        $ training_count = 1
        $ training_tier = 1
        $ sister.add_event(sis_panty01)

    elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Master Somrak{/b}!"
        player_name "I'm ready to learn new techniques!"
        show player 1
        show master 2
        mas "You are eager to learn! Good, good!"
        show master 3
        mas "But my lessons are not free, young apprentice."
        mas "Your new payment for your training will be..."
        show player 11
        show master 9
        mas "...a used pair of {b}panties{/b}!"
        show master 1
        player_name "..."
        show master 3
        mas "And make sure they are {b}used{/b}!"
        show master 5
        show player 12
        player_name "Used?"
        show player 11
        show master 3
        mas "You must witness the woman take them off personally!"
        show master 9
        mas "Make sure they have been worn and they have absorbed her scent!"
        show master 6
        show player 21
        player_name "Uh... I'll see what I can find, Sir."
        show master 4
        show player 5
        mas "You must bow before you leave, idiot!" with hpunch
        show master 6
        show player 40
        player_name "Yes, {b}Master Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Good! Now, go!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 2
        $ sister.add_event(sis_panty02)

    elif training_count == 2 and training_tier == 3 and sister.over(sis_couch02):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Master Somrak{/b}!"
        player_name "I'm ready to learn new techniques!"
        show player 1
        show master 2
        mas "You are eager to learn! Good, good!"
        show master 3
        mas "But my lessons are not free, young apprentice."
        mas "Your new payment for your training will be..."
        show player 11
        show master 9
        mas "...wet {b}panties{/b}!"
        show master 1
        player_name "..."
        show master 3
        mas "And make sure they are {b}wet{/b}!"
        show master 5
        show player 12
        player_name "Wet?"
        show player 11
        show master 3
        mas "You must be a witness!"
        show master 9
        mas "The {b}panties{/b} must be {b}soaked{/b} with her juices!"
        show master 3
        mas "Make sure they have been worn by an aroused woman!!"
        show master 6
        show player 21
        player_name "Uh... I'll see what I can find, Sir."
        show master 4
        show player 5
        mas "You have to bow before you leave, idiot!"
        show master 6
        show player 40
        player_name "Yes, {b}Master Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Good! Now, go!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 3
        $ sister.add_event(sis_panty03)

    elif training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Master Somrak{/b}!"
        player_name "I'm ready to learn new techniques!"
        show player 1
        show master 2
        mas "Excellent!"
        show master 3
        mas "But my last lesson is not free, young apprentice."
        mas "The last payment for your training will be..."
        show player 11
        show master 9
        mas "...{b}panties{/b} drenched in {b}squirt{/b}!!!"
        show master 1
        player_name "!!!"
        show master 3
        mas "Make sure they are completely {b}drenched in squirt{/b}!"
        show master 5
        show player 12
        player_name "Squirt?"
        show master 4
        show player 22
        mas "Are you man or parrot?!" with hpunch
        show master 5
        show player 5
        player_name "..."
        show player 11
        show master 3
        mas "You must be a witness!"
        show master 9
        mas "Make sure they have been {b}soaked{/b} and {b}sprayed{/b} with the juices of a woman!!"
        show player 21
        show master 5
        player_name "That's going to be hard to do..."
        show master 6
        player_name "...But I'll see what I can find, Sir."
        show master 2
        show player 5
        mas "You must bow, remember?"
        show master 6
        show player 40
        player_name "Yes, {b}Master Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Good! Now, go!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 4
        $ sister.add_event(sis_panty04)
    $ callScreen(location_count)

label cedric_dialogue:
    scene expression gTimer.image("training{}_b")
    show ced 1 at left
    show player 14f at right
    with dissolve
    player_name "Hi!"
    player_name "You think you could spot me?"
    show ced 2
    show player 1f
    ced "Uh..."
    show player 11f
    ced "Do you even lift, bro?"
    show player 10f
    show ced 1
    player_name "Huh?"
    show ced 2
    show player 5f
    ced "Sorry, I don't spot shrimps."
    hide ced
    hide player
    with dissolve
    $ callScreen(location_count)

label tired_training_dialogue:
    scene expression gTimer.image("training{}_b")
    show player 5 with dissolve
    player_name "( I'm tired, I should go home and sleep. )"
    hide player with dissolve
    $ callScreen(location_count)

label cant_solo_lift:
    scene expression gTimer.image("training{}_b")
    show player 11 at left with dissolve
    player_name "( I can't do that on my own. )"
    player_name "( I need someone to spot me! )"
    hide player with dissolve
    $ callScreen(location_count)