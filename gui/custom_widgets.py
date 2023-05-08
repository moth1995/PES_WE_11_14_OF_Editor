from tkinter import Canvas, Scrollbar, Tk, Label, Frame
from PIL import ImageTk, Image, ImageDraw
import os, sys
from editor.utils.constants import *

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

class FormationExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        pes_coordinates = [9, 63, 9, 41, 12, 87, 12, 17, 26, 77, 26, 61, 26, 43, 26, 
            27, 43, 66, 43, 38,]
        
        gk_coordinate = [2, 51]
        pes_coordinates = gk_coordinate + pes_coordinates
        original_width = 50
        original_heigh = 100
        factor = 5
        field = Image.open(resource_path("resources/img/field_1.png")).convert("RGB")

        f = FormationFrame(self, field, original_width, original_heigh, factor, pes_coordinates)
        f.pack()


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

class FormationFrame(Frame):
    def __init__(self, parent, field:Image, width:int, height:int, factor:int, pes_coordinates:"list[int]"):
        super().__init__(parent)
        self.selected_item = None

        self.factor = factor
        self.new_width = width * self.factor
        self.new_heigh = height * self.factor
        field = field.resize((self.new_width, self.new_heigh))
        self.field = ImageTk.PhotoImage(field)

        self.my_canvas = Canvas(self, width=self.new_width, heigh=self.new_heigh, bg="white")
        self.my_canvas.pack(pady=20)
        # creating the field first
        self.my_canvas.create_image(self.new_width/2, self.new_heigh/2, image=self.field, tags=f"field")
        # lets load the image for the dot
        #self.load_dots(pes_coordinates[PLAYERS_IN_TEAM*2:])
        self.load_formation(pes_coordinates)
        self.my_canvas.bind("<B1-Motion>", self.__drag_and_drop)
        self.my_canvas.bind("<Button-1>", self.__on_click)
        #print(self.get_pes_coord())

    def __get_arrows_coords(self):
            arrow_coords = []
            
            return arrow_coords

    def create_dot(self, canvas:Canvas):
        # Define the size of the circle and arrows
        circle_radius = 50
        arrow_size = 60
        # Define the color of the circle
        circle_color = "#FF0000"
        # Draw the circle
        circle_center_x = circle_radius + arrow_size
        circle_center_y = circle_radius + arrow_size
        circle_bbox = (circle_center_x - circle_radius, circle_center_y - circle_radius, circle_center_x + circle_radius, circle_center_y + circle_radius)
        canvas.create_oval(circle_bbox, fill=circle_color, outline="", tags="shape")

        # Draw the arrows
        arrow_coords = [
            (circle_center_x, circle_center_y - circle_radius - arrow_size, circle_center_x, circle_center_y - circle_radius),
            (circle_center_x, circle_center_y + circle_radius, circle_center_x, circle_center_y + circle_radius + arrow_size),
            (circle_center_x - circle_radius - arrow_size, circle_center_y, circle_center_x - circle_radius, circle_center_y),
            (circle_center_x + circle_radius, circle_center_y, circle_center_x + circle_radius + arrow_size, circle_center_y),
            (circle_center_x - int(circle_radius*0.7), circle_center_y - int(circle_radius*0.7), circle_center_x - int(circle_radius*0.7) - arrow_size, circle_center_y - int(circle_radius*0.7) - arrow_size),
            (circle_center_x + int(circle_radius*0.7), circle_center_y - int(circle_radius*0.7), circle_center_x + int(circle_radius*0.7) + arrow_size, circle_center_y - int(circle_radius*0.7) - arrow_size),
            (circle_center_x - int(circle_radius*0.7), circle_center_y + int(circle_radius*0.7), circle_center_x - int(circle_radius*0.7) - arrow_size, circle_center_y + int(circle_radius*0.7) + arrow_size),
            (circle_center_x + int(circle_radius*0.7), circle_center_y + int(circle_radius*0.7), circle_center_x + int(circle_radius*0.7) + arrow_size, circle_center_y + int(circle_radius*0.7) + arrow_size)
        ]
        for arrow in arrow_coords:
            canvas.create_line(arrow, width=6)

        # Add text to the center of the circle
        text = "5"
        font = ("Arial", 30)
        canvas.create_text(circle_center_x, circle_center_y, text=text, font=font, fill="white")


    def load_dots(self, positions_idx):
        self.imgs = []
        self.pos_names = []
        for i in range(PLAYERS_IN_TEAM):
            pos_name = self.position_to_string(positions_idx[i])
            self.pos_names.append(pos_name)
            img = Image.open(resource_path("resources/img/circle.png")).convert("RGBA")
            img = img.resize((20,20))
            temp_draw = ImageDraw.Draw(img)
            # Add Text to an image
            temp_draw.text((4 if len(pos_name)==2 else 2, 5), pos_name, fill=(255, 255, 255))
            self.imgs.append(ImageTk.PhotoImage(img))

    def load_formation(self, form_data:tuple):
        # first we delete the already created tags
        #print(form_data)
        for i in range(PLAYERS_IN_TEAM):
            self.my_canvas.delete("dot_%d" % i)
        self.load_dots(form_data[PLAYERS_IN_TEAM*2:])
        new_coordinates = form_data[:PLAYERS_IN_TEAM*2]
        self.coordinates = [self.__pes_coord_to_coordinates(new_coordinates[i], new_coordinates[i+1]) for i in range(0, len(new_coordinates), 2)]
        
        #print(self.coordinates)
        for i, coordinate in enumerate(self.coordinates):
            # las coordenadas se envian invertidas a como aparecen en el pes para coincidir con nuestro field
            self.my_canvas.create_image(coordinate[0], coordinate[1], image=self.imgs[i], tags=f"dot_{i}")
        
        """
        # create dots using image draw maybe useful for the future
        im = Image.new('RGBA', (22, 22), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.ellipse((5, 5, 20, 20), fill=(255, 0, 0), outline=(0, 0, 0))
        draw.text((4,5), text="RM", fill=(255, 255, 255))
        self.img = ImageTk.PhotoImage(im)
        self.my_canvas.create_image(50,50, image=self.img, tags="dot_12")
        """
        
    def position_to_string(self, pos:int):
        if (pos <= 0):
            return "GK"
        elif (pos < 4 or (pos > 5 and pos < 8)):
            return "CB"
        elif (pos == 4):
            return "CWP"
        elif (pos == 5):
            return "CWP"
        elif (pos == 8):
            return "LB"
        elif (pos == 9):
            return "RB"
        elif (pos < 15):
            return "DMF"
        elif (pos == 15):
            return "LWB"
        elif (pos == 16):
            return "RWB"
        elif (pos < 22):
            return "CMF"
        elif (pos == 22):
            return "LMF"
        elif (pos == 23):
            return "RMF"
        elif (pos < 29):
            return "AMF"
        elif (pos == 29):
            return "LWF"
        elif (pos == 30):
            return "RWF"
        elif (pos < 36):
            return "SS"
        elif (pos < 41):
            return "CF"
        return "pos"

    def __pes_coord_to_coordinates(self, y:int, x:int):
        new_x = float(x * self.factor / 2)
        new_y = float((self.new_width - y * self.factor ) * 2)
        return [new_x, new_y]

    """
    current_x = x * self.factor / 2
    2 * current_x / self.factor = x    

    current_y = (self.new_width - y * self.factor ) * 2
    (current_y /2 - self.new_width) / - self.factor = y

    """


    def __coord_to_pes_coordinates(self, x:float, y:float):
        x = int(2 * (x) / self.factor)
        y = int((y /2 - (self.new_width)) / - self.factor)
        return [x,y]

    def get_pes_coord(self):
        pes_coordinates = []
        for coord in self.coordinates:
            pes_coord = self.__coord_to_pes_coordinates(coord[0], coord[1])
            pes_coordinates.append(pes_coord[1])
            pes_coordinates.append(pes_coord[0])
        return tuple(pes_coordinates)

    def __drag_and_drop(self, event):
        tag=self.my_canvas.gettags("current")[0]
        old_pos = (self.my_canvas.coords(tag))
        dx, dy = event.x - old_pos[0], event.y - old_pos[1]
        new_x, newy = dx + old_pos[0], dy + old_pos[1]
        # if the new coordinates are inside the image range then we move it
        # but also we need to prevent from moving the field and the gk dot!
        if self.__coordinates_in_range(new_x, newy) and tag != "field" and tag!="dot_0" and self.selected_item!= None: 
            # move the selected item
            self.my_canvas.move(tag, dx, dy)
            self.coordinates[self.selected_item] = [new_x, newy]

    def __on_click(self, event):
        tag=self.my_canvas.gettags("current")[0]
        if tag!="field":
            self.selected_item = int(tag.strip("dot_"))
        else:
            self.selected_item = None
        self.event_generate("<<DotSelected>>")

    def __coordinates_in_range(self, new_x:float, new_y:float):
        return 15<new_x<236 and 15<new_y<476

    def __coordinates_in_dot_range(self, new_x:float, new_y:float, dot_x_range:"list[int,int]", dot_y_range:"list[int,int]"):
        return dot_x_range[0]<new_x<dot_x_range[1] and dot_y_range[0]<new_y<dot_y_range[1]

if __name__ == "__main__":
    #app = TableExampleApp()
    app = FormationExampleApp()
    app.geometry("800x600")
    app.mainloop()