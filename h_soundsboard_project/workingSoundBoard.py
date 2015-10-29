#!/usr/bin/pyton
from gi.repository import Gtk
import os



def populate_sound_list():
    file=open('./sound.txt')
    commands=open('./sound_command.txt', 'w')
    for i in file:
        commands.write('mplayer ./music/{} &\n'.format(i.rstrip('\n')))
    file.close()
    commands.close()

populate_sound_list()




class soundWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="sound window")
        self.set_default_size(200,200)

        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        file=open('./sound.txt')
        for i in file:
            y=i
            i=Gtk.Button.new_with_label(i)
            box1.pack_start(i,True,True,0)
            i.connect("clicked", self.play_sound,y)
        file.close()
        button0=Gtk.Button.new_with_label("Kill Sound")
        button0.connect("clicked", self.kill_sound)
        box1.pack_start(button0,True,True,0)
        self.add(box1)        
            
    def play_sound(self,widget,y):
##      file=open('./sound.txt')
##      for i in file:
            os.system('mplayer ./music/{} &'.format(y.rstrip('\n')))
##            print(y)

    def kill_sound(self,widget):
        os.system('killall mplayer &')
                  
soundWindow().connect("delete-event", Gtk.main_quit)
soundWindow().show_all()
Gtk.main()






    


