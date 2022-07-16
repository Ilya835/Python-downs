from tkinter import *


class MainFrame(Frame):
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.master.title("Соси хуй")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle()
        canvas.create_line()