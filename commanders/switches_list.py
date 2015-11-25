#!/usr/bin/python3

from gi.repository import Gtk
import serial
import struct

SER=serial.Serial('/dev/ttyUSB0',9600)

def ReadFile():

    switch_file=open('switches.txt','r+')
    slist=[]
    for i in switch_file:
        slist.append(i)
    return slist
    switch_file.close()

##switchlist=ReadFile()
##for i in switchlist:
##    print(i)


class SwitchWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Switch Window")
#        self.set_default_size(200,400)
        box0=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,)
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        box2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        switchlist=ReadFile()
        z=0
        for i in switchlist:
#            print ('RUNNING!!')
            a=i
            y=i
            z=z+1
            y=Gtk.Label(i.rstrip('\n'))
            i=Gtk.Switch()
            i.connect('notify::active',self.on_switch_activated,z,a)
            i.set_active(False)
            box1.pack_start(y,True,True,0)
            box1.pack_start(i,True,True,0)
        REFRESH=Gtk.Button.new_with_label('Refresh')
        box2.pack_start(REFRESH,True,True,0)
        box0.pack_start(box1,True,True,0)   
        box0.pack_start(box2,True,True,0)
        self.add(box0)

    def on_switch_activated(self,switch,gparam,z,a):
#        print(z,' ',switch.get_active())

        if switch.get_active():
            print (a,' ','ON')
            SER.write(struct.pack('>B',z))
        else:
            z=z+20
            print (a,' ','OFF')
            SER.write(struct.pack('>B',z))
win=SwitchWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
    
