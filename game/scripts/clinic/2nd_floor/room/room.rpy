label hospital_second_floor_room_dialogue:
    $ location_count = "Hospital 2nd Floor Room"
    $ callScreen(location_count)

label erik_bullying_2:
    $ location_count = "Hospital 2nd Floor Room"
    scene hospital_bed
    show player 392 at Position (xpos=805, ypos=665)
    show micoe 5 at left
    with fade
    "Hello, how-"
    "..."
    show micoe 4
    "Hum hum!!"
    player_name "Uh...."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "Oh good! You're starting to wake up."
    show micoe 2
    "How are you feeling?"
    show micoe 1
    show player 398 at Position (xpos=772, ypos=664)
    player_name "I..."
    show player 397 at Position (xpos=772, ypos=660)
    player_name "I feel fine."
    show player 394 at Position (xpos=768, ypos=660)
    player_name "A bit dizzy actually."
    pause
    show player 396 at Position (xpos=772, ypos=660)
    player_name "Where am I?"
    show player 397
    show micoe 5
    "You're in the hospital."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "I am?"
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "That's right!"
    show micoe 2
    micoe "And I'm {b}Nurse Micoe{/b}."
    show micoe 5
    micoe "You had a minor concussion, but you'll be fine."
    micoe "You can go home when you feel ready."
    micoe "Just make sure to drink plenty of water and get some rest."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Oh, I see... Thank you."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 2
    micoe "I forgot to mention that you have a visitor!"
    hide micoe with dissolve
    pause
    show player 393
    pause
    show erik 4f at left with dissolve
    eri "Hey, {b}[firstname]{/b}!"
    eri "How are you doing?"
    show erik 1f
    show player 395
    player_name "Hey {b}Erik{/b}. I'm fine, I think!"
    show player 393
    show erik 5f
    eri "Dexter really got you good, huh."
    show erik 1f
    show player 395
    player_name "Nah, {b}Dexter{/b} punches like a girl!"
    show player 393
    show erik 4f
    eri "Heh heh."
    eri "Thanks for standing up for me today."
    show erik 1f
    show player 395
    player_name "It's alright."
    show player 393
    show erik 5f
    eri "No one has ever stood up to {b}Dexter{/b} before."
    show erik 4f
    eri "Everyone in the school is talking about it."
    show erik 1f
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Eh... I wish it didn't have to go that way..."
    player_name "...And I still got my ass kicked!"
    show player 393 at Position (xpos=772, ypos=660)
    show erik 4f
    eri "Well, {b}Dexter{/b} will think twice before he does something like that again."
    show erik 1f
    show player 395
    player_name "Heh! We'll see about that."
    show player 393
    pause
    show erik 4f
    eri "Hey, I overheard the nurse say you can go home."
    eri "Ready?"
    show erik 1f
    show player 395
    player_name "Yeah."
    hide player
    hide erik
    with dissolve
    $ erik_bullying_2.finish()
    show unlock40 at truecenter with dissolve
    $ loc_clinic_unlocked = True
    $ gTimer.tick(3)
    pause
    hide unlock40 with dissolve
    $ callScreen(location_count)