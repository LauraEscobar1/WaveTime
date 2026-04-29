import customtkinter as ctk
from config import THEMES
from core.time_manager import TimeManager
from ui.clock_canvas import ClockCanvas
from ui.controls import Controls


class WaveTime:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("420x640")
        self.root.title("WaveTime")

        
        self.theme_name = "light"
        self.theme = THEMES[self.theme_name]

        self.time_manager = TimeManager()

        self.build_ui()

    def build_ui(self):

        self.root.configure(fg_color=self.theme["bg"])

        
        self.container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

     
        self.title = ctk.CTkLabel(
            self.container,
            text="WaveTime",
            font=("Georgia", 34, "bold"),
            text_color=self.theme["text"]
        )
        self.title.pack(pady=(15, 5))

       
        self.clock = ClockCanvas(
            self.container,
            self.time_manager,
            self.theme
        )

        
        self.controls = Controls(
            self.container,
            self.time_manager,
            self.toggle_theme
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