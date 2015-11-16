#!/usr/bin/python3

from gi.repository import Gtk
import serial


##SER=serial.Serial(None,9600)
SER=serial.Serial('/dev/ttyUSB0',9600)

UP=Gtk.Image.new_from_file('./arrow-up.png')
DOWN=Gtk.Image.new_from_file('./arrow-down.png')
LEFT=Gtk.Image.new_from_file('./arrow-left.png')
RIGHT=Gtk.Image.new_from_file('./arrow-right.png')

class NumGridWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="This")
        hb=Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title='Bot Commander 0.2'
        self.set_titlebar(hb)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)
        self.connect("key-press-event", self.key_watch)
        self.connect("key-release-event", self.key_watch_release)
        box0=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid0=Gtk.Grid()
        bt0=Gtk.Button.new_with_label("0")
        bt0.connect("clicked", self.clicked,0)
        row=0
        column=0
        for i in range (1,10):
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
            i.connect("pressed",self.clicked,y)
            i.connect("released",self.clicked,y)
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
        if y==8:
            print('UP')
            try:
                SER.write(b'1')
            except ValueError:
                print('Using Port None!')
        elif y==2:
            print('DOWN')
            try:
               SER.write(b'2')
            except ValueError:
                print('Using Port None!')
        elif y==4:
            print('LEFT')
            try:
                SER.write(b'3')
            except ValueError:
                print('Using Port None!')
        elif y==6:
            print('RIGHT')
            try:
                SER.write(b'4')
            except ValueError:
                print('Using Port None!')
        elif y==0:
            print('STOP')
            try:
                SER.write(b'0')
            except ValueError:
                print('Using Port None!')
        else:
            print(y)
            try:
                SER.write(b'0')
            except ValueError:
                print('Using Port None!')

    def key_watch(self,widget,event):

        if event.keyval==65362:
            SER.write(b'1')
        elif event.keyval==65364:
            SER.write(b'2')
        elif event.keyval==65361:
            SER.write(b'3')
        elif event.keyval==65363:
            SER.write(b'4')

    def key_watch_release(self,widget,event):
        bit=((event.keyval)-65300)
        if bit==62:
            SER.write(b'5')
        if bit ==64:
            SER.write(b'6')
        if bit==61:
            SER.write(b'7')
        if bit==63:
            SER.write(b'8')
##
##            print(bit)


numgrid=NumGridWin()
numgrid.connect("delete-event", Gtk.main_quit)
numgrid.show_all()
Gtk.main()
