import customtkinter as ctk
from config import TIMEZONES


class Controls:
    def __init__(self, parent, time_manager, toggle_theme):

        self.time_manager = time_manager
        self.toggle_theme = toggle_theme
        self.selected_zone = "Colombia"
        self.showing_time = False

        self.time_label = ctk.CTkLabel(
            parent,
            text="",
            font=("Georgia", 18, "bold")
        )
        self.time_label.pack(pady=(5, 2))

        self.status_label = ctk.CTkLabel(
            parent,
            text="🌍 Colombia | ☀️ Modo claro",
            font=("Georgia", 12)
        )
        self.status_label.pack(pady=(0, 8))

        self.bar = ctk.CTkFrame(parent, corner_radius=10)
        self.bar.pack(padx=20, pady=(5, 15), fill="x")

        self.inner = ctk.CTkFrame(self.bar, fg_color="transparent")
        self.inner.pack(padx=10, pady=10, fill="x")

        self.inner.grid_columnconfigure(0, weight=1)
        self.inner.grid_columnconfigure(1, weight=1)
        self.inner.grid_columnconfigure(2, weight=1)

        self.clock_btn = ctk.CTkButton(
            self.inner,
            text="🕒\nHora",
            command=self.toggle_time,
            corner_radius=15
        )
        self.clock_btn.grid(row=0, column=0, padx=5, sticky="ew")

        self.zone_btn = ctk.CTkButton(
            self.inner,
            text="🌍\nColombia",
            command=self.change_zone,
            corner_radius=15
        )
        self.zone_btn.grid(row=0, column=1, padx=5, sticky="ew")

        self.theme_btn = ctk.CTkButton(
            self.inner,
            text="🎨\nTema",
            command=self.toggle_theme,
            corner_radius=15
        )
        self.theme_btn.grid(row=0, column=2, padx=5, sticky="ew")

        self.update_time()

    def change_zone(self):
        zones = list(TIMEZONES.keys())
        index = zones.index(self.selected_zone)
        index = (index + 1) % len(zones)

        self.selected_zone = zones[index]
        self.time_manager.set_timezone(TIMEZONES[self.selected_zone])

        self.zone_btn.configure(text=f"🌍\n{self.selected_zone}")
        self.update_status()

    def toggle_time(self):
        self.showing_time = not self.showing_time
        if not self.showing_time:
            self.time_label.configure(text="")

    def update_time(self):
        if self.showing_time:
            h, m, s = self.time_manager.get_time()
            self.time_label.configure(text=f"{h:02d}:{m:02d}:{s:02d}")
        self.time_label.after(1000, self.update_time)

    def update_theme(self, theme, mode_name):

        if mode_name == "light":
            bar_color = "#C43670"
            btn_color = "#F283AF"
            text_color = "black"
            mode_text = "☀️ Modo claro"
        else:
            bar_color = "#d95f8c"
            btn_color = "#870339"
            text_color = "white"
            mode_text = "🌙 Modo oscuro"

        self.bar.configure(fg_color=bar_color)

        for btn in [self.clock_btn, self.zone_btn, self.theme_btn]:
            btn.configure(
                fg_color=btn_color,
                hover_color=btn_color,
                text_color=text_color
            )

        self.time_label.configure(text_color=text_color)

        self.current_mode = mode_text
        self.update_status()

        self.status_label.configure(text_color=text_color)

    def update_status(self):
        mode = getattr(self, "current_mode", "☀️ Modo claro")
        self.status_label.configure(
            text=f"🌍 {self.selected_zone} | {mode}"
        )