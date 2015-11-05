#!/usr/bin/python

from gi.repository import Gtk

class NumGridWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="This")

        box0=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid0=Gtk.Grid()
        bt0=Gtk.Button.new_with_label("0")
        row=0
        column=0
        for i in range (1,10):
            y=i
            i=Gtk.Button.new_with_label('{}'.format(y))
            grid0.attach(i, column,-row,1,1)
            column=column+1
            if column==3:
                column=0
                row=row+1
        row=row+1
        grid0.attach(bt0,1,row,1,1)
        box0.add(grid0)
        self.add(box0)
            


numgrid=NumGridWin()
numgrid.connect("delete-event", Gtk.main_quit)
numgrid.show_all()
Gtk.main()
