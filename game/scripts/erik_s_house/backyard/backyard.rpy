label erik_backyard_dialogue:
    $ location_count = "Erik's Backyard"
    if erik.in_progress(erik_thief):
        scene eriks_backyard_n
        show door_thief_night at Position (xpos=882,ypos=655)
        player_name "( Is he...trying to get into {b}Mrs. Johnson{/b}'s back door? )"
        player_name "( This must be the burglar we keep hearing about in the news. )"
        player_name "( I should get a closer look... )"
    $ callScreen(location_count)

label erik_thief_block2:
    scene eriks_backyard_n
    show door_thief_night at Position (xpos=882,ypos=655)
    player_name "( I can't leave just yet. )"
    player_name "( What if he's trying to break in?! )"
    player_name "( I have to make sure nothing bad happens... )"
    $ callScreen(location_count)

label erik_thief:
    $ unlock_ui()
    scene eriks_backyard_c
    show larry 1 at Position (xpos=800) with dissolve
    show player 12 at left with dissolve
    player_name "...Uhm!"
    player_name "Excuse me!"
    show player 16
    show larry 2 at right with dissolve
    thief "!!!" with hpunch
    show player 12
    player_name "What're you doing?"
    show player 16
    show larry 3 with dissolve
    thief "Oh shi-"
    hide larry with dissolve
    show player 15
    player_name "HEY!"
    player_name "Stay right there!!"
    hide player with dissolve

    scene erik_house_cs03 with fade
    show text "I was about to confront him while he was trying to break in...\n...But he took off right away, making his way towards the fence.\nI was catching up to him, and then..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    if pStats.dex() >= 5:
        scene erik_house_cs05 with fade
        show text "...He ran up to the fence and tried to jump...\n...But I was just in time to get a hold of him and pin him down..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
    else:

        scene erik_house_cs04 with fade
        show text "...He ran up to the fence and jumped over it with one step!!\nI wasn't quite agile enough to get him..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text

        scene eriks_backyard_c with None
        show player 25 with dissolve
        player_name "[dex_warn]Damn..."
        player_name "[dex_warn]I can't believe he jumped that high, and I let him get away!"
        player_name "[dex_warn]I need to get in better shape if I ever want to catch him."
        show player 24
        player_name "[dex_warn]Ugh."
        player_name "[dex_warn]I should get back to bed..."
        hide player with dissolve
        scene black with fade
        jump sleeping

    scene eriks_backyard_c
    show larry 4 at left
    with dissolve
    player_name "Hey!"
    show larry 5
    pause
    show larry 4
    player_name "What were you doing?!"
    player_name "Stop moving around!"
    player_name "You're not going anywhere."
    show larry 7
    show erik 52 at Position (xpos=750)
    show erikmom 52 at right
    erimom "What's making all that noise in our backyard?"
    erimom "Who's out there?"
    show erikmom 38
    show erik 53
    eri "{b}[firstname]{/b}?"
    show erik 52
    show larry 6
    player_name "I'm sorry, {b}Mrs. Johnson{/b}. I didn't want to wake you up..."
    show larry 4
    player_name "...But I caught this guy trying to sneak into your house!"
    show larry 7
    show erik 51
    show erikmom 19
    erimom "!!!"
    show erikmom 52
    erimom "What? What happened?"
    show erikmom 38
    show erik 52
    show larry 6
    player_name "Well, I heard some noises from my room, and I saw this guy sneaking around in your backyard."
    player_name "I went outside to see where he went and found him by your door trying to break in!"
    show larry 4
    player_name "He tried to run away, but I was able to catch up to him..."
    show larry 7
    show erikmom 19
    erimom "Oh my!"
    show erikmom 38
    show larry 5
    erimom "Let's see who's behind this mask..."
    hide erikmom
    hide larry
    show larry 8 at left
    with dissolve
    pause
    show larry 9
    show erikmom 61 at right
    with dissolve
    show erik 51
    erimom "!!!" with hpunch
    show erik 53
    eri "{b}Dad{/b}?!"
    show erik 3b
    player_name "!!!"
    show erikmom 51 with dissolve
    show larry 10
    larry "I'm so sorry..."
    show larry 11
    show erikmom 52
    erimom "{b}Larry{/b}! What on earth are you doing in town? I thought you were living out of state?"
    show erikmom 51
    show erik 52
    show larry 10
    larry "I... I know... It's just..."
    larry "...A few years ago my band fell apart."
    larry "I had money problems and... I had to come back."
    show larry 9
    show erikmom 52
    erimom "You've been back here for a few years now?!"
    show erikmom 51
    show larry 11
    larry "..."
    show erikmom 52
    erimom "Explain yourself, {b}Larry{/b}!"
    show erikmom 51
    show larry 10
    larry "I... I didn't have the guts to see you after I had left you..."
    show larry 9
    show erikmom 19
    erimom "And you just decided it'd be good to start stealing?"
    show erikmom 19c
    show larry 11
    larry "..."
    show larry 10
    larry "I couldn't find work!"
    larry "And... everybody knows me around here."
    larry "I didn't want anybody to know..."
    show larry 11
    show erikmom 52
    erimom "Why come back at all, then? "
    show erikmom 51
    show erik 51
    show larry 10
    larry "I... wanted to see my only son, {b}Erik{/b}..."
    larry "I've been stopping by at night for the last couple months, hoping to bump into him..."
    show larry 9
    show erik 52
    show erikmom 52
    erimom "You should have thought about that before leaving us!!"
    erimom "You know what? You haven't changed one bit."
    erimom "You still just think about yourself!!"
    show erikmom 51
    show erik 53
    eri "{b}Mom{/b}... What happens now?"
    show larry 11
    show erik 51
    show erikmom 52
    erimom "Call the police."
    erimom "We'll let them deal with him."
    hide erikmom
    hide erik
    hide larry
    with dissolve
    scene black with fade

    scene erik_house_night_cops
    pause
    show player 5f at Position (xpos=650)
    show erik 52 at Position (xpos=775)
    show erikmom 51 at right
    show harold 3f at left
    show larry 13 at Position (xpos=275)
    with dissolve
    harold "It's a good thing you called!"
    harold "We've been trying to catch him for two years..."
    show harold 1f
    show erikmom 52
    show larry 12
    erimom "I... I never thought I'd see him again..."
    erimom "...He's always been trouble!"
    erimom "I'm just glad it's over and he can be out of our lives for good!"
    show erikmom 51
    show larry 12b
    show erik 51
    show player 11f
    larry "{b}Erik{/b}!"
    show erik 52
    larry "I'm glad you're doing okay..."
    larry "...I miss you!!"
    show larry 12
    show erik 50
    show player 5f
    eri "..."
    show larry 13
    show harold 3f
    harold "Come on, {b}Larry{/b}. Let's take you to the station."
    hide harold
    hide larry
    with dissolve
    show player 11f
    show erik 2
    show erikmom 61
    with dissolve
    pause
    hide player
    hide erik
    hide erikmom
    with dissolve
    $ erik.complete_events(erik_thief)
    show unlock44 at truecenter with dissolve
    pause
    hide unlock44 with dissolve
    jump sleeping