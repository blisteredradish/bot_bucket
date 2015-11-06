#!/usr/bin/python3

from gi.repository import Gtk

class KeyCheckWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Key Checker')
        self.set_position(Gtk.WindowPosition.CENTER)
        box0=Gtk.Box()

        self.connect("key-press-event", self.key_watch)
        self.connect("key-release-event", self.key_watch_release)

    def key_watch(self,widget,event):
        
        print(event.keyval)
##        print('\n')
    def key_watch_release(self,widget,event):
        print(event.keyval,' released')
        print('_____________________________________________\n')
win=KeyCheckWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
