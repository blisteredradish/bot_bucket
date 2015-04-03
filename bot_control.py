#!/usr/bin/python

from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="button box")

        self.button = Gtk.Button(label="command")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print ("command")

win=MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
        

    
