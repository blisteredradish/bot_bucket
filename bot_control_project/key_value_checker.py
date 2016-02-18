#!/usr/bin/python3

from gi.repository import Gtk

class KeyCheckWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Key Checker')
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(300,300)
        box0=Gtk.Box()
        button0=Gtk.Button(label='This',border_width=20)
        
        box0.pack_start(button0,True,True,1)
        self.add(box0)

        self.connect("key-press-event", self.key_watch)
        self.connect("key-release-event", self.key_watch_release)

    def key_watch(self,widget,event):
        print(event.keyval)
    def key_watch_release(self,widget,event):
        print(event.keyval,' released')
        print('_____________________________________________\n')
win=KeyCheckWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
