label obituary_records(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "It seems like the only name under Boatsmith is..."
    player_name "...Ben Dover?"
    player_name "Now I just need to visit the cemetary and find the right tomb stone."
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label scroll(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "There's a strange picture on it."
    player_name "It looks like a crescent moon..."
    player_name "{b}It must be useful for something...{/b}"
    return

label treasure_map(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is too cool! An actual treasure map!"
    player_name "Hmm..."
    player_name "It looks like a drawing of the {b}coast...{/b}"
    player_name "...And that looks like our local beach?"
    player_name "... and here, there's an X on a {b}small island...{/b}"
    player_name "I wonder what it leads to?"
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label weird_coin(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Huh?"
    player_name "That looks like a really old coin."
    player_name "Just look at these odd {b}symbols{/b}!"
    player_name "I should keep it. Maybe it's worth something?"
    return

label old_book(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is a really old book."
    player_name "It looks like it can {b}decipher symbols into numbers{/b}..."
    player_name "I think I'll hang onto it. Could make for an interesting read."
    return

label golden_compass(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whoa!!"
    player_name "I can't believe it! I found the treasure!."
    player_name "This has to be the compass Terry was talking about."
    return

label tigger(item):
    scene backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whew, this mean bastard put up quite a fight."
    player_name "... and just look at those teeth!"
    player_name "It's no wonder why Terry wanted him dead."
    player_name "I can't wait to show him!"
    return