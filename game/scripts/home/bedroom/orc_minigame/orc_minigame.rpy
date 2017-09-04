init python:
    def orcHit():
        global life
        global slider_time
        if orc_slider.xpos >= 470 and orc_slider.xpos <= 527:
            life -= 1
            slider_time -= 0.75
            renpy.jump("orc_battle_hit")
        else:
            renpy.jump("orc_battle_fail")

transform orc_slide1:
    xpos 229
    ypos 695
    ease slider_time xpos 772
    ease slider_time xpos 229
    repeat

transform orc_slide2:
    xpos 772
    ypos 695
    ease slider_time xpos 229
    ease slider_time xpos 772
    repeat

image orc_slider = "buttons/arrows_02.png"

label orc_battle_prep:
    $ life = 3
    $ slider_time = 3.5
    jump orc_battle_start

label orc_battle_start:
    $ location_count = "Orc Battle"
    $ x = renpy.random.randint(0,99)
    if x < 74:
        $ orc_slider = At(ImageReference("orc_slider"), orc_slide1)
    else:
        $ orc_slider = At(ImageReference("orc_slider"), orc_slide2)
    scene expression "backgrounds/minigame07a.jpg"
    if life > 2:
        show expression "buttons/health_01.png" as life1 at Position(xpos=432, ypos=667)
    if life > 1:
        show expression "buttons/health_01.png" as life2 at Position(xpos=509, ypos=667)
    if life > 0:
        show expression "buttons/health_01.png" as life3 at Position(xpos=585, ypos=667)
    show expression orc_slider
    $ callScreen(location_count, False, False)

label orc_battle_hit:
    scene expression "backgrounds/minigame07b.jpg"
    if life > 2:
        show expression "buttons/health_01.png" as life1 at Position(xpos=432, ypos=667)
    if life > 1:
        show expression "buttons/health_01.png" as life2 at Position(xpos=509, ypos=667)
    if life > 0:
        show expression "buttons/health_01.png" as life3 at Position(xpos=585, ypos=667)
    with hpunch
    $ renpy.pause(0.7, hard=True)
    if life > 0:
        jump orc_battle_start
    else:
        jump orc_battle_finish

label orc_battle_finish:
    $ location_count = "Bedroom"
    scene expression "backgrounds/minigame07c.jpg" with dissolve
    $ renpy.pause(0.7, hard=True)
    scene expression "backgrounds/minigame07d.jpg" with dissolve
    $ renpy.pause(1, hard=True)
    scene expression Animation("backgrounds/minigame07e.jpg", 0.5, "backgrounds/minigame07f.jpg", 0.5) with fade
    pause
    $ gTimer.tick()
    if not June.known(june_cosplay):
        scene bedroom_sex2
        if June.over(june_mc_help_2):
            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "Looks like we got the same ending again."
            show player_sitting 3
            june "Sorry..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, It's okay!"
            show june_sitting 12
            show player_sitting 5
            june "Do you still think it's weird?"
            show june_sitting 13
        else:

            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "I... I didn't know that's how the game ends, I swear!"
            show june_sitting 13
            show player_sitting 4
            player_name "That was... unexpected?"
            show june_sitting 12
            show player_sitting 3
            june "This is so embarrassing..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, It's okay!"
            show june_sitting 12
            show player_sitting 5
            june "You didn't find that too weird?"
            show june_sitting 13
            $ june_mc_help_2.finish()
        menu:
            "It's gross.":
                show june_sitting 13 at Position(xpos=300,ypos=787)
                show player_sitting 4 at right
                player_name "I dunno... It's kind of gross?"
                show player_sitting 5
                june "..."
                show player_sitting 6
                player_name "But, whatever, it's fine."
                show player_sitting 1
                show june_sitting 12
                june "I'm sorry... If I had known..."
                june "Do you still want to play the game with me though?"
                show player_sitting 2
                show june_sitting 13
                player_name "Yeah, it's fun!"
                show player_sitting 1
                show june_sitting 12
                june "Thanks... Anyway, I really should get going, It's getting late."
                show player_sitting 2
                show june_sitting 11
                player_name "Okay!"
                player_name "Have a good night!"
                show player_sitting 1
                show june_sitting 10
                june "You too, {b}[firstname]{/b}."
            "It's hot!":

                show player_sitting 2 at right
                show june_sitting 11 at Position(xpos=300,ypos=787)
                player_name "Nah, it's actually kind of funny... "
                player_name "... and kind of hot."
                show june_sitting 10
                show player_sitting 1
                june "Really? You... think so?"
                show june_sitting 11
                show player_sitting 2
                player_name "Yeah, I guess orcs can be pretty sexy!"
                show player_sitting 1
                june "..."
                show june_sitting 10
                june "I... I love orcs..."
                show player_sitting 5
                june "In fact, I was actually planning on cosplaying as one soon..."
                show player_sitting 2
                show june_sitting 11
                player_name "An orc costume? What for?"
                show player_sitting 1
                show june_sitting 10
                june "I was planning on going to a comic convention dressed as an orc..."
                show june_sitting 12
                june "... but there's a problem."
                june "I don't think I can find all the costume pieces in time."
                show player_sitting 2
                show june_sitting 11
                player_name "That sounds cool!"
                show player_sitting 1
                show june_sitting 10
                june "You think so?"
                show player_sitting 2
                show june_sitting 11
                player_name "What is it you're missing?"
                show player_sitting 1
                show june_sitting 10
                june "I have the body paint... But I need the fake ears, the teeth and... the belt."
                show player_sitting 2
                show june_sitting 11
                player_name "I bet I could find those for you!"
                show player_sitting 1
                show june_sitting 10
                june "Really? You would do that for me??"
                show player_sitting 2
                show june_sitting 11
                player_name "I can try!"
                show player_sitting 6
                player_name "I think you'd look amazing as an orc!"
                show player_sitting 1
                june "..."
                show player_sitting 3
                show june_sitting 10
                june "That's really sweet. Thanks, {b}[firstname]{/b}."
                show player_sitting 2
                show june_sitting 11
                player_name "Well, I should probably go to bed..."
                show player_sitting 1
                show june_sitting 10
                june "Yeah, I should get home too..."
                june "Thanks for having me over! It was fun."
                show player_sitting 6
                show june_sitting 11
                player_name "Yeah, it really was."
                show player_sitting 1
                show june_sitting 10
                june "Let me know if you ever find those costume parts!"
                june "See you tomorrow?"
                show player_sitting 2
                show june_sitting 11
                player_name "Sure!"
                player_name "Come on, I'll see you out."
                scene bedroom_night
                show player 35
                with fade
                player_name "Hmm... I wonder where I could find those {b}costume parts{/b}."
                player_name "Maybe I should go check at the {b}mall{/b}?"
                show player 55 at Position(xoffset=12)
                player_name "*Yawn*"
                show player 56
                player_name "I'll go tomorrow, I need some sleep..."
                hide player with dissolve
                $ June.add_event(june_cosplay)
                jump sleeping
    else:

        scene bedroom_sex2
        show june_sitting 2 at Position(xpos=300,ypos=787)
        show player_sitting 1 at right
        with fade
        june "Finally! I've been trying to beat this one for days..."
        show june_sitting 3
        june "You're getting really good at this."
        show june_sitting 4
        show player_sitting 6
        player_name "Yeah, I guess that game really is addicting!"
        show june_sitting 1
        show player_sitting 2
        player_name "Hey, what's the time?"
        show june_sitting 5
        show player_sitting 5
        june "Oh crap, it's past midnight..."
        show june_sitting 6
        show player_sitting 4
        player_name "Oh, we've been here longer than I thought..."
        player_name "Looks like we lost track of time."
        show june_sitting 5
        show player_sitting 1
        june "I should get home, my parents are probably worried sick."
        show june_sitting 3
        june "Thanks for the evening, {b}[firstname]{/b}."
        show june_sitting 4
        show player_sitting 2
        player_name "See you at school?"
        show player_sitting 1
        show june_sitting 3
        june "You bet!"
    $ callScreen(location_count)

label orc_battle_fail:
    $ location_count = "Bedroom"
    $ gTimer.tick()
    scene bedroom_sex2
    show june_sitting 4 at Position(xpos=300,ypos=787)
    show player_sitting 4 at right
    with fade
    player_name "Oops..."
    show player_sitting 3
    show june_sitting 3
    june "Huh, I guess we'll need to practice a bit."
    show player_sitting 4
    show june_sitting 4
    player_name "Ha ha, sorry."
    show player_sitting 3
    show june_sitting 3
    june "It's okay, I'm sure we'll beat it eventually!"
    show player_sitting 6
    show june_sitting 4
    player_name "I hope so! Otherwise I'm a terrible team mate..."
    show player_sitting 1
    show june_sitting 3
    june "Anyway, I should get going, it's starting to get pretty late."
    june "Let me know if you want to play again tomorrow!"
    show player_sitting 2
    show june_sitting 4
    player_name "Okay!"
    player_name "Have a good night!"
    show player_sitting 1
    show june_sitting 3
    june "You too, {b}[firstname]{/b}."
    $ callScreen(location_count)