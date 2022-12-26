from tkinter import Button, Entry, Frame, Label, messagebox
from tkinter.ttk import Combobox
from editor import common_functions, OptionFile

class ShopTab(Frame):
    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.points_lbl = Label(self, text= f"Please enter a value between 0 and 99999 and press enter\nCurrent points {self.of.shop.points}")
        self.new_points_box = Entry(self, width=8)
        self.new_points_box.bind('<Return>', lambda event: self.shop_set_points())
        self.unlock_lock_lbl = Label(self, text= f"Unlock/Lock Shop Items")
        self.unlock_shop_btn = Button(self, text="Unlock shop", command = lambda: messagebox.showinfo(title=self.appname,message=self.of.shop.unlock_shop()))
        self.lock_shop_btn = Button(self, text="Lock shop", command = lambda: messagebox.showinfo(title=self.appname,message=self.of.shop.lock_shop()))
        # Since we don't know the name of the background menu we generate some random names
        self.bg_list = [f"Main Menu BG {i+1}" for i in range(self.of.shop.TOTAL_BGS)]
        self.bg_selector_lbl = Label(self, text= f"Main Menu Background Selector")
        self.bg_selector_cmb = Combobox(self, state="readonly", value=self.bg_list, width=20)
        self.bg_selector_btn = Button(self,text="Set", command=lambda: messagebox.showinfo(title=self.appname,message=self.of.shop.set_background(self.bg_selector_cmb.current())))

    def shop_set_points(self):
        value = common_functions.intTryParse(self.new_points_box.get())
        if isinstance(value, int):
            try:
                self.of.shop.set_points(value)
                self.points_lbl.config(text=f"Please enter a value between 0 and 99999 and press enter\nCurrent points {value}")
                messagebox.showinfo(title=self.appname,message="Points set correctly")
            except ValueError as e:
                messagebox.showerror(title=self.appname,message=e)
        else:
            messagebox.showerror(title=self.appname,message="Please insert a number not a string")

    def publish(self):
        self.points_lbl.place(x=220, y=20)
        self.new_points_box.place(x = 320, y = 60)
        self.unlock_lock_lbl.place(x = 280, y = 100)
        self.unlock_shop_btn.place(x = 260, y = 130)
        self.lock_shop_btn.place(x = 360, y = 130)
        if self.of.shop.HAS_BG:
            self.bg_selector_cmb.current(self.of.shop.bg)
            self.bg_selector_lbl.place(x = 280, y = 170)
            self.bg_selector_cmb.place(x = 280, y = 200)
            self.bg_selector_btn.place(x = 340, y = 230)
