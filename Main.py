import customtkinter as ctk
from config import THEMES
from core.time_manager import TimeManager
from ui.clock_canvas import ClockCanvas
from ui.controls import Controls

class WaveTime:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("420x620")
        self.root.title("WaveTime")

        self.theme_name = "light"
        self.theme = THEMES[self.theme_name]

        self.time_manager = TimeManager()

        self.build_ui()

    def build_ui(self):
        self.root.configure(fg_color=self.theme["bg"])

        # TÍTULO BONITO SIN CORAZÓN
        self.title = ctk.CTkLabel(
            self.root,
            text="WaveTime",
            font=("Times New Roman", 32, "bold"),
            text_color=self.theme["text"]
        )
        self.title.pack(pady=10)

        # RELOJ
        self.clock = ClockCanvas(self.root, self.time_manager, self.theme)

        # CONTROLES
        self.controls = Controls(
            self.root,
            self.time_manager,
            self.toggle_theme,
            self.theme
        )
        self.controls.update_theme(self.theme, self.theme_name)

    def toggle_theme(self):
        self.theme_name = "dark" if self.theme_name == "light" else "light"
        self.theme = THEMES[self.theme_name]

        self.root.configure(fg_color=self.theme["bg"])
        self.title.configure(text_color=self.theme["text"])

        self.clock.update_theme(self.theme)
        self.controls.update_theme(self.theme, self.theme_name)


if __name__ == "__main__":
    app = WaveTime()
    app.root.mainloop()