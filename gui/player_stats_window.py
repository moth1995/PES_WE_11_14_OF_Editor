from pathlib import Path
import time
from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label, LabelFrame, Spinbox, Toplevel, filedialog, messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

from editor import Player, common_functions
from editor.utils.constants import *
from .psd import PSD

class PlayerStatsWindow(Toplevel):
    psd = PSD()

    def __init__(self, master, player:Player, nations):
        Toplevel.__init__(self, master)
        w = 870 # width for the Tk root
        h = 750 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.title("%s Player Stats: %s" % (master.appname, player.name))
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.appname = master.appname

        self.has_face_hair_folder = master.has_face_hair_folder
        self.face_hair_folder = master.face_hair_folder
        self.face_hair_version = master.face_hair_version
        self.faces_location = master.faces_location
        self.hairs_location = master.hairs_location
        self.last_working_dir = master.master.master.last_working_dir
        
        frame_container_0 = Frame(self,)
        frame_container_1 = Frame(self,)
        frame_container_2 = Frame(self,)
        frame_container_3 = Frame(self,)
        frame_container_0.pack(side="left", anchor="n", pady=10, )
        frame_container_1.pack(side="left", anchor="n", pady=10, padx=2)
        frame_container_2.pack(side="left", anchor="n", pady=10, padx=2)
        frame_container_3.pack(side="left", anchor="n", pady=10, padx=2)
        
        player_basic_settings_frame = LabelFrame(frame_container_0, text="Basic Settings")
        player_appearance_label_frame = LabelFrame(frame_container_0, text="Quick Appearance Menu")
        player_abilities_frame = LabelFrame(frame_container_1, text="Abilities")
        player_special_abilities_frame = LabelFrame(frame_container_2, text="Special Abilities")
        player_position_frame = LabelFrame(frame_container_3, text="Position")
        player_physical_frame = LabelFrame(frame_container_3, text="Physique")
        player_face_hair_preview_frame = LabelFrame(frame_container_3, text="Face/Hair Preview")
        control_buttons_frame = Frame(frame_container_0,)
        
        player_basic_settings_frame.pack(anchor="n", ipadx=2, ipady=2)
        player_appearance_label_frame.pack(anchor="n", pady=20, ipadx=2, ipady=2)
        control_buttons_frame.pack(anchor="n", pady=20, ipadx=2, ipady=2)
        
        player_abilities_frame.pack(ipadx=2, ipady=2)
        
        player_special_abilities_frame.pack(ipadx=2, ipady=2)
        
        player_position_frame.pack(anchor="n", ipadx=2, ipady=2)
        player_physical_frame.pack(anchor="nw")
        player_face_hair_preview_frame.pack(anchor="nw", ipadx=2, ipady=2)


        self.star_on = Image.open(common_functions.resource_path("resources/img/star_on.png"))
        self.star_off = Image.open(common_functions.resource_path("resources/img/star_off.png"))
        self.special_abilities_img_on = ImageTk.PhotoImage(self.star_on)
        self.special_abilities_img_off = ImageTk.PhotoImage(self.star_off)
        self.no_face_preview = Image.open(common_functions.resource_path("resources/img/no_face_preview.png"))
        self.no_hair_preview = Image.open(common_functions.resource_path("resources/img/no_hair_preview.png"))
        self.no_face_img = ImageTk.PhotoImage(self.no_face_preview)
        self.no_hair_img = ImageTk.PhotoImage(self.no_hair_preview)
        
        player_idx_label = Label(player_basic_settings_frame, text="Player ID")
        player_idx_label.grid(row=0, column=0, sticky="e")
        self.player_idx_entry = Entry(player_basic_settings_frame, width=6)
        self.player_idx_entry.delete(0,'end')
        self.player_idx_entry.insert(0,player.idx)
        self.player_idx_entry.configure(state="disabled")
        self.player_idx_entry.grid(row=0, column=1, sticky="w")

        player_name_label = Label(player_basic_settings_frame, text="Player Name")
        player_name_label.grid(row=1, column=0, sticky="e")
        self.player_name_entry = Entry(player_basic_settings_frame, width=20)
        self.player_name_entry.focus_force()
        self.player_name_entry.delete(0,'end')
        self.player_name_entry.insert(0,player.name)
        self.player_name_entry.grid(row=1, column=1, sticky="w")

        player_shirt_name_label = Label(player_basic_settings_frame, text="Player Shirt Name")
        player_shirt_name_label.grid(row=2, column=0, sticky="e")
        self.player_shirt_name_entry = Entry(player_basic_settings_frame, width=20)
        self.player_shirt_name_entry.delete(0,'end')
        self.player_shirt_name_entry.insert(0,player.shirt_name)
        self.player_shirt_name_entry.grid(row=2, column=1, sticky="w")

        player_callname_label = Label(player_basic_settings_frame, text=player.callname.name)
        player_callname_label.grid(row=3, column=0, sticky="e")
        self.player_callname_entry = Entry(player_basic_settings_frame, width=6)
        self.player_callname_entry.delete(0,'end')
        self.player_callname_entry.insert(0,player.callname())
        self.player_callname_entry.grid(row=3, column=1, sticky="w")

        player_nationality_label = Label(player_basic_settings_frame, text=player.nation.name)
        player_nationality_label.grid(row=4, column=0, sticky="e")
        self.player_nationality_combobox = Combobox(player_basic_settings_frame, state="readonly", value=nations, width=20)
        self.player_nationality_combobox.set(player.nation())
        self.player_nationality_combobox.grid(row=4, column=1, sticky="w")

        player_age_label = Label(player_basic_settings_frame, text=player.basic_settings.age.name)
        player_age_label.grid(row=5, column=0, sticky="e")
        self.player_age_int_var = IntVar(player_basic_settings_frame, player.basic_settings.age())
        player_age_spinbox = Spinbox(player_basic_settings_frame, from_= 15, to = 46, textvariable=self.player_age_int_var, width = 5)
        player_age_spinbox.grid(row=5, column=1, sticky="w")

        player_stronger_foot_label = Label(player_basic_settings_frame, text=player.basic_settings.stronger_foot.name)
        player_stronger_foot_label.grid(row=6, column=0, sticky="e")
        self.player_stronger_foot_combobox = Combobox(player_basic_settings_frame, state="readonly", value=FOOT_FAV_SIDE[:2], width=20)
        self.player_stronger_foot_combobox.set(player.basic_settings.stronger_foot())
        self.player_stronger_foot_combobox.grid(row=6, column=1, sticky="w")

        player_injury_label = Label(player_basic_settings_frame, text=player.basic_settings.injury.name)
        player_injury_label.grid(row=7, column=0, sticky="e")
        self.player_injury_combobox = Combobox(player_basic_settings_frame, state="readonly", value=INJURY_VALUES, width=20)
        self.player_injury_combobox.set(player.basic_settings.injury())
        self.player_injury_combobox.grid(row=7, column=1, sticky="w")

        player_style_of_dribble_label = Label(player_basic_settings_frame, text=player.basic_settings.style_of_dribble.name)
        player_style_of_dribble_label.grid(row=8, column=0, sticky="e")
        self.player_style_of_dribble_combobox = Combobox(player_basic_settings_frame, state="readonly", value=list(range(1,5)), width=20)
        self.player_style_of_dribble_combobox.set(player.basic_settings.style_of_dribble())
        self.player_style_of_dribble_combobox.grid(row=8, column=1, sticky="w")

        player_free_kick_type_label = Label(player_basic_settings_frame, text=player.basic_settings.free_kick_type.name)
        player_free_kick_type_label.grid(row=9, column=0, sticky="e")
        self.player_free_kick_type_combobox = Combobox(player_basic_settings_frame, state="readonly", value=list(range(1,17)), width=20)
        self.player_free_kick_type_combobox.set(player.basic_settings.free_kick_type())
        self.player_free_kick_type_combobox.grid(row=9, column=1, sticky="w")

        player_penalty_kick_label = Label(player_basic_settings_frame, text=player.basic_settings.penalty_kick.name)
        player_penalty_kick_label.grid(row=10, column=0, sticky="e")
        self.player_penalty_kick_combobox = Combobox(player_basic_settings_frame, state="readonly", value=list(range(1,9)), width=20)
        self.player_penalty_kick_combobox.set(player.basic_settings.penalty_kick())
        self.player_penalty_kick_combobox.grid(row=10, column=1, sticky="w")

        player_drop_kick_style_label = Label(player_basic_settings_frame, text=player.basic_settings.drop_kick_style.name)
        player_drop_kick_style_label.grid(row=11, column=0, sticky="e")
        self.player_drop_kick_style_combobox = Combobox(player_basic_settings_frame, state="readonly", value=list(range(1,5)), width=20)
        self.player_drop_kick_style_combobox.set(player.basic_settings.drop_kick_style())
        self.player_drop_kick_style_combobox.grid(row=11, column=1, sticky="w")

        player_goal_celebration_1_label = Label(player_basic_settings_frame, text=player.basic_settings.goal_celebration_1.name)
        player_goal_celebration_1_label.grid(row=12, column=0, sticky="e")
        self.player_goal_celebration_1_combobox = Combobox(player_basic_settings_frame, state="readonly", value=["No"] + list(range(1,128)), width=20)
        self.player_goal_celebration_1_combobox.current(player.basic_settings.goal_celebration_1())
        self.player_goal_celebration_1_combobox.grid(row=12, column=1, sticky="w")

        player_goal_celebration_2_label = Label(player_basic_settings_frame, text=player.basic_settings.goal_celebration_2.name)
        player_goal_celebration_2_label.grid(row=13, column=0, sticky="e")
        self.player_goal_celebration_2_combobox = Combobox(player_basic_settings_frame, state="readonly", value=["No"] + list(range(1,128)), width=20)
        self.player_goal_celebration_2_combobox.current(player.basic_settings.goal_celebration_2())
        self.player_goal_celebration_2_combobox.grid(row=13, column=1, sticky="w")

        player_growth_type_label = Label(player_basic_settings_frame, text=player.basic_settings.growth_type.name)
        player_growth_type_label.grid(row=14, column=0, sticky="e")
        self.player_growth_type_combobox = Combobox(player_basic_settings_frame, state="readonly", value=GROWTH_TYPE_NAMES, width=20)
        self.player_growth_type_combobox.grid(row=14, column=1, sticky="w")

        player_unknown_growth_type_label = Label(player_basic_settings_frame, text="%s value" % player.basic_settings.growth_type.name)
        player_unknown_growth_type_label.grid(row=15, column=0, sticky="e")
        player_growth_type_value_var = IntVar(player_basic_settings_frame, player.basic_settings.growth_type())
        player_unknown_growth_type_entry = Entry(player_basic_settings_frame, width=6, textvariable=player_growth_type_value_var)
        player_unknown_growth_type_entry.grid(row=15, column=1, sticky="w")
        player_unknown_growth_type_entry.config(state="readonly")

        self.player_growth_type_combobox.set(player.basic_settings.growth_type.get_growth_type_name())
        #self.player_growth_type_combobox.event_generate("<<ComboboxSelected>>")
        self.player_growth_type_combobox.bind(
            "<<ComboboxSelected>>", lambda _ : player_growth_type_value_var.set(player.basic_settings.growth_type.get_growth_type_value(self.player_growth_type_combobox.get()))
        )

        #player_appearance_label = Label(self, text="Quick Appearance Menu")
        #player_appearance_label.grid(row=16, column=0, sticky="nwse", columnspan=2)

        player_height_label = Label(player_appearance_label_frame, text=player.appearance.height.name)
        player_height_label.grid(row=17, column=0, sticky="e")
        self.player_height_entry = Entry(player_appearance_label_frame, width=6)
        self.player_height_entry.delete(0,'end')
        self.player_height_entry.insert(0,player.appearance.height())
        self.player_height_entry.grid(row=17, column=1, sticky="w")

        player_weight_label = Label(player_appearance_label_frame, text=player.appearance.weight.name)
        player_weight_label.grid(row=18, column=0, sticky="e")
        self.player_weight_entry = Entry(player_appearance_label_frame, width=6)
        self.player_weight_entry.delete(0,'end')
        self.player_weight_entry.insert(0,player.appearance.weight())
        self.player_weight_entry.grid(row=18, column=1, sticky="w")

        player_face_label = Label(player_appearance_label_frame, text=player.appearance.face.name)
        player_face_label.grid(row=19, column=0, sticky="e")
        self.player_face_combobox = Combobox(player_appearance_label_frame, state="readonly", value=FACE_TYPE, width=20)
        self.player_face_combobox.set(player.appearance.face())
        self.player_face_combobox.grid(row=19, column=1, sticky="w")

        player_skin_colour_label = Label(player_appearance_label_frame, text=player.appearance.skin_colour.name)
        player_skin_colour_label.grid(row=20, column=0, sticky="e")
        self.player_skin_colour_combobox = Combobox(player_appearance_label_frame, state="readonly", value=list(range(1,7)), width=20)
        self.player_skin_colour_combobox.set(player.appearance.skin_colour())
        self.player_skin_colour_combobox.grid(row=20, column=1, sticky="w")

        player_head_height_label = Label(player_appearance_label_frame, text=player.appearance.head_height.name)
        player_head_height_label.grid(row=21, column=0, sticky="e")
        self.player_head_height_int_var = IntVar(player_appearance_label_frame, player.appearance.head_height())
        player_head_height_spinbox = Spinbox(player_appearance_label_frame, from_= -7, to = 7, textvariable=self.player_head_height_int_var, width = 5)
        player_head_height_spinbox.grid(row=21, column=1, sticky="w")

        player_head_width_label = Label(player_appearance_label_frame, text=player.appearance.head_width.name)
        player_head_width_label.grid(row=22, column=0, sticky="e")
        self.player_head_width_int_var = IntVar(player_appearance_label_frame, player.appearance.head_width())
        player_head_width_spinbox = Spinbox(player_appearance_label_frame, from_= -7, to = 7, textvariable=self.player_head_width_int_var, width = 5)
        player_head_width_spinbox.grid(row=22, column=1, sticky="w")

        player_face_idx_label = Label(player_appearance_label_frame, text=player.appearance.face_idx.name)
        player_face_idx_label.grid(row=23, column=0, sticky="e")
        self.player_face_idx_int_var = IntVar(player_appearance_label_frame, player.appearance.face_idx())
        self.player_face_idx_spinbox = Spinbox(player_appearance_label_frame, from_= MIN_FACE_IDX, to = MAX_FACE_IDX, textvariable=self.player_face_idx_int_var, width = 5)
        self.player_face_idx_spinbox.grid(row=23, column=1, sticky="w")

        player_hair_idx_label = Label(player_appearance_label_frame, text=player.appearance.hair.name)
        player_hair_idx_label.grid(row=24, column=0, sticky="e")
        self.player_hair_idx_int_var = IntVar(player_appearance_label_frame, player.appearance.hair())
        self.player_hair_idx_spinbox = Spinbox(player_appearance_label_frame, from_= MIN_HAIR_IDX, to = MAX_HAIR_IDX, textvariable=self.player_hair_idx_int_var, width = 5)
        self.player_hair_idx_spinbox.grid(row=24, column=1, sticky="w")

        #self.player_hair_idx_entry = Entry(self, width=6)
        #self.player_hair_idx_entry.delete(0,'end')
        #self.player_hair_idx_entry.insert(0,player.appearance.hair())
        #self.player_hair_idx_entry.grid(row=24, column=1, sticky="w")

        player_special_hairstyles_2_label = Label(player_appearance_label_frame, text=player.appearance.special_hairstyles_2.name)
        player_special_hairstyles_2_label.grid(row=25, column=0, sticky="e")
        self.player_special_hairstyles_2_var = IntVar(player_appearance_label_frame, NO_YES.index(player.appearance.special_hairstyles_2()))
        self.player_special_hairstyles_2_chk_btn = Checkbutton(
            player_appearance_label_frame, 
            variable=self.player_special_hairstyles_2_var, 
            command=lambda : self.toggle_appearance_menu(2),
        )
        self.player_special_hairstyles_2_chk_btn.grid(row=25, column=1, sticky="w")

        self.face_preview_lbl = Label(player_face_hair_preview_frame, relief="solid", width=128, height=128, bg="SystemWindow", image=self.no_face_img)
        self.face_preview_lbl.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        self.hair_preview_lbl = Label(player_face_hair_preview_frame, relief="solid", width=128, height=128, bg="SystemWindow", image=self.no_hair_img)
        self.hair_preview_lbl.grid(row=0, column=1, sticky="ne", padx=5, pady=5)
        self.import_new_face_bin_btn = Button(
            player_face_hair_preview_frame, 
            text = "Replace Face", 
            command= lambda: self.import_face_hair_file(self.faces_location[self.player_face_idx_int_var.get() - 1])
        )
        self.import_new_face_bin_btn.grid(row=1, column=0, padx=5, pady=5)
        self.import_new_hair_bin_btn = Button(
            player_face_hair_preview_frame, 
            text = "Replace Hair",
            command= lambda: self.import_face_hair_file(self.hairs_location[self.player_face_idx_int_var.get() - 1])
        )
        self.import_new_hair_bin_btn.grid(row=1, column=1, padx=5, pady=5)


        # Setting the logic for when we select face = build and special hairstyles 2 trigger
        self.player_face_combobox.bind(
            "<<ComboboxSelected>>", 
            lambda _ : self.toggle_appearance_menu(0) if self.player_face_combobox.get() ==FACE_TYPE[BUILD] else self.toggle_appearance_menu(1)
        )
        self.player_face_combobox.event_generate("<<ComboboxSelected>>")
        #self.toggle_appearance_menu(2)
        self.player_face_idx_int_var.trace_add("write", self.face_idx_var_tracer)


        """
        player_hair_type_label = Label(self, text="Hair Type")
        player_hair_type_label.grid(row=22, column=0, sticky="e")
        self.player_hair_type_combobox = Combobox(
            self, 
            state="readonly", 
            value=[
                "BALD", "BUZZ CUT", "VERY SHORT 1", "VERY SHORT 2", 
                "STRAIGHT 1", "STRAIGHT 2", "CURLY 1", "CURLY 2", 
                "PONYTAIL 1", "PONYTAIL 2", "DREADLOCKS", "PULLED BACK", 
                "SPECIAL HAIRSTYLES",
            ],
            width=20
        )
        self.player_hair_type_combobox.bind('<<ComboboxSelected>>', lambda event: self.hairstyle_options(player))
        self.player_hair_type_combobox.set(player.appearance.hair()[0])
        self.player_hair_type_combobox.event_generate('<<ComboboxSelected>>')
        self.player_hair_type_combobox.grid(row=22, column=1, sticky="w")
        """

        apply_button = Button(control_buttons_frame, text="Apply", command=lambda: self.update_player_data(player))
        apply_button.grid(row=29, column=0, sticky="e")
        cancel_button = Button(control_buttons_frame, text="Cancel", command=lambda :self.stop_window())
        cancel_button.grid(row=29, column=1, sticky="w")
        psd_button = Button(control_buttons_frame, text = "PSD Paste", command= lambda : self.psd.paste_psd(self, self.selection_get(selection = "CLIPBOARD"), nations))
        psd_button.grid(row=30, column=0, sticky="e")
        psd_button = Button(control_buttons_frame, text = "PSD Copy", command= lambda : self.to_clipboard())
        psd_button.grid(row=30, column=1, sticky="w")

        """
        self.test_var = IntVar(self, 99)
        self.test = Entry(self, textvariable=self.test_var,)
        self.abilities_entry_tracer(self.test_var, self.test)
        self.test_var.trace_add("write", lambda *_,var = self.test_var, entry =  self.test: self.abilities_entry_tracer(var,entry))
        self.test.grid(row=26, column=1, sticky="w")
        

        column_2_row_counter = 0
        self.abilities_entries = {}
        for ability in player.abilities:

            lb = Label(self, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            e = Entry(self, width=3)
            e.delete(0, 'end')
            e.insert(0, ability())
            e.grid(row=column_2_row_counter, column=3, sticky="e")
            self.abilities_entries[ability.name] = e

            column_2_row_counter+=1
        """
        
        column_2_row_counter = 0
        self.abilities_entries = {}
        for ability in player.abilities:

            lb = Label(player_abilities_frame, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            self.abilities_entries[ability.name]=IntVar(self, ability())
            e = Entry(
                player_abilities_frame, 
                width=3,
                textvariable=self.abilities_entries[ability.name],
            )
            e.grid(row=column_2_row_counter, column=3, sticky="e")
            ## set the tracer to the variable
            self.abilities_entries[ability.name].trace_add(
                "write", 
                lambda *_, var = self.abilities_entries[ability.name], entry =  e: 
                    self.abilities_entry_tracer(var,entry)
            )
            ## apply the right colour
            self.abilities_entry_tracer(self.abilities_entries[ability.name], e)
            column_2_row_counter+=1

        """
        self.abilities_1_8_entries = {}

        for ability in player.abilities_1_8:

            lb = Label(self, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            e = Entry(self, width=3)
            e.delete(0,'end')
            e.insert(0,ability())
            e.grid(row=column_2_row_counter, column=3, sticky="e")
            self.abilities_1_8_entries[ability.name] = e

            column_2_row_counter+=1
        """
        self.abilities_1_8_entries = {}

        for ability in player.abilities_1_8:

            lb = Label(player_abilities_frame, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            self.abilities_1_8_entries[ability.name]=IntVar(self, ability())

            e = Entry(player_abilities_frame, width=3, textvariable=self.abilities_1_8_entries[ability.name])
            e.grid(row=column_2_row_counter, column=3, sticky="e")

            ## set the tracer to the variable
            self.abilities_1_8_entries[ability.name].trace_add(
                "write", 
                lambda *_, var = self.abilities_1_8_entries[ability.name], entry =  e: 
                    self.abilities_1_8_entry_tracer(var,entry)
            )
            ## apply the right colour
            self.abilities_1_8_entry_tracer(self.abilities_1_8_entries[ability.name], e)

            column_2_row_counter+=1


        column_4_row_counter = 0
        self.special_abilities_status_var = {}
        for special_ability in player.special_abilities:

            lb = Label(player_special_abilities_frame, text=special_ability.name)
            lb.grid(row=column_4_row_counter, column=4, sticky="e")

            self.special_abilities_status_var[special_ability.name]=IntVar(self, special_ability())
            chk = Checkbutton(
                player_special_abilities_frame, 
                variable = self.special_abilities_status_var[special_ability.name],
                image = self.special_abilities_img_off,
                selectimage = self.special_abilities_img_on,
                indicatoron = False,
                highlightthickness = 0,
                bd = 0,                
            )
            chk.grid(row=column_4_row_counter, column=5, sticky="e")
            column_4_row_counter+=1

        player_favored_side_label = Label(player_position_frame, text=player.position.favored_side.name)
        player_favored_side_label.grid(row=5, column=6, sticky="e")
        self.player_favored_side_combobox = Combobox(player_position_frame, state="readonly", value=FOOT_FAV_SIDE, width=20)
        self.player_favored_side_combobox.set(player.position.favored_side())
        self.player_favored_side_combobox.grid(row=5, column=7, sticky="w")

        player_registered_position_label = Label(player_position_frame, text=player.position.registered_position.name)
        player_registered_position_label.grid(row=6, column=6, sticky="e")
        self.player_registered_position_combobox = Combobox(
            player_position_frame, 
            state="readonly", 
            value=[
                position.name 
                for i, position in enumerate(player.position)
                if i > 1
            ],
            width=25,
        )
        self.player_registered_position_combobox.current(player.position.registered_position())
        self.player_registered_position_combobox.grid(row=6, column=7, sticky="w")

        column_6_row_counter = 7
        self.positions_status_var = {}
        for i, position in enumerate(player.position):
            if i > 1:
                lb = Label(player_position_frame, text=position.name)
                lb.grid(row=column_6_row_counter, column=6, sticky="e")

                self.positions_status_var[position.name]=IntVar(player_position_frame, position())
                chk = Checkbutton(player_position_frame, variable=self.positions_status_var[position.name])

                chk.grid(row=column_6_row_counter, column=7, sticky="nsew")
                column_6_row_counter+=1

        physique_type_lbl = Label(player_physical_frame, text="Physique")
        physique_type_lbl.grid(row=0, column=0, sticky="e", columnspan=2)
        self.physique_type_cmb = Combobox(player_physical_frame, state="readonly", values=BODY_TYPES)
        self.physique_type_cmb.grid(row=0, column=2, sticky="w", columnspan=2)
        self.physique_type_cmb.set(player.appearance.body_type)
        self.physique_type_cmb.bind("<<ComboboxSelected>>", lambda _ : self.set_body_parameters(self.physique_type_cmb.get()))
        
        body_parameters_row_counter = 1
        self.body_parameters = {}
        for i, body_parameter in enumerate(player.appearance.body_parameters):
            if i==5:
                body_parameters_row_counter = 1
            lb = Label(player_physical_frame, text=body_parameter.name)
            lb.grid(row=body_parameters_row_counter, column=0 if i<5 else 2, sticky="e")

            self.body_parameters[body_parameter.name]=IntVar(self, body_parameter())
            e = Spinbox(
                player_physical_frame, 
                width=3,
                textvariable=self.body_parameters[body_parameter.name],
                from_= -7, 
                to = 7,
            )
            e.grid(row=body_parameters_row_counter, column=1 if i<5 else 3, sticky="w")
            ## set the tracer to the variable
            self.body_parameters[body_parameter.name].trace_add(
                "write", 
                self.body_type_tracer
            )
            body_parameters_row_counter+=1


        self.lift()
        self.grab_set()
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.stop_window)

    def body_type_tracer(self, var:str, index:int, mode:str):
        try:
            new_body_parameters = tuple(body_parameter.get() for body_parameter in self.body_parameters.values())
            if new_body_parameters in BODY_TYPES_VALUES:
                self.physique_type_cmb.set(BODY_TYPES[BODY_TYPES_VALUES.index(new_body_parameters)])
            else:
                self.physique_type_cmb.set("Edit")
        except:
            pass

    def set_body_parameters(self, selected_option):
        print(selected_option)
        if selected_option in BODY_TYPES[:-1]:
            new_body_parameters = BODY_TYPES_VALUES[BODY_TYPES.index(selected_option)]
            for i, body_parameter in enumerate(self.body_parameters.values()):
                body_parameter.set(new_body_parameters[i])


    def to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.psd.copy_psd(self))

        self.update()
        time.sleep(.2)
        self.update()

    def face_idx_var_tracer(self, var:str, index:int, mode:str):
        try:
            if self.player_special_hairstyles_2_var.get() and self.player_face_idx_int_var.get():
                self.player_hair_idx_int_var.set(self.player_face_idx_int_var.get())
                if (
                    self.has_face_hair_folder and 
                    self.face_hair_folder !="" and 
                    self.face_hair_version !=-1 and 
                    self.player_face_idx_int_var.get() - 1<= len(self.faces_location) and
                    self.player_face_idx_int_var.get() - 1<= len(self.hairs_location)
                ):
                    self.face_img = common_functions.get_face_texture(self.faces_location[self.player_face_idx_int_var.get() - 1])
                    self.hair_img = common_functions.get_hair_texture(self.hairs_location[self.player_face_idx_int_var.get() - 1])
                    self.face_preview_lbl.config(
                        image=self.face_img, 
                        relief="solid", 
                        width=128, 
                        height=128,
                        bg="SystemWindow",
                    )
                    self.hair_preview_lbl.config(
                        image=self.hair_img, 
                        relief="solid",
                        width=128, 
                        height=128,
                        bg="SystemWindow",
                    )
                    self.import_new_face_bin_btn.config(state="normal")
                    self.import_new_hair_bin_btn.config(state="normal")
                else:
                    self.face_preview_lbl.config(
                        image=self.no_face_img, 
                        relief="solid", 
                        bg="SystemWindow",
                        width=128,
                        height=128,
                    )
                    self.hair_preview_lbl.config(
                        image=self.no_hair_img, 
                        relief="solid", 
                        bg="SystemWindow",
                        width=128, 
                        height=128,
                    )
                    self.import_new_face_bin_btn.config(state="disabled")
                    self.import_new_hair_bin_btn.config(state="disabled")
                
        except:
            ## Here we catch the exception given when the face_idx value is empty
            pass

    def abilities_entry_tracer(self, var:IntVar, entry:Entry):

        try:
            if var.get() < 75:
                entry.config(background=STATS_BG_COLOURS[0])
                #entry.config(foreground=FG_COLOURS[0])
            elif var.get() < 80:
                entry.config(background=STATS_BG_COLOURS[1])
                #entry.config(foreground=FG_COLOURS[1])
            elif var.get() < 90:
                entry.config(background=STATS_BG_COLOURS[2])
                #entry.config(foreground=FG_COLOURS[2])
            elif var.get() < 95:
                entry.config(background=STATS_BG_COLOURS[3])
                #entry.config(foreground=FG_COLOURS[3])
            else:
                entry.config(background=STATS_BG_COLOURS[4])
                #entry.config(foreground=FG_COLOURS[4])
        except Exception as e:
            entry.config(background=STATS_BG_COLOURS[0])
            #entry.config(foreground=FG_COLOURS[0])
            #print(e)

    def abilities_1_8_entry_tracer(self, var:IntVar, entry:Entry):

        try:
            if var.get() < 7:
                entry.config(background=STATS_1_8_BG_COLOURS[0])
                #entry.config(foreground=FG_COLOURS[0])
            elif var.get() < 8:
                entry.config(background=STATS_1_8_BG_COLOURS[1])
                #entry.config(foreground=FG_COLOURS[1])
            else:
                entry.config(background=STATS_1_8_BG_COLOURS[2])
                #entry.config(foreground=FG_COLOURS[4])
        except Exception as e:
            entry.config(background=STATS_1_8_BG_COLOURS[0])
            #entry.config(foreground=FG_COLOURS[0])
            #print(e)


    def toggle_appearance_menu(self, case:int):
        """
        This functions take care of disabling or enabling some stuff from the menu depending on the specific case

        Args:
            case (int): possible values listed below
            0 = for when we selected "BUILD" option on the face combobox, it will do the following:
                - Disabled face id spinbox and special hairstyles 2 checkbox
                - Set face id to 0 and special hairstyles 2 to "NO"
            1 = for when we selected something different from "BUILD" on the face combobox, it will do the following:
                - Enable face id spinbox and special hairstyles 2 checkbox
            2 = for the switch on/off of special hairstyles 2
                - on: will disabled hair id entry and set the value to the same as face id entry
                - off: will enabled the hair id entry
            any other value outside those covers will raise a NotImplementedError

        """
        if case == 0:
            #print("caso 1")
            self.player_face_idx_spinbox.config(state="disabled",from_=MIN_FACE_IDX, to=MAX_FACE_IDX)
            self.player_hair_idx_spinbox.config(state="normal",from_=MIN_HAIR_IDX, to=MAX_HAIR_IDX)
            self.player_face_idx_int_var.set(0)
            
            #self.player_hair_idx_int_var.set(0)
            self.player_special_hairstyles_2_var.set(0)
            self.player_special_hairstyles_2_chk_btn.config(state="disabled")
            self.face_preview_lbl.config(
                image=self.no_face_img, 
                relief="solid", 
                bg="SystemWindow",
                width=128,
                height=128,
            )
            self.hair_preview_lbl.config(
                image=self.no_hair_img, 
                relief="solid", 
                bg="SystemWindow",
                width=128, 
                height=128,
            )
            self.import_new_face_bin_btn.config(state="disabled")
            self.import_new_hair_bin_btn.config(state="disabled")

        elif case == 1:
            #print("caso2")
            self.player_face_idx_spinbox.config(state="normal",from_=MIN_FACE_IDX + 1, to=MAX_FACE_IDX + 1)
            if self.player_special_hairstyles_2_var.get():
                self.player_hair_idx_spinbox.config(state="disabled", from_=MIN_HAIR_IDX + 1, to=MAX_HAIR_IDX + 1)
                self.player_special_hairstyles_2_chk_btn.config(state="normal")

                if (
                    self.has_face_hair_folder and 
                    self.face_hair_folder !="" and 
                    self.face_hair_version !=-1 and 
                    self.player_face_idx_int_var.get() - 1<= len(self.faces_location) and
                    self.player_face_idx_int_var.get() - 1<= len(self.faces_location)
                ):
                    self.face_img = common_functions.get_face_texture(self.faces_location[self.player_face_idx_int_var.get() - 1])
                    self.hair_img = common_functions.get_hair_texture(self.hairs_location[self.player_face_idx_int_var.get() - 1])

                    self.face_preview_lbl.config(
                        image=self.face_img, 
                        relief="solid", 
                        width=128, 
                        height=128,
                        bg="SystemWindow",
                    )
                    self.hair_preview_lbl.config(
                        image=self.hair_img, 
                        relief="solid",
                        width=128, 
                        height=128,
                        bg="SystemWindow",
                    )
                    self.import_new_face_bin_btn.config(state="normal")
                    self.import_new_hair_bin_btn.config(state="normal")



            else:
                self.player_hair_idx_spinbox.config(from_=MIN_HAIR_IDX, to=MAX_HAIR_IDX)
                self.player_special_hairstyles_2_chk_btn.config(state="normal")
                self.import_new_face_bin_btn.config(state="disabled")
                self.import_new_hair_bin_btn.config(state="disabled")
                self.face_preview_lbl.config(
                    image=self.no_face_img, 
                    relief="solid", 
                    bg="SystemWindow",
                    width=128,
                    height=128,
                )
                self.hair_preview_lbl.config(
                    image=self.no_hair_img, 
                    relief="solid", 
                    bg="SystemWindow",
                    width=128, 
                    height=128,
                )


        elif case == 2 and self.player_special_hairstyles_2_var.get():
            #print("caso 3")
            old_value = self.player_hair_idx_int_var.get()
            self.player_face_idx_spinbox.config(state="normal",from_=MIN_FACE_IDX + 1, to=MAX_FACE_IDX + 1)
            self.player_hair_idx_spinbox.config(state="disabled", from_=MIN_HAIR_IDX + 1, to=MAX_HAIR_IDX + 1)
            try:
                self.player_hair_idx_int_var.set(self.player_face_idx_int_var.get())
            except:
                self.player_hair_idx_int_var.set(old_value)
            if (
                self.has_face_hair_folder and 
                self.face_hair_folder !="" and 
                self.face_hair_version !=-1 and 
                self.player_face_idx_int_var.get() - 1<= len(self.faces_location) and
                self.player_face_idx_int_var.get() - 1<= len(self.faces_location)
            ):
                self.face_img = common_functions.get_face_texture(self.faces_location[self.player_face_idx_int_var.get() - 1])
                self.hair_img = common_functions.get_hair_texture(self.hairs_location[self.player_face_idx_int_var.get() - 1])

                self.face_preview_lbl.config(
                    image=self.face_img, 
                    relief="solid", 
                    width=128, 
                    height=128,
                    bg="SystemWindow",
                )
                self.hair_preview_lbl.config(
                    image=self.hair_img, 
                    relief="solid",
                    width=128, 
                    height=128,
                    bg="SystemWindow",
                )
                self.import_new_face_bin_btn.config(state="normal")
                self.import_new_hair_bin_btn.config(state="normal")
            else:
                self.face_preview_lbl.config(
                    image=self.no_face_img, 
                    relief="solid", 
                    bg="SystemWindow",
                    width=128,
                    height=128,
                )
                self.hair_preview_lbl.config(
                    image=self.no_hair_img, 
                    relief="solid", 
                    bg="SystemWindow",
                    width=128, 
                    height=128,
                )
                self.import_new_face_bin_btn.config(state="disabled")
                self.import_new_hair_bin_btn.config(state="disabled")

        elif case == 2 and not self.player_special_hairstyles_2_var.get():
            #print("caso 4")
            self.player_face_idx_spinbox.config(state="normal",from_=MIN_FACE_IDX + 1, to=MAX_FACE_IDX + 1)
            self.player_hair_idx_spinbox.config(state="normal", from_=MIN_HAIR_IDX, to=MAX_HAIR_IDX)
            self.face_preview_lbl.config(
                image=self.no_face_img, 
                relief="solid", 
                bg="SystemWindow",
                width=128,
                height=128,
            )
            self.hair_preview_lbl.config(
                image=self.no_hair_img, 
                relief="solid", 
                bg="SystemWindow",
                width=128, 
                height=128,
            )
            self.import_new_face_bin_btn.config(state="disabled")
            self.import_new_hair_bin_btn.config(state="disabled")

        else:
            raise NotImplementedError("Case ID: %d, not supported yet" % case)

    def import_face_hair_file(self, file_dst_location:str):
        filetypes = [
            ("PES/WE Binary File", ".bin .str"),
            ('All files', '*.*'),
        ]

        filename = filedialog.askopenfilename(
            title=f'{self.appname} Select your file',
            initialdir=self.last_working_dir,
            filetypes=filetypes)
        if filename == "":
            return 0
        self.last_working_dir = str(Path(filename).parents[0])
        file_src_contents = common_functions.read_file_to_mem(filename)
        if common_functions.write_file_from_mem(file_dst_location, file_src_contents):
            self.toggle_appearance_menu(2)
            messagebox.showinfo(parent=self, title=self.appname, message="File imported successfully")
        else:
            self.toggle_appearance_menu(2)
            messagebox.showerror(parent=self, title=self.appname, message="There was an error while importing the file!")


    def update_player_data(self, player:Player):
        player.name = self.player_name_entry.get()
        player.shirt_name = self.player_shirt_name_entry.get()
        player.callname.set_value(common_functions.intTryParse(self.player_callname_entry.get()))
        player.nation.set_value(self.player_nationality_combobox.get())
        player.basic_settings.age.set_value(common_functions.intTryParse(self.player_age_int_var.get()))
        player.basic_settings.stronger_foot.set_value(self.player_stronger_foot_combobox.get())
        player.basic_settings.injury.set_value(self.player_injury_combobox.get())
        player.basic_settings.style_of_dribble.set_value(common_functions.intTryParse(self.player_style_of_dribble_combobox.get()))
        player.basic_settings.free_kick_type.set_value(common_functions.intTryParse(self.player_free_kick_type_combobox.get()))
        player.basic_settings.penalty_kick.set_value(common_functions.intTryParse(self.player_penalty_kick_combobox.get()))
        player.basic_settings.drop_kick_style.set_value(common_functions.intTryParse(self.player_drop_kick_style_combobox.get()))
        player.basic_settings.goal_celebration_1.set_value(self.player_goal_celebration_1_combobox.current())
        player.basic_settings.goal_celebration_2.set_value(self.player_goal_celebration_2_combobox.current())
        player.basic_settings.growth_type.set_value(self.player_growth_type_combobox.get())

        player.appearance.face.set_value(self.player_face_combobox.get())
        player.appearance.skin_colour.set_value(common_functions.intTryParse(self.player_skin_colour_combobox.get()))
        player.appearance.head_height.set_value(common_functions.intTryParse(self.player_head_height_int_var.get()))
        player.appearance.head_width.set_value(common_functions.intTryParse(self.player_head_width_int_var.get()))
        player.appearance.face_idx.set_value(common_functions.intTryParse(self.player_face_idx_int_var.get()))

        """
        player.appearance.hair.set_value(
            [
                self.player_hair_type_combobox.get(),
                common_functions.intTryParse(self.player_hair_shape_spinbox.get()),
                common_functions.intTryParse(self.player_hair_front_spinbox.get()),
                common_functions.intTryParse(self.player_hair_volume_spinbox.get()),
                common_functions.intTryParse(self.player_hair_darkness_spinbox.get()),
                common_functions.intTryParse(self.player_hair_bandana_type_spinbox.get()),
            ]
        )
        """
        
        player.appearance.hair.set_value(common_functions.intTryParse(self.player_hair_idx_int_var.get()))
        player.appearance.special_hairstyles_2.set_value(NO_YES[self.player_special_hairstyles_2_var.get()])

        player.appearance.height.set_value(common_functions.intTryParse(self.player_height_entry.get()))
        player.appearance.weight.set_value(common_functions.intTryParse(self.player_weight_entry.get()))

        for ability in player.abilities:
            ability.set_value(common_functions.intTryParse(self.abilities_entries.get(ability.name).get()))

        for ability in player.abilities_1_8:
            ability.set_value(common_functions.intTryParse(self.abilities_1_8_entries.get(ability.name).get()))

        for special_ability in player.special_abilities:
            special_ability.set_value(common_functions.intTryParse(self.special_abilities_status_var.get(special_ability.name).get()))

        player.position.favored_side.set_value(self.player_favored_side_combobox.get())
        player.position.registered_position.set_value(self.player_registered_position_combobox.current())
        
        for i, position in enumerate(player.position):
            if i > 1:
                position.set_value(common_functions.intTryParse(self.positions_status_var.get(position.name).get()))

        new_body_parameters = tuple(body_parameter.get() for body_parameter in self.body_parameters.values())
        player.appearance.body_parameters = new_body_parameters

        for flag in player.edited_flags:
            flag.set_value(1)
        
        self.stop_window()


    def stop_window(self):
        self.quit()
        self.destroy()




