__author__ = 'jonas'

# Main Program for this project

from gi.repository import Gtk, Gio
from appLogic import Sudoku

class NumPad(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.currentSymbol = "-"
        grid = Gtk.Grid()
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
        for i in range(1,4):
            for j in range(1,4):
                button = Gtk.Button(label = 3 * (j-1) + i)
                button.connect("clicked", self.on_clicked_numpad)
                grid.attach(button,i,j,1,1)

        button = Gtk.Button(label = "-")
        button.connect("clicked", self.on_clicked_numpad)
        grid.attach(button,2,5,1,1)
        self.add(grid)

    def on_clicked_numpad(self, widget):
        self.currentSymbol = widget.get_label()
        print(self.currentSymbol)

    def get_current_symbol(self):
        return self.currentSymbol

class Tile(Gtk.Button):

    def __init__(self, tileText, posx, posy, win):
        Gtk.Button.__init__(self)
        self.set_alignment(0,0)
        self.set_label(tileText)
        self.position = (posx, posy)
        self.numpad = win.numpad
        self.connect("clicked", self.on_clicked)

    def getposition(self):
        return (self.position)

    def on_clicked(self, widget):
        widget.set_label(self.numpad.currentSymbol)
        (ax, ay) = widget.get_alignment()
        print("AX: %  AY: %", ax, ay)
        # print(self.numpad.currentSymbol)
        # print(self)
        # print(widget)

    def __repr__(self):
        return "Tile (%i,%i)" % (self.getposition())

class Square(Gtk.Box):
    def __init__(self, offx, offy, win):
        Gtk.Box.__init__(self)
        grid = Gtk.Grid()
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
        for i in range(1,4):
            for j in range(1,4):
                tile = Tile("-",3 * (offx - 1) + i, 3 * (offy - 1) + j, win)
                win.tiles.append(tile)
                grid.attach(tile,i,j,1,1)
        self.add(grid)

class SudokuSenseWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(30)
        self.set_default_size(400, 200)
        self.tiles = []
        self.setup = False
        self.sudoku = Sudoku()
        print(self.tiles)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Sudoku Sense"
        self.set_titlebar(hb)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        hb.pack_start(box)

        self.numpad = NumPad()
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
                square = Square(i,j, self)
                TileGrid.attach(square,i,j,1,1)

        ButtonGrid = Gtk.Grid()
        ButtonGrid.set_row_spacing(8)
        ButtonGrid.set_column_spacing(3)
        MainGrid.add(ButtonGrid)

        self.button_setup = Gtk.Button(label = "Setup")
        self.button_setup.connect("clicked", self.on_clicked_setup)
        ButtonGrid.attach(self.button_setup,1,1,1,1)
        print(dir(self.button_setup))

        self.button_clear = Gtk.Button(label = "Clear")
        self.button_clear.connect("clicked", self.on_clicked_clear)
        ButtonGrid.attach(self.button_clear,1,2,1,1)

        self.button_done = Gtk.Button(label = "Done")
        self.button_done.connect("clicked", self.on_clicked_done)
        ButtonGrid.attach(self.button_done,1,3,1,1)

        # self.numpad = NumPad()
        ButtonGrid.attach(self.numpad,1,4,1,1)

    def refreshSudoku(self):
        self.sudoku.getstatus()
        for i in range(1,4):
            for j in range(1,4):
                self.sudoku.gettile(i,j)

    def on_clicked_setup(self, widget):
        print("setup")
        if self.setup:
            self.setup = False
            widget.set_label("Setup")
        else:
            self.setup = True
            widget.set_label("Save")
        self.refreshSudoku()

    def on_clicked_clear(self, widget):
        print("clear")
        self.sudoku.clear_tiles(all = True)
        self.refreshSudoku()

    def on_clicked_done(self, widget):
        print("done")
        Gtk.main_quit()

win = SudokuSenseWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
