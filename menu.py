from tkinter import *
from PIL import ImageTk, Image
import json
import subprocess
import sys

class FoodItems():
    def __init__(self):
        self.f = open('data.json')

    def popular(self):
        self.list = ["Sandwich 1", "Taco", "Hot Dog", "Pasta", "Teriyaki", "Fries"]
        return self.list

    def new(self):
        self.list = ["Ice Cream", "Nuggets", "Cheese Burger", "Curry", "Sandwich 2", "Fish Fingers"]
        return self.list

    def full(self):
        self.data = json.load(self.f)
        return self.data

class GUI:
    global photos, x, y, cart, data, popular, new, menu

    x = 0

    y = 0

    photos = []

    cart = []

    data = FoodItems()
    popular = data.popular()
    new = data.new()
    menu = data.full()

    def __init__(self, parent):

        self.main_frame = Frame(parent, bg="white")
        self.main_frame.pack()

        x = self.main_frame.winfo_x()
        y = self.main_frame.winfo_y()

        #Logo
        self.imagef_osc = Image.open("images/osc.png")
        self.resize_image = self.imagef_osc.resize((100,50))
        self.imagef_osc = ImageTk.PhotoImage(self.resize_image)
        self.imagel_osc = Label(self.main_frame, image = self.imagef_osc, bg="white")

        #Order Now Label
        self.label_order_now = Label(self.main_frame, text="ORDER NOW", font=("Arial 30"), bg="white")

        #Catergories Drinks
        self.img_drinks = Image.open("images/drinks.png")
        self.resize_image = self.img_drinks.resize((120, 35))
        self.img_drinks = ImageTk.PhotoImage(self.resize_image)
        self.button_drinks = Button(self.main_frame, image=self.img_drinks, width=120, bg="white", borderwidth=0)

        #Catergories Sandwhiches
        self.img_sandwiches = Image.open("images/sandwiches.png")
        self.resize_image = self.img_sandwiches.resize((120, 35))
        self.img_sandwiches = ImageTk.PhotoImage(self.resize_image)
        self.button_sandwiches = Button(self.main_frame, image=self.img_sandwiches, width=120, bg="white", borderwidth=0)

        #Catergories Snacks
        self.img_snacks = Image.open("images/snacks.png")
        self.resize_image = self.img_snacks.resize((120, 35))
        self.img_snacks = ImageTk.PhotoImage(self.resize_image)
        self.button_snack = Button(self.main_frame, image=self.img_snacks, width=120, bg="white", borderwidth=0)

        #Catergories Icecream
        self.img_icecream = Image.open("images/icecream.png")
        self.resize_image = self.img_icecream.resize((120, 35))
        self.img_icecream = ImageTk.PhotoImage(self.resize_image)
        self.button_icecream = Button(self.main_frame, image=self.img_icecream, width=120, bg="white", borderwidth=0)

        #Popular Label
        self.label_popular = Label(self.main_frame, text="Popular", font=("Arial 30"), bg="white")

        #Popular Cards
        column_n = 0
        row_n = 3
        for i in menu:
            if (menu[i]["name"] in popular):
                self.display_card(menu[i]["image"], menu[i]["name"], row_n, column_n)
                if column_n < 3:
                    column_n += 1
                else:
                    column_n = 0
                    row_n += 1
            else:
                pass

        #New Label
        self.label_new = Label(self.main_frame, text="New", font=("Arial 30"), bg="white")

        #New Cards
        column_n = 0
        row_n = 6

        for i in menu:
            if (menu[i]["name"] in new):
                self.display_card(menu[i]["image"], menu[i]["name"], row_n, column_n)
                if column_n < 3:
                    column_n += 1
                else:
                    column_n = 0
                    row_n += 1
            else:
                pass

        #Cancel buttons
        self.img_cancel = Image.open("images/cancel_order.png")
        self.resize_image = self.img_cancel.resize((180, 50))
        self.img_cancel = ImageTk.PhotoImage(self.resize_image)
        self.button_cancel = Button(self.main_frame, image=self.img_cancel, width=120, bg="white", borderwidth=0, command=self.cancel)

        #View button
        self.img_view = Image.open("images/view_order.png")
        self.resize_image = self.img_view.resize((180, 50))
        self.img_view = ImageTk.PhotoImage(self.resize_image)
        self.button_view = Button(self.main_frame, image=self.img_view, width=120, bg="white", borderwidth=0, command=self.order)

        #Frame Pack
        self.imagel_osc.grid(column = 0, row = 0, sticky="NSEW")
        self.label_order_now.grid(column = 1, row = 0, columnspan= 2, sticky="NSEW")
        self.button_drinks.grid(column=0, row=1, sticky="NSEW")
        self.button_sandwiches.grid(column=1, row=1, sticky="NSEW")
        self.button_snack.grid(column=2, row=1, sticky="NSEW")
        self.button_icecream.grid(column=3, row=1, sticky="NSEW")
        self.label_popular.grid(column=0, row=2)
        self.label_new.grid(column=0, row=5)
        self.button_cancel.grid(column=0, columnspan=2, row=8, sticky="NSEW")
        self.button_view.grid(column=2, columnspan=2,  row=8, sticky="NSEW")

    def display_card(self, image_i, name, row_n, column_n):
        self.img_menu = Image.open(image_i)
        self.resize_image = self.img_menu.resize((120, 120))
        self.img_menu = ImageTk.PhotoImage(self.resize_image)
        photos.append(self.img_menu)
        self.button_img = Button(self.main_frame, image=self.img_menu, bg="white", borderwidth=0, command=lambda:self.add_item(name))
        self.button_img.grid(row=row_n, column=column_n, sticky="NSEW")

    def add_item(self, name):
        top = Toplevel(bg="white")
        top.geometry("+%d+%d" %(x+130,y+250))
        top.overrideredirect(True)
        Label(top, text=name, font=("Arial 30"), bg="white").grid(column=0, row=0, padx=20, columnspan=2)

        img_food = Image.open(menu[name]["image"])
        resize_image = img_food.resize((120, 120))
        img_food = ImageTk.PhotoImage(resize_image)
        Label(top, image=img_food, width=120, bg="white", borderwidth=0).grid(column=0, row=1, sticky="NSEW", padx=50, columnspan=2)

        Label(top, text=("Price: $" + menu[name]["price"]), font=("Arial 20"), bg="white").grid(column=0, row=2, padx=20, columnspan=2)

        def no():
            top.destroy()

        def yes():
            cart.append(str(name))
            top.destroy()

        img_no = Image.open("images/no.png")
        resize_image = img_no.resize((120, 35))
        img_no = ImageTk.PhotoImage(resize_image)
        button_no = Button(top, image=img_no, width=120, bg="white", borderwidth=0, command=no)
        button_no.grid(column=0, row=3, sticky="NSEW", pady=20, padx=20)

        img_yes = Image.open("images/yes.png")
        resize_image = img_yes.resize((120, 35))
        img_yes = ImageTk.PhotoImage(resize_image)
        button_yes = Button(top, image=img_yes, width=120, bg="white", borderwidth=0, command=yes)
        button_yes.grid(column=1, row=3, sticky="NSEW", pady=20, padx=20)

        top.mainloop()

    def order(self):

        top = Toplevel(bg="white")
        top.geometry("+%d+%d" %(x+130,y+250))
        top.overrideredirect(True)
        Label(top, text="Cart", font=("Arial 30"), bg="white").grid(column=0, row=0, columnspan=4, pady=20, padx=20)

        def no():
            top.destroy()

        def yes():
            subprocess.Popen(["python3", "pay.py"])
            sys.exit(0)

        def remove(xxx):
            cart.remove(xxx)
            top.destroy()

        r = 1

        total = 0

        for i in range(len(cart)):
            img_i = Image.open(menu[(cart[i])]["image"])
            resize_image = img_i.resize((70, 70))
            img_i = ImageTk.PhotoImage(resize_image)
            photos.append(img_i)

            Label(top, image=img_i, width=120, bg="white", borderwidth=0).grid(column=0, row=r, sticky="NSEW")

            Label(top, text=cart[i], font=("Arial 18"), bg="white").grid(column=1, row=r)
            Label(top, text="$" + menu[(cart[i])]["price"], font=("Arial 18"), bg="white").grid(column=2, row=r)
            button_remove = Button(top, text="X", bg="white", command=lambda:remove(menu[(cart[i])]["name"]))
            button_remove.grid(column=3, row=r, sticky="NSWE")

            total += int(menu[(cart[i])]["price"])

            r += 1

        Label(top, text="Total: $" + str(total), font=("Arial 18"), bg="white").grid(column=2, row=r)

        img_no = Image.open("images/no.png")
        resize_image = img_no.resize((120, 35))
        img_no = ImageTk.PhotoImage(resize_image)
        button_no = Button(top, image=img_no, width=120, bg="white", borderwidth=0, command=no)
        button_no.grid(column=1, row=r+1)

        img_yes = Image.open("images/yes.png")
        resize_image = img_yes.resize((120, 35))
        img_yes = ImageTk.PhotoImage(resize_image)
        button_yes = Button(top, image=img_yes, width=120, bg="white", borderwidth=0, command=yes)
        button_yes.grid(column=2, row=r+1)

        top.mainloop()

    def cancel(self):
        top = Toplevel(bg="white")
        top.geometry("+%d+%d" %(x+130,y+250))
        top.overrideredirect(True)
        Label(top, text="Cancel Order", font=("Arial 30"), bg="white").grid(column=0, row=0, columnspan=2, pady=20, padx=20)

        def no():
            top.destroy()

        def yes():
            exit()

        img_no = Image.open("images/no.png")
        resize_image = img_no.resize((120, 35))
        img_no = ImageTk.PhotoImage(resize_image)
        button_no = Button(top, image=img_no, width=120, bg="white", borderwidth=0, command=no)
        button_no.grid(column=0, row=1, sticky="NSEW", pady=20, padx=20)

        img_yes = Image.open("images/yes.png")
        resize_image = img_yes.resize((120, 35))
        img_yes = ImageTk.PhotoImage(resize_image)
        button_yes = Button(top, image=img_yes, width=120, bg="white", borderwidth=0, command=yes)
        button_yes.grid(column=1, row=1, sticky="NSEW", pady=20, padx=20)

        top.mainloop()

    def view_order(self):
        return


if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
