init python:
    import re
    class Trigger(object):
        """A Trigger is just a place holder used for the FSM

        Triggers are global in nature and when applied to any state machine 
        it triggers to all statemachines.
        """        
        def __init__(self,name,description):
            self._name = name
            self._desc = description
        
        def __repr__(self):
            return "{}: {}".format(self._name, self._desc)

    class State(object):
        """A State object holds a list of all the states that are
        Reachable from this state.  The next state is determined by
        the trigger supplied.

        In addition to keeping track of the state transitions, there
        is also the ability to accomplish tasks.  Tasks consist of
        setting, clearing, assigning, or generating one or more new
        Triggers.
        """
        def __init__(self,name,description=None):
            self._name = name
            self._desc = description
            self._table = {}
            self._actions = {}
        def __repr__(self):
            return "{}: {}".format(self._name,self._desc)
        def dump(self):
            result = ""
            for t in self._table:
                result += str(t)+"\n"
            return result
        
        
        
        
        def add(self,trigger,state,actions=None,location=None,
                force_location=None):
            if state in self._table:
                raise Exception("Duplicate trigger added")
            self._table[trigger] = state
            if actions:
                self._actions[trigger] = actions
            else:
                self._actions[trigger] = []
            if location is not None:
                self._actions[trigger].append('location')
                self._actions[trigger].append(location)
            if force_location is not None:
                self._actions[trigger].append('force')
                self._actions[trigger].append(force_location)
        
        
        
        def trigger(self,trigger,machine):
            if trigger in self._table:
                
                
                actions = self._actions[trigger]
                for i in xrange(0,len(actions)-1,2):
                    act = actions[i].lower()
                    target = actions[i+1]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    act = act.lower()
                    if act == 'set':
                        machine.set(target,True)
                    elif act=='clear':
                        machine.set(target,False)
                    elif act == 'assign':
                        machine.set(target[0],target[1])
                    elif act == 'inc' or act=='increment':
                        machine.increment(target,1)
                    elif act == 'dec' or act=='decrement':
                        machine.increment(target,-1)
                    elif act == 'trigger':
                        machine.trigger(target)
                    elif act == 'triggeronzero':
                        machine.triggerOnZero(target[0],target[1])
                    elif act == 'location':
                        machine._loc = target
                    elif act == 'force':
                        machine._force_loc = target
                    elif act == 'call':
                        renpy.call(target)
                    else:
                        raise Exception("{} unknown action: {} on {}".format(self._name, act,target))
                return self._table[trigger]
            else:
                return None
        
        def get_actions(self,trigger):
            return self._actions[trigger]

    class Machine(KeepRefs):
        _trigger_queue = []
        _running = False
        def __init__(self,name,location,description=None,states=None, vars=None,
                     force_location=False):
            super(Machine,self).__init__()
            self._name = name
            self._desc = description
            if states:
                self._states = states
            else:
                self._states={}
            if vars:
                self._vars = vars
            else:
                self._vars = {}
            self._state=None
            self._loc = location
            self._force_loc = force_location
        
        def __repr__(self):
            if self._state is None:
                state="NOT INITIALIZED"
            else:
                state = self._state._name
            return "{}@{} at {}".format(self._name, state, self._loc)
        
        def dump(self):
            vlist =""
            for k,v in self._vars.iteritems():
                vlist+="\n{}:{}".format(k,v)
            loc = "Location: {} Forced: {}\n".format(self._loc,self._force_loc)
            return self._state.dump()+loc+vlist
        
        @classmethod
        def trigger(cls,trigger):
            if trigger not in cls._trigger_queue:
                cls._trigger_queue.append(trigger)
                cls._do_trigger()
        @classmethod
        def _do_trigger(cls):
            
            if cls._running:
                return
            cls._running = True
            while len(cls._trigger_queue) > 0:
                trigger = cls._trigger_queue[0]
                
                
                
                
                
                
                
                
                
                for m in machines:
                    result = m.get_state().trigger(trigger,m)
                    if result is not None:
                        
                        m._state = result
                cls._trigger_queue = cls._trigger_queue[1:]
            cls._running = False
        
        def add(self,*args):
            for s in args:
                if self._state is None:
                    self._state = s
                self._states[s] = s
        def get(self,var):
            return self._vars[var]
        def set(self,var,value):
            self._vars[var] = value
        def increment(self,var,amount):
            self._vars[var] += amount
        def get_state(self):
            return self._state
        def is_set(self,flag):
            return self._vars[flag]
        def triggerOnZero(self,target,trigger):
            if target in self._vars:
                r = self._vars[target]-1
                if r < 0:
                    r = 0
            else:
                r = 0
            self._vars[target] = r
            if r <= 0:
                self.trigger(trigger)
        def where(self):
            return self._loc
        def forced(self):
            return self._force_loc
label INIT_FSM:
    python:

        T_all_sleep = Trigger("sleep", "Sleep for the night")
        T_all_school_entrance = Trigger("hallway", "Meet everyone back at school")


        T_angelica_house_visit = Trigger("house visit", "Angelica pays your house a visit")
        T_angelica_ritual_deal = Trigger("ritual deal", "Angelica makes you agree to her ritual deal")
        T_angelica_requires_whip = Trigger("requires whip", "Angelica requires a whip for her next sacrement")
        T_angelica_sinful_thoughts = Trigger("sinful thoughts", "Angelica says she will punish you if you have sinful thoughts")
        T_angelica_strapon_request = Trigger("strapon request", "Angelica's final sacrament requires a special tool")
        T_angelicas_final_ritual = Trigger("final ritual", "Angelica's final sacrament shall now begin")


        T_aqua_special_lure = Trigger("special lure", "Find the golden compass to trade for the special lure")
        T_aqua_obituary_records = Trigger("obituary records", "Get access to the obituary Records")
        T_aqua_tomb_engraving = Trigger("tomb engraving", "Discover an engraving on the boatsmith's tomb")
        T_aqua_bell_engraving = Trigger("bell engraving", "Discover an engraving on the chuech bell")
        T_aqua_altar_puzzle_solve = Trigger("altar puzzle solve", "You solved the painful puzzle at the altar")
        T_aqua_treasure_found = Trigger("treasure found", "You found the treasure after such hard work")
        T_aqua_treasure_unlocked = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_lure_steal = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_dive = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_chase_fail = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_squid_defeated = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_maze_conquered = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_lair_found = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_friended = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_mating_offer = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_test_pass = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
        T_aqua_mated = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")

        T_harold_donuts = Trigger("advance", "Give Harold with donuts")
        T_harold_leaves = Trigger("leaves", "Harold decided to leave")
        T_harold_missing = Trigger("missing", "Harold has gone missing")
        T_harold_photo_clue = Trigger("photo clue", "A photo of Harold and Helen suggesting where he is")
        T_harold_found = Trigger("found", "You found Harold")
        T_harold_glasses = Trigger("glasses", "You gave Harold his glasses")
        T_harold_grows_a_pair = Trigger("grows a pair", "Harold grows a pair and rushes to help Yumi")
        T_harold_backup = Trigger("backup", "Harold's backup helped save the day")
        T_harold_find_goods = Trigger("find goods", "Harold needs you to find the stolen goods for him")
        T_harold_found_goods = Trigger("found goods", "You found the stolen goods for Harold")
        T_harold_promotion = Trigger("pomotion", "Harold will now get a promotion for finding the goods")
        T_harold_indecisiveness = Trigger("indecisiveness", "Harold still hasn't decided to stay with or leave Helen")
        T_harold_new_girl = Trigger("new girl", "Harold found foudn himself a new girl to be with")


        T_helen_confessional = Trigger("confessional", "Helen has entered the confessional")
        T_helen_convince_fail = Trigger("convince fail", "You failed to convince Helen to change")
        T_helen_convince_change = Trigger("convince change", "You convinced Helen to try to change")
        T_helen_secret_sacrement = Trigger("secret asacrement", "Ask Helen to join the ancient sacrement")
        T_helen_angelica_ritual = Trigger("convince change", "Helen does the sacrement with Angelica")
        T_helen_caught_masturbating = Trigger("caught masturbating", "You caught Helen masturbating")
        T_helen_sexy_lingerie = Trigger("sexy lingerie", "You gave Helen a sexy red corset lingerie set")
        T_helen_torture = Trigger("torture", "Helen gets tortured by Angelica for her own good")
        T_helen_thanks = Trigger("thanks", "Helen thanks you for your concern and offer")
        T_helen_master_servant = Trigger("master servant", "Helen wants a spanking from her master")
        T_helen_route = Trigger("route", "This sets you permanently onto Helen's route")
        T_helen_master_servant_sex = Trigger("master servant sex", "Helen wants to have more sex with you to stay pure")


        T_mc_homework = Trigger("homework", "Complete French homework")
        T_mc_nun_thoughts = Trigger("nun thoughts", "You go over the predicament the nun has put you in")


        T_mia_on_zero = Trigger("advance", "Mia story delay")
        T_mia_kiss = Trigger("kiss", "Kiss Mia while studying")
        T_mia_kicked_out = Trigger("kicked out", "Kicked out of Mia's house")
        T_mia_plan = Trigger("plan", "Plan with Mia")
        T_mia_results = Trigger("results", "Learn results with Mia")
        T_mia_delay = Trigger("delay", "Delay a story trigger")
        T_mia_tattoo_start = Trigger("tattoo start", "Start the process of helping Mia get a tattoo")
        T_mia_easel_found = Trigger("easel", "Found an easel to draw a tattoo for Mia")
        T_mia_visit = Trigger("visit", "Visit and talk to Mia")
        T_mia_wrong_tattoo = Trigger("wrong tattoo", "Mia doesn't like the tattoo you drew")
        T_mia_right_tattoo = Trigger("right tattoo", "Mia likes the tattoo you drew")
        T_mia_visit_tattoo_parlor = Trigger("visit tattoo", "Go with Mia to the tattoo parlor")
        T_mia_tattoo_done = Trigger("tattoo done", "Mia has rebelled and has a new tattoo")
        T_mia_night_invite = Trigger("night invite", "Mia invites you over for the night")
        T_mia_strip_tease = Trigger("strip tease", "Mia give you a nice strip show")
        T_mia_grounded = Trigger("grounded", "Mia has been grounded after being caught")
        T_mia_message = Trigger("message", "Mia's message requests your urgent help")
        T_mia_key_found = Trigger("key found", "Found the key to Helen's locked room")
        T_mia_rescue = Trigger("rescue", "Rescue Mia from being tied up")
        T_mia_concerned = Trigger("concerned", "You are concerned about Mia not contacting you")
        T_mias_request = Trigger("request", "Mia asks that you try talk to Helen")
        T_mia_helen_deny = Trigger("helen deny", "Helen refuses to talk to you")
        T_mia_church_mention = Trigger("church mention", "Mia mentions Helen only listens to God or the Church")
        T_mia_priest_outfit = Trigger("priest outfit", "Borrow the priest outfit to disguise yourself")
        T_mia_thanks = Trigger("thanks", "Mia gives you thanks for your help")
        T_mia_clues_summary = Trigger("clues summary", "You've summarised the clues you've gathered so far")
        T_mia_give_news = Trigger("give news", "Give Mia the news you learnt")
        T_mia_gives_glasses = Trigger("gives glasses", "Mia gives you the pair of glasses for her dad")
        T_mia_dinner_plan = Trigger("dinner plan", "Mia has a plan to get Harold and Helen to have dinner")
        T_mia_route = Trigger("route", "This sets you permanently onto Mia's route")
        T_mia_family_reunion = Trigger("family reunion", "Mia has a reunion with Harold and Helen for getting back together")
        T_mia_sex = Trigger("sex", "Mia has sex with you")
        T_mia_stay_alone = Trigger("stay alone", "Mia wishes to be alone after her parents leaft for good")


        T_roz_favour = Trigger("favour", "Roz needs a favour in return for the obituary records")
        T_roz_fuckery = Trigger("fuckery", "Quite literally some fuckery with Roz")


        T_sis_hallway = Trigger("hallway", "Meet sister in hallway")
        T_sis_panty_raid = Trigger("panty raid", "Steal sis's panties")


        T_perv_visit = Trigger("Visit", "Visit Somrak at gym")
        T_perv_pay = Trigger("Pay", "Pay Somrak a pair of panties")
        T_perv_train = Trigger("Train", "Somrak teaches a leason")
        T_perv_finish = Trigger("Finish", "Somrak has finished a set of leasons")


        T_terry_intro = Trigger("intro", "Meet Terry the fisher")
        T_terry_secret_lure = Trigger("secret lure", "Terry shows you his secret lure")
        T_terry_tigger = Trigger("tigger", "The one that got away with the little piggy")
        T_terry_lure_trade = Trigger("tigger", "The one that got away with the little piggy")
        T_terry_retire = Trigger("tigger", "The one that got away with the little piggy")
        T_terry_overjoyed_swim = Trigger("tigger", "The one that got away with the little piggy")
        T_terry_hang_tigger = Trigger("tigger", "The one that got away with the little piggy")


        T_yumi_backup_request = Trigger("backup request", "Yumi requests urgent backup")



        S_aqua_start = State("start")
        S_aqua_boatsmith_search = State("boatsmith search", "Search for the holder of the golden compass")
        S_aqua_graveyard_search = State("graveyard search", "Search the graveyard for clues")
        S_aqua_bell_search = State("bell search", "Search the church bell for clues")
        S_aqua_altar_search = State("altar search", "Search the forest altar for clues")
        S_aqua_treasure_search = State("treasure search", "Search the beach for the treasure")
        S_aqua_treasure_unlock = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_trade = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_fishing = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_chase = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_squid_gaurd = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_maze = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_lair = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_found = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_mating_proposal = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_valor_test = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_mate = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_end = State("treasure unlock", "Now you need to unlock the treasure chest")


        S_aqua_start.add(T_aqua_special_lure, S_aqua_boatsmith_search)
        S_aqua_boatsmith_search.add(T_aqua_obituary_records, S_aqua_graveyard_search,
                                    actions = ['set', 'tomb search']
                                    )
        S_aqua_graveyard_search.add(T_aqua_tomb_engraving, S_aqua_bell_search,
                                    actions = ['set', 'bell search']
                                    )
        S_aqua_bell_search.add(T_aqua_bell_engraving, S_aqua_altar_search,
                               actions = ['set', 'altar search']
                               )
        S_aqua_altar_search.add(T_aqua_altar_puzzle_solve, S_aqua_treasure_search,
                                actions = ['set', 'treasure search',
                                           'set', 'altar pass']
                                )
        S_aqua_treasure_search.add(T_aqua_treasure_found, S_aqua_treasure_unlock)
        S_aqua_treasure_unlock.add(T_aqua_treasure_unlocked, S_aqua_trade, 
                                   actions = ['set', 'treasure pass']
                                   )
        S_aqua_trade.add(T_terry_lure_trade, S_aqua_fishing)
        S_aqua_fishing.add(T_aqua_lure_steal, S_aqua_chase)
        S_aqua_chase.add(T_aqua_dive, S_aqua_squid_gaurd)
        S_aqua_squid_gaurd.add(T_aqua_squid_defeated, S_aqua_maze, 
                               actions = ['set', 'squid pass']
                               )
        S_aqua_squid_gaurd.add(T_aqua_chase_fail, S_aqua_chase)
        S_aqua_maze.add(T_aqua_maze_conquered, S_aqua_lair, 
                        actions = ['set', 'maze pass']
                        )
        S_aqua_maze.add(T_aqua_chase_fail, S_aqua_chase)
        S_aqua_lair.add(T_aqua_lair_found, S_aqua_found)
        S_aqua_found.add(T_aqua_friended, S_aqua_mating_proposal)
        S_aqua_mating_proposal.add(T_aqua_mating_offer, S_aqua_valor_test)
        S_aqua_valor_test.add(T_aqua_test_pass, S_aqua_mate)
        S_aqua_mate.add(T_aqua_mated, S_aqua_end)

        M_aqua = Machine("aqua", location = "Lair", force_location = False,
                vars = {'sex speed': .175, 'tomb search': False, 'bell search': False, 'altar search': False, 'altar pass': False, 'treasure search': False, 'treasure pass': False,
                        'squid pass': False, 'maze pass': False},
                )
        M_aqua.add(S_aqua_start, S_aqua_boatsmith_search, S_aqua_graveyard_search,
                   S_aqua_bell_search, S_aqua_altar_search, S_aqua_treasure_search,
                   S_aqua_treasure_unlock, S_aqua_trade, S_aqua_fishing, S_aqua_chase,
                   S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
                   S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate, S_aqua_end)


        M_perv = Machine("Somrak",location='Gym',force_location=True)


        S_helen_start = State("start", "The default state for Helen to start in")
        S_helen_route_split = State("route split", "The split to dtermine if you go with Mia or Helen")
        S_helen_harold_moved_on = State("route split", "Harold has moved on from Helen and found a new woman")
        S_helen_mia_breakdown = State("route split", "Mia is devistated that her parents have split for good")
        S_helen_master_servant_fun = State("master servant fun", "Helen has some fun with you as her master")
        S_helen_aftersex_mia_suspicious = State("aftersex mia suspicious", "Mia is suspicious about you visiting her mom's room during the day")
        S_helen_end = State("end", "The end of Helen's route")


        S_helen_start.add(T_helen_route, S_helen_route_split)
        S_helen_route_split.add(T_harold_new_girl, S_helen_harold_moved_on)
        S_helen_route_split.add(T_helen_master_servant, S_helen_mia_breakdown)
        S_helen_harold_moved_on.add(T_helen_master_servant, S_helen_master_servant_fun)
        S_helen_mia_breakdown.add(T_harold_new_girl, S_helen_master_servant_fun)
        S_helen_master_servant_fun.add(T_helen_master_servant_sex, S_helen_aftersex_mia_suspicious)
        S_helen_aftersex_mia_suspicious.add(T_mia_stay_alone, S_helen_end)

        M_helen = Machine("helen",location="Helen's Bedroom",
                          vars = {'helen route': False,
                                  'sex speed': .175,
                                  'corset lingerie': False},
        )
        M_helen.add(S_helen_start, S_helen_route_split, S_helen_mia_breakdown, S_helen_harold_moved_on, S_helen_master_servant_fun, S_helen_aftersex_mia_suspicious, S_helen_end)


        S_mia_start = State("start", "Welcoming MC back from his")
        S_mia_do_homework = State("homework", "Waiting for MC to catch up on homework")
        S_mia_wait_homework = State("show hw", "Waiting for MC to bring the finished homework")
        S_mia_parent_blocking = State("blocked", "Helen prevents you from visiting mia")
        S_mia_consult = State("consult", "Consult with mia to be able to do night study sessions again")
        S_mia_impress_harold = State("impress", "Impress Harold by finding his favourite donut")
        S_mia_parent_unblock = State("unbanned", "Find out if from Mia if you were unbanned")
        S_mia_tattoo_help = State("tattoo", "Help Mia get a tattoo")
        S_mia_find_easel = State("easel", "Find an easel to draw a tattoo for Mia")
        S_mia_draw_tattoo = State("draw tattoo", "Draw a tattoo for Mia")
        S_mia_show_tattoo = State("show tattoo", "Show Mia the tattoo you drew")
        S_mia_get_tattoo = State("get tattoo", "Go with Mia to get a tattoo")
        S_mia_buy_tattoo = State("buy tattoo", "Watch Mia get her tattoo")
        S_mia_return_favor = State("return favor", "Mia wants to return the favor for helping her get her tattoo")
        S_mia_night_visit = State("night visit", "Mia has invited you for a secret night visit")
        S_mia_strip_aftermath = State("strip aftermath", "Talk to Mia to find out what happend after she was caught")
        S_mia_midnight_call = State("midnight call", "Mia sent you a message")
        S_mia_midnight_help = State("rescue", "Go to Mia and see why she needs help")
        S_mia_locked_room = State("locked room", "Enter the secret locked room")
        S_mia_need_space = State("need space", "Best to leave Mia nad her parent's alone for now")
        S_mia_concerning_visit = State("concerning visit", "You've decided to visit Mia since you haven't heard from her")
        S_mia_helen_fight = State("helen fight", "Mia has a fight with Helen")
        S_mia_helen_talk = State("helen talk", "Mia asked you to try talk to Helen")
        S_mia_helen_refusal = State("helen refusal", "Helen refused to talk to you")
        S_mia_church_plan = State("church plan", "Go to church to see if there's a way to convince Helen")
        S_mia_convince_helen = State("convince helen", "Go to the confessional to talk to Helen")
        S_mia_priest_act = State("priest act", "Act as a priest to try convince Helen")
        S_mia_return_priest_outfit = State("return priest outfit", "Return the priest outfit to the nun's chambers")
        S_mia_nun_thoughts = State("nun thoughts", "You go over the predicament the nun has put you in")
        S_mia_helen_change_news = State("helen change news", "You tell Mia the good news that Helen is willing to change")
        S_mia_waiting_for_harold = State("waiting for harold", "Mia and Helen are waiting for Harold to return")
        S_mia_urgent_message = State("urgent message", "You wake up to an urgent message from Mia")
        S_mia_urgent_help = State("urgent help", "Mia urgently needs help finding Harold")
        S_mia_clues = State("clues", "Look for clues as to where Harold dissapeared to")
        S_mia_search_desk = State("search desk", "Search Harold's desk for clues")
        S_mia_find_harold = State("find harold", "Look for Harold at Ravens Hill")
        S_mia_harold_found_news = State("harold found news", "Return and give the news that Harold is okay")
        S_mia_angelicas_patience = State("angelicas patience", "Angelica is awaiting your end of the deal")
        S_mia_angelicas_impatience = State("angelicas impatience", "Angelica decided to pay you a visit to remind you of your deal")
        S_mia_church_night_visit = State("church night visit", "You visit the church at night like Angelica told you to")
        S_mia_find_sinners = State("find sinners", "Angelica wants you to find sinners for her sacrement")
        S_mia_church_sacrement = State("church sacrement", "Go with Helen to the church to do the first sacrement")
        S_mia_glasses_favor = State("glasses favor", "Mia wants to ask you a favor to return her dads glasses")
        S_mia_harold_gift = State("glasses gift", "Go to Harold to give him his pair of glasses")
        S_mia_inmate_status = State("inmate status", "Harold needs a status update on the inmate transfer")
        S_mia_harold_backup = State("harold backup", "Go tell Harold that his back is needed")
        S_mia_harold_to_the_rescue = State("harold to the rescue", "Harold comes to rescue Yumi")
        S_mia_harold_yumi_out = State("harold yumi out", "Harold and Yumi take the rest of the day off")
        S_mia_unexpected_visit = State("unexpected visit", "You pay Mia an unexpected visit")
        S_mia_helen_outfit_request = State("helen outfit request", "Helen has asked you to buy her a sexy lingerie outfit")
        S_mia_angelicas_delay = State("angelicas delay", "Angelica will contact you in the morning")
        S_mia_angelicas_home_visit = State("angelicas home visit", "Angelica visits your home to tell you part 2 of her sacrement")
        S_mia_angelicas_order = State("angelicas order", "Angelica has ordered you to acquire a whip for her")
        S_mia_angelicas_whip = State("angelicas whip", "Angelica requires a whip")
        S_mia_helen_condition = State("helen condition", "You are worried about Helen's condition after her whipping")
        S_mia_favor = State("favor", "Mia has a favor to ask of you")
        S_mia_convince_harold = State("convince harold", "You need to try convince Harold to go to dinner with Mia and Helen")
        S_mia_stolen_goods = State("stolen goods", "Harold needs to find the stolen goods of a thief for a promotion")
        S_mia_return_goods = State("return goods", "You should return the stolen goods to Harold")
        S_mia_angelicas_final_delay = State("angelicas final delay", "Angelica will contact you in the morning")
        S_mia_angelicas_final_home_visit = State("angelicas final home visit", "Angelica visits your home to tell you the final part of her sacrement")
        S_mia_harolds_thoughts = State("harolds thoughts", "You want to ask Harold about hsi replationship with Helen before you do the final sacrament")
        S_mia_angelicas_final_request = State("angelicas final request", "You've decided to listen to Angelica's final request")
        S_mia_helens_final_sacrament = State("helens final sacrament", "You are now attending the final sacrament for Helen")
        S_mia_route_split = State("route split", "The split to dtermine if you go with Mia or Helen")
        S_mia_study_sex = State("study sex", "Mia has suggested to try studying while having sex")
        S_mia_end = State("end", "The end of Mia's route")























        S_mia_start.add(T_all_school_entrance, S_mia_do_homework,
                        actions = ["assign", ['homework', 1]],
                        location = "Mia's House Entrance",
                        force_location=False
                        )
        S_mia_do_homework.add(T_mc_homework, S_mia_do_homework,
                              actions = ["triggerOnZero", ['homework', T_mia_on_zero]]
                              )
        S_mia_do_homework.add(T_mia_on_zero, S_mia_wait_homework,
                              actions = ["clear", 'front door locked',
                                         "inc", 'progress count']
                              )
        S_mia_wait_homework.add(T_mia_kiss, S_mia_parent_blocking,
                                actions = ["set", 'study'
                                           "inc", 'progress count']
                                )
        S_mia_parent_blocking.add(T_mia_kicked_out, S_mia_consult)
        S_mia_consult.add(T_mia_plan, S_mia_impress_harold,
                          actions = ["set", 'buy donuts']
                          )
        S_mia_impress_harold.add(T_harold_donuts, S_mia_parent_unblock)
        S_mia_parent_unblock.add(T_mia_results, S_mia_tattoo_help,
                                 actions = ["inc", 'progress count']
                                 )
        S_mia_tattoo_help.add(T_mia_delay, S_mia_tattoo_help,
                                 actions = ["set", 'story delay']
                                 )
        S_mia_tattoo_help.add(T_mia_tattoo_start, S_mia_find_easel,
                              actions = ["clear", 'story delay']
                              )
        S_mia_find_easel.add(T_mia_easel_found, S_mia_draw_tattoo)
        S_mia_draw_tattoo.add(T_mia_visit, S_mia_show_tattoo)
        S_mia_show_tattoo.add(T_mia_wrong_tattoo, S_mia_draw_tattoo)
        S_mia_show_tattoo.add(T_mia_right_tattoo, S_mia_get_tattoo,
                              actions = ["inc", 'progress count']
                              )
        S_mia_get_tattoo.add(T_mia_visit_tattoo_parlor, S_mia_buy_tattoo)
        S_mia_buy_tattoo.add(T_mia_tattoo_done, S_mia_return_favor)
        S_mia_return_favor.add(T_mia_night_invite, S_mia_night_visit)
        S_mia_night_visit.add(T_mia_strip_tease, S_mia_strip_aftermath,
                              actions = ["set", 'story delay',
                                         "inc", 'progress count']
                              )
        S_mia_strip_aftermath.add(T_mia_delay, S_mia_strip_aftermath,
                                  actions = ["clear", 'story delay']
                                  )
        S_mia_strip_aftermath.add(T_mia_grounded, S_mia_midnight_call)
        S_mia_midnight_call.add(T_mia_message, S_mia_midnight_help)
        S_mia_midnight_help.add(T_mia_key_found, S_mia_locked_room,
                                actions = ["clear", 'helens locked room locked']
                                )
        S_mia_locked_room.add(T_mia_rescue, S_mia_need_space,
                              actions = ["assign", ['event delay', 4],
                                         "inc", 'progress count']
                              )
        S_mia_need_space.add(T_all_sleep, S_mia_need_space,
                             actions = ["triggerOnZero", ['event delay', T_mia_concerned]]
                             )
        S_mia_need_space.add(T_mia_concerned, S_mia_concerning_visit)
        S_mia_concerning_visit.add(T_harold_leaves, S_mia_helen_fight,
                                   actions = ["set", 'harold left']
                                   )
        S_mia_helen_fight.add(T_mias_request, S_mia_helen_talk)
        S_mia_helen_talk.add(T_mia_helen_deny, S_mia_helen_refusal,
                             actions = ["set", 'helen button',
                                        "set", 'helen button change']
                             )
        S_mia_helen_refusal.add(T_mia_church_mention, S_mia_church_plan,
                                actions = ["inc", 'progress count']
                                )
        S_mia_church_plan.add(T_mia_priest_outfit, S_mia_convince_helen)
        S_mia_convince_helen.add(T_helen_confessional, S_mia_priest_act)
        S_mia_priest_act.add(T_helen_convince_fail, S_mia_church_plan)
        S_mia_priest_act.add(T_helen_convince_change, S_mia_return_priest_outfit,
                             actions = ["set", 'helen dialogue change']
                             )
        S_mia_return_priest_outfit.add(T_mia_priest_outfit, S_mia_nun_thoughts,
                             actions = ["clear", 'helen button change']
                             )
        S_mia_nun_thoughts.add(T_mc_nun_thoughts, S_mia_helen_change_news,
                               actions = ["inc", 'progress count']
                               )
        S_mia_helen_change_news.add(T_mia_thanks, S_mia_waiting_for_harold,
                                    actions = ["assign", ['event delay', 3]]
                                    )
        S_mia_waiting_for_harold.add(T_all_sleep, S_mia_waiting_for_harold,
                                     actions = ["triggerOnZero", ['event delay', T_mia_on_zero]]
                                     )
        S_mia_waiting_for_harold.add(T_mia_on_zero, S_mia_urgent_message,
                                     actions = ["inc", 'progress count']
                                     )
        S_mia_urgent_message.add(T_mia_message, S_mia_urgent_help)
        S_mia_urgent_help.add(T_harold_missing, S_mia_clues)
        S_mia_clues.add(T_mia_clues_summary, S_mia_search_desk,
                        actions = ["clear", 'questioned yumi',
                                   "clear", 'questioned earl']
                        )
        S_mia_search_desk.add(T_harold_photo_clue, S_mia_find_harold)
        S_mia_find_harold.add(T_harold_found, S_mia_harold_found_news)
        S_mia_harold_found_news.add(T_mia_give_news, S_mia_angelicas_patience,
                                    actions = ["assign", ['event delay', 3],
                                               "inc", 'progress count']
                                    )
        S_mia_angelicas_patience.add(T_all_sleep, S_mia_angelicas_patience,
                                     actions = ["triggerOnZero", ['event delay', T_mia_on_zero]]
                                     )
        S_mia_angelicas_patience.add(T_mia_on_zero, S_mia_angelicas_impatience)
        S_mia_angelicas_impatience.add(T_angelica_house_visit, S_mia_church_night_visit,
                                       actions = ["clear", 'church night locked']
                                       )
        S_mia_church_night_visit.add(T_angelica_ritual_deal, S_mia_find_sinners)
        S_mia_find_sinners.add(T_helen_secret_sacrement, S_mia_church_sacrement,
                               actions = ["inc", 'progress count']
                               )
        S_mia_church_sacrement.add(T_helen_angelica_ritual, S_mia_glasses_favor,
                                   actions = ["set", 'helen angelica training',
                                              "set", 'church night locked']
                                   )
        S_mia_glasses_favor.add(T_mia_gives_glasses, S_mia_harold_gift)
        S_mia_harold_gift.add(T_harold_glasses, S_mia_inmate_status)
        S_mia_inmate_status.add(T_yumi_backup_request, S_mia_harold_backup)
        S_mia_harold_backup.add(T_harold_grows_a_pair, S_mia_harold_to_the_rescue)
        S_mia_harold_to_the_rescue.add(T_harold_backup, S_mia_harold_yumi_out)
        S_mia_harold_yumi_out.add(T_all_sleep, S_mia_unexpected_visit,
                                  actions = ["inc", 'progress count']
                                  )
        S_mia_unexpected_visit.add(T_helen_caught_masturbating, S_mia_helen_outfit_request)
        S_mia_helen_outfit_request.add(T_helen_sexy_lingerie, S_mia_angelicas_delay)
        S_mia_angelicas_delay.add(T_all_sleep, S_mia_angelicas_home_visit)
        S_mia_angelicas_home_visit.add(T_angelica_requires_whip, S_mia_angelicas_order,
                                       actions = ["clear", 'church night locked']
                                       )
        S_mia_angelicas_order.add(T_angelica_sinful_thoughts, S_mia_angelicas_whip,
                                  actions = ["set", 'helen angelica training 2']
                                  )
        S_mia_angelicas_whip.add(T_helen_torture, S_mia_helen_condition,
                                 actions = ["inc", 'progress count']
                                 )
        S_mia_helen_condition.add(T_helen_thanks, S_mia_favor)
        S_mia_favor.add(T_mia_dinner_plan, S_mia_convince_harold)
        S_mia_convince_harold.add(T_harold_find_goods, S_mia_stolen_goods)
        S_mia_stolen_goods.add(T_harold_found_goods, S_mia_return_goods,
                               actions = ["set", 'stolen goods recovered']
                               )
        S_mia_return_goods.add(T_harold_promotion, S_mia_angelicas_final_delay,
                               actions = ["inc", 'progress count']
                               )
        S_mia_angelicas_final_delay.add(T_all_sleep, S_mia_angelicas_final_home_visit)
        S_mia_angelicas_final_home_visit.add(T_angelica_strapon_request, S_mia_harolds_thoughts)
        S_mia_harolds_thoughts.add(T_harold_indecisiveness, S_mia_angelicas_final_request)
        S_mia_angelicas_final_request.add(T_angelicas_final_ritual, S_mia_helens_final_sacrament,
                                          actions = ["inc", 'progress count']
                                          )
        S_mia_helens_final_sacrament.add(T_mia_route, S_mia_route_split,
                                         actions = ["set", 'mia route',
                                                    "clear", 'harold left',
                                                    "clear", 'helen angelica training',
                                                    "clear", 'helen angelica training 2']
                                         )


        S_mia_route_split.add(T_mia_family_reunion, S_mia_study_sex)
        S_mia_study_sex.add(T_mia_sex, S_mia_end,
                            actions = ["inc", 'progress count']
                            )

        M_mia = Machine("mia",
                        vars = {
                            'progress count': 0,
                            'progress mark': 2, 
                            'front door locked': True,
                            'study': False,
                            'buy donuts': False,
                            'story delay': False,
                            'helens locked room locked': True,
                            'harold left': False,
                            'helen button': False,
                            'helen button change': False,
                            'helen dialogue change': False,
                            'questioned yumi': False,
                            'questioned earl': False,
                            'church night locked': True,
                            'helen angelica training': False,
                            'helen angelica training 2': False,
                            'stolen goods recovered': False,
                            'mia route': False,
                            'sex speed': .175,
                            'sex 1st choice': "",
                            'cum 1st choice': "",
                            'anal sex': False,
                            'vaginal sex': False,
                            'butt speed': 0},
                        location = "School Hall", force_location = True,
        )
        M_mia.add(S_mia_start, S_mia_do_homework, S_mia_wait_homework,
                  S_mia_parent_blocking, S_mia_impress_harold,
                  S_mia_parent_unblock, S_mia_tattoo_help,
                  S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo,
                  S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor,
                  S_mia_night_visit, S_mia_strip_aftermath,
                  S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room,
                  S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight,
                  S_mia_helen_talk, S_mia_helen_refusal, S_mia_church_plan,
                  S_mia_convince_helen, S_mia_priest_act,
                  S_mia_return_priest_outfit, S_mia_nun_thoughts,
                  S_mia_helen_change_news, S_mia_waiting_for_harold,
                  S_mia_urgent_message, S_mia_urgent_help, S_mia_clues,
                  S_mia_search_desk, S_mia_find_harold,
                  S_mia_harold_found_news, S_mia_angelicas_patience,
                  S_mia_angelicas_impatience, S_mia_church_night_visit,
                  S_mia_find_sinners, S_mia_church_sacrement,
                  S_mia_glasses_favor, S_mia_harold_gift, S_mia_inmate_status,
                  S_mia_harold_backup, S_mia_harold_to_the_rescue,
                  S_mia_harold_yumi_out, S_mia_unexpected_visit,
                  S_mia_helen_outfit_request, S_mia_angelicas_delay,
                  S_mia_angelicas_home_visit, S_mia_angelicas_order,
                  S_mia_angelicas_whip, S_mia_helen_condition, S_mia_favor,
                  S_mia_convince_harold, S_mia_stolen_goods,
                  S_mia_return_goods, S_mia_angelicas_final_delay,
                  S_mia_angelicas_final_home_visit, S_mia_harolds_thoughts,
                  S_mia_angelicas_final_request, S_mia_helens_final_sacrament,
                  S_mia_route_split, S_mia_study_sex, S_mia_end
        )



        S_roz_start = State("start")
        S_roz_sexy_time = State("sexy time", "Lets get funky with ol' Rozzy")
        S_roz_end = State("end", "The end of the end but not for Roz")


        S_roz_start.add(T_roz_favour, S_roz_sexy_time)
        S_roz_sexy_time.add(T_roz_fuckery, S_roz_end)

        M_roz = Machine("roz", location = "Hospital", force_location = False,
                        vars = {'fun time': False, 'sex speed': .4},
                        )
        M_roz.add(S_roz_start, S_roz_sexy_time, S_roz_end)



        S_sis_start = State("start")
        S_sis_bored = State("bored", "Waiting for something to happen")
        S_sis_bedroom1 = State("Bedroom1", "Waiting for panty raid")


        S_sis_start.add(T_sis_hallway, S_sis_bored)
        S_sis_bored.add(T_sis_panty_raid, S_sis_bedroom1,
                        actions=['clear','door locked',
                                 'assign',['default location','bedroom'],
                        ])

        M_sis = Machine("sister",location="Sis' Bedroom", force_location=False,
                        vars={'door locked':True, 'default location':'bedroom', 'sex speed': .175},
                        )
        M_sis.add(S_sis_start, S_sis_bored, S_sis_bedroom1)



        S_perv_start = State("start")
        S_perv_wait_clean = State("waiting","Waiting for clean panties")
        S_perv_teach_1 = State("teaching","Level one")
        S_perv_wait_used = State("waiting","Waiting for used panties")


        S_perv_start.add(T_perv_visit, S_perv_wait_clean,
                         actions=['clear','need_rest',
                                  'trigger',T_sis_panty_raid,
                         ])
        S_perv_wait_clean.add(T_perv_pay, S_perv_teach_1,
                              actions=['assign',('session',2)])
        S_perv_teach_1.add(T_perv_train,S_perv_teach_1,
                           actions=['set','need_rest',
                                    'triggerOnZero',('session',T_perv_finish)])
        S_perv_teach_1.add(T_perv_finish,S_perv_wait_used)
        S_perv_teach_1.add(T_all_sleep,S_perv_teach_1,
                           actions=['clear','need_rest',])

        M_perv = Machine("Somrak",location="Gym",force_location=True)
        M_perv.add(S_perv_start, S_perv_wait_clean, S_perv_teach_1)



        S_terry_start = State("start")
        S_terry_secret = State("secret", "The secret behind his fishing")
        S_terry_lure = State("lure", "The lure that made terry famous for his fishing")
        S_terry_nemesis = State("nemesis", "Sara tells you the cause of Terry's drunken state")
        S_terry_drunk = State("drunk", "Terry is out drunk for the day")
        S_terry_trade = State("drunk", "Terry is out drunk for the day")
        S_terry_bored = State("drunk", "Terry is out drunk for the day")
        S_terry_retire = State("drunk", "Terry is out drunk for the day")
        S_terry_tigger_sign = State("drunk", "Terry is out drunk for the day")
        S_terry_end = State("drunk", "Terry is out drunk for the day")


        S_terry_start.add(T_terry_intro, S_terry_secret)
        S_terry_secret.add(T_terry_secret_lure, S_terry_lure)
        S_terry_lure.add(T_all_sleep, S_terry_nemesis)
        S_terry_nemesis.add(T_terry_tigger, S_terry_drunk)
        S_terry_drunk.add(T_all_sleep, S_terry_trade)
        S_terry_trade.add(T_terry_lure_trade, S_terry_bored)
        S_terry_bored.add(T_terry_retire, S_terry_retire)
        S_terry_retire.add(T_terry_overjoyed_swim, S_terry_tigger_sign)
        S_terry_tigger_sign.add(T_terry_hang_tigger, S_terry_end)

        M_terry = Machine("terry", location = "Pier", force_location = False,
                          vars = {'default location': 'Pier'},
                          )
        M_terry.add(S_terry_start, S_terry_secret, S_terry_lure, S_terry_nemesis, S_terry_drunk, S_terry_trade, S_terry_bored, S_terry_retire, S_terry_tigger_sign, S_terry_end)



        T_mom_kitchen = Trigger("kitchen visit", "Visit mom in the kitchen")


        S_mom_start = State("start")


        S_mom_start.add(T_mom_kitchen, S_mom_start) 

        M_mom = Machine("mom", location = "Mom's Bedroom", force_location = False,
                vars = {'sex speed': .4},
                )
        M_mom.add(S_mom_start)


        S_june_start = State("start")


        M_june = Machine("june",location="Computer Lab", force_location=False,
                vars={'sex speed': .3},
                )
        M_june.add(S_june_start)


        S_erimom_start = State("start")


        M_erimom = Machine("erimom",location="Yoga", force_location=False,
                vars={'sex speed': .3},
                )
        M_erimom.add(S_erimom_start)


        S_aunt_start = State("start")


        M_aunt = Machine("aunt",location="Garden", force_location=False,
                vars={'sex speed': .4},
                )
        M_aunt.add(S_aunt_start)
    return