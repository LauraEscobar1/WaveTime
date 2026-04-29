import customtkinter as ctk
import math
from core.clock_logic import ClockLogic

class ClockCanvas:
    def __init__(self, parent, time_manager, theme):
        self.time_manager = time_manager
        self.theme = theme

        self.canvas = ctk.CTkCanvas(
            parent,
            width=320,
            height=320,
            highlightthickness=0,
            bg=theme["bg"]  
        )
        self.canvas.pack(pady=10)

        self.center = 160
        self.radius = 130

        self.update()

    def draw(self):
        self.canvas.delete("all")
        c = self.theme

        
        self.canvas.create_oval(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            fill=c["card"],
            outline=c["accent"],
            width=5
        )


        for i in range(60):
            angle = math.radians(i * 6 - 90)

            inner = self.radius - 12 if i % 5 == 0 else self.radius - 6
            width = 2 if i % 5 == 0 else 1

            x1 = self.center + inner * math.cos(angle)
            y1 = self.center + inner * math.sin(angle)
            x2 = self.center + self.radius * math.cos(angle)
            y2 = self.center + self.radius * math.sin(angle)

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill=c["text"],
                width=width
            )


        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = self.center + (self.radius - 28) * math.cos(angle)
            y = self.center + (self.radius - 28) * math.sin(angle)

            self.canvas.create_text(
                x, y,
                text=str(i),
                fill=c["text"],
                font=("Georgia", 15, "bold")  
            )

    def draw_hand(self, angle, length, width, color):
        x = self.center + length * math.cos(angle)
        y = self.center + length * math.sin(angle)

        self.canvas.create_line(
            self.center, self.center, x, y,
            width=width,
            fill=color
        )

    def update(self):
        self.draw()

        h, m, s = self.time_manager.get_time()
        ha, ma, sa = ClockLogic.get_angles(h, m, s)

        c = self.theme

        
        self.draw_hand(ha, 60, 6, c["text"])
        self.draw_hand(ma, 90, 3, c["text"])
        self.draw_hand(sa, 110, 1, c["accent"])

        self.canvas.create_oval(
            self.center - 4, self.center - 4,
            self.center + 4, self.center + 4,
            fill=c["accent"],
            outline=""
        )

        self.canvas.after(1000, self.update)

    def update_theme(self, theme):
        self.theme = theme

    
        self.canvas.configure(bg=theme["bg"])