from pathlib import Path
from tkinter import Button, Checkbutton, IntVar, Label, LabelFrame, Toplevel, filedialog, messagebox
from tkinter.ttk import Combobox

from editor.csv_exporter import create_csv, write_players

class ExportToCSVWindow(Toplevel):

    def __init__(self, master, of):
        super().__init__(master)
        self.of = of
        w = 300 # width for the Tk root
        h = 150 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.appname = master.title()
        self.last_working_dir = master.last_working_dir
        self.title("%s Export to CSV" % (master.title()))
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        
        frame = LabelFrame(self, text="Export to CSV")
        frame.pack()
        
        self.include_unused_var = IntVar(frame, 1)
        Checkbutton(frame, text="Include Unused?", variable=self.include_unused_var).grid(row=6,column=0,columnspan=2)
        self.include_edited_var = IntVar(frame, 1)
        Checkbutton(frame, text="Include Edited?", variable=self.include_edited_var).grid(row=6,column=0,columnspan=2)
        
        Label(frame,text="Select Team").grid(row=0,column=0,)
        self.team_name_cmb = Combobox(frame, values=self.of.teams_names, state="readonly")
        self.team_name_cmb.grid(row=0,column=1)
        self.team_name_cmb.current(0)
        
        
        
        Button(
            frame, 
            text="Export team", 
            command = lambda: self.export_to_csv(1)
        ).grid(row=1,column=0, columnspan=2)
        
        Button(
            frame, 
            text="Export all players", 
            command=lambda : self.export_to_csv(2)
        ).grid(row=5,column=0,columnspan=2)


        

        self.focus_force()
        self.lift()
        self.grab_set()
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.stop_window)


    def export_to_csv(self, type):
        try:
            filetypes = [
                ("CSV Files", ".csv"),
                ('All files', '*.*'),
            ]
            
            filename = filedialog.asksaveasfile(master=self,
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
            players = []
            if type == 1:
                if self.include_edited_var.get() and self.include_unused_var.get():
                    players = [player for player in self.of.teams[self.team_name_cmb.current()].players if player is not None]
                    
                elif self.include_edited_var.get() and not self.include_unused_var.get():
                    players = [player for player in self.of.teams[self.team_name_cmb.current()].players if player is not None and not player.is_unused]
                    
                elif not self.include_edited_var.get() and self.include_unused_var.get():
                    players = [player for player in self.of.teams[self.team_name_cmb.current()].players if player is not None and not player.is_edit]
                    
                elif not self.include_edited_var.get() and not self.include_unused_var.get():
                    players = [player for player in self.of.teams[self.team_name_cmb.current()].players if player is not None and not player.is_edit and not player.is_unused]
            if type == 2:
                player_list = self.of.players[1:] + self.of.edited_players
                if self.include_edited_var.get() and self.include_unused_var.get():
                    players = [player for player in player_list if player is not None]
                    
                elif self.include_edited_var.get() and not self.include_unused_var.get():
                    players = [player for player in player_list if player is not None and not player.is_unused]
                    
                elif not self.include_edited_var.get() and self.include_unused_var.get():
                    players = [player for player in player_list if player is not None and not player.is_edit]
                    
                elif not self.include_edited_var.get() and not self.include_unused_var.get():
                    players = [player for player in player_list if player is not None and not player.is_edit and not player.is_unused]

            write_players(filename.name, players)
            messagebox.showinfo(parent=self, title=self.appname,message=f"Players exported to CSV located at {filename.name}")
        except Exception as e:
            messagebox.showerror(parent=self, title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")


    def stop_window(self):
        self.quit()
        self.destroy()

