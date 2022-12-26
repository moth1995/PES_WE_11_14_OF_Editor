import os
import sys
from pathlib import Path
from tkinter import Tk, Menu, filedialog, messagebox
from tkinter.ttk import Notebook

import yaml

from editor import OptionFile, Team, Player,common_functions, create_csv, write_players, load_csv
from editor.utils.constants import *

from gui import ClubTab, LogosTab, ShopTab, StadiumLeagueTab, PlayersTab, Config
from gui.export_to_csv_window import ExportToCSVWindow

class Gui(Tk):
    appname="PES/WE OF Editor 2011-2014"
    report_callback_exception = common_functions.report_callback_exception
    last_working_dir = os.getcwd()
    current_exe_name = Path(sys.argv[0]).stem
    of = None
    def __init__(self):
        Tk.__init__(self)
        self.title(self.appname)
        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (MAIN_WINDOW_W/2)
        y = (hs/2) - (MAIN_WINDOW_H/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (MAIN_WINDOW_W, MAIN_WINDOW_H, x, y))
        self.iconbitmap(default=common_functions.resource_path("resources/img/pes_indie.ico"))
        load_defaults = False
        try:
            with open(os.getcwd() + "/" + self.current_exe_name + ".yaml") as stream:
                self.settings_file = yaml.safe_load(stream)
                self.last_working_dir = self.settings_file.get('Last Working Dir')
                self.my_config = Config(self.settings_file.get('Last Config File Used'))
        except Exception as e:
            load_defaults = True
            messagebox.showinfo(title=self.appname, message=f"No setting file found\nLoading default options")
        if load_defaults:
            try:
                self.my_config = Config()
            except Exception as e:
                messagebox.showerror(title=self.appname, message=f"No config files found code error {e}")
                self.quit()
                self.destroy()

        self.my_menu=Menu(self.master)
        self.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=0)
        self.edit_menu = Menu(self.my_menu, tearoff=0)
        self.help_menu = Menu(self.my_menu, tearoff=0)

        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", state='disabled',command=self.save_btn_action)
        self.file_menu.add_command(label="Save as...", state='disabled', command=self.save_as_btn_action)
        self.file_menu.add_command(label="Save as OF decrypted", state='disabled',command=self.save_of_decrypted_btn_action)
        self.file_menu.add_command(label="Exit", command= lambda : self.stop())

        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Export to CSV", state='disabled', command=self.export_to_csv)
        self.edit_menu.add_command(label="Import from CSV", state='disabled', command=self.import_from_csv)
        #self.edit_menu.add_command(label="Convert OF to DB (Experimental)", state='disabled', command=self.convert_of_to_db)
        self.edit_submenu = Menu(self.my_menu, tearoff=0)
        # Dinamically loading game versions as sub menu
        dinamic_menues_val = {}
        for i in range(len(self.my_config.games_config)):
            game_name = self.my_config.games_config[i]
            if ":" in game_name:
                if game_name.split(":")[0] in dinamic_menues_val:
                    
                    dinamic_menues_val[game_name.split(":")[0]].append((i, game_name.split(":")[1]))
                else:
                    dinamic_menues_val[game_name.split(":")[0]] = []
                    dinamic_menues_val[game_name.split(":")[0]].append((i, game_name.split(":")[1]))
            else:
                dinamic_menues_val[game_name] = [i, game_name]
                #
        
        
        # we add the dinamic menues now
        if len(dinamic_menues_val)>0:
            for key in dinamic_menues_val.keys():
                
                if isinstance(dinamic_menues_val.get(key)[0], int):
                    self.edit_submenu.add_command(
                        label = dinamic_menues_val.get(key)[1], 
                        command = lambda i=dinamic_menues_val.get(key)[0]: self.change_config(self.my_config.filelist[i])
                    )
                    ## aca es donde esta en el root folder, lo agregamos directamente
                else:
                    dinamic_menu = Menu(self.my_menu, tearoff=0)
                    self.edit_submenu.add_cascade(label = key, menu=dinamic_menu)
                    for item in dinamic_menues_val.get(key):
                        dinamic_menu.add_command(label=item[1], command= lambda i=item[0]: self.change_config(self.my_config.filelist[i]))
                        #self.edit_submenu.add_command(label=game_name, command= lambda i=i: self.change_config(self.my_config.filelist[i]))
        
        self.edit_menu.add_cascade(label="Game Version", menu=self.edit_submenu)

        self.my_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Manual", command=self.manual)
        self.help_menu.add_command(label="About", command=self.about)
        game_ver = self.my_config.file["Gui"]["Game Name"]
        self.title(f"{self.appname} Version: {game_ver}")
        self.tabs_container=Notebook(self)
        self.protocol('WM_DELETE_WINDOW', self.stop)

    def create_config(self):
        self.my_config = Config()

    def change_config(self, file):
        self.my_config = Config(file)
        game_ver = self.my_config.file["Gui"]["Game Name"]
        self.title(f"{self.appname} Version: {game_ver}")
        self.tabs_container.destroy()
        self.of = None
        self.file_menu.entryconfig("Save", state="disabled")
        self.file_menu.entryconfig("Save as...", state="disabled")
        self.file_menu.entryconfig("Save as OF decrypted", state="disabled")
        self.edit_menu.entryconfig("Export to CSV", state="disabled")
        self.edit_menu.entryconfig("Import from CSV", state="disabled")
        #self.edit_menu.entryconfig("Convert OF to DB (Experimental)", state="disabled")
        self.tabs_container=Notebook(self)

    def publish(self):
        """
        Method to expose the gui into the form
        """
        # Players tab placing
        
        self.players_tab.publish()

        # Clubs tab placing

        self.clubs_tab.publish()

        # Stadium Leagues tab placing

        self.stadium_league_tab.publish()

        # Shop tab placing

        self.shop_tab.publish()

        #Placing tabs and container in the root

        self.tabs_container.pack()
        #self.clubs_tab.pack(fill="both", expand=1)
        #self.stadium_league_tab.pack(fill="both", expand=1)
        #self.shop_tab.pack(fill="both", expand=1)

        self.tabs_container.add(self.players_tab, text="Players")
        self.tabs_container.add(self.clubs_tab, text="Clubs")
        self.tabs_container.add(self.stadium_league_tab, text="Stadiums & Leagues")
        self.tabs_container.add(self.logos_tab, text="Logos")
        #self.tabs_container.add(self.shop_tab, text="Shop")

        self.tabs_container.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def on_tab_change(self,event):
        tab = event.widget.tab('current')['text']
        if tab == 'Clubs':
            self.clubs_tab.refresh_gui()
        if tab == 'Players':
            self.players_tab.update_teams_cmb_values()

        #elif tab == 'Swap Teams' or tab == 'Export/Import CSV' or tab == 'Extra':
            #refresh_gui()

    def open(self):
        """
        Shows the user an interactive menu to select their afl file and then update the whole gui
        enabling widgets

        Returns:
            Bolean: Returns False if the user hits the "cancel" button, otherwise does their actions
        """
        filetypes = [
            ('All files', '*.*'),
            ("PES/WE PS2 Option File", ".psu .xps"),
            ("PES/WE PSP Option File", ".bin"),
            ("PES/WE 3DS Option File", ".dat"),
        ]

        filename = filedialog.askopenfilename(
            title=f'{self.appname} Select your option file',
            initialdir=self.last_working_dir,
            filetypes=filetypes)
        if filename == "":
            return 0
        self.last_working_dir = str(Path(filename).parents[0])
        #isencrypted = messagebox.askyesno(title=self.appname, message="Is your option file encrypted?")
        if self.of == None:
            self.of = OptionFile(filename,self.my_config.file)
        else:
            old_of = self.of
            try:
                self.of = OptionFile(filename,self.my_config.file)
            except Exception as e:
                self.of = old_of
                messagebox.showerror(
                    self.appname,
                    f"Fail to open new option file, previous option file restore, code error: {e}"
                )
        """
        try :
            f = open("./test/we2007.bin","wb")
            f.write(self.of.data)
            f.close()
            print("of desencriptado guardado")
        except Exception as e:
            print(e)
        """
        #for player in self.of.players:
            #if player.basic_settings.growth_type.get_growth_type_name() == "Unknown":
                #print(player.idx, player.name, player.basic_settings.growth_type())
        self.reload_gui_items()

    def reload_gui_items(self):
        """
        Refresh the whole gui once there's an update in one of the elements such as a new afl file or any file name change, etc

        Args:
            item_idx (int, optional): optional parameter, in case you need to keep the current selection on the listbox after the update
        """
        self.file_menu.entryconfig("Save", state="normal")
        self.file_menu.entryconfig("Save as...", state="normal")
        self.file_menu.entryconfig("Save as OF decrypted", state="normal")
        self.edit_menu.entryconfig("Export to CSV", state="normal")
        self.edit_menu.entryconfig("Import from CSV", state="normal")
        #self.edit_menu.entryconfig("Convert OF to DB (Experimental)", state="normal")
        self.tabs_container.destroy()
        self.tabs_container=Notebook(self)
        self.players_tab = PlayersTab(self.tabs_container,self.of, MAIN_WINDOW_W, MAIN_WINDOW_H, self.appname)
        self.clubs_tab = ClubTab(self.tabs_container,self.of, MAIN_WINDOW_W, MAIN_WINDOW_H, self.appname)
        self.stadium_league_tab = StadiumLeagueTab(self.tabs_container,self.of, MAIN_WINDOW_W, MAIN_WINDOW_H, self.appname)
        self.logos_tab = LogosTab(self.tabs_container,self.of, MAIN_WINDOW_W, MAIN_WINDOW_H, self.appname)
        self.shop_tab = ShopTab(self.tabs_container,self.of, MAIN_WINDOW_W, MAIN_WINDOW_H, self.appname)
        self.publish()

    def save_btn_action(self):
        try:
            #call the object method save_file
            self.of.save_option_file()
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except Exception as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin")

    def test_save_btn_action(self):
        try:
            #call the object method save_file
            with open("", "rb") as dec_of:
                self.of.data = bytearray(dec_of.read())
            self.of.save_option_file()
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except Exception as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin")


    def save_as_btn_action(self):
        try:
            new_location = filedialog.asksaveasfile(initialdir=self.last_working_dir, title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f"{self.of.extension}")
            if new_location is None:
                return 0
            self.of.save_option_file(new_location.name)
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except Exception as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")

    def save_of_decrypted_btn_action(self):
        try:
            new_location = filedialog.asksaveasfile(initialdir=self.last_working_dir, title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f"{self.of.extension}")
            if new_location is None:
                return 0
            self.of.encrypted = False
            self.of.save_option_file(new_location.name)
            self.of.encrypted = self.my_config.file['option_file_data']['ENCRYPTED']
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except Exception as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")

    def convert_of_to_db(self):
        try:
            folder_selected = filedialog.askdirectory(initialdir=self.last_working_dir,title=self.appname, )
            if folder_selected == "":
                return
            players_file = open(folder_selected + "/db.bin_000", "wb")
            for i in range(Player.first_unused):
                players_file.write(self.of.data[self.of.players[i].address : self.of.players[i].address + Player.size])
            players_file.close()
            
            national_relink = open(folder_selected + "/db.bin_001", "wb")
            temp_team = Team(self.of, 0)
            national_relink.write(self.of.data[temp_team.dorsal_start_address : temp_team.__club_dorsal_address])
            national_relink.close()

            messagebox.showinfo(title=self.appname,message=f"All changes saved at {folder_selected}")
        except Exception as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")

    def export_to_csv(self):
        
        csv_window = ExportToCSVWindow(self, self.of)
        csv_window.mainloop()
        
        """
        try:
            filetypes = [
                ("CSV Files", ".csv"),
                ('All files', '*.*'),
            ]
            
            filename = filedialog.asksaveasfile(
                initialdir=self.last_working_dir,
                title=f'{self.appname} Export to CSV', 
                mode='w', 
                filetypes=filetypes, 
                defaultextension=".csv"
            )

            if filename is None:
                return 0
            self.last_working_dir = str(Path(filename.name).parents[0])
            #print(filename.name)
            create_csv(filename.name)
            write_players(filename.name, self.of.players[1:])
            messagebox.showinfo(title=self.appname,message=f"Players exported to CSV located at {filename.name}")
        except Exception as e:
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")
        """
    def import_from_csv(self):
        try:
            filetypes = [
                ("CSV Files", ".csv"),
                ('All files', '*.*'),
            ]

            filename = filedialog.askopenfilename(
                initialdir=self.last_working_dir,
                title="Select your CSV file", 
                filetypes=filetypes
            )
            
            if filename=="":
                return 0

            self.last_working_dir = str(Path(filename).parents[0])

            # Here we call the function to load the data into the option file from csv
            load_csv(filename, self.of)
            self.players_tab.apply_player_filter()
            messagebox.showinfo(title=self.appname,message="CSV file imported")
            
        except Exception as e:
            print(e)

    def about(self):
        messagebox.showinfo(title=self.appname,message=
        """Thanks to PeterC10 for python de/encrypt code for OF and growth type values map,
        Yerry11 for png import/export
        """.replace('        ', ''))

    def manual(self):
        messagebox.showinfo(title=self.appname,message=
        r"""Maybe in the future there'll be one
        """.replace('        ', ''))

    def save_settings(self):
        settings_file_name = os.getcwd() + "/" +self.current_exe_name +".yaml"
        
        dict_file = {
            'Last Config File Used' : self.my_config.file_location,
            'Last Working Dir' : self.last_working_dir,
        }

        settings_file = open(settings_file_name, "w")
        yaml.dump(dict_file, settings_file)
        settings_file.close()

    def start(self):
        self.resizable(False, False)
        self.mainloop()

    def stop(self):
        self.save_settings()
        self.quit()
        self.destroy()








