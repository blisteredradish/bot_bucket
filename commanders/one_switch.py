#!/usr/bin/python3
import serial

SER=serial.Serial('/dev/ttyUSB0',9600)

##SER=serial.Serial('/dev/ttyACM0',9600)

from gi.repository import Gtk

class Switch(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Switch 2000')
        self.set_border_width(10)

        box0=Gtk.Box(spacing=10)
        self.add(box0)

        switch0=Gtk.Switch()
        switch0.connect('notify::active',self.on_switch_activated)
        switch0.set_active(False)
        box0.pack_start(switch0,True,True,0)

    def on_switch_activated(self,switch,gparam):
        if switch.get_active():
            state="on"
            SER.write(b'1')
        else:
            state="off"
            SER.write(b'0')
        print('switch ',state)
        

swin=Switch()
swin.connect('delete-event',Gtk.main_quit)
swin.show_all()
Gtk.main()
