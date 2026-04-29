import tkinter as tk
from config import TIMEZONES

class Controls:
    def __init__(self, root, clock_canvas, time_manager, change_theme_callback):

        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Tema
        self.theme_button = tk.Button(
            frame,
            text="🌙 Cambiar tema",
            command=change_theme_callback
        )
        self.theme_button.pack(side="left", padx=10)

        # Zona horaria
        self.zone_var = tk.StringVar(value="Colombia")

        self.dropdown = tk.OptionMenu(
            frame,
            self.zone_var,
            *TIMEZONES.keys(),
            command=self.change_zone
        )
        self.dropdown.pack(side="left", padx=10)

        self.time_manager = time_manager

    def change_zone(self, selection):
        offset = TIMEZONES[selection]
        self.time_manager.set_timezone(offset)