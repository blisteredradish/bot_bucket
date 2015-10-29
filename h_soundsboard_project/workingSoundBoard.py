#!/usr/bin/pyton
from gi.repository import Gtk
import os

def creat_list():
    os.system ('touch ./sound.txt')
    os.system ('ls ./sounds/ > sound.txt')



def populate_sound_list():
    file=open('./sound.txt')
    commands=open('./sound_command.txt', 'w')
    for i in file:
        commands.write('mplayer ./music/{} &\n'.format(i.rstrip('\n')))
    file.close()
    commands.close()

creat_list()
populate_sound_list()

class soundWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sound Commander")
        self.set_border_width(10)
        self.set_default_size(200,200)
        header=Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title="Sound Commander"
        self.set_titlebar(header)
        
        box0=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        label_1=Gtk.Label('C\nO\nM\nM\nA\nN\nD\nE\nR')

        file=open('./sound.txt')
        for i in file:
            y=i
            i=Gtk.Button.new_with_label(i.rstrip('\n'))
            box1.pack_start(i,True,True,0)
            i.connect("clicked", self.play_sound,y)
        file.close()
        button0=Gtk.Button.new_with_label("Kill Sound")
        button0.connect("clicked", self.kill_sound)
        box1.pack_start(button0,True,True,0)
        box2.pack_start(label_1,True,True,0)
        box0.pack_start(box1,True,True,0)
        box0.pack_start(box2,True,True,0)
        self.add(box0)        
            
    def play_sound(self,widget,y):

            os.system('mplayer ./sounds/{} &'.format(y.rstrip('\n')))

    def kill_sound(self,widget):
        os.system('killall mplayer &')
                  
soundWindow().connect("delete-event", Gtk.main_quit)
soundWindow().show_all()
Gtk.main()






    


