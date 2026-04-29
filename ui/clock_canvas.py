import tkinter as tk
import math
from core.clock_logic import ClockLogic

class ClockCanvas:
    def __init__(self, root, time_manager, theme):
        self.root = root
        self.time_manager = time_manager
        self.theme = theme

        self.canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0)
        self.canvas.pack(pady=10)

        self.center = 200
        self.radius = 150

        self.draw_face()
        self.update()

    def draw_face(self):
        self.canvas.delete("all")

        colors = self.theme

        self.canvas.configure(bg=colors["bg"])

        self.canvas.create_oval(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            fill=colors["clock_bg"],
            outline=colors["accent"],
            width=4
        )

        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = self.center + (self.radius - 25) * math.cos(angle)
            y = self.center + (self.radius - 25) * math.sin(angle)

            self.canvas.create_text(
                x, y,
                text=str(i),
                fill=colors["fg"],
                font=("Arial", 14, "bold")
            )

    def draw_hand(self, angle, length, width, color):
        x = self.center + length * math.cos(angle)
        y = self.center + length * math.sin(angle)

        self.canvas.create_line(
            self.center, self.center, x, y,
            width=width,
            fill=color,
            tags="hands"
        )

    def update(self):
        self.canvas.delete("hands")

        hour, minute, second = self.time_manager.get_time()
        h_angle, m_angle, s_angle = ClockLogic.get_angles(hour, minute, second)

        colors = self.theme

        self.draw_hand(h_angle, 70, 5, colors["fg"])
        self.draw_hand(m_angle, 100, 3, colors["fg"])
        self.draw_hand(s_angle, 120, 1, colors["second"])

        self.root.after(1000, self.update)

    def update_theme(self, new_theme):
        self.theme = new_theme
        self.draw_face()