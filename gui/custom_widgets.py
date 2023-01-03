from tkinter import Canvas, Tk, Label, Frame, PhotoImage
from PIL import ImageTk, Image
from tkinter import Canvas, Scrollbar, Tk, Label, Frame
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class TableExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        t = Table(self, 32,3)
        t.place(x=30, y=20)
        t.set(0,0,"Hello, world")
        t.set_column_width(0, 3)
        t.set_column_width(1, 3)
        t.set_column_width(2, 20)
        t.set_row(3,["CB", "3", "Schiavi"])

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



class Table(Frame):
    def __init__(self, parent, rows=10, columns=2, default_text=""):
        # use black background so it "peeks through" to 
        # form grid lines
        super().__init__(parent, background="black", highlightbackground="black", highlightthickness=1)
        self._widgets = []
        self.selected_row = None
        self.total_rows = rows
        self.total_columns = columns
        for row in range(self.total_rows):
            current_row = []
            bg_colour = "#ffffff" if row<11 else "#d0d5db"
            for column in range(self.total_columns):
                label = Label(
                    self, 
                    text = default_text,#text="%s/%s" % (row, column), 
                    borderwidth = 0, 
                    height = 1, 
                    width = 10, 
                    activebackground = "#0078d7", 
                    background = bg_colour, 
                    relief = "solid", 
                    anchor = 'nw'
                )
                label.bind("<Button-1>", self.on_left_click)
                label.bind("<Double-Button-1>", self.on_double_click)
                label.bind("<Button-3>", self.on_right_click)
                label.grid(row=row, column=column, sticky="nsew")#, padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def on_left_click(self, e):
        selected_row = e.widget.grid_info()['row']
        for row in range(self.total_rows):
            bg_colour = "#ffffff" if row<11 else "#d0d5db"
            for w in self.grid_slaves(row=row):
                if row == selected_row:
                    w.config(background= w['activebackground'])
                    w.config(fg="#ffffff")
                    self.selected_row = selected_row
                else:
                    w.config(background = bg_colour)
                    w.config(fg="#000000")
        self.event_generate("<<LeftClic>>")

    def on_double_click(self, e):
        self.event_generate("<<DoubleClic>>")

    def on_right_click(self, e):
        self.event_generate("<<RightClic>>")


    def set(self, row:int, column:int, value:int):
        widget = self._widgets[row][column]
        widget.config(text=value)

    def set_row(self, row:int, list_of_values:list):
        if len(list_of_values) != self.total_columns:
            raise ValueError("Values delivered doesn't match the total of columns")
        for column in range(self.total_columns):
            self.set(row, column, list_of_values[column])

    def set_column_width(self, column:int, value:int):
        for row in range(self.total_rows):
            widget = self._widgets[row][column]
            widget.config(width=value)

    def get_selected_row(self):
        if self.selected_row is None:
            raise IndexError("You haven't select any row")
        return self.get_row(self.selected_row)

    def get_row(self, row:int):
        return [self._widgets[row][column]['text'] for column in range(self.total_columns)]

    def get(self):
        return [self.get_row(row) for row in range(self.total_rows)]

class Coordinates():
    def __init__(self, x:int, y:int, factor:int, width:int, heigh:int):
        #self.x = x * factor *2
        #self.y = heigh * factor - y  * factor /2
        self.x = x * factor / 2
        self.y = (width - y) * factor * 2
        self.factor = factor
        self.width = width
        self.heigh = heigh

    def normalize_for_pes(self):
        self.x = int(self.x / self.factor)
        self.y = int((self.y - (self.heigh * self.factor)) / -self.factor)

class FormationExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        original_width = 50
        original_heigh = 100
        factor = 5
        new_width = original_width * factor
        new_heigh = original_heigh * factor
        self.my_canvas = Canvas(self, width=new_width, heigh=new_heigh, bg="white")
        self.my_canvas.pack(pady=20)
        
        field = Image.open(resource_path("resources/img/field_1.png")).convert("RGB")
        field = field.resize((new_width, new_heigh))
        self.field = ImageTk.PhotoImage(field)
        self.my_canvas.create_image(new_width/2, new_heigh/2, image=self.field)
        img = Image.open(resource_path("resources/img/circle.png")).convert("RGB")
        img = img.resize((20,20))
        self.img = ImageTk.PhotoImage(img)
        
        pes_coordinates = [9, 63, 9, 41, 12, 87, 12, 17, 26, 77, 26, 61, 26, 43, 26, 
            27, 43, 66, 43, 38,]
        
        gk_coordinate = [2, 51]
        pes_coordinates = gk_coordinate + pes_coordinates
        coordinates = [
            Coordinates(
                pes_coordinates[pes_coordinate+1], 
                pes_coordinates[pes_coordinate], 
                factor, 
                original_width, 
                original_heigh,
            ) 
            for pes_coordinate in range(0,len(pes_coordinates),2)
        ]
                    

        for coordinate in coordinates:
            self.my_canvas.create_image(coordinate.x, coordinate.y, image=self.img)



if __name__ == "__main__":
    #app = TableExampleApp()
    app = FormationExampleApp()
    app.geometry("800x600")
    app.mainloop()