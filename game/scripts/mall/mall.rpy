label mall_dialogue:
    $ location_count = "Mall"
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)
    if mall_count == 0:
        scene mall
        show player 14 with dissolve
        player_name "( I love the mall! )"
        show player 17
        player_name "( You can go shopping for all sorts of stuff, there's even a movie theater! )"
        hide player 17 with dissolve
        $ mall_count = 1

    elif M_mom.get_state() == S_mom_mall_outing:
        scene location_mall_blur
        show player 13 at left with dissolve
        show mom 165 at Position(xpos=.75, ypos=1.0) with dissolve
        mom "Thanks again for coming with me, Sweetie!"
        show player 14
        show mom 164
        player_name "No problem, [mom_name]. I'm having fun!"
        show player 13
        show mom 166
        mom "Me too! It's been so long since just the two of us got out and spent some time together..."
        show mom 164
        mom "..."
        show mom 165
        mom "Are there any stores you'd like to visit while we're here?"
        show player 14
        show mom 164
        player_name "Hmm, No, not really."
        show player 13
        show mom 165
        mom "Alright, well Erik's Mom was telling me all about this new store that opened up recently."
        mom "I think she said it was called, {b}Cupid{/b}."
        mom "We should go check it out! What do you say?"
        show player 14
        show mom 164
        player_name "Sure, [mom_name]. Okay."
        show player 13
        show mom 165
        mom "... I think she said it was up on the {b}second floor{/b}."
        show mom 167 at right with dissolve
        mom "Lead the way, Sweetie."
        hide player
        hide mom
        with dissolve
        $ M_mom.trigger(T_mom_mall_arrival)
    $ callScreen(location_count)

label mom_mall_outing_block:
    if location_count == "Mall":
        scene location_mall_blur
    elif location_count == "Mall Second Floor":
        scene location_mall_upstairs_blur
    show player 1
    player_name "Hmm, I'm supposed to be looking for a store called, {b}Cupid.{/b}"
    show player 4
    player_name "[mom_name] said it should be on the {b}second floor{/b}."
    $ callScreen(location_count)

label rump_dialogue:
    scene mall_closeup
    show xtra 18 zorder 2 at left
    with dissolve
    player_name "( Looks like the new mayor is giving a speech today. )"
    show rump 1 at Position(xpos = 330)
    show iwanka 1 at Position(xpos = 860)
    with dissolve
    pause
    show rump 2
    rump "Good afternoon, citizens of Summerville."
    rump "It is through your hard work and dedication that I am able to be here today and say..."
    rump "I am greatly honored to be elected as the mayor of our great town."
    show rump 4 at Position(xpos = 374)
    show iwanka 2
    rump "Along with my daughter, Iwanka."
    rump "Who will be fully in charge of all matters related to foreign affairs."
    show rump 3 at Position(xpos = 266)
    show iwanka 1
    rump "And as promised during my campaign..."
    rump "We will take this pathetic shopping center, and turn it into a great {b}MALL{/b}!"
    show rump 2 at Position(xpos = 330)
    rump "It will not be easy!"
    rump "It will not be quick!"
    show rump 3 at Position(xpos = 266)
    rump "But I will see to it as mayor, that our wonderful town becomes {b}GREAT AGAIN!{/b}"
    hide rump
    hide iwanka
    with dissolve
    player_name "( He sure has a way with words... )"
    $ callScreen(location_count)