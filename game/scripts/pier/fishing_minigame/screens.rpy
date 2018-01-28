init python:
    class Fish:
        def __init__(self, image = "", name = "", ypos = 0, bait = "", swim_time = 0, flip = 1.0, variation = 1):
            self.image = image
            self.name = name
            self.xpos = 0
            self.ypos = ypos
            self.width = 0
            self.height = 0
            self._bait = bait
            self.swim_time = swim_time
            self._flip = flip
            self._variation = variation
            
            self._reset = [self.xpos, self.ypos, self._flip]
        
        def flip(self, invert = False):
            if invert:
                self._flip = -self._flip
            return self._flip < 0
        
        def displayable(self):
            return renpy.displayable(self.image)
        
        def animation(self):
            return Transform(child = self.displayable(), xpos = self.xpos, ypos = self.ypos, xzoom = self._flip)
        
        def xpos_calc(self, screen_width, offscreen_offset):
            if not self.flip():
                return (-offscreen_offset - self.width)
            else:
                return (screen_width + offscreen_offset)
        
        def bait_check(self, bait):
            return bait in [self._bait, "golden lure"]
        
        def movement(self, frame_pixel_width, frames_per_second):
            return (frame_pixel_width + self.width) / (self.swim_time * frames_per_second)
        
        def hitbox(self, hookXpos, hookYpos):
            return bool(all(self.hitbox_check(hookXpos, hookYpos)))
        
        def hitbox_check(self, hookXpos, hookYpos):
            Lxpos, Rxpos, Uypos, Lypos = self.hitbox_calc()
            
            yield Lxpos < hookXpos < Rxpos
            yield Uypos < hookYpos < Lypos
            
            return
        
        def hitbox_calc(self):
            if self._flip == 1.0:
                Lxpos = self.xpos - (((self.width / 4) / 2.5) * 1.5)
            else:
                Lxpos = self.xpos + (self.width - (((self.width / 4) / 2.5) * 2))
            Rxpos = Lxpos + (self.width / 3)
            if self._variation == 1:
                Uypos = self.ypos + (self.height / 4)
                Lypos = self.ypos + (self.height - (self.height / 4))
            elif self._variation == 2:
                Uypos = self.ypos + (self.height / 2.5)
                Lypos = self.ypos + (self.height - (self.height / 6))
            
            return [Lxpos, Rxpos, Uypos, Lypos]
        
        def hitbox_draw(self):
            Lxpos, Rxpos, Uypos, Lypos = self.hitbox_calc()
            
            return (Lxpos, Uypos, (Rxpos - Lxpos), (Lypos - Uypos))
        
        def reset(self):
            self.xpos, self.ypos, self._flip = self._reset
            return

    fishes = {}
    fishes["Seatrout"] = Fish("buttons/fishing_fish01a.png", "Seatrout", 550, "worms", 11, -1.0)
    fishes["Snapper"] = Fish("buttons/fishing_fish02a.png", "Snapper", 350, "standard lure", 16, -1.0)
    fishes["Mackerel"] = Fish("buttons/fishing_fish03a.png", "Mackerel", 450, "fancy lure", 14)
    fishes["Tiger Fish"] = Fish("buttons/fishing_fish04a.png", "Tiger Fish", 625, "golden lure", 10, variation = 2)

    class Fishing(renpy.Displayable):
        def __init__(self, bait, **kwargs):
            super(Fishing, self).__init__(**kwargs)
            self._bg = renpy.displayable("backgrounds/minigame06a.jpg")
            
            import os
            os.environ["SDL_VIDEODRIVER"] = "fbcon"
            os.environ["SDL_FBDEV"] = "/dev/fb1"
            os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
            os.environ["SDL_MOUSEDRV"] = "TSLIB"
            
            if renpy.variant("pc"):
                self._instructions = renpy.displayable("buttons/fishing_instructions01.png")
            elif renpy.variant("mobile"):
                self._instructions = renpy.displayable("buttons/fishing_instructions01b.png")
                self._left_arrow = renpy.displayable("buttons/attack_01.png")
                self._right_arrow = renpy.displayable("buttons/attack_03.png")
            
            self._fish_exclamation = renpy.displayable("buttons/fishing_exclamation.png")
            self._fish_done = renpy.displayable("buttons/fishing_done.png")
            self._fish_catch = renpy.displayable("buttons/fishing_catch.png")
            self._fish_catch_hover = renpy.displayable("buttons/fishing_catchb.png")
            
            self._hitbox_test = False
            self._offscreen_offset = 50
            self._fish_frame_pixel_width = 0
            self._frames_per_second = 30
            
            self._bait = bait
            self._bait_dropped = False
            self._hook_xpos = 0
            
            self._bait_presets = {"worms": {
                                            "ypos": 4,
                                            "name": "bait01"
                                            },
                                  "standard lure": {
                                                    "ypos": 3,
                                                    "name": "bait02"
                                                    },
                                  "fancy lure": {
                                                 "ypos": 2,
                                                 "name": "bait03"
                                                 },
                                  "golden lure": {
                                                  "ypos": 5,
                                                  "name": "bait04"
                                                  },
                                  }
            
            self._hook_ypos = self._bait_presets[self._bait]["ypos"]
            self._selected_bait = renpy.displayable("buttons/fishing_" + self._bait_presets[self._bait]["name"] + ".png")
            
            for name in fishes:
                fishes[name].reset()
            
            self._aqua = renpy.displayable("private/buttons/fishing_fish05.png")
            self._aqua_appeared = False
            self._aqua_timer = 0
            
            self._render_fish = False
            self._fish_caught = False
            self._caught_fish = None
            self._fish_caught_hover = False
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            self._width, self._height = render.get_size()
            
            self._fish_frame_pixel_width = self._width + 100
            
            fishing_exclamation_render = renpy.render(self._fish_exclamation, width, height, st, at)
            fishing_done_render = renpy.render(self._fish_done, width, height, st, at)
            fishing_catch_render = renpy.render(self._fish_catch, width, height, st, at)
            fishing_catch_hover_render = renpy.render(self._fish_catch_hover, width, height, st, at)
            
            if not self._bait_dropped:
                if renpy.variant("mobile"):
                    left_arrow_render = renpy.render(self._left_arrow, width, height, st, at)
                    right_arrow_render = renpy.render(self._right_arrow, width, height, st, at)
                    self._left_arrow_width, self._left_arrow_height = left_arrow_render.get_size()
                    self._right_arrow_width, self._right_arrow_height = right_arrow_render.get_size()
                    render.blit(left_arrow_render, (0, self._left_arrow_height))
                    render.blit(right_arrow_render, ((self._width - self._right_arrow_width), self._right_arrow_height))
            
            if not self._fish_caught:
                instructions_render = renpy.render(self._instructions, width, height, st, at)
                render.blit(instructions_render, (70, 100))
                
                if not self._aqua_appeared:
                    if self._hook_xpos == 0:
                        bait_render = renpy.render(self._selected_bait, width, height, st, at)
                        self._bait_width, self._bait_height = bait_render.get_size()
                        self._hook_xpos = (self._width / 2) - (self._bait_width / 2)
                    
                    if not self._bait_dropped:
                        bait_transform = Transform(self._selected_bait, xpos = self._hook_xpos, ypos = self._hook_ypos)
                        bait_render = renpy.render(bait_transform, width, height, st, at)
                    else:
                        if self._hook_ypos <= 5:
                            self._selected_bait = renpy.displayable("buttons/fishing_" + self._bait_presets[self._bait]["name"] + "b.png")
                            
                            self._hook_xpos = self._hook_xpos + (self._bait_width / 3.9)
                            self._hook_ypos = 5
                            bait_render = renpy.render(self._selected_bait, width, height, st, at)
                            self._bait_width, self._bait_height = bait_render.get_size()
                        
                        if self._hook_ypos < self._height:
                            self._hook_ypos += (self._height - 5) / (10 * self._frames_per_second)
                        else:
                            renpy.hide_screen("fishing_test")
                            renpy.call("after_fishing", None, self._bait)
                        
                        
                        
                        
                        
                        
                        bait_transform = Transform(self._selected_bait, xpos = self._hook_xpos, ypos = self._hook_ypos)
                        bait_render = renpy.render(bait_transform, width, height, st, at)
                    self._hook_xpos_center = self._hook_xpos + (self._bait_width / 2)
                    self._hook_ypos_center = self._hook_ypos + (self._bait_height / 2)
                
                for name in fishes:
                    if name == "Tiger Fish":
                        if M_terry.get_state() == S_terry_retire and tigger not in inventory.items:
                            self._render_fish = True
                        else:
                            self._render_fish = False
                    else:
                        self._render_fish = True
                    
                    if self._render_fish:
                        if fishes[name].xpos == 0:
                            fish_render = renpy.render(fishes[name].displayable(), width, height, st, at)
                            fishes[name].width, fishes[name].height = fish_render.get_size()
                            fishes[name].xpos = fishes[name].xpos_calc(self._width, self._offscreen_offset)
                        fish_render = renpy.render(fishes[name].animation(), width, height, st, at)
                        render.blit(fish_render, (fishes[name].xpos, fishes[name].ypos))
                        
                        if (fishes[name].xpos <= (self._width + self._offscreen_offset)) and (fishes[name].xpos >= (-self._offscreen_offset - fishes[name].width)):
                            if not fishes[name].flip():
                                fishes[name].xpos -= fishes[name].movement(self._fish_frame_pixel_width, self._frames_per_second)
                            else:
                                fishes[name].xpos += fishes[name].movement(self._fish_frame_pixel_width, self._frames_per_second)
                        else:
                            if not fishes[name].flip():
                                fishes[name].xpos = -self._offscreen_offset - fishes[name].width
                            else:
                                fishes[name].xpos = self._width + self._offscreen_offset
                            fishes[name].flip(True)
                        
                        if fishes[name].bait_check(self._bait) and self._bait_dropped:
                            if fishes[name].hitbox(self._hook_xpos_center,self._hook_ypos_center):
                                self._fish_caught = True
                                self._caught_fish = fishes[name]
                
                if self._hitbox_test:
                    for f in fishes:
                        render.canvas().rect("#FF0000", fishes[f].hitbox_draw(), 2)
                    
                    if self._bait == "golden lure" and M_aqua.get_state() == S_aqua_fishing:
                        render.canvas().rect("#FF0000", (230, 730, (390 - 230), (self._height - 730)), 2)
                
                if not self._aqua_appeared:
                    render.blit(bait_render, (self._hook_xpos, self._hook_ypos))
            
            if self._fish_caught:
                render.blit(fishing_exclamation_render, (800, 90))
                render.blit(renpy.render(self._caught_fish.displayable(), width, height, st, at), (self._caught_fish.xpos, self._caught_fish.ypos))
                if not self._caught_fish.flip():
                    render.blit(fishing_done_render, ((self._caught_fish.xpos - 102), (self._caught_fish.ypos - 102)))
                else:
                    render.blit(fishing_done_render, ((self._caught_fish.xpos + self._caught_fish.width - 102), (self._caught_fish.ypos - 102)))
                if not self._fish_caught_hover:
                    if not self._caught_fish.flip():
                        render.blit(fishing_catch_render, ((self._caught_fish.xpos - 102), ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102)))
                    else:
                        render.blit(fishing_catch_render, ((self._caught_fish.xpos + self._caught_fish.width - 102), ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102)))
                else:
                    if not self._caught_fish.flip():
                        render.blit(fishing_catch_hover_render, ((self._caught_fish.xpos - 102), ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102)))
                    else:
                        render.blit(fishing_catch_hover_render, ((self._caught_fish.xpos + self._caught_fish.width - 102), ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102)))
            
            if self._bait == "golden lure" and M_aqua.get_state() == S_aqua_fishing:
                if self._hook_xpos_center > 230 and self._hook_xpos_center < 390:
                    if self._hook_ypos_center > 730:
                        self._aqua_appeared = True
                        if self._aqua_timer == 0:
                            self._aqua_timer = st
                        elif (st - self._aqua_timer) > 0.02:
                            if (st - self._aqua_timer) > 1.5:
                                renpy.hide_screen("fishing_test")
                                renpy.jump("aqua_lure_steal")
                            aqua_render = renpy.render(self._aqua, width, height, st, at)
                            render.blit(aqua_render, (248, 661))
            
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            import pygame
            
            if renpy.variant("mobile") and not self._bait_dropped:
                if x > self._hook_xpos and x < (self._hook_xpos + self._bait_width):
                    if y > self._hook_ypos and y < (self._hook_ypos + self._bait_height):
                        if ev.type == pygame.MOUSEBUTTONUP:
                            self._bait_dropped = True
                
                elif x < self._left_arrow_width:
                    if y > self._left_arrow_height and y < (self._left_arrow_height * 2):
                        if ev.type == pygame.MOUSEBUTTONUP and self._hook_xpos > 37:
                            self._hook_xpos -= 4
                            renpy.redraw(self, 0)
                            raise renpy.IgnoreEvent()
                
                elif x > (self._width - self._right_arrow_width):
                    if y > self._right_arrow_height and y < (self._right_arrow_height * 2):
                        if ev.type == pygame.MOUSEBUTTONUP and self._hook_xpos < 882:
                            self._hook_xpos += 4
                            renpy.redraw(self, 0)
                            raise renpy.IgnoreEvent()
            
            if ev.type == pygame.KEYDOWN and not self._bait_dropped:
                if ev.key == pygame.K_LEFT and self._hook_xpos > 37:
                    self._hook_xpos -= 4
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                
                elif ev.key == pygame.K_RIGHT and self._hook_xpos < 882:
                    self._hook_xpos += 4
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                
                elif ev.key == pygame.K_RETURN:
                    self._bait_dropped = True
            
            if self._fish_caught:
                if not self._caught_fish.flip():
                    if x > (self._caught_fish.xpos - 102) and x < (self._caught_fish.xpos + 102):
                        if y > ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102) and y < ((self._caught_fish.ypos + (self._caught_fish.height / 2)) + 102):
                            self._fish_caught_hover = True
                            
                            if ev.type == pygame.MOUSEBUTTONUP:
                                renpy.hide_screen("fishing_test")
                                renpy.call("after_fishing", self._caught_fish.name, self._bait)
                        else:
                            self._fish_caught_hover = False
                    else:
                        self._fish_caught_hover = False
                else:
                    if x > (self._caught_fish.xpos + self._caught_fish.width - 102) and x < (self._caught_fish.xpos + self._caught_fish.width + 102):
                        if y > ((self._caught_fish.ypos + (self._caught_fish.height / 2)) - 102) and y < ((self._caught_fish.ypos + (self._caught_fish.height / 2)) + 102):
                            self._fish_caught_hover = True
                            
                            if ev.type == pygame.MOUSEBUTTONUP:
                                renpy.hide_screen("fishing_test")
                                renpy.call("after_fishing", self._caught_fish.name, self._bait)
                        else:
                            self._fish_caught_hover = False
                    else:
                        self._fish_caught_hover = False
            
            return self._selected_bait.event(ev, x, y, st)

screen bait_menu:
    add "buttons/fishing_instructions02.png" pos 110,100
    add "buttons/fishing_button01c.png" pos 250,250
    add "buttons/fishing_button02c.png" pos 150,250
    add "buttons/fishing_button03c.png" pos 250,150
    add "buttons/fishing_button04c.png" pos 150,150
    if worm in inventory.items:
        imagebutton:
            focus_mask True
            idle "buttons/fishing_button01a.png"
            hover "buttons/fishing_button01b.png"
            action SetVariable("bait", "worms"), Return()
            xpos 250
            ypos 250

    if lure01 in inventory.items:
        imagebutton:
            focus_mask True
            idle "buttons/fishing_button02a.png"
            hover "buttons/fishing_button02b.png"
            action SetVariable("bait", "standard lure"), Return()
            xpos 150
            ypos 250

    if special_lure in inventory.items:
        imagebutton:
            focus_mask True
            idle "buttons/fishing_button04a.png"
            hover "buttons/fishing_button04b.png"
            action SetVariable("bait", "golden lure"), Return()
            xpos 150
            ypos 150

screen fishing_minigame(bait):
    add Fishing(bait)