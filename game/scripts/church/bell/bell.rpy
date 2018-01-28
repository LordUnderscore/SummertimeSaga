label church_bell_dialogue:
    $ location_count = "Church Cloister Bell"
    $ callScreen(location_count)

label church_bell:
    scene location_church_bell_closeup
    if M_aqua.get_state() == S_aqua_bell_search:
        player_name "This bell is massive!"
        player_name "I wonder how Ben Dover was connected to it?"
        player_name "Maybe he helped to build it?"
        player_name "...It sure does look really old."
        player_name "and there's an engraving on it too, just like the tombstone!"
        player_name "Hmm..."
        player_name "Looks like some kind of {b}stone alter{/b}, with {b}trees{/b} around it and the {b}moon{/b} shining down."
        player_name "One of the tree's has a {b}hole{/b} in it too."
        player_name "I wonder what's up with that?"
        player_name "Where could I find something like this in Summerville?"
        $ M_aqua.trigger(T_aqua_bell_engraving)
    else:

        pause
    $ callScreen(location_count)