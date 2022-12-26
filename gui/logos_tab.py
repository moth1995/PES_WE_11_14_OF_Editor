from tkinter import Button, Frame, Toplevel, filedialog, messagebox
from editor import PESImg, OptionFile

class LogosTab(Frame):
    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.load_logos()

    def load_logos(self):
        fila = 0
        columna = 0
        for i in range(len(self.of.logos_tk)):
            if columna > 9:
                columna= 0
                fila += 1
            newButton = Button(self, image=self.of.logos_tk[i], width=54, height=54, command=lambda logo_idx=i:self.on_click(logo_idx))
            newButton.grid(column=columna, row=fila)
            columna += 1

    def remove_widget(self):
        for widget in self.winfo_children():
            widget.destroy()

    def on_click(self,i):
        self.window = Toplevel(self)
        w = 300 # width for the Tk root
        h = 100 # height for the Tk root
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.import_btn = Button(self.window, text="Import PNG", command=lambda : self.open_png(i))
        self.import_btn.pack()
        self.export_btn = Button(self.window, text="Export as PNG", command=lambda : self.write_png(self.of.logos_png[i].png))
        self.export_btn.pack()
        self.delete_btn = Button(self.window, text="Delete Logo", command=lambda : self.remove_logo(i))
        self.delete_btn.pack()
        self.window.grab_set()
        self.window.resizable(False, False)
        self.window.mainloop()

    def open_png(self,i):
        png_location = filedialog.askopenfilename(initialdir=".",title="Open a PNG file", filetypes=(("PNG files","*.png"),("All files", "*")))
        if png_location == "":
            return 0
        with open(png_location, "rb") as png_f:
            pes_img = PESImg(bytearray(png_f.read()))
        if pes_img.width != 32 or pes_img.height != 32 or pes_img.bpp!=4:
            messagebox.showerror(title = self.appname, message = "Image must be 32x32 and 16 colours indexed")
            return 0
        self.of.logos[i].update_logo(pes_img.pes_palette, pes_img.pes_idat)
        self.reload_logos()

    def write_png(self,img_bytes):
        file = filedialog.asksaveasfile(initialdir=".",title="Save as PNG", mode='wb', filetypes=(("PNG files","*.png"),("All files", "*")), defaultextension=".png")
        if file is None:
            return 0
        with open(file.name,'wb') as img:
            img.write(img_bytes)
        messagebox.showinfo(title = self.appname, message = f"Image exported successfully at {file.name}")


    def remove_logo(self,i):
        self.of.logos[i].delete_logo()
        self.reload_logos()

    def reload_logos(self):
        self.of.set_logos()
        self.remove_widget()
        self.load_logos()
