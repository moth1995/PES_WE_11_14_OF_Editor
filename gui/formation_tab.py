from tkinter import Frame
from editor import Team

class FormationTab(Frame):
    

    def __init__(self, master, team:Team, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.team = team
        self.appname = appname
