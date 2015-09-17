__author__ = 'jonas'

# My new project :)
from gi.repository import Gtk, Gio

class NumPad(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        grid = Gtk.Grid()
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
        for i in range(1,4):
            for j in range(1,4):
                button = Gtk.Button(label = 3 * (j-1) + i)
                grid.attach(button,i,j,1,1)

        button = Gtk.Button(label = "-")
        grid.attach(button,2,5,1,1)
        self.add(grid)

class Tile(Gtk.Button):

    def __init__(self, tileText, posx, posy):
        Gtk.Button.__init__(self)
        self.set_label(tileText)
        self.position = (posx, posy)
        self.connect("clicked", self.on_clicked)

    def getposition(self):
        return (self.position)

    def on_clicked(self, widget):
        print(self)

    def __repr__(self):
        return "Tile (%i,%i)" % (self.getposition())

class Square(Gtk.Box):
    def __init__(self, offx, offy, tiles_list):
        Gtk.Box.__init__(self)
        grid = Gtk.Grid()
        for i in range(1,4):
            for j in range(1,4):
                tile = Tile("",3 * (offx - 1) + i, 3 * (offy - 1) + j)
                tiles_list.append(tile)
                grid.attach(tile,i,j,1,1)
        self.add(grid)

class SudokuSenseWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(30)
        self.set_default_size(400, 200)
        self.tiles = []
        print(self.tiles)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Sudoku Sense"
        self.set_titlebar(hb)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        hb.pack_start(box)

        MainGrid = Gtk.Grid()
        MainGrid.set_row_spacing(8)
        MainGrid.set_column_spacing(8)
        self.add(MainGrid)

        TileGrid = Gtk.Grid()
        TileGrid.set_row_spacing(3)
        TileGrid.set_column_spacing(3)
        MainGrid.add(TileGrid)

        for i in range(1, 4):
            for j in range(1, 4):
                square = Square(i,j, self.tiles)
                TileGrid.attach(square,i,j,1,1)

        ButtonGrid = Gtk.Grid()
        ButtonGrid.set_row_spacing(8)
        ButtonGrid.set_column_spacing(3)
        MainGrid.add(ButtonGrid)

        button_list_tiles = Gtk.Button(label = "List tiles")
        button_list_tiles.connect("clicked", self.on_clicked_list)
        ButtonGrid.attach(button_list_tiles,1,41,1,1)

        button_setup = Gtk.Button(label = "Setup")
        ButtonGrid.attach(button_setup,1,1,1,1)

        button_setup = Gtk.Button(label = "Clear")
        ButtonGrid.attach(button_setup,1,2,1,1)

        button_setup = Gtk.Button(label = "Done")
        ButtonGrid.attach(button_setup,1,3,1,1)

        numPad = NumPad()
        ButtonGrid.attach(numPad,1,4,1,1)

    def on_clicked_list(self, widget):
        print(self.tiles)

win = SudokuSenseWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
