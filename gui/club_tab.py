from tkinter import Entry, Frame, Label, Listbox, Scrollbar, StringVar, colorchooser, messagebox, Button, TclError
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from editor import OptionFile
from editor import common_functions
from editor.utils.constants import *

class ClubTab(Frame):
    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.clubs_list_box = Listbox(self, height = 31, width = 30, exportselection=False)
        self.clubs_list_box.bind('<<ListboxSelect>>',lambda _ : self.set_club_data())
        self.clubs_list_box.delete(0,'end')
        self.clubs_list_box.insert('end',*self.of.clubs_names)
        self.clubs_list_box_sb = Scrollbar(self, orient="vertical") 
        self.clubs_list_box_sb.config(command = self.clubs_list_box.yview)
        self.clubs_list_box.config(yscrollcommand = self.clubs_list_box_sb.set)
        self.clubs_list_box.select_set(0)
        self.clubs_id_var = StringVar()
        self.clubs_id_label = Label(self,text="Club ID")
        self.clubs_id_box = Entry(self, width=3, state="readonly", textvariable=self.clubs_id_var)
        self.clubs_name_lbl = Label(self,text="Club name")
        self.clubs_box = Entry(self, width=30)
        self.clubs_abbr_box = Entry(self, width=15)
        self.clubs_stad_lbl = Label(self,text="Home stadium")
        self.clubs_stad_cmb = Combobox(self, state="readonly", value=self.of.stadiums_names, width=30)
        self.clubs_flag_lbl = Label(self,text="Flag")
        self.clubs_flag_img_lbl = Label(self,borderwidth=2, relief="solid")
        self.clubs_flag_cmb = Combobox(self, state="readonly", value=[f"Flag Background {i}" for i in range(12)], width=30)
        self.clubs_flag_cmb.bind('<<ComboboxSelected>>', lambda _: self.update_flag_lbl())
        self.clubs_color1_btn = Button(self, height=2, width=5, command=lambda: self.update_color1_btn())
        self.clubs_color2_btn = Button(self, height=2, width=5, command=lambda: self.update_color2_btn())

        self.clubs_supp_lbl = Label(self, text="Color Supporter")
        self.clubs_sup_c1_lbl = Label(self, height=2, width=5)
        self.clubs_sup_c1_cmb = Combobox(self, state="readonly", value=SUPP_COLOURS, width=10)
        self.clubs_sup_c1_cmb.bind('<<ComboboxSelected>>', lambda _: self.update_color_supp("c1", self.clubs_sup_c1_cmb.current()))
        self.clubs_sup_c2_lbl = Label(self, height=2, width=5)
        self.clubs_sup_c2_cmb = Combobox(self, state="readonly", value=SUPP_COLOURS, width=10)
        self.clubs_sup_c2_cmb.bind('<<ComboboxSelected>>', lambda event: self.update_color_supp("c2", self.clubs_sup_c2_cmb.current()))
        self.clubs_apply_btn = Button(self, text="Apply", command=lambda: self.update_club_val())
        self.clubs_discard_btn = Button(self, text="Discard", command=lambda: self.set_club_data())
        

    def update_color_supp(self, color_order, color_index):
        color = SUPP_COLOURs_HEX[color_index]
        if color_order=="c1":
            self.clubs_sup_c1_lbl.configure(background=color)
        elif color_order=="c2":
            self.clubs_sup_c2_lbl.configure(background=color)
        else:
            raise ValueError

    def update_club_val(self):
        try:
            #club_id = self.clubs_list_box.get(0, "end").index(self.clubs_list_box.get(self.clubs_list_box.curselection()))
            club_id = self.clubs_list_box.curselection()[0]
            self.of.clubs[club_id].update_name(self.clubs_box.get())
            self.of.clubs[club_id].update_abbr(self.clubs_abbr_box.get())
            self.of.clubs[club_id].update_stadium(self.clubs_stad_cmb.current())
            self.of.clubs[club_id].update_flag(self.clubs_flag_cmb.current())
            self.of.clubs[club_id].update_color1(common_functions.hex_to_rgb(self.clubs_color1_btn['bg']))
            self.of.clubs[club_id].update_color2(common_functions.hex_to_rgb(self.clubs_color2_btn['bg']))
            self.of.clubs[club_id].update_supp_color(self.clubs_sup_c1_cmb.current(), self.clubs_sup_c2_cmb.current())
            self.refresh_gui(club_id)
        except TclError as e:
            messagebox.showerror(
                self.appname,
                message=f"You must select an item from the widget\nError code: {e}"
            )

    def update_color1_btn(self):
        my_color = colorchooser.askcolor()
        self.clubs_color1_btn.configure(bg=my_color[1])
        self.update_flag_lbl()

    def update_color2_btn(self):
        my_color = colorchooser.askcolor()
        self.clubs_color2_btn.configure(bg=my_color[1])
        self.update_flag_lbl()

    def update_flag_lbl(self):
        flag_id = str(self.clubs_flag_cmb.current())
        img = (Image.open(common_functions.resource_path("resources/img/backflag" + flag_id + ".png")).convert('RGB'))
        width = img.size[0]
        height = img.size[1]
        for i in range(0,width):# process all pixels
            for j in range(0,height):
                data = img.getpixel((i,j))
                if (data[0]==0 and data[1]==0 and data[2]==0):
                    img.putpixel((i,j),tuple(common_functions.hex_to_rgb(self.clubs_color1_btn['bg'])))
                elif (data[0]==255 and data[1]==255 and data[2]==255):
                    img.putpixel((i,j),tuple(common_functions.hex_to_rgb(self.clubs_color2_btn['bg'])))
        img = ImageTk.PhotoImage(img)
        self.clubs_flag_img_lbl.configure(image=img)
        self.clubs_flag_img_lbl.image =img

    def set_club_data(self):
        # set the name to the entry box
        club_id = self.clubs_list_box.get(0, "end").index(self.clubs_list_box.get(self.clubs_list_box.curselection()))
        self.clubs_id_var.set(str(club_id))
        self.clubs_box.delete(0,'end')
        self.clubs_box.insert(0,self.clubs_list_box.get(self.clubs_list_box.curselection()))
        # set the abbr name to the entry box
        self.clubs_abbr_box.delete(0,'end')
        self.clubs_abbr_box.insert(0,self.of.clubs[club_id].abbr)
        # set the stadium
        self.clubs_stad_cmb.current(self.of.clubs[club_id].stadium)
        # set flag style
        self.clubs_flag_cmb.current(self.of.clubs[club_id].flag_style)
        # set colours into the buttons
        self.clubs_color1_btn.configure(bg=self.of.clubs[club_id].color1)
        self.clubs_color2_btn.configure(bg=self.of.clubs[club_id].color2)
        # Set the flag style and colours
        self.update_flag_lbl()
        # set colours into the labels
        self.update_color_supp("c1",self.of.clubs[club_id].supp_color_c1)
        self.update_color_supp("c2",self.of.clubs[club_id].supp_color_c2)
        # set the selected colour in combo box
        self.clubs_sup_c1_cmb.current(self.of.clubs[club_id].supp_color_c1)
        self.clubs_sup_c2_cmb.current(self.of.clubs[club_id].supp_color_c2)

    def refresh_gui(self,item_idx=None):
        """
        Updates every gui element that use the teamlist 
        """
        self.clubs_list_box.delete(0,'end')
        self.clubs_list_box.insert('end',*self.of.clubs_names)
        self.clubs_stad_cmb['value'] = self.of.stadiums_names
        if item_idx!=None:
            # After we clic on the button we lost the item selection so with this we solve it
            self.clubs_list_box.select_set(item_idx)
        else:
            self.clubs_list_box.select_set(0)
            self.clubs_list_box.event_generate("<<ListboxSelect>>")

    def publish(self):
        self.clubs_id_label.place(x=210, y=10)
        self.clubs_id_box.place(x=255, y=10)
        self.clubs_list_box.place(x=5, y=20)
        self.clubs_list_box_sb.place(x = 190, y = 20 , height = 500)
        self.clubs_name_lbl.place(x=210, y=30)
        self.clubs_box.place(x=210, y=50)
        self.clubs_abbr_box.place(x=210, y=80)
        self.clubs_stad_lbl.place(x=210, y=100)
        self.clubs_stad_cmb.place(x=210, y=120)
        self.clubs_flag_lbl.place(x=210, y=150)
        self.clubs_flag_img_lbl.place(x=210, y=170)
        self.clubs_flag_cmb.place(x=210, y=240)
        self.clubs_color1_btn.place(x=210, y=270)
        self.clubs_color2_btn.place(x=265, y=270)
        self.clubs_supp_lbl.place(x=220, y=315)
        self.clubs_sup_c1_lbl.place(x=225, y=340)
        self.clubs_sup_c1_cmb.place(x=210, y=380)
        self.clubs_sup_c2_lbl.place(x=315, y=340)
        self.clubs_sup_c2_cmb.place(x=300, y=380)
        self.clubs_apply_btn.place(x=245, y=420)
        self.clubs_discard_btn.place(x=305, y=420)
