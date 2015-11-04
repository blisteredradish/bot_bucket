#!/usr/bin/python

from gi.repository import Gtk, GObject
import serial
ser=serial.Serial('/dev/ttyUSB0',9600)


class controlWindow(Gtk.Window):
    def __init__(self):

 
        
        Gtk.Window.__init__(self,title="Bot Commander")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(240,150)
            
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box3=Gtk.Box()
        box3.set_homogeneous(False)
        grid1=Gtk.Grid()
        
##Window Label Section
        label1=Gtk.Label("Robot Commander")
        label2=Gtk.Label("Now with Arrow Keys!")
        box2.pack_start(label1,True,True,0)
##        box2.pack_start(label2,True,True,0)
##Button Section
        button1=Gtk.Button.new_with_label("1")
        button2=Gtk.Button.new_with_label("2")
        button3=Gtk.Button.new_with_label("3")
        button4=Gtk.Button.new_with_label("4")
        button5=Gtk.Button.new_with_label("5")
        button6=Gtk.Button.new_with_label("6")
        button7=Gtk.Button.new_with_label("7")
        button8=Gtk.Button.new_with_label("8")
        button9=Gtk.Button.new_with_label("9")
        button0=Gtk.Button.new_with_label("0")

        button8.connect("pressed",self.button8_pressed)
        button8.connect("released", self.button_released)
        self.connect("key-press-event", self.key_watch)
        self.connect("key-release-event", self.key_release)

        grid1.add(button0)
        grid1.attach_next_to(button2,button0,Gtk.PositionType.TOP,1,1)
        grid1.attach_next_to(button1,button2,Gtk.PositionType.LEFT,1,1)
        grid1.attach_next_to(button3,button2,Gtk.PositionType.RIGHT,1,1)
        grid1.attach_next_to(button4,button1,Gtk.PositionType.TOP,1,1)
        grid1.attach_next_to(button5,button2,Gtk.PositionType.TOP,1,1)
        grid1.attach_next_to(button6,button3,Gtk.PositionType.TOP,1,1)
        grid1.attach_next_to(button7,button4,Gtk.PositionType.TOP,1,1)

        grid1.attach_next_to(button8,button5,Gtk.PositionType.TOP,1,1)
        grid1.attach_next_to(button9,button6,Gtk.PositionType.TOP,1,1)

        box3.pack_start(grid1,True,True,0)

        
        box1.pack_start(box2,True,True,0)
        box1.pack_start(box3,True,True,0)

        self.add(box1)
        
    def button8_pressed(self,widget):
        print("Pressed")

    def button_released(self,widget):
        print("Released")

        
    def key_release(self,widget,event):
        print("0")    
        ser.write(b'0')
    def key_watch(self,widget,event):
        if event.keyval==65362:
            print("UP")
            ser.write(b'1')
          
        elif event.keyval==65364:
            print("DOWN")
            ser.write(b'2')
        elif event.keyval==65361:
            print("LEFT")
            ser.write(b'3')
        elif event.keyval==65363:
            print("RIGHT")
            ser.write(b'4')
                    

controlWindow().connect("delete-event", Gtk.main_quit)
controlWindow().show_all()
Gtk.main()
