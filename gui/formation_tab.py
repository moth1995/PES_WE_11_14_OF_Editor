from tkinter import Button, Frame, Label
from tkinter.ttk import Combobox
from editor import Team
from .custom_widgets import FormationFrame
from PIL import Image
from editor.utils.common_functions import resource_path
from editor.utils.constants import *

class FormationTab(Frame):
    

    def __init__(self, master, team:Team, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.team = team
        self.appname = appname
        self.gk_coordinate = tuple([2, 51])
        pes_coordinates = self.gk_coordinate + team.formation.form_values
        original_width = 50
        original_heigh = 100
        factor = 5
        field = Image.open(resource_path("resources/img/field_1.png")).convert("RGB")
        self.players_names_list = [player.name for player in self.team.players[:PLAYERS_IN_TEAM]]
        
        self.main_frame = Frame(self)
        self.main_frame.pack()
        self.formation = FormationFrame(self.main_frame, field, original_width, original_heigh, factor, pes_coordinates)
        self.formation.grid(row=0, column=0, rowspan=3)
        self.formation.bind("<<DotSelected>>", lambda _ : self.on_dot_selected(self.formation.selected_item))
        
        self.team_settings_frame = Frame(self.main_frame)
        self.team_settings_frame.grid(row=0, column=1, sticky="n", pady=20)
        
        self.player_settings_frame = Frame(self.main_frame)
        self.player_settings_frame.grid(row=1, column=1, sticky="n", pady=20)
        
        self.apply_btn = Button(self.main_frame,text="Apply", command=lambda : self.update_formation_slot())
        self.apply_btn.grid(row=2, column=1, pady=20)
        
        Label(self.team_settings_frame, text = "Formation Slot").grid(row=0, column=0)
        self.formation_slot_cmb = Combobox(self.team_settings_frame, state="readonly", values=FORM_SLOTS)
        self.formation_slot_cmb.grid(row=1, column=0)
        self.formation_slot_cmb.current(self.team.formation.strategy)
        self.formation_slot_cmb.bind(
            "<<ComboboxSelected>>", 
            lambda _ : self.set_formation_slot(self.formation_slot_cmb.current()))

        
        Label(self.team_settings_frame, text = "Formation").grid(row=0, column=1)
        self.formation_cmb = Combobox(self.team_settings_frame, state="readonly", values=team.formation.form_names)
        self.formation_cmb.grid(row=1, column=1)
        self.formation_cmb.set(self.team.formation.form_name)
        self.formation_cmb.bind(
            "<<ComboboxSelected>>", 
            lambda _ : self.formation.load_formation(
                self.gk_coordinate + self.team.formation.form_data[
                    self.formation_cmb.current()
                ]
            )
        )
        Label(self.team_settings_frame, text="Long FK").grid(row=2, column=0)
        self.lfk_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.lfk_cmb.grid(row=3, column=0)
        self.lfk_cmb.current(self.team.formation.jobs[0])
        Label(self.team_settings_frame, text="Short FK").grid(row=4, column=0)
        self.sfk_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.sfk_cmb.grid(row=5, column=0)
        self.sfk_cmb.current(self.team.formation.jobs[1])
        Label(self.team_settings_frame, text="Left CK").grid(row=6, column=0)
        self.lck_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.lck_cmb.grid(row=7, column=0)
        self.lck_cmb.current(self.team.formation.jobs[2])
        Label(self.team_settings_frame, text="Right CK").grid(row=2, column=1)
        self.rck_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.rck_cmb.grid(row=3, column=1)
        self.rck_cmb.current(self.team.formation.jobs[3])
        Label(self.team_settings_frame, text="Penalty").grid(row=4, column=1)
        self.pk_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.pk_cmb.grid(row=5, column=1)
        self.pk_cmb.current(self.team.formation.jobs[4])
        Label(self.team_settings_frame, text="Captain").grid(row=6, column=1)
        self.cap_cmb = Combobox(self.team_settings_frame, state="readonly", values=self.players_names_list)
        self.cap_cmb.grid(row=7, column=1)
        self.cap_cmb.current(self.team.formation.jobs[5])
        
        
        self.role_cmb = Combobox(self.player_settings_frame, state="disabled", width= 5, values=list(ROLES.values()))
        self.role_cmb.pack()
        self.role_cmb.bind("<<ComboboxSelected>>", lambda _ : self.on_role_cmb_selected())
        
        self.roles = self.team.formation.roles
        
        
        
    def set_formation_slot(self, slot_idx:int):
        self.team.formation.strategy = slot_idx
        print(self.team.formation.strategy)
        print(self.team.formation.coordinates_address)
        print(self.team.formation.form_values)
        self.formation.load_formation(
                        self.gk_coordinate + self.team.formation.form_values
                    )
        self.formation_cmb.set(self.team.formation.form_name)


    def on_dot_selected(self, idx):
        print(idx)
        if idx is None :
            self.role_cmb.config(state="disabled",)
            self.role_cmb.set("")
            return 0
        self.role_cmb.config(state="readonly",)
        self.role_cmb.set(self.roles[self.formation.selected_item])

    def on_role_cmb_selected(self):
        self.roles[self.formation.selected_item] = self.role_cmb.get()
        ### falta updatear el dot
        print(self.roles)
    
    def update_formation_slot(self):
        print("init update formation slot")
        jobs = (
            self.lfk_cmb.current(),
            self.sfk_cmb.current(),
            self.lck_cmb.current(),
            self.rck_cmb.current(),
            self.pk_cmb.current(),
            self.cap_cmb.current(),
        )
        self.team.formation.jobs = jobs
        self.team.formation.form_values = self.formation.get_pes_coord()[2:] + tuple((ROLES_INT.get(role) for role in self.roles))
        
        print("values updated to:")
        print(self.team.formation.jobs)
        print(self.team.formation.form_values)