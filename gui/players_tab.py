from tkinter import Button, Entry,  Frame, IntVar, Label, Listbox, Scrollbar, messagebox
from tkinter.ttk import Combobox

from editor import (
    OptionFile, 
    Player, 
    common_functions, 
    Team,
)
from editor.utils.constants import *

from .player_stats_window import PlayerStatsWindow
from .team_config_window import TeamConfigWindow
from .custom_widgets import Table

class PlayersTab(Frame):

    order_by_name = False

    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.player_filter_list = self.of.nations + PLAYER_FILTER_EXTRA
        self.players_filter_combobox = Combobox(self, state="readonly", value=self.player_filter_list, width=30)
        self.players_filter_combobox.set("All Players")
        self.players_filter_combobox.bind(
            '<<ComboboxSelected>>', 
            lambda _ : self.apply_player_filter()
        )
        self.players_filter_combobox.bind(
            '<Key>', 
            lambda event: common_functions.find_in_combobox(
                event,
                self.players_filter_combobox,
                self.players_filter_combobox["values"],
            )
        )

        self.players_list_box = Listbox(self, height = 37, width = 30, exportselection=False)
        self.players_list_box.bind('<Double-1>',lambda _ : self.on_lb_double_click())
        self.players_list_box.bind('<<ListboxSelect>>',lambda _ : self.on_lb_click())
        self.players_list_box_sb = Scrollbar(self.master, orient="vertical") 
        self.players_list_box_sb.config(command = self.players_list_box.yview)
        self.players_list_box.config(yscrollcommand = self.players_list_box_sb.set)
        # Loading all players into the listbox
        self.apply_player_filter()

        self.player_info_label = Label(
            self, 
            text="", 
            width=25, 
            height=50, 
            anchor="nw",
            justify="left",
            background="black", 
            foreground="white",
        )
        self.dorsal_lbl = Label(self, text= "Dorsal: ")
        self.dorsal_lbl.place(x = 631, y = 4)
        self.dorsal_number_var = IntVar(self, 0)
        self.dorsal_number_entry = Entry(self, width=4,  state="readonly", textvariable= self.dorsal_number_var)
        self.dorsal_number_entry.bind("<Return>", lambda _ : self.set_dorsal_number_from_entry())
        self.dorsal_number_entry.place(x = 681, y = 4)
        self.team_a = Team(self.of, 0)
        self.team_b = Team(self.of, 0)

        self.team_a_combobox = Combobox(self, state="readonly", value=self.of.teams_names, width=31)
        self.team_b_combobox = Combobox(self, state="readonly", value=self.of.teams_names, width=31)
        self.team_a_table = Table(self, 32, 3, "...")
        self.team_a_table.set_column_width(0, 4)
        self.team_a_table.set_column_width(1, 3)
        self.team_a_table.set_column_width(2, 22)
        self.team_b_table = Table(self, 32, 3, "...")
        self.team_b_table.set_column_width(0, 4)
        self.team_b_table.set_column_width(1, 3)
        self.team_b_table.set_column_width(2, 22)


        self.team_a_table.bind(
            "<<DoubleClic>>", 
            lambda _ 
            : 
            self.on_table_double_click(
                self.team_a_table, 
                self.team_a, 
                self.team_a_combobox,
            )
        )
        self.team_a_table.bind(
            "<<LeftClic>>", 
            lambda _ 
            : 
            self.on_table_left_click(
                self.team_a_table, 
                self.team_a, 
                self.team_a_combobox,
            )
        )

        self.team_a_table.bind(
            "<<RightClic>>", 
            lambda _ 
            : 
            self.on_table_right_click(
                self.team_a_table, 
                self.team_a, 
                self.team_a_combobox,
            )
        )

        self.team_b_table.bind(
            "<<DoubleClic>>", 
            lambda _ 
            : 
            self.on_table_double_click(
                self.team_b_table, 
                self.team_b, 
                self.team_b_combobox,
            )
        )
        self.team_b_table.bind(
            "<<LeftClic>>", 
            lambda _ 
            : 
            self.on_table_left_click(
                self.team_b_table, 
                self.team_b, 
                self.team_b_combobox,
            )
        )

        self.team_b_table.bind(
            "<<RightClic>>", 
            lambda _ 
            : 
            self.on_table_right_click(
                self.team_b_table, 
                self.team_b, 
                self.team_b_combobox,
            )
        )


        self.all_players_control_frame = Frame(self,)


        self.order_by_name_button = Button(
            self.all_players_control_frame, 
            text="Order by A-Z", 
            width = 26,
            command=lambda: self.on_order_by_clic(),
        )

        self.all_players_transfer_team_a = Button(
            self.all_players_control_frame, 
            text="Transfer Team A", 
            width = 13,
            command=lambda: self.listbox_transfer(self.team_a),
            anchor="nw",
        )
        self.all_players_transfer_team_b = Button(
            self.all_players_control_frame, 
            text="Transfer Team B", 
            width = 13,
            command=lambda: self.listbox_transfer(self.team_b),
            anchor="nw",
        )

        self.order_by_name_button.grid(row=0, column=0, sticky='nswe', columnspan=2)
        self.all_players_transfer_team_a.grid(row=1, column=0, sticky='nswe')
        self.all_players_transfer_team_b.grid(row=1, column=1, sticky='nswe')


        self.transfer_control_frame = Frame(self,)
        self.transfer_player_team_a_to_team_b_btn = Button(
            self.transfer_control_frame, 
            width=29,  
            text="Transfer >>>", 
            command= lambda: self.transfer(self.team_a_table, self.team_b_table, self.team_a, self.team_b)
        )
        
        self.transfer_player_team_b_to_team_a_btn = Button(
            self.transfer_control_frame, 
            width=29,  
            text="<<< Transfer", 
            command=lambda: self.transfer(self.team_b_table, self.team_a_table, self.team_b, self.team_a)
        )
        
        btn3 = Button(
            self.transfer_control_frame, 
            width=29, 
            text="Release", 
            command = 
                lambda 
                    : 
                self.release_player(self.team_a_table, self.team_a)
        )
        btn4 = Button(
            self.transfer_control_frame, 
            width=29,  
            text="Release", 
            command = 
                lambda 
                    : 
                self.release_player(self.team_b_table, self.team_b)
        )
        
        btn5 = Button(self.transfer_control_frame, width=58,  text="<<Swap Selected Players>>", command=self.swap_selected)
        
        self.btn6 = Button(self.transfer_control_frame, width=58,  text="<<Swap All Players>>", command=self.swap_all)
        
        self.transfer_player_team_a_to_team_b_btn.grid(row=0, column=0, sticky='nswe')
        self.transfer_player_team_b_to_team_a_btn.grid(row=0, column=1, sticky='nswe')
        btn3.grid(row=1, column=0, sticky='nswe')
        btn4.grid(row=1, column=1, sticky='nswe')
        btn5.grid(row=2, column=0, sticky='nswe', columnspan=2)
        self.btn6.grid(row=3, column=0, sticky='nswe', columnspan=2)


        self.team_a_combobox.bind(
            "<<ComboboxSelected>>",
            lambda _, 
            : 
            self.on_team_cmb_selected(self.team_a, self.team_a_combobox.current() , self.team_a_table, True)
        )
        self.team_b_combobox.bind(
            "<<ComboboxSelected>>",
            lambda _, 
            : 
            self.on_team_cmb_selected(self.team_b, self.team_b_combobox.current() , self.team_b_table, False)
        )

        self.team_a_combobox.current(0)
        self.team_b_combobox.current(0)

        self.team_a_combobox.event_generate("<<ComboboxSelected>>")
        self.team_b_combobox.event_generate("<<ComboboxSelected>>")
        
        self.team_in_use = None
        self.last_selected_item = None


        
        #self.bind("<Motion>", lambda e: self.find_widget_placing(e, self.all_players_control_frame))


    def set_dorsal_number_from_entry(self):
        try:
            self.team_in_use.dorsals[self.last_selected_item] = self.dorsal_number_var.get()
            self.team_in_use.dorsals=self.team_in_use.dorsals
            self.trigger_update_on_teams()
            
        except:
            pass
    def transfer(self, table_src:Table, table_dst:Table, team_src:Team, team_dst:Team):
        table_src_item = table_src.selected_row
        if (table_src_item is None or table_src_item >= team_src.current_players_in_team):
            return 0
        if team_src.players[table_src_item].idx in [player.idx for player in team_dst.players if player is not None]:
            return 0
        if team_dst.total_available_slots == 0:
            messagebox.showerror(self.appname, "Team is full you cant transfer more players here!")
            return 0



        if team_src.is_national_team and team_dst.is_national_team:
            # if both teams are national teams we just update the nation id
            team_src.players[table_src_item].national_id = team_dst.idx

            new_slot = team_dst.players.index(None)
            team_src.players[table_src_item], team_dst.players[new_slot] = None, team_src.players[table_src_item]
            team_src.dorsals[table_src_item] = None
            team_dst.set_random_dorsal(new_slot)
            team_src.players = team_src.players
            team_src.dorsals = team_src.dorsals
            team_dst.players = team_dst.players
            team_dst.dorsals = team_dst.dorsals

        elif not team_src.is_national_team and not team_dst.is_national_team:
            # if both teams are club teams we just update the club id
            team_src.players[table_src_item].club_id = team_dst.idx
            new_slot = team_dst.players.index(None)
            team_src.players[table_src_item], team_dst.players[new_slot] = None, team_src.players[table_src_item]
            team_src.dorsals[table_src_item] = None
            team_dst.set_random_dorsal(new_slot)
            team_src.players = team_src.players
            team_src.dorsals = team_src.dorsals
            team_dst.players = team_dst.players
            team_dst.dorsals = team_dst.dorsals


        elif team_src.is_national_team and not team_dst.is_national_team:
            #if the first team is national we follow this logic
            if team_src.players[table_src_item].club_id is not None:
                # if the player is registered on other team we need to free him first
                temp_team = Team(self.of, team_src.players[table_src_item].club_id)
                pos = [player.idx for player in temp_team.players if player is not None].index(team_src.players[table_src_item].idx)
                temp_team.players[pos] = None
                temp_team.dorsals[pos] = None
                temp_team.players = temp_team.players
                temp_team.dorsals = temp_team.dorsals
                #messagebox.showerror(self.appname, f"Player: {team_src.players[table_src_item].name} is registerd on {self.teams_filter_list[team_src.players[table_src_item].club]} national team, you need to release it there first")
                #return 0             
            team_src.players[table_src_item].club_id = team_dst.idx
            team_src.players[table_src_item].free_agent = False

            new_slot = team_dst.players.index(None)
            team_dst.players[new_slot] = team_src.players[table_src_item]
            team_dst.set_random_dorsal(new_slot)
            team_dst.players = team_dst.players
            team_dst.dorsals = team_dst.dorsals

        elif not team_src.is_national_team and team_dst.is_national_team:

            if team_src.players[table_src_item].national_id is not None:

                temp_team = Team(self.of, team_src.players[table_src_item].national_id)
                pos = [player.idx for player in temp_team.players if player is not None].index(team_src.players[table_src_item].idx)
                temp_team.players[pos] = None
                temp_team.dorsals[pos] = None
                temp_team.players = temp_team.players
                temp_team.dorsals = temp_team.dorsals

                #messagebox.showerror(self.appname, f"Player: {self.team_a.players[item_a].name} is registerd on {self.teams_filter_list[self.team_a.players[item_a].national_id]} national team, you need to release it there first")
                #return 0

            team_src.players[table_src_item].national_id = team_dst.idx

            new_slot = team_dst.players.index(None)
            team_dst.players[new_slot] = team_src.players[table_src_item]
            team_dst.set_random_dorsal(new_slot)
            team_dst.players = team_dst.players
            team_dst.dorsals = team_dst.dorsals

        else:
            raise Exception("Unhandle case of transfer report it please")
        
        self.trigger_update_on_teams()
        
    def release_player(self, table:Table, team:Team):
        table_item_id = table.selected_row
        if table_item_id is None or table_item_id >= team.current_players_in_team:
            return 0
        player = self.of.get_player_by_idx(team.players[table_item_id].idx)
        if team.is_club:
            player.free_agent = True
        if team.idx == player.club_id:
            player.club_id = None
        elif team.idx == player.national_id:
            player.national_id = None

        team.players[table_item_id] = None
        team.dorsals[table_item_id] = None
        try:
            team.players = team.players
            team.dorsals = team.dorsals
            self.dorsal_number_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror(self.appname, e)
        self.trigger_update_on_teams()

    def swap_selected(self):
        item_a = self.team_a_table.selected_row
        item_b = self.team_b_table.selected_row
        
        
        if (
            (
            item_a == item_b and self.team_a.idx == self.team_b.idx) or 
            (item_a is None or 
            item_b is None) or 
            item_a >= self.team_a.current_players_in_team or 
            item_b >= self.team_b.current_players_in_team
        ):
            # if they're the same item aka player, and the same team, or if any item was selected we don't do anything
            return 0
        if self.team_a.idx == self.team_b.idx:
            self.team_a.players[item_a],self.team_a.players[item_b] = self.team_a.players[item_b], self.team_a.players[item_a]
            self.team_a.dorsals[item_a], self.team_a.dorsals[item_b] = self.team_a.dorsals[item_b], self.team_a.dorsals[item_a]
            self.team_a.players = self.team_a.players
            self.team_b.players = self.team_a.players
            self.team_a.dorsals = self.team_a.dorsals
            self.team_b.dorsals = self.team_a.dorsals
        else:
            if self.team_a.is_national_team and self.team_b.is_national_team:
                # if both teams are national teams we just update the nation id
                self.team_a.players[item_a].national_id = self.team_b.idx
                self.team_b.players[item_b].national_id = self.team_a.idx
            elif not self.team_a.is_national_team and not self.team_b.is_national_team:
                # if both teams are club teams we just update the club id
                self.team_a.players[item_a].club_id = self.team_b.idx
                self.team_b.players[item_b].club_id = self.team_a.idx
            elif self.team_a.is_national_team and not self.team_b.is_national_team:
                #if the first team is national we follow this logic
                if self.team_b.players[item_b].national_id is not None:
                    temp_team = Team(self.of, self.team_b.players[item_b].national_id)
                    pos = [player.idx for player in temp_team.players if player is not None].index(self.team_b.players[item_b].idx)
                    temp_team.players[pos] = None
                    temp_team.dorsals[pos] = None
                    temp_team.players = temp_team.players
                    temp_team.dorsals = temp_team.dorsals

                if self.team_a.players[item_a].club_id is not None:
                    temp_team = Team(self.of, self.team_a.players[item_a].club_id)
                    pos = [player.idx for player in temp_team.players if player is not None].index(self.team_a.players[item_a].idx)
                    temp_team.players[pos] = None
                    temp_team.dorsals[pos] = None
                    temp_team.players = temp_team.players
                    temp_team.dorsals = temp_team.dorsals


                    #messagebox.showerror(self.appname, f"Player: {self.team_b.players[item_b].name} is registerd on {self.teams_filter_list[self.team_b.players[item_b].national_id]} national team, you need to release it there first")
                    #return 0             
                self.team_a.players[item_a].national_id = None
                self.team_a.players[item_a].club_id = self.team_b.idx
                self.team_a.players[item_a].free_agent = False

                self.team_b.players[item_b].national_id = self.team_a.idx
                self.team_b.players[item_b].club_id = None
                self.team_b.players[item_b].free_agent = True

            elif not self.team_a.is_national_team and self.team_b.is_national_team:

                if self.team_a.players[item_a].national_id is not None:
                    temp_team = Team(self.of, self.team_a.players[item_a].national_id)
                    pos = [temp_player.idx for temp_player in temp_team.players if temp_player is not None].index(self.team_a.players[item_a].idx)
                    temp_team.players[pos] = None
                    temp_team.dorsals[pos] = None
                    temp_team.players = temp_team.players
                    temp_team.dorsals = temp_team.dorsals

                if self.team_b.players[item_b].club_id is not None:
                    temp_team = Team(self.of, self.team_b.players[item_b].club_id)
                    pos = [temp_player.idx for temp_player in temp_team.players if temp_player is not None].index(self.team_b.players[item_b].idx)
                    temp_team.players[pos] = None
                    temp_team.dorsals[pos] = None
                    temp_team.players = temp_team.players
                    temp_team.dorsals = temp_team.dorsals
                    
                    #messagebox.showerror(self.appname, f"Player: {self.team_a.players[item_a].name} is registerd on {self.teams_filter_list[self.team_a.players[item_a].national_id]} national team, you need to release it there first")
                    #return 0             

                #if the second team is national we follow this logic                    
                self.team_a.players[item_a].national_id = self.team_b.idx
                self.team_a.players[item_a].club_id = None
                self.team_a.players[item_a].free_agent = True

                self.team_b.players[item_b].national_id = None
                self.team_b.players[item_b].club_id = self.team_a.idx
                self.team_b.players[item_b].free_agent = False

            else:
                raise Exception("Unhandle case of transfer report it please")

            self.team_a.players[item_a],self.team_b.players[item_b] = self.team_b.players[item_b], self.team_a.players[item_a]
            
            self.team_a.players = self.team_a.players
            self.team_b.players = self.team_b.players
        self.trigger_update_on_teams()

    def swap_all(self):
        if self.team_a.idx == self.team_b.idx:
            return 0
        if self.team_a.max_players != self.team_b.max_players:
            messagebox.showerror(self.appname, "Sorry, you can't Swap a National team with a Club team")
            return 0
        self.team_a.players,self.team_b.players = self.team_b.players, self.team_a.players
        for player in self.team_a.players:
            if player is None: continue
            if self.team_a.is_national_team:
                player.national_id = self.team_a.idx
            else:
                player.club_id = self.team_a.idx

        for player in self.team_b.players:
            if player is None: continue

            if self.team_b.is_national_team:
                player.national_id = self.team_b.idx
            else:
                player.club_id = self.team_b.idx

        self.team_a.dorsals,self.team_b.dorsals = self.team_b.dorsals, self.team_a.dorsals
        self.trigger_update_on_teams()
        
    def listbox_transfer(self, team:Team):
        if len(self.players_list_box.curselection()) == 0:
            return
        item_idx = self.players_list_box.curselection()[0]
        player_idx = self.player_idx_list[item_idx]
        player = self.of.get_player_by_idx(player_idx)


        if player.idx in [player.idx for player in team.players if player is not None]:
            # if the player was already on the team there's not need to tranfer it again
            return 0
        if team.total_available_slots == 0:
            messagebox.showerror(self.appname, "Team is full you cant transfer more players here!")
            return 0
        
        if team.is_national_team and player.national_id is not None:
            temp_team = Team(self.of, player.national_id)
            pos = [temp_player.idx for temp_player in temp_team.players if temp_player is not None].index(player.idx)
            temp_team.players[pos] = None
            temp_team.dorsals[pos] = None
            temp_team.players = temp_team.players
            temp_team.dorsals = temp_team.dorsals
            player.national_id = team.idx

            
            #messagebox.showerror(
            #    self.appname, 
            #    f"Player: {player.name} is registerd on {self.teams_filter_list[player.national_id]} national team, you need to release it there first"
            #)
            #return 0
        elif team.is_national_team and player.national_id is None:
            player.national_id = team.idx
        elif not team.is_national_team and player.club_id is None:
            player.club_id = team.idx
            player.free_agent = False
        elif not team.is_national_team and player.club_id is not None:
            temp_team = Team(self.of, player.club_id)
            pos = [temp_player.idx for temp_player in temp_team.players if temp_player is not None].index(player.idx)
            temp_team.players[pos] = None
            temp_team.dorsals[pos] = None
            temp_team.players = temp_team.players
            temp_team.dorsals = temp_team.dorsals
            player.club_id = team.idx

        else:
            raise Exception("no deberiamos estar aca")            
            #messagebox.showerror(
            #    self.appname, 
            #    f"Player: {player.name} is registerd on {self.teams_filter_list[player.club_id]} club team, you need to release it there first"
            #)
            #return 0

        new_slot = team.players.index(None)
        team.players[new_slot] = player
        team.set_random_dorsal(new_slot)
        team.players = team.players
        team.dorsals = team.dorsals
        self.trigger_update_on_teams()

    def trigger_update_on_teams(self):
        self.team_a_combobox.event_generate("<<ComboboxSelected>>")
        self.team_b_combobox.event_generate("<<ComboboxSelected>>")


    def update_teams_cmb_values(self):
        cmb_a_item_idx = self.team_a_combobox.current()
        cmb_b_item_idx = self.team_b_combobox.current()
        self.team_a_combobox.config(values=self.of.teams_names)
        self.team_b_combobox.config(values=self.of.teams_names)
        self.team_a_combobox.current(cmb_a_item_idx)
        self.team_b_combobox.current(cmb_b_item_idx)

    def on_team_cmb_selected(self, team: Team, team_idx:int, team_table:Table, is_team_a:bool):
        team = Team(self.of, team_idx)
        #print(team.idx)
        for i, clean_data in enumerate([["...","...","..."]] * Team.total_players_in_clubs):
            team_table.set_row(i, clean_data)
        for i, player in enumerate(team.players):
            if player is not None:
                player.init_stats()
                team_table.set_row(i, [POSITION_NAMES[player.position.registered_position()], team.dorsals[i], player.name])
            else:
                team_table.set_row(i, ["...","...","..."])
        
        if is_team_a:
            self.team_a = team
        else:
            self.team_b = team
        #if team.formation is None:
            #return 0
        
        self.update_transfer_buttons()

    def update_transfer_buttons(self):
        team_a_cmb_item = self.team_a_combobox.current()
        team_b_cmb_item = self.team_b_combobox.current()
        
        if team_a_cmb_item == team_b_cmb_item:
            self.transfer_player_team_a_to_team_b_btn.config(state="disabled")
            self.transfer_player_team_b_to_team_a_btn.config(state="disabled")
            self.btn6.config(state="disabled")
            
        else:
            self.transfer_player_team_a_to_team_b_btn.config(state="normal")
            self.transfer_player_team_b_to_team_a_btn.config(state="normal")
            self.btn6.config(state="normal")
            

    def on_table_double_click(self, table:Table, team:Team, team_cmb:Combobox):
        item_idx = table.selected_row
        team = Team(self.of, team_cmb.current())
        if item_idx<team.dorsal_size:
            player = team.players[item_idx]
            if player is not None:
                player.init_stats()
                psw = PlayerStatsWindow(self, player, self.of.nations)
                psw.mainloop()
                self.of.set_players_names()
                self.of.set_edited_players_names()
                team_cmb.current(team.idx)
                team_cmb.event_generate("<<ComboboxSelected>>")
                self.apply_player_filter()
                self.set_player_info_label(player)

    def on_table_left_click(self, table:Table, team:Team, team_cmb:Combobox):
        item_idx = table.selected_row
        team = Team(self.of, team_cmb.current())
        self.dorsal_number_entry.config(state="readonly")
        if item_idx<team.current_players_in_team and team.players[item_idx] is not None:
            player = team.players[item_idx]
            if team.dorsals[item_idx] is not None:
                self.dorsal_number_var.set(team.dorsals[item_idx])
                self.dorsal_number_entry.config(state="normal")
            self.team_in_use = team
            self.last_selected_item = item_idx
            player.init_stats()
            self.set_player_info_label(player)
    def on_table_right_click(self, table:Table, team:Team, team_cmb:Combobox):
        if team.real_idx is None:
            return 0
        team_config_window = TeamConfigWindow(self, team, team_cmb.get())
        team_config_window.mainloop()


    def on_lb_double_click(self):
        """
        Creates a new window showing selected player attributes
        """
        if len(self.players_list_box.curselection()) == 0:
            return
        #item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection()))
        #player = self.of.get_player_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        item_idx = self.players_list_box.curselection()[0]
        #item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection()))
        player_idx = self.player_idx_list[item_idx]
        #player = self.of.get_player_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        player = self.of.players[player_idx] if player_idx < Player.first_edited_id else self.of.edited_players[player_idx - Player.first_edited_id]
        player.init_stats()
        psw = PlayerStatsWindow(self, player, self.of.nations)
        psw.mainloop()
        self.of.set_players_names()
        self.of.set_edited_players_names()
        self.players_list_box.delete(item_idx,item_idx)
        self.players_list_box.insert(item_idx, player.name)
        self.players_list_box.select_set(item_idx)
        self.team_a_combobox.event_generate("<<ComboboxSelected>>")
        self.team_b_combobox.event_generate("<<ComboboxSelected>>")
        self.set_player_info_label(player)


    def find_widget_placing(self, e, widget):
    
        widget.place(x=e.x,y=e.y)
        print(f"{e.x},{e.y}")

    def apply_player_filter(self):
        filter_selected = self.players_filter_combobox.get()
        if filter_selected == self.player_filter_list[-1]:
            # All Players
            player_list = [player.name for i, player in enumerate(self.of.players) if i>0] + [player.name for player in self.of.edited_players]
            self.player_idx_list = [player.idx for i, player in enumerate(self.of.players) if i>0] + [player.idx for player in self.of.edited_players]
        elif filter_selected == self.player_filter_list[-2]:
            # Edited Players
            player_list = [player.name for player in self.of.edited_players]
            self.player_idx_list = [player.idx for player in self.of.edited_players]
        elif filter_selected == self.player_filter_list[-3]:
            # Unused
            player_list = [self.of.players[i].name for i in range(Player.first_unused, len(self.of.players))]
            self.player_idx_list = [self.of.players[i].idx for i in range(Player.first_unused, len(self.of.players))]
        elif filter_selected == self.player_filter_list[-4]:
            # ML OLD
            player_list = [self.of.players[i].name for i in range(Player.first_ml_old, Player.first_unused)]
            self.player_idx_list = [self.of.players[i].idx for i in range(Player.first_ml_old, Player.first_unused)]
        elif filter_selected == self.player_filter_list[-5]:
            # ML Youth
            player_list = [self.of.players[i].name for i in range(Player.first_ml_youth, Player.first_ml_old)]
            self.player_idx_list = [self.of.players[i].idx for i in range(Player.first_ml_youth, Player.first_ml_old)]
        elif filter_selected == self.player_filter_list[-6]:
            # Shop
            player_list = [self.of.players[i].name for i in range(Player.first_shop, Player.first_ml_youth)]
            self.player_idx_list = [self.of.players[i].idx for i in range(Player.first_shop, Player.first_ml_youth)]
        elif filter_selected == self.player_filter_list[-7]:
            # ML Default
            player_list = [self.of.players[i].name for i in range(Player.first_ml_default, Player.first_shop)]
            self.player_idx_list = [self.of.players[i].idx for i in range(Player.first_ml_default, Player.first_shop)]

        elif filter_selected == self.player_filter_list[-8]:
            # Free Agents
            player_list = [player.name for i, player in enumerate(self.of.players) if i>0 and player.free_agent] + [player.name for player in self.of.edited_players if player.free_agent]
            self.player_idx_list = [player.idx for i, player in enumerate(self.of.players) if i>0 and player.free_agent] + [player.idx for player in self.of.edited_players if player.free_agent]
        
        
        elif filter_selected in self.of.nations:
            # Filter by Nation
            player_list = [
                player.name
                for i, player in enumerate(self.of.players)
                if player.nation() == filter_selected and i > 0
            ] + [
                player.name
                for player in self.of.edited_players
                if player.nation() == filter_selected
            ]
            
            self.player_idx_list = [
                player.idx 
                for i, player in enumerate(self.of.players)
                if player.nation() == filter_selected and i>0
            ] + [
                player.idx
                for player in self.of.edited_players
                if player.nation() == filter_selected
            ]
        else:
            # Default case, we just leave it empty
            player_list = []
            self.player_idx_list = []
        if self.order_by_name: 
            player_list, self.player_idx_list = (list(t) for t in zip(*sorted(zip(player_list, self.player_idx_list))))
        self.players_list_box.delete(0,'end')
        self.players_list_box.insert('end',*player_list)

    def on_order_by_clic(self):
        self.order_by_name = False if self.order_by_name else True
        self.order_by_name_button['text'] = 'Order by ID' if self.order_by_name else 'Order by A-Z'
        self.apply_player_filter()

    def on_lb_click(self):
        """
        Display player info at the black label
        """
        self.dorsal_number_entry.config(state="readonly")
        if len(self.players_list_box.curselection()) == 0:
            return
        item_idx = self.players_list_box.curselection()[0]
        #item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection()))
        #print(item_idx)
        player_idx = self.player_idx_list[item_idx]
        #print(player_idx)
        #player = self.of.get_player_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        player = self.of.players[player_idx] if player_idx < Player.first_edited_id else self.of.edited_players[player_idx - Player.first_edited_id]
        #print(f"player id antes de la condicion: {player_id}")
        #print(player_id)
        player.init_stats()
        self.set_player_info_label(player)

    def set_player_info_label(self, player):
        player.init_stats()

        national_name = player.national_team_name
        club_name = player.club_team_name

        player_info = f"""Player ID: {player.idx}
    
        Name: {player.name}
        Shirt Name: {player.shirt_name}
        Nationality: {player.nation()}
        National Team: {national_name}
        Club: {club_name}
        Age: {player.basic_settings.age()}
        Stronger Foot: {player.basic_settings.stronger_foot()}
        """.replace("        ", "")
        abilities =""
        for ability in player.abilities:
            abilities += "%s: %d\n" % (ability.name, ability())
            
        positions = "Side: {}\nReg Position: {}\n\n".format(player.position.favored_side(), POSITION_NAMES[player.position.registered_position()])

        abilities_1_8 = ""
        for ability in player.abilities_1_8:
            abilities_1_8 += "%s: %d\n" % (ability.name, ability())

        self.player_info_label.config(text=player_info + positions +abilities + abilities_1_8)

    def publish(self):
        self.players_list_box.place(x = 2, y = 26)
        self.players_list_box_sb.place(x = 187, y =49.5 , height = 595)
        self.player_info_label.place(x = 631, y = 26)
        self.players_filter_combobox.place(x = 2, y = 2)
        self.all_players_control_frame.place(x = 2, y = 625)
        self.team_a_combobox.place(x = 207, y = 2)
        self.team_a_table.place(x = 207, y = 26)
        self.team_b_table.place(x = 419, y = 26)
        self.team_b_combobox.place(x = 419, y = 2)
        self.transfer_control_frame.place(x = 206, y = 573)


