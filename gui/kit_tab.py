from tkinter import Frame,  ttk, LabelFrame, Label, IntVar, Spinbox, Button, StringVar, colorchooser
from tkinter.ttk import Combobox
from editor import Team
from editor.utils.constants import *
class KitTab(Frame):

    def __init__(self, master, team:Team, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.team = team
        self.appname = appname

        self.frame1 = ttk.Frame(self)
        self.frame1.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        self.kit_combox = Combobox(self.frame1, state="readonly", values=KIT_TYPES, )
        self.kit_combox.bind("<<ComboboxSelected>>", lambda _ : self.get_kit_info())
        self.kit_combox.set(KIT_TYPES[PA])
        self.kit_combox.grid(row=0, column=0, sticky="NWE")  
        frame_01 = LabelFrame(self, text="Menu")
        frame_01.grid(column=1, row=0, padx=5, pady=5, sticky="NWE")

        Label(frame_01, text="Option").grid(column=1, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Size").grid(column=2, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="X").grid(column=3, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Y").grid(column=4, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Type").grid(column=5, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Shirt Font").grid(column=0, row=1, padx=5, pady=5,  sticky="WE")
        
        self.front_shirt_cmb = ttk.Combobox(frame_01, values=OFF_ON,width=5,state="readonly")
        self.front_shirt_cmb.grid(column=1, row=1, padx=10, pady=5, sticky="W")
        
        self.font_size_spb_var = IntVar(self, 0)

        self.font_size_spb = Spinbox(frame_01,textvariable=self.font_size_spb_var, from_=0, to=30,  width=5)
        self.font_size_spb.grid(column=2, row=1, padx=10, pady=5, sticky="W")

        self.posc_font_x_var = IntVar(self, 0)
        posc_font_x = Spinbox(frame_01,textvariable=self.posc_font_x_var, from_=0, to=30, command=None, width=5)
        posc_font_x.grid(column=3, row=1, padx=10, pady=5, sticky="W")
        
        self.posc_font_y_var = IntVar(self, 0)
        posc_font_y_spb = Spinbox(frame_01,textvariable=self.posc_font_x_var, from_=0, to=30, command=None, width=5)
        posc_font_y_spb.grid(column=4, row=1, padx=10, pady=5, sticky="W")

        self.font_curve_cmb = ttk.Combobox(frame_01, values=FONT_CURVE,width=7,state="readonly")
        self.font_curve_cmb.grid(column=5, row=1, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Front Number").grid(column=0, row=2, padx=5, pady=5, sticky="WE")

        self.front_number_cmb = ttk.Combobox(frame_01, values=OFF_ON,width=5,state="readonly")
        self.front_number_cmb.grid(column=1, row=2, padx=10, pady=5, sticky="W")

        self.front_number_spb_size_var = IntVar(self, 0)

        front_number_size_spb = Spinbox(frame_01, textvariable=self.front_number_spb_size_var,  from_=0, to=22, width=5)
        front_number_size_spb.grid(column=2, row=2, padx=10, pady=5, sticky="W")

        self.x_posc_front_num_spb_var = IntVar(self, 0)

        x_posc_front_num_spb = Spinbox(frame_01, textvariable=self.x_posc_front_num_spb_var, from_=0, to=29,  width=5)
        x_posc_front_num_spb.grid(column=3, row=2, padx=10, pady=5, sticky="W")

        self.y_posc_front_num_spb_var = IntVar(self, 0)

        y_posc_front_num_spb = Spinbox(frame_01, textvariable=self.y_posc_front_num_spb_var, from_=0, to=29,   width=5)
        y_posc_front_num_spb.grid(column=4, row=2, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Back Number").grid(column=0, row=3, padx=5, pady=5, sticky="WE")

        self.b_number_size_var = IntVar(self, 0)

        b_number_size_spb = Spinbox(frame_01, textvariable=self.b_number_size_var, from_=0, to=31,   width=5)
        b_number_size_spb.grid(column=2, row=3, padx=10, pady=5, sticky="W")

        self.y_posc_num_back_spb_var = IntVar(self, 0)

        y_posc_num_back_spb = Spinbox(frame_01, textvariable=self.y_posc_num_back_spb_var, from_=0, to=18,   width=5)
        y_posc_num_back_spb.grid(column=4, row=3, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Short Number").grid(column=0, row=4, padx=5, pady=5, sticky="WE")

        self.short_number_pos_cmb = ttk.Combobox(frame_01, values=OFF_LEFT_RIGHT,width=5,state="readonly")
        self.short_number_pos_cmb.grid(column=1, row=4, padx=10, pady=5, sticky="W")

        self.short_number_size_var = IntVar(self, 0)

        short_number_size_spb = Spinbox(frame_01, textvariable=self.short_number_size_var, from_=0, to=28,   width=5)
        short_number_size_spb.grid(column=2, row=4, padx=10, pady=5, sticky="W")

        self.x_posc_short_num_spb_var = IntVar(self, 0)

        x_posc_short_num_spb = Spinbox(frame_01, textvariable=self.x_posc_short_num_spb_var, from_=0, to=25, width=5)
        x_posc_short_num_spb.grid(column=3, row=4, padx=10, pady=5, sticky="W")

        self.y_posc_short_num_spb_var = IntVar(self, 0)

        y_posc_short_num_spb = Spinbox(frame_01, textvariable=self.y_posc_short_num_spb_var, from_=0, to=19, width=5)
        y_posc_short_num_spb.grid(column=4, row=4, padx=10, pady=5, sticky="W")
        
        Label(frame_01, text="Overlay").grid(column=0, row=5, padx=5, pady=5, sticky="WE")

        self.overlay_spb_var = IntVar(self, 0)

        overlay_spb = Spinbox(frame_01,textvariable=self.overlay_spb_var, from_=0, to=14, width=5)
        overlay_spb.grid(column=1, row=5, padx=10, pady=5, sticky="W")

        self.posc_overlay_y_spb_var = IntVar(self, 0)

        posc_overlay_y_spb = Spinbox(frame_01,textvariable=self.posc_overlay_y_spb_var, from_=0, to=10, width=5)
        posc_overlay_y_spb.grid(column=4, row=5, padx=10, pady=5, sticky="W")
        
        Label(frame_01, text="Model").grid(column=0, row=6, padx=5, pady=5, sticky="WE")

        self.model_spb_var = IntVar(self, 0)

        model_spb = Spinbox(frame_01, textvariable=self.model_spb_var, from_=0, to=154, width=5)
        model_spb.grid(column=1, row=6, padx=10, pady=5, sticky="W")

        Label(frame_01, text="License").grid(column=0, row=7, padx=5, pady=5, sticky="WE")
    
        self.license_cmb = ttk.Combobox(frame_01, values=NO_YES,width=5,state="readonly")
        self.license_cmb.grid(column=1, row=7, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Radar Color").grid(column=0, row=8, padx=5, pady=5, sticky="WE")
        
        self.colors_rgb_var = StringVar(self, "")

        self.btn_radar_color = Button(
            frame_01,
            width=7, 
            textvariable=self.colors_rgb_var,
            command=self.select_color
        )
        self.btn_radar_color.grid(column=1, row=8, padx=10, pady=5, sticky="W")

        frame_02 = Frame(self, )
        frame_02.grid(column=1, row=1, padx=5, pady=5, sticky="W")

        apply_btn = ttk.Button(frame_02, text="Apply", command=lambda : self.set_kit_data())
        apply_btn.grid(column=0, row=0, padx=10, pady=5)

        cancel_btn = ttk.Button(frame_02, text="Close", command=lambda : self.master.master.stop_window())
        cancel_btn.grid(column=1, row=0, padx=10, pady=5)
        
        self.kit_combox.event_generate("<<ComboboxSelected>>")

    def select_color(self):
        colors = colorchooser.askcolor(parent = self, title="Select a radar color", initialcolor=self.colors_rgb_var.get())
        if colors[0] is None :
            return 0
        self.colors_rgb_var.set(colors[1])
        self.btn_radar_color.configure(bg=colors[1])

    def get_kit_info(self):
        
        kit_list = self.team.kits.kits

        kit_type = self.kit_combox.current()
        if kit_type == 0:
            kit = kit_list[kit_type]
        elif kit_type == 1:
            kit = kit_list[kit_type]
        elif kit_type == 2:
            kit = kit_list[kit_type]
        elif kit_type == 3:
            kit = kit_list[kit_type]

        self.license_cmb.set(kit.license)
        self.model_spb_var.set(kit.model)
        self.front_shirt_cmb.set(kit.font_shirt)
        self.front_number_cmb.set(kit.front_number)
        self.short_number_pos_cmb.set(kit.short_number)
        self.overlay_spb_var.set(kit.overlay)
        self.posc_overlay_y_spb_var.set(kit.posc_overlay_y)
        self.font_curve_cmb.set(kit.font_curve)
        self.font_size_spb_var.set(kit.font_size)
        self.b_number_size_var.set(kit.number_size_back)
        self.short_number_size_var.set(kit.short_number_size)
        self.front_number_spb_size_var.set(kit.front_number_size)
        self.y_posc_num_back_spb_var.set(kit.y_posc_num_back)
        self.x_posc_front_num_spb_var.set(kit.x_posc_front_num)
        self.y_posc_front_num_spb_var.set(kit.y_posc_front_num)
        self.x_posc_short_num_spb_var.set(kit.x_posc_short_number)
        self.y_posc_short_num_spb_var.set(kit.y_posc_short_number)
        self.btn_radar_color.configure(bg=kit.color_radar)
        self.colors_rgb_var.set(kit.color_radar)


    def set_kit_data(self):
        
        kit_list = self.team.kits.kits

        kit_type = self.kit_combox.current()
        if kit_type == GA:
            kit = kit_list[kit_type]
        elif kit_type == PA:
            kit = kit_list[kit_type]
        elif kit_type == GB:
            kit = kit_list[kit_type]
        elif kit_type == PB:
            kit = kit_list[kit_type]

        kit.model = self.model_spb_var.get()
        kit.font_shirt = self.front_shirt_cmb.get()
        kit.front_number = self.front_number_cmb.get()
        kit.short_number = self.short_number_pos_cmb.get()
        kit.overlay = self.overlay_spb_var.get()
        kit.posc_overlay_y = self.posc_overlay_y_spb_var.get()
        kit.font_curve = self.font_curve_cmb.get()
        kit.font_size = self.font_size_spb_var.get()
        kit.number_size_back = self.b_number_size_var.get()
        kit.short_number_size = self.short_number_size_var.get()
        kit.front_number_size = self.front_number_spb_size_var.get()
        kit.y_posc_num_back = self.y_posc_num_back_spb_var.get()
        kit.x_posc_front_num = self.x_posc_front_num_spb_var.get()
        kit.y_posc_front_num = self.y_posc_front_num_spb_var.get()
        kit.x_posc_short_number = self.x_posc_short_num_spb_var.get()
        kit.y_posc_short_number = self.y_posc_short_num_spb_var.get()
        kit.color_radar = self.colors_rgb_var.get()

        # license has to be updated on the four set of kits
        for kit in kit_list:
            kit.license = self.license_cmb.get()

        self.team.kits.update_data()
