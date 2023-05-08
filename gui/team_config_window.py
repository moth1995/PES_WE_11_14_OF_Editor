from tkinter import Button, Toplevel
from editor import Team
from tkinter.ttk import Notebook
from .kit_tab import KitTab
from .formation_tab import FormationTab

class TeamConfigWindow(Toplevel):

    def __init__(self, master, team:Team, team_cmb):
        super().__init__(master)
        w = 650 # width for the Tk root
        h = 600 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.team_cmb = team_cmb
        app_name = master.master.master.title()
        self.title("%s Team Config: %s" % (master.master.master.title(), team.of.teams_names[team.idx]))
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.tabs_container=Notebook(self)
        
        self.formation_tab = FormationTab(self.tabs_container,team, w, h, app_name)
        self.kit_tab = KitTab(self.tabs_container,team, w, h, app_name)
        
        self.tabs_container.pack()
        #self.tabs_container.add(self.formation_tab, text="Formation")
        self.tabs_container.add(self.kit_tab, text="Kit Config")
        
        close_btn = Button(self, text="Close", command=self.stop_window)
        close_btn.pack()

        self.focus_force()
        self.lift()
        self.grab_set()
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.stop_window)

    def stop_window(self):
        self.team_cmb.event_generate("<<ComboboxSelected>>")
        self.quit()
        self.destroy()

