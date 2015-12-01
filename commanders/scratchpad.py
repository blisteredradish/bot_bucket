import serial
from gi.repository import Gtk
SER=serial.Serial('/dev/ttyUSB0',9600)
x='25'
class ThisWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='ThisWindow')
        self.set_default_size(200,200)
        button0=Gtk.Button.new_with_label('send')
        button0.connect("clicked",self.on_clicked)
        self.add(button0)

    def on_clicked(self,widget):
        print (x)
        SER.write(x.encode())

win=ThisWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
