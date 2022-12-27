from pathlib import Path
from tkinter import Button, IntVar, LabelFrame, Radiobutton, Toplevel, filedialog, messagebox

class FaceHairFolderWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master)
        w = 300 # width for the Tk root
        h = 170 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.title("Select Face/Hair Folder")
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.last_working_dir = master.last_working_dir
        self.appname = master.appname
        self.folder_selected = ""
        self.players_tab = master.players_tab

        frame = LabelFrame(self, text="Face/Hair Folder Options")
        frame.pack()
        self.platform = IntVar(self, self.players_tab.face_hair_version)

        select_folder_btn = Button(frame, text="Select your Face/Hair Folder", command=self.select_folder_btn_clicked)
        select_folder_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # Dictionary to create multiple buttons
        values = {
                "PS2" : 0,
                "PSP" : 1,
            }
        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        col_counter = 0
        for (text, value) in values.items():
            Radiobutton(frame, text = text, variable = self.platform,
            value = value, indicator = -1).grid(row=1, column=col_counter,padx=10, pady=10)
            col_counter+=1

        Button(frame, text="Close", command=lambda: self.stop_window()).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.focus_force()
        self.lift()
        self.grab_set()
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.stop_window)

    def select_folder_btn_clicked(self):
        try:
            self.folder_selected = filedialog.askdirectory(parent= self, initialdir=self.last_working_dir,title=self.appname, )
            if self.folder_selected == "":
                return
            self.players_tab.has_face_hair_folder = True
            self.players_tab.face_hair_folder = self.folder_selected
        except Exception as e:
            messagebox.showerror(parent= self, title=self.appname,message=f"Error while trying to select your folder, error type={e}, try a different location")



    def stop_window(self):
        self.players_tab.face_hair_version = self.platform.get()
        self.quit()
        self.destroy()

