label erik_basement_backroom_dialogue:
    $ location_count = "Erik's Basement Backroom"
    $ callScreen(location_count)

label backroom_aquarium:
    scene expression "backgrounds/location_erik_basement_aquarium.jpg" with None
    show expression "objects/closeup_box.png" at truecenter with dissolve
    player_name "( Here they are! I better get them back to {b}Erik{/b}. )"
    $ inventory.get_item(eriks_cards)
    hide expression "objects/closeup_box.png" with dissolve
    $ callScreen("Backroom Aquarium", False)

label mrsj_afterpoker_fun:
    scene erik_basement_back_c
    show erikmomsex 1 at left
    with dissolve
    erimom "I was wondering what was taking you two so long!"
    show erikmomsex 3
    eri "Sorry, Mom."
    show erikmomsex 1
    erimom "I thought you two didn't want to spend time with me..."
    show erikmomsex 2
    player_name "Of course we do."
    show erikmomsex 1
    erimom "I see you both can't help staring at me."
    erimom "Would you boys like to... touch me?"
    show erikmomsex 2
    player_name "We can?"
    show erikmomsex 3
    eri "Are you sure, Mom?"
    show erikmomsex 1
    erimom "Why don't you give it try?"
    show erikmomsex 4 with fastdissolve
    pause
    show erikmomsex 5
    erimom "Haha!"
    show erikmomsex 6
    erimom "That's all?"
    erimom "You two must be shy!"
    show erikmomsex 7 with fastdissolve
    erimom "Maybe you just need a little encouragement..."
    show erikmomsex 8_9 with fastdissolve
    pause 8
    show erikmomsex 10 with fastdissolve
    erimom "Oh my!"
    erimom "Someone is excited..."
    show erikmomsex 11
    erimom "... and wants more."
    show erikmomsex 12 with fastdissolve
    pause
    show erikmomsex 13_14_13_12
    pause 7.5
    show erikmomsex 12b_13b_14b
    erimom "I could use some help, boys!"
    erimom "Why don't you suck on my nipples, {b}[firstname]{/b}..."
    erimom "... {b}Erik{/b} already knows what to do."
    show erikmomsex 15_16_17
    $ anim_toggle = False
    $ xray = False
    label mrsj_afterpoker_fun_repeat:
        show erikmomsex 17
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        if anim_toggle:
            show erikmomsex 15_16_17 at left
            pause 8
        else:
            $ animcounter = 0
            while animcounter < 3:
                show erikmomsex 15
                pause
                show erikmomsex 16
                pause
                show erikmomsex 17
                pause
                $ animcounter += 1
        show erikmomsex 17
        menu:
            "Keep going.":
                jump mrsj_afterpoker_fun_repeat
            "Make her cum.":

                show erikmomsex 15_16_17 at left
                pause 8
                show erikmomsex 18
                erimom "Ahhh!!!" with hpunch
                show erikmomsex 19 with fastdissolve
                erimom "Goodness me!"
                erimom "That was well done, boys..."
                erimom "I feel like you two wanted more..."
                erimom "I... I think we should stop... for tonight, at least."

                scene erik_basement
                show player 1f at Position(xpos=756)
                show erik 1 at Position(xpos=876)
                show erikmom 28f at left
                with fade
                erimom "Alright boys! I think this is enough for tonight..."
                erimom "I have to get up early tomorrow."
                show erikmom 27f at Position(xoffset=-1)
                show erik 5
                eri "Sorry for keeping you up, Mom..."
                show erikmom 28f
                show erik 1
                erimom "It's fineee! I enjoyed our little night."
                show erikmom 27f at Position(xoffset=-1)
                show player 14f
                player_name "Thanks for playing with us, {b}Mrs. Johnson{/b}."
                show erikmom 28f
                show player 1f
                erimom "It was my pleasure, playing with... with each other."
                show erikmom 34 at center
                hide erik
                hide player
                with dissolve
                erimom "You boys let me know if you need someone to play with again..."
                show erikmom 35
                player_name "Sure thing, {b}Mrs. Johnson{/b}..."
                $ location_count = "Erik's House"
                $ unlock_ui()
                $ mrsj_afterpoker_fun = False
                $ mrsj_poker_night.finish()
                scene erikhouse_night with fade
                $ callScreen(location_count)