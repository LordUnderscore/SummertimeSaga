label office_dialogue:
    $ location_count = "Mrs Smith's Office"
    if quest09_1 == True and quest09 not in completed_quests:
        scene office_clear
        show principal 22 at Position(xpos = 200, ypos = 764)
        player_name "!!!"
        window hide
        pause
        show principal 23
        window hide
        pause
        show principal 22
        window hide
        pause
        show principal 23
        window hide
        pause
        show principal 24 with hpunch
        smi "!!!"
        show principal 25
        smi "What're you doing in {b}MY OFFICE{/b}??"
        show principal 24
        player_name "I... I was told to bring you this {b}receipt{/b} for a delivery?"
        show principal 25
        smi "You insubordinate simpleton! Can't you see I'm busy?"
        show principal 24
        player_name "I'm sorry, {b}Mrs. Smith{/b}..."
        show principal 25
        smi "No one ever taught you how to {b}KNOCK{/b}?!"
        show principal 24
        player_name "..."
        show principal 25
        smi "Drop off the {b}receipt{/b} in my {b}green drawer{/b}."
        show principal 24
        player_name "Yes, {b}Mrs. Smith{/b}! Right away..."

    elif office_count == 0:
        scene office
        show principal 5 at right with dissolve
        show player 1 at left with dissolve
        smi "What are you doing here?!"
        show player 11 at left
        show principal 3 at right
        player_name "Oh... umm..."
        show player 21 at left
        player_name "I was... looking for the washroom!"
        show player 22 at left
        show principal 4 at right
        smi "Don't play dumb with me, {b}[firstname]{/b}!"
        smi "Didn't I just tell you earlier, to get to class??!"
        show player 10 at left
        show principal 1 at right
        player_name "Well..."
        show player 22 at left
        show principal 2 at right
        smi "Now, get out of my {b}OFFICE{/b}!!!"
        hide player 22 at left with dissolve
        hide principal 2 at right with dissolve

    elif office_count == 1:
        scene office
        show principal 6 at right
        show player 1 at left
        with dissolve
        ann "{b}Mrs. Smith{/b}?"
        show principal 7 at right
        smi "What is it??"
        show principal 6 at right
        ann "Reporting repeated offenders as you ordered!"
        show principal 9 at right
        show player 13 at left
        smi "This... Young man right here?"
        show principal 8 at right
        ann "Yes, Ma'am!"
        show principal 9 at right
        smi "Hmmm... You must be {b}[firstname]{/b}, am I right?"
        show player 10 at left
        player_name "Uh.. Yes Ma'am!"
        show player 5 at left
        smi "You're the one causing trouble in the locker room..."
        smi "...and spreading rumours..."
        show principal 7 at right
        smi "What happened, exactly, {b}Annie{/b}?"
        show principal 6 at right
        ann "Well, his... he... He's showing inappropriate body parts to the girls in the locker room, Ma'am."
        show principal 9 at right
        smi "Is that so?"
        show player 10 at left
        player_name "Well... I can explain-"
        show player 22 at left
        show principal 10 at right with hpunch
        smi "{b}SILENCE{/b}!!!"
        show principal 9 at right
        show player 5 at left
        smi "...I need to see exactly what happened. Show me what you did, now."
        show principal 6 at right
        ann "Ma'am, it won't work..."
        ann "It only seems to happen when... he sees women in the {b}nude{/b}, Ma'am."
        show principal 7 at right
        smi "Well, what are you waiting for, {b}Annie{/b}?"
        smi "You're going to have to help him with that."
        show principal 11 at right
        show player 11 at left
        ann "{b}What??!{/b}"
        show principal 12 at right
        smi "You're the one who witnessed it and reported the infraction..."
        smi "...It's your {b}duty{/b} to carry out the report!"
        player_name "We really don't have to do this-"
        show principal 10 at right
        show player 22 at left
        smi "No one's leaving until I get a full report! Do it, or you both are in {b}DETENTION{/b}!!!"
        show principal 13 at right
        ann "..."
        show player 8 at left
        show principal 14 at right
        window hide
        pause
        show player 63 at left
        show principal 15 at right
        window hide
        pause
        show principal 16 at right
        show player 64 at left
        smi "Now, look at those {b}firm breasts{/b} of hers..."
        show principal 17 at right
        smi "Don't you want to... suck on them? {b}[firstname]{/b}?"
        show player 65 at left
        player_name "..."
        show player 66 at left
        window hide
        pause
        show player 66 at left with hpunch
        window hide
        pause
        show player 67 at left
        smi "There we are..."
        show principal 18 at right
        smi "That's enough, {b}Annie{/b}. You can leave now..."
        show principal 5 at right with dissolve
        smi "So!..."
        smi "This is what I've been hearing about this whole time."
        hide player 67 at left
        show principal 19 at left
        with dissolve
        smi "You've made quite a reputation around school..."
        smi "I can see why..."
        smi "...this has been a..."
        show principal 20 at left
        window hide
        pause
        show principal 21 at left with hpunch
        window hide
        pause
        smi "...distraction!"
        show player 69 at left
        show principal 1 at right
        with dissolve
        player_name "I'm sorry, Ma'am!"
        player_name "It won't happen again, I promise!"
        show principal 5 at right
        show player 68 at left
        smi "Alright young man: Here's the deal..."
        smi "I won't send you to detention, as long as you keep this... \"problem\" of yours... to yourself."
        smi "My priority is order and discipline in this school, and I plan on keeping it that way!"
        show principal 1 at right
        show player 69 at left
        player_name "Yes, {b}Mrs. Smith{/b}!"
        show principal 2 at right
        show player 68 at left
        smi "Now, get out of my {b}OFFICE{/b}!!"
        hide player 68 at left with dissolve
        hide principal 2 at right with dissolve
        $ office_count = 0
    $ callScreen(location_count)

label desk03_locked_dialogue:
    scene office
    show player 30 at left
    player_name "Hmmm... I wonder what's in there?"
    show player 22 at left with hpunch
    show principal 4 at right with dissolve
    smi "What are you doing?"
    show principal 1 at right
    show player 29 at left
    player_name "Oh, I'm sorry... I was just looking!"
    show player 3 at left
    show principal 5 at right
    smi "If I {b}EVER{/b} catch you going through my things..."
    show principal 2 at right
    smi "...you can be sure, you'll be spending the rest of the year in {b}DETENTION{/b}!!!"
    $ callScreen(location_count)

label principle_drawer:
    scene principle_drawer
    show expression "objects/object_papers_01.png" at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "What's with all those... leather things... in here?"
    player_name "weird..."
    call screen principle_drawer

label milk_delivery:
    scene office with None
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smi "Ah, wonderful."
    smi "Are those the new {b}milk cartons{/b}?"
    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... Yeah."
    show principal 27f
    show player 163f
    smi "I sampled the last batch..."
    smi "It was quite... delightful. You're lucky I'm in a good mood."
    smi "Please, tell the milk provider I'm doubling our next order."
    smi "We keep running out. The students absolutely love it!"
    show principal 26f
    show player 164f
    player_name "Will do! Where can I put these cartons?"
    show principal 27f
    show player 163f
    smi "You can give them to {b}Annie{/b}, she'll take care of them."
    show principal 4f at Position (xpos = 470)
    show player 167f
    smi "Now, get out of my office, I have some unfinished business to attend to."
    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Yes, {b}Mrs. Smith{/b}!"
    hide principal
    hide titty
    hide player
    with dissolve
    $ quest09_1 = False
    $ quest09_2 = True
    $ callScreen(location_count)