#!/usr/bin/python

from gi.repository import Gtk
import serial
import struct
SER=serial.Serial('/dev/ttyUSB0',9600)

UP=Gtk.Image.new_from_file('./arrow-up.png')
DOWN=Gtk.Image.new_from_file('./arrow-down.png')
LEFT=Gtk.Image.new_from_file('./arrow-left.png')
RIGHT=Gtk.Image.new_from_file('./arrow-right.png')

class NumGridWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="This")

        box0=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid0=Gtk.Grid()
        bt0=Gtk.Button.new_with_label("0")
        bt0.connect("clicked", self.clicked,0)
        row=0
        column=0
        for i in range (1,22):
            y=i
            if y==8:
                i=Gtk.Button(None,image=UP)
            elif y==2:
                i=Gtk.Button(None,image=DOWN)
            elif y==4:
                i=Gtk.Button(None,image=LEFT)
            elif y==6:
                i=Gtk.Button(None,image=RIGHT)
            else:
                i=Gtk.Button.new_with_label('{}'.format(y))
            i.connect("clicked",self.clicked,y)
            grid0.attach(i, column,-row,1,1)
            column=column+1
            if column==3:
                column=0
                row=row+1
        row=row+1
        grid0.attach(bt0,1,row,1,1)
        box0.add(grid0)
        self.add(box0)

    def clicked(self,widget,y):
        print (y)
        SER.write(struct.pack('>B',y))


numgrid=NumGridWin()
numgrid.connect("delete-event", Gtk.main_quit)
numgrid.show_all()
Gtk.main()
