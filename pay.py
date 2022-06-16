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
        self.label_pay = Label(main_frame, text="Pay", font=("Arial 30 bold"), bg="white")

        #eftpos
        self.img_cash = Image.open("images/cash.png")
        self.resize_image = self.img_cash.resize((140,240))
        self.img_cash = ImageTk.PhotoImage(self.resize_image)
        self.button_cash = Button(main_frame, image=self.img_cash, command=self.start, bg="white", borderwidth=0)

        #eftpos
        self.img_eftpos = Image.open("images/eftpos.png")
        self.resize_image = self.img_eftpos.resize((140,240))
        self.img_eftpos = ImageTk.PhotoImage(self.resize_image)
        self.button_eftpos = Button(main_frame, image = self.img_eftpos, command=self.start, bg="white", borderwidth=0)

        #total
        self.label_total = Label(main_frame, text="Total: $", font=("Arial 18"), bg="white")

        #Buttons
        self.img_no = Image.open("images/go_back.png")
        self.resize_image = self.img_no.resize((120, 35))
        self.img_no = ImageTk.PhotoImage(self.resize_image)
        self.button_no = Button(main_frame, image=self.img_no, width=120, bg="white", borderwidth=0)
        self.button_no.grid(column=0, row=4)

        self.img_yes = Image.open("images/confirm.png")
        self.resize_image = self.img_yes.resize((120, 35))
        self.img_yes = ImageTk.PhotoImage(self.resize_image)
        self.button_yes = Button(main_frame, image=self.img_yes, width=120, bg="white", borderwidth=0)
        self.button_yes.grid(column=1, row=4)

        #Frame Pack
        self.imagel_osc.grid(column = 0, row = 0, sticky=W, columnspan=2)
        self.label_pay.grid(column = 0, row= 1, columnspan=2)
        self.button_cash.grid(column = 0, row = 2)
        self.button_eftpos.grid(column = 1, row = 2)
        self.label_total.grid(column = 0, row = 3, columnspan=2)

    def start(self):
        subprocess.Popen(["python3", "menu.py"])
        sys.exit(0)


if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
