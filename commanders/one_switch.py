#!/usr/bin/python3
import serial

##SER=serial.Serial('/dev/ttyUSB0',9600)
SER=serial.Serial(None,9600)
##SER=serial.Serial('/dev/ttyACM0',9600)

MAX_SWITCH=5

from gi.repository import Gtk

class Switch(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Switch 2000')
        self.set_border_width(10)

        box0=Gtk.Box(spacing=10,orientation=Gtk.Orientation.VERTICAL)
        
        
        self.add(box0)

##        switch0=Gtk.Switch()
##        switch0.connect('notify::active',self.switch_0_activated)
##        switch0.set_active(False)

        for i in range(1,MAX_SWITCH):
            z=i
            y=Gtk.Label(i)
            i=Gtk.Switch()
            i.connect('notify::active',self.switch_0_activated,z)
            i.set_active(False)
            box0.pack_start(y,True,True,0)
            box0.pack_start(i,True,True,0)

    def switch_0_activated(self,switch,gparam,z):
        if switch.get_active():
            state="on"
##            SER.write(b'1')
        else:
            state="off"
##            SER.write(b'0')
        print('switch ',z,state)

        
        

swin=Switch()
swin.connect('delete-event',Gtk.main_quit)
swin.show_all()
Gtk.main()
