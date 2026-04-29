import customtkinter as ctk
from config import TIMEZONES


class Controls:
    def __init__(self, parent, time_manager, toggle_theme):

        self.time_manager = time_manager
        self.toggle_theme = toggle_theme
        self.selected_zone = "Colombia"

        self.time_label = ctk.CTkLabel(
            parent,
            text="",
            font=("Georgia", 18, "bold")
        )
        self.time_label.pack(pady=5)

        self.bar = ctk.CTkFrame(parent, corner_radius=25)
        self.bar.pack(padx=20, pady=20, fill="x")

        self.clock_btn = ctk.CTkButton(
            self.bar,
            text="🕒\nHora",
            command=self.show_time,
            corner_radius=20
        )
        self.clock_btn.pack(side="left", expand=True, pady=10)

        self.zone_btn = ctk.CTkButton(
            self.bar,
            text="🌍\nColombia",
            command=self.change_zone,
            corner_radius=20
        )
        self.zone_btn.pack(side="left", expand=True)

        self.theme_btn = ctk.CTkButton(
            self.bar,
            text="🎨\nTema",
            command=self.toggle_theme,
            corner_radius=20
        )
        self.theme_btn.pack(side="left", expand=True)

    def change_zone(self):
        zones = list(TIMEZONES.keys())
        index = zones.index(self.selected_zone)
        index = (index + 1) % len(zones)

        self.selected_zone = zones[index]
        self.time_manager.set_timezone(TIMEZONES[self.selected_zone])

        self.zone_btn.configure(text=f"🌍\n{self.selected_zone}")

    def show_time(self):
        h, m, s = self.time_manager.get_time()
        self.time_label.configure(text=f"{h:02d}:{m:02d}:{s:02d}")

    def update_theme(self, theme, mode_name):

        self.bar.configure(
            fg_color=theme["card"]
        )

        for btn in [self.clock_btn, self.zone_btn, self.theme_btn]:
            btn.configure(
                fg_color=theme["accent"],
                hover_color=theme["accent"],
                text_color="white"
            )

        self.clock_btn.configure(
            fg_color=theme["text"]
        )

        if mode_name == "light":
            self.time_label.configure(text_color=theme["text"])
        else:
            self.time_label.configure(text_color=theme["text"])