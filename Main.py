import tkinter as tk
from config import THEMES
from core.time_manager import TimeManager
from ui.clock_canvas import ClockCanvas
from ui.controls import Controls

class WaveTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WaveTime 💖")

        self.current_theme = "light"

        self.time_manager = TimeManager()

        self.clock = ClockCanvas(
            root,
            self.time_manager,
            THEMES[self.current_theme]
        )

        self.controls = Controls(
            root,
            self.clock,
            self.time_manager,
            self.toggle_theme
        )

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.clock.update_theme(THEMES[self.current_theme])


if __name__ == "__main__":
    root = tk.Tk()
    app = WaveTimeApp(root)
    root.mainloop()