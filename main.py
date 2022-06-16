from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sys

class GUI:
    def __init__(self, parent):

        main_frame = Frame(parent, bg="white")
        main_frame.pack()

        #Logo
        self.imagef_osc = Image.open("images/osc.png")
        self.resize_image = self.imagef_osc.resize((100,50))
        self.imagef_osc = ImageTk.PhotoImage(self.resize_image)
        self.imagel_osc = Label(main_frame, image = self.imagef_osc, bg="white")

        #Order Now Label
        self.label_order_now = Label(main_frame, text="ORDER NOW", font=("Arial 30 bold"), bg="white")

        #Start
        self.img_start = Image.open("images/start.png")
        self.resize_image = self.img_start.resize((170,80))
        self.img_start = ImageTk.PhotoImage(self.resize_image)
        self.button_start = Button(main_frame, image=self.img_start, command=self.start, bg="white", borderwidth=0)

        #Burger
        self.label_title = Label(main_frame, text="Special", font=("Arial 30"), bg="white")
        self.imagef_burger = Image.open("images/burger.png")
        self.resize_image = self.imagef_burger.resize((215,150))
        self.imagef_burger = ImageTk.PhotoImage(self.resize_image)
        self.imagel_burger = Label(main_frame, image = self.imagef_burger, bg="white")

        #Frame Pack
        self.imagel_osc.grid(column = 0, row = 0, sticky=W)
        self.label_order_now.grid(column = 0, row= 1, pady=(50))
        self.button_start.grid(column = 0, row = 2, pady=(0,50))
        self.label_title.grid(column = 0, row = 3)
        self.imagel_burger.grid(column = 0, row = 4, padx=(50,50), pady=(50,50))

    def start(self):
        subprocess.Popen(["python3", "menu.py"])
        sys.exit(0)


if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
