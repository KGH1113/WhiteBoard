import tkinter as tk
import pyautogui
from PIL import ImageGrab
import os

class DrawingApp:
    def __init__(self):
        # Create a window that displays the screen capture
        self.root = tk.Tk()
        self.root.title("Drawing App")
        self.root.geometry("{}x{}".format(pyautogui.size().width, pyautogui.size().height))
        self.canvas = tk.Canvas(self.root, width=pyautogui.size().width, height=pyautogui.size().height)
        self.canvas.pack()
        img = ImageGrab.grab()
        img.save(os.path.join(os.getcwd(), 'image.png'))
        self.canvas_image = tk.PhotoImage(file=os.path.join(os.getcwd(), 'image.png'))
        self.canvas.create_image(0, 0, image=self.canvas_image)
        
        # Initialize variables for drawing
        self.pen_color = 'red'
        self.previous_x = None
        self.previous_y = None
        self.lines = []
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_drawing)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.end_drawing)
        
        # Bind key events
        self.root.bind('<Key-r>', self.set_pen_color_red)
        self.root.bind('<Key-b>', self.set_pen_color_blue)
        self.root.bind('<Key-e>', self.erase)
        
        self.root.mainloop()
    
    def start_drawing(self, event):
        self.previous_x = event.x
        self.previous_y = event.y
    
    def draw(self, event):
        if self.previous_x is not None and self.previous_y is not None:
            line = self.canvas.create_line(self.previous_x, self.previous_y, event.x, event.y, fill=self.pen_color)
            self.lines.append(line)
            self.previous_x = event.x
            self.previous_y = event.y
    
    def end_drawing(self, event):
        self.previous_x = None
        self.previous_y = None
    
    def set_pen_color_red(self, event):
        self.pen_color = 'red'
    
    def set_pen_color_blue(self, event):
        self.pen_color = 'blue'
    
    def erase(self, event):
        for line in self.lines:
            if self.canvas.find_withtag('current') == (line,):
                self.canvas.delete(line)

DrawingApp()