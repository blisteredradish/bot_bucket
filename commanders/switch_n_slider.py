 #!/usr/bin/python3
import serial

SER=serial.Serial('/dev/ttyUSB0',9600)

##SER=serial.Serial('/dev/ttyACM0',9600)

from gi.repository import Gtk

class Switch(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Switch 2000')
        self.set_border_width(10)
        self.set_default_size(200,50)

        box0=Gtk.Box(spacing=10)
        grid0=Gtk.Grid()

        ad1=Gtk.Adjustment(255,1,255,15,10,0)
        
        switch0=Gtk.Switch()
        switch0.connect('notify::active',self.on_switch_activated)
        switch0.set_active(False)

        self.scale1=Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        self.scale1.set_hexpand(True)
        self.scale1.connect('value-changed', self.scale1_moved)
        
        grid0.attach(switch0,0,0,1,1)
        grid0.attach(self.scale1,0,1,1,1)

        box0.pack_start(grid0,True,True,0)
        self.add(box0)

    def on_switch_activated(self,switch,gparam):
        if switch.get_active():
            state="on"
            SER.write(b'1')
        else:
            state="off"
            SER.write(b'0')
        print('switch ',state)

    def scale1_moved(self,event):
        value=int(self.scale1.get_value())
        print(value)
        
        SER.write(bytes([value]))

swin=Switch()
swin.connect('delete-event',Gtk.main_quit)
swin.show_all()
Gtk.main()
