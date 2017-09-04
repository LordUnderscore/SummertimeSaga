label gym_dialogue:
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ location_count = "School Courtyard"
    if player.started(intense_gymercise):
        scene gym with None
        show coach 3 at right
        show jersey 11 at left
        with dissolve
        bri "Well, look what the cat dragged in."
        bri "How's your training?"
        show jersey 10
        show coach 1
        player_name "Uhm... I've been trying to go to the gym!"
        show jersey 11
        show coach 3
        bri "Trying, huh?"
        bri "Let's see how many push-ups you can do, now."
        show coach 2
        bri "Maybe you beat your personal best of... What was it again, two!?"
        show coach 4
        show jersey 22
        bri "Now drop and give twenty!" with hpunch
        show coach 6
        show jersey 29
        with fastdissolve
        pause 0.5
        show jersey 30
        pause 0.5
        show jersey 29
        bri "One!"
        show jersey 30
        pause 0.5
        show jersey 29
        bri "Two!"
        show jersey 30
        pause 0.7
        show jersey 29
        bri "Three!"
        show jersey 30
        pause 0.9
        show jersey 29
        bri "Four!"
        show jersey 27
        show coach 2
        with fastdissolve
        bri "Congratulations, {b}[firstname]{/b}! You've improved from worthless to pathetic!"
        show coach 3
        bri "Keep training, maggot!"
        show coach 1
        show jersey 28
        player_name "Yes... {b}Coach Bridget{/b}..."
        show coach 3
        show jersey 27
        bri "Now get out of my sight!"
        bri "And you better show more progress next time!"
        show coach 1
        player_name "Sorry, {b}Coach Bridget{/b}!"
        hide coach
        hide jersey
        with dissolve
        $ intense_gymercise.finish()

    elif gym_count == 0:
        scene gym
        show jersey 13 at left with dissolve
        show coach 2 at right with dissolve
        bri "Look who decided to show up!"
        show coach 1 at right
        show jersey 17 at left
        player_name "Hi, {b}Coach Bridget{/b}!"
        show jersey 18 at left
        player_name "I know I've missed a few training sessions, but I assure you that I will be ready for the Regional Athletics Tri-"
        show coach 3 at right
        show jersey 22 at left
        bri "Shut up, you maggot!" with hpunch
        bri "You are one month behind everyone else, {b}[firstname]{/b}, and I'm not going to let you drag down the team with your lack of commitment!"
        bri "If you can't make the qualifying scores, you can {b}forget about your credits and graduating this year.{/b}"
        show coach 7 at right
        show jersey 10 at left
        player_name "Don't worry, Ma'am! I'm sure the qualifiers will be no problem!"
        show coach 3 at right
        show jersey 11 at left
        bri "...Oh yeah?"
        bri "Why don't you show us your \"elite athletic skills\" by doing {b}20 pushups{/b} right now, you pathetic little twerp?!"
        show coach 5 at right
        show jersey 10 at left
        player_name "But-"
        show jersey 23 at left
        bri "{b}*WHISTLE*{/b}"
        show coach 6 at right
        show jersey 29 at left
        player_name "Ghh..."
        show jersey 30 at left
        bri "One..."
        show jersey 29 at left
        player_name "Ghhhh..."
        show jersey 30 at left
        bri "Two..."
        show jersey 29 at left
        player_name "...I...I can't..."
        show jersey 30 at left
        bri "Thr-"
        bri "... ... ..."
        show coach 3 at right
        bri "What?!! Is that all you got??"
        show jersey 27 at left
        bri "You can't even do 3 miserable pushups?!"
        show coach 7 at right
        player_name "I..."
        player_name "I'm... Sorry... Ma'am..."
        show coach 3 at right
        bri "You better get your ass to the {b}local Gym{/b} now, and start lifting, if you want to pass this class..."
        show coach 4 at right
        bri "... just stick to {b}Mrs. Bissette's class{/b}, where hard work and good grades don't matter!"
        bri "Now, {b}GET OUT OF MY SIGHT!!!{/b}"
        hide coach 7 with dissolve

        show unlock3 at truecenter
        $ renpy.pause()
        hide unlock3 with dissolve
        $ loc_gym_unlocked = True
        if quest02 not in completed_quests:
            $ quest_list.append(quest02)

        show ronda 3 at right with dissolve
        ron "You're never going to make it past the qualifiers..."
        ron "Why do you even bother coming to this class?"
        show ronda 2 at right
        show jersey 28 at left
        player_name "I can still make it..."
        player_name "...And you know what...I was thinking, maybe you could help me tr-"
        show ronda 4 at right
        show jersey 27 at left
        ron "Hold it right there!"
        ron "If, by some miracle, you manage to {b}make the trials{/b}... then come talk to me. Otherwise, you can stop wasting your breath."
        show ronda 1 at right
        show jersey 28 at left
        player_name "Okay!"
        player_name "But when I do, you'll have to show me some of your tricks!"
        show ronda 3 at right
        ron "I'll be at the {b}swimming pool{/b} for the next two weeks, training for the 200m trials..."
        ron "If you make the team, then come see me."
        show ronda 1 at right
        show jersey 20 at left
        player_name "Deal!!"
        show ronda 3 at right
        show jersey 19 at left
        ron "Ugh... Pathetic..."
        hide ronda 2 at right with dissolve
        hide jersey 19 at left with dissolve
        show unlock4 at truecenter
        $ renpy.pause()
        hide unlock4 with dissolve
        hide gym
        $ loc_pool_unlocked = True
        $ gym_count = 1
        $ classroom_door_count = 2
        $ shower_door_count = 1
        $ stairs_count = 2
        $ left_hall_count = 2
        $ wearing_jersey_count = 1
    else:

        scene gym
        show jersey 11 at left with dissolve
        show coach 3 at right with dissolve
        bri "{b}[firstname]{/b}!"
        show jersey 31 at left
        bri "You better be training your ass off at the {b}Gym{/b}, or I'm going to shove my foot up your ass!!"
        show jersey 32 at left
        show coach 7 at right
        player_name "Yes, Ma'am!!!"
        hide coach 7 at right with dissolve
        hide jersey 32 at left with dissolve
    $ callScreen(location_count)

label coach_button_dialogue:
    scene location_gym_closeup
    show jersey 11 at left with dissolve
    show coach 3 at right with dissolve
    bri "{b}[firstname]{/b}!"
    show jersey 13 at left
    bri "You better be training your ass off at the {b}Gym{/b}, or I'm going to shove my foot up your ass!!"
    show jersey 32 at left
    show coach 7 at right
    player_name "Yes, Ma'am!!!"
    show jersey 31 at left
    show coach 3 at right
    bri "Got any questions?!"
    menu:
        "Where do I train?":
            show jersey 10 at left
            show coach 1 at right
            player_name "I... Well, where should I train?"
            show coach 7 at right
            show jersey 13 at left
            bri "..."
            show jersey 22 at left
            show coach 3 at right
            bri "I just told you!"
            show coach 4 at right
            bri "At the {b}GYM{/b}!!!"
            show jersey 10 at left
            show coach 7 at right
            player_name "But... What should I train?"
            show jersey 11 at left
            show coach 3 at right
            bri "You have to work on your {b}strength{/b} and {b}dexterity{/b} if you want to make it!"
            bri "You'll be competing in the {b}110m hurdle{/b} race to qualify this {b}school{/b} and your team into the {b}state championship{/b}!"
            show jersey 10 at left
            show coach 7 at right
            player_name "That's... A lot of pressure."
            show jersey 23 at left
            show coach 3 at right
            bri "...And you better NOT fail me!"
            show jersey 32 at left
            show coach 7 at right
            player_name "Yes, Ma'am!!!"
            hide coach 7 at right with dissolve
            hide jersey 32 at left with dissolve
        "No.":

            show jersey 10 at left
            show coach 1 at right
            player_name "I don't think so..."
            show jersey 11 at left
            show coach 3 at right
            bri "{b}GOOD{/b}!"
            show jersey 22 at left
            show coach 4 at right
            bri "Now get to {b}WORK{/b}!!"
            show jersey 32 at left
            show coach 7 at right
            player_name "Yes, Ma'am!!!"
            hide coach 7 at right with dissolve
            hide jersey 32 at left with dissolve
    $ callScreen(location_count)