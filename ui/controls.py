import customtkinter as ctk
from config import TIMEZONES

class Controls:
    def __init__(self, parent, time_manager, toggle_theme, theme):

        self.time_manager = time_manager
        self.theme = theme

        # BOTONES PRINCIPALES
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.frame.pack(pady=10)

        self.theme_btn = ctk.CTkButton(
            self.frame,
            text="🎨 Cambiar tema",
            corner_radius=20,
            command=toggle_theme
        )
        self.theme_btn.pack(side="left", padx=10)

        self.zone = ctk.CTkOptionMenu(
            self.frame,
            values=list(TIMEZONES.keys()),
            command=self.change_zone
        )
        self.zone.set("Colombia")
        self.zone.pack(side="left", padx=10)

        # INDICADOR DE MODO
        self.mode_label = ctk.CTkLabel(parent, text="")
        self.mode_label.pack(pady=5)

        # BARRA INFERIOR
        self.bottom_bar = ctk.CTkFrame(parent, corner_radius=20)
        self.bottom_bar.pack(padx=20, pady=15, fill="x")

        self.btn_clock = ctk.CTkLabel(self.bottom_bar, text="🕒\nReloj")
        self.btn_clock.pack(side="left", expand=True, pady=10)

        self.btn_zone = ctk.CTkLabel(self.bottom_bar, text="🌍\nZona")
        self.btn_zone.pack(side="left", expand=True)

        self.btn_theme = ctk.CTkLabel(self.bottom_bar, text="🎨\nTema")
        self.btn_theme.pack(side="left", expand=True)

    def change_zone(self, selection):
        self.time_manager.set_timezone(TIMEZONES[selection])

    def update_theme(self, theme, mode_name):
        self.theme = theme

        # BOTONES CON COLOR REAL
        self.theme_btn.configure(
            fg_color=theme["accent"],
            text_color="white"
        )

        self.zone.configure(
            fg_color=theme["card"],
            text_color=theme["text"]
        )

        # TEXTO MODO
        if mode_name == "light":
            self.mode_label.configure(text="☀️ Modo claro", text_color=theme["text"])
        else:
            self.mode_label.configure(text="🌙 Modo oscuro", text_color=theme["text"])

        # BARRA
        self.bottom_bar.configure(fg_color=theme["card"])