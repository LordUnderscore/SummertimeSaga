label lockershowers_dialogue:
    $ location_count = "Boy's Locker Shower"
    $ callScreen(location_count)

label latinas_button_dialogue:
    if lockershowers_count == 0 and gTimer.gameDay() >= 1:
        scene location_lockershowers_closeup
        show player 57 at left with dissolve
        show latinas 1 at right with dissolve
        lopez "Hey! What are you doing in here?"
        show player 58 at left
        show latinas 1 at right
        player_name "Umm... Just trying to take a shower?"
        show latinas 2 at right
        show player 59 at left
        lopez "Listen, boy. This is our turf, so go take a walk elsewhere!"
        show latinas 3 at right
        martinez "Wait, {b}Lopez{/b}!"
        martinez "Yo, I think this guy's the one people have been talking about!"
        show latinas 2 at right
        lopez "What?! No way..."
        lopez "You telling me this guy's packing a {b}huge dick{/b}?"
        show latinas 3 at right
        martinez "Alright boy! Show us what you got down there, and you can get in!"
        show latinas 1 at right
        show player 60 at left
        player_name "Uhh... I think I'll pass. I'll just shower at home then-"
        show latinas 4 at right
        window hide
        pause
        show player 61 at left
        show latinas 5 at right with hpunch
        window hide
        pause
        player_name "..."
        show player 62 at left
        martinez "There you go!"
        show latinas 6 at right
        lopez "...That's what you call {b}big{/b}?"
        show latinas 7 at right
        show player 63 at left
        martinez "You soft?!..."
        martinez "...He needs a little excitement..."
        martinez "...Hmm..."
        show latinas 8 at right
        martinez "...This should do the trick!"
        show latinas 9 at right
        window hide
        pause
        show player 64 at left
        show latinas 10 at right with hpunch
        window hide
        pause
        show latinas 11 at right
        lopez "Oh my god, puta!"
        martinez "Chill, everyone's seen 'em at school already! Haha!"
        show latinas 12 at right
        lopez "Yo, it's not doing anything!"
        show latinas 13 at right
        martinez "Maybe he's into guys?"
        show latinas 14 at right
        lopez "Here, I know what will work!"
        show latinas 15 at right
        window hide
        pause
        show latinas 15 at right with hpunch
        window hide
        pause
        show player 65 at left
        player_name "...Oh... No..."
        show player 65 at left
        window hide
        pause
        show player 66 at left with hpunch
        window hide
        pause
        show latinas 16 at right
        show player 67 at left
        lopez "Oh, shit!"
        lopez "{b}Annie{/b}'s coming!!"
        show latinas 17 at right
        show player 68 at left
        show annie 1
        ann "..."
        show annie 3
        ann "What's going on here??"
        show player 69 at left
        show annie 1
        player_name "I was just trying to-"
        show player 68 at left
        show annie 3
        ann "Expose yourself inappropriately?"
        show annie 4
        ann "{b}AGAIN{/b}!?"
        show player 69 at left
        show annie 6
        player_name "No, that's not-"
        show player 68 at left
        show annie 5
        ann "I don't want to hear your pathetic excuses!"
        ann "My orders are to bring in repeated offenders to the {b}Office{/b}!"
        show annie 7
        ann "Come with me, {b}NOW{/b}!!!"
        show annie 8f
        ann "...and you two, get out of here before I send you both to detention!!!"
        hide latinas 17 at right
        hide player 68 at left
        hide annie 8f
        with dissolve

        $ lockershowers_count = 1
        $ office_count = 1

        jump office_dialogue
    else:

        scene location_lockershowers_closeup
        show player 57 at left with dissolve
        show latinas 1 at right with dissolve
        lopez "Hey! You here to get us in trouble again?"
        show player 58 at left
        show latinas 1 at right
        player_name "Umm... Just trying to take a shower?"
        show player 59 at left
        show latinas 3 at right
        martinez "Get out of here, yo!"
        show latinas 1 at right
        player_name "..."
    $ callScreen(location_count)