def init_widgets():
    return [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors["group_active"],
            background=colors["panel_background"],
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
            scale="False",
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors["group_active"],
            background=colors["panel_background"],
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors["group_active"],
            inactive=colors["group_inative"],
            rounded=False,
            highlight_color=colors["current_screen_background"],
            highlight_method="line",
            this_current_screen_border=colors["window_name"],
            this_screen_border=colors["other_tab_border"],
            other_current_screen_border=colors["window_name"],
            other_screen_border=colors["other_tab_border"],
            foreground=colors["group_active"],
            background=colors["panel_background"],
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors["current_tab_border"],
            background=colors["current_screen_background"],
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors["group_active"],
            background=colors["panel_background"],
        ),
        widget.WindowName(
            foreground=colors["window_name"],
            background=colors["panel_background"],
            fontsize=16,
            padding=0,
        ),
        widget.Systray(background=colors["panel_background"], padding=5),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors["panel_background"],
            background=colors["panel_background"],
        ),
        widget.TextBox(
            text="",
            foreground=colors["even_widgets"],
            background=colors["panel_background"],
            padding=0,
            fontsize=37,
        ),
        widget.Net(
            interface="enp4s0",
            format="{down} ↓↑ {up}",
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            padding=5,
        ),
        widget.TextBox(
            text="",
            foreground=colors["other_tab_border"],
            background=colors["even_widgets"],
            padding=0,
            fontsize=37,
        ),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors["group_active"],
            background=colors["other_tab_border"],
            fontsize=11,
        ),
        widget.ThermalSensor(
            foreground=colors["group_active"],
            background=colors["other_tab_border"],
            threshold=90,
            padding=5,
        ),
        widget.TextBox(
            text="",
            foreground=colors["even_widgets"],
            background=colors["other_tab_border"],
            padding=0,
            fontsize=37,
        ),
        widget.TextBox(
            text=" ⟳",
            padding=2,
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            fontsize=14,
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="{updates} Updates",
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")
            },
        ),
        widget.TextBox(
            text="",
            foreground=colors["other_tab_border"],
            background=colors["even_widgets"],
            padding=0,
            fontsize=37,
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors["group_active"],
            background=colors["other_tab_border"],
            padding=0,
            fontsize=14,
        ),
        widget.Memory(
            foreground=colors["group_active"],
            background=colors["other_tab_border"],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
            padding=5,
        ),
        widget.TextBox(
            text="",
            foreground=colors["even_widgets"],
            background=colors["other_tab_border"],
            padding=0,
            fontsize=37,
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            padding=0,
        ),
        widget.Volume(
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            padding=5,
        ),
        widget.TextBox(
            text="",
            foreground=colors["other_tab_border"],
            background=colors["even_widgets"],
            padding=0,
            fontsize=37,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors["panel_background"],
            background=colors["other_tab_border"],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(
            foreground=colors["group_active"],
            background=colors["other_tab_border"],
            padding=5,
        ),
        widget.TextBox(
            text="",
            foreground=colors["even_widgets"],
            background=colors["other_tab_border"],
            padding=0,
            fontsize=37,
        ),
        widget.Clock(
            foreground=colors["group_active"],
            background=colors["even_widgets"],
            format="%A, %B %d - %H:%M ",
        ),
    ]