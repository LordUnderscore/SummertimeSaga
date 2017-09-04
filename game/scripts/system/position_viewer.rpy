init -1100 python:
    class PositionViewer(object):
        def __init__(self):
            
            self.int_range = 1500
            self.float_range = 7.0
            self.state_org = {}
        
        def viewer(self):
            if not config.developer:
                return
            sle = renpy.game.context().scene_lists
            for layer in config.layers:
                
                for tag in sle.layers[layer]:
                    d = sle.get_displayable_by_tag(layer, tag[0])
                    zoom = None
                    if getattr(d, "state", False):
                        zoom = d.state.zoom
                    state = renpy.get_placement(d)
                    
                    if layer not in self.state_org:
                        self.state_org[layer] = {}
                    if tag[0] not in self.state_org[layer]:
                        self.state_org[layer][tag[0]] = {}
                    self.state_org[layer][tag[0]] = {}
                    if state.xpos is not None:
                        self.state_org[layer][tag[0]]["xpos"] = state.xpos
                    
                    
                    if state.ypos is not None:
                        self.state_org[layer][tag[0]]["ypos"] = state.ypos
                    
                    
                    if state.xanchor is not None:
                        self.state_org[layer][tag[0]]["xanchor"] = state.xanchor
                    
                    
                    if state.yanchor is not None:
                        self.state_org[layer][tag[0]]["yanchor"] = state.yanchor
                    
                    
                    if zoom is not None:
                        self.state_org[layer][tag[0]]["zoom"] = zoom
            renpy.show_screen("_position_viewer", viewer=self)
            renpy.restart_interaction()
        
        def reset(self):
            for layer in config.layers:
                if self.state_org.get(layer):
                    for tag, props in self.state_org[layer].iteritems():
                        if tag and props:
                            renpy.show(tag, [Transform(**props)], layer=layer)
            renpy.restart_interaction()
        
        def generate_changed(self, tag, prop, layer, int=False):
            def changed(v):
                state = renpy.get_placement(renpy.game.context().scene_lists.get_displayable_by_tag(layer, tag))
                kwargs={"xpos":state.xpos, "ypos":state.ypos, "xanchor":state.xanchor, "yanchor":state.yanchor}
                if int:
                    kwargs[prop] = v - self.int_range
                else:
                    kwargs[prop] = v -self.float_range
                renpy.show(tag, [Transform(**kwargs)], layer=layer)
                renpy.restart_interaction()
            return changed


screen _position_viewer(viewer, layer="master", tag=""):
    key "game_menu" action Hide("_position_viewer")
    $ sle = renpy.game.context().scene_lists
    $ state = None
    if tag:
        $ d = sle.get_displayable_by_tag(layer, tag)
        if d:
            $ state = renpy.get_placement(d)

    frame:
        xfill True
        ysize 400
        background "#0002"
        vbox:

            text _("layers")
            hbox:
                for l in config.layers:
                    if l not in ["screens", "transient", 'overlay', "debug"]:
                        textbutton "[l]" action [SelectedIf(l == layer), Show("_position_viewer", viewer=viewer, layer=l)]

            text _("images")
            hbox:
                for t in sle.layers[layer]:
                    textbutton "{}".format(t[0]) action [SelectedIf(t[0] == tag), Show("_position_viewer", viewer=viewer, layer=layer, tag=t[0])]

            if state:
                $ xpos    = state.xpos
                $ ypos    = state.ypos
                $ xanchor = state.xanchor
                $ yanchor = state.yanchor

                if state.xpos is None:
                    $ xpos = 0.
                if state.ypos is None:
                    $ ypos = 0.
                if state.xanchor is None:
                    $ xanchor = 0.
                if state.yanchor is None:
                    $ yanchor = 0.

                text "{}".format(tag)
                if isinstance(xpos, int):
                    hbox:
                        xfill True
                        text "xpos {:>10}".format(xpos)
                        null width 10
                        if xpos is not None:
                            bar adjustment ui.adjustment(range=viewer.int_range*2, value=xpos+viewer.int_range, page=1, changed=viewer.generate_changed(tag, "xpos", layer, True)) xalign 1.
                elif isinstance(xpos, float):
                    hbox:
                        xfill True
                        text "xpos {:>10.4f}".format(xpos)
                        null width 10
                        if xpos is not None:
                            bar adjustment ui.adjustment(range=viewer.float_range*2, value=xpos+viewer.float_range, page=.05, changed=viewer.generate_changed(tag, "xpos", layer)) xalign 1.
                if isinstance(ypos, int):
                    hbox:
                        xfill True
                        text "ypos {:>10}".format(ypos)
                        null width 10
                        if ypos is not None:
                            bar adjustment ui.adjustment(range=viewer.int_range*2, value=ypos+viewer.int_range, page=1, changed=viewer.generate_changed(tag, "ypos", layer, True)) xalign 1.
                        else:
                            bar adjustment ui.adjustment(range=viewer.int_range*2, value=0+viewer.int_range, page=1, changed=viewer.generate_changed(tag, "ypos", layer, True)) xalign 1.
                elif isinstance(ypos, float):
                    hbox:
                        xfill True
                        text "ypos {:>10.4f}".format(ypos)
                        null width 10
                        if ypos is not None:
                            bar adjustment ui.adjustment(range=viewer.float_range*2, value=ypos+viewer.float_range, page=.05, changed=viewer.generate_changed(tag, "ypos", layer)) xalign 1.
                if isinstance(xanchor, int):
                    hbox:
                        xfill True
                        text "xanchor {:>7}".format(xanchor)
                        null width 10
                elif isinstance(xanchor, float):
                    hbox:
                        xfill True
                        text "xanchor {:>7.4f}".format(xanchor)
                        null width 10
                        if xanchor is not None:
                            bar adjustment ui.adjustment(range=viewer.float_range*2, value=xanchor+viewer.float_range, page=.05, changed=viewer.generate_changed(tag, "xanchor", layer)) xalign 1.
                if isinstance(yanchor, int):
                    hbox:
                        xfill True
                        text "yanchor {:>7}".format(yanchor)
                        null width 10
                        if yanchor is not None:
                            bar adjustment ui.adjustment(range=viewer.int_range*2, value=yanchor+viewer.int_range, page=1, changed=viewer.generate_changed(tag, "yanchor", layer, True)) xalign 1.
                elif isinstance(yanchor, float):
                    hbox:
                        xfill True
                        text "yanchor {:>7.4f}".format(yanchor)
                        null width 10
                        if yanchor is not None:
                            bar adjustment ui.adjustment(range=viewer.float_range*2, value=yanchor+viewer.float_range, page=.05, changed=viewer.generate_changed(tag, "yanchor", layer)) xalign 1.
                if getattr(d, "state", False):
                    hbox:
                        xfill True
                        text "zoom {:>10}".format(float(d.state.zoom))
                        null width 10
                        bar adjustment ui.adjustment(range=viewer.float_range*2, value=float(d.state.zoom)+viewer.float_range, step=1, changed=viewer.generate_changed(tag, "zoom", layer)) xalign 1.
                null height 20
        hbox:
            xalign 1.
            yalign 1.
            textbutton _("reset") action [viewer.reset, renpy.restart_interaction]
            textbutton _("close") action Hide("_position_viewer")

init -1099 python:

    km = renpy.Keymap(
        rollback = renpy.rollback,
        screenshot = _screenshot,
        toggle_fullscreen = renpy.toggle_fullscreen,
        toggle_skip = _keymap_toggle_skipping,
        fast_skip = _fast_skip,
        game_menu = _invoke_game_menu,
        hide_windows = renpy.curried_call_in_new_context("_hide_windows"),
        launch_editor = _launch_editor,
        reload_game = _reload_game,
        developer = _developer,
        quit = renpy.quit_event,
        iconify = renpy.iconify,
        help = _help,
        choose_renderer = renpy.curried_call_in_new_context("_choose_renderer"),
        console = _console.enter,
        profile_once = _profile_once,
        self_voicing = Preference("self voicing", "toggle"),
        position_viewer = PositionViewer().viewer,
        )

    config.underlay = [ km ]

    del km

init 1000 python:
    config.locked = False
    config.keymap["position_viewer"] = 'K_F9'
    config.locked = True