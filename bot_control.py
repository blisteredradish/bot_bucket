#!/usr/bin/python

from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="button box")

        self.button1 = Gtk.Button(label="command1")
        self.button1.connect("clicked", self.on_button_clicked)
        self.add(self.button1)

        self.button2 = Gtk.Button(label="command2")
        self.button2.connect("clicked", self.on_button_clicked)
        self.add(self.button2)

    def on_button_clicked(self, widget):
        print ("command")

win=MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
        

    
