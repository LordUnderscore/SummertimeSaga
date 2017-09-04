label mall_dialogue:
    $ location_count = "Mall"
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)
    if mall_count == 0:
        scene mall with None
        show player 14 with dissolve
        player_name "( I love the mall! )"
        show player 17
        player_name "( You can go shopping for all sorts of stuff, there's even a movie theater! )"
        hide player 17 with dissolve
        $ mall_count = 1
    $ callScreen(location_count)

label rump_dialogue:
    scene mall_closeup with None
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