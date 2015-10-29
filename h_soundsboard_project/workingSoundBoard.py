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
        box0=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
##SOUND PORTION
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
##LIGHT PORTION
        
        lightFile=open('./light.txt')
        
        for i in lightFile:
            y=i
            i=Gtk.Button.new_with_label(i)
            i.connect("clicked", self.display_light,y)
            box2.pack_start(i,True,True,0)
        
        lightFile.close()
        lightButton0=Gtk.Button.new_with_label("kill message")
        lightButton0.connect("clicked", self.kill_xmessage)
        box2.pack_start(lightButton0,True,True,0)
          
        box0.pack_start(box1,True,True,0)
        box0.pack_start(box2,True,True,0)
        self.add(box0)
        
##SOUND FUNCTIONS            
    def play_sound(self,widget,y):
##      file=open('./sound.txt')
##      for i in file:
            os.system('mplayer ./music/{} &'.format(y.rstrip('\n')))
##            print(y)

    def kill_sound(self,widget):
        os.system('killall mplayer &')
##LIGHT FUNCTIONS
    def display_light(self,widget,y):
        os.system('xmessage {} &'.format(y.rstrip('\n')))

    def kill_xmessage(self,widget):
        os.system('killall xmessage')

soundWindow().connect("delete-event", Gtk.main_quit)
soundWindow().show_all()
Gtk.main()






    


