import tkinter as tk
import math
import time

class JarvisCircleLayer:
    def __init__(self, canvas, x, y, radius, width, color, speed, segments, rotation_direction=1):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.color = color
        self.speed = speed
        self.segments = segments
        self.rotation_direction = rotation_direction
        self.angle = 0
        self.arc_list = []

    def draw(self):
        # Clear the previous arcs
        for arc in self.arc_list:
            self.canvas.delete(arc)
        
        self.arc_list = []  # Reset the arc list
        # Divide the full circle into segments
        for i in range(self.segments):
            start_angle = self.angle + (i * (360 / self.segments))
            extent = 360 / (2 * self.segments)  # Extent of each arc (half-circle)

            arc = self.canvas.create_arc(
                self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius,
                start=start_angle, extent=extent,
                outline=self.color, width=self.width, style=tk.ARC
            )
            self.arc_list.append(arc)

    def animate(self):
        # Update the angle based on speed and direction
        self.angle += self.speed * self.rotation_direction
        if self.angle >= 360:
            self.angle = 0
        self.draw()

def create_jarvis_interface(canvas):
    # Create 3 layered circles, each with increased thickness
    circles = [
        JarvisCircleLayer(canvas, x=canvas.winfo_width()//2, y=canvas.winfo_height()//2, radius=200, width=6, color='cyan', speed=1, segments=12, rotation_direction=1),
        JarvisCircleLayer(canvas, x=canvas.winfo_width()//2, y=canvas.winfo_height()//2, radius=300, width=8, color='blue', speed=2, segments=18, rotation_direction=-1),
        JarvisCircleLayer(canvas, x=canvas.winfo_width()//2, y=canvas.winfo_height()//2, radius=400, width=10, color='lightblue', speed=1.5, segments=24, rotation_direction=1)
    ]
    
    # Animation loop for all circles
    while True:
        for circle in circles:
            circle.animate()
        canvas.update()
        time.sleep(0.01)

def exit_fullscreen(event):
    window.attributes('-fullscreen', False)

# Set up the window
window = tk.Tk()
window.title("JARVIS Sci-Fi Interface")

# Full screen mode
window.attributes('-fullscreen', True)
window.bind("<Escape>", exit_fullscreen)  # Press 'Esc' to exit full screen

# Create a full screen canvas
canvas = tk.Canvas(window, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

# Start the JARVIS-like interface animation
window.after(100, lambda: create_jarvis_interface(canvas))

window.mainloop()
