#!/usr/bin/python

from gi.repository import Gtk, GObject
import serial
ser=serial.Serial(None,9600)##replace with /dev/ttyUSB0

UP_IMG=Gtk.Image.new_from_file('../../arrow-up.png')
DOWN_IMG=Gtk.Image.new_from_file('../../arrow-down.png')
RIGHT_IMG=Gtk.Image.new_from_file('../../arrow-right.png')
LEFT_IMG=Gtk.Image.new_from_file('../../arrow-left.png')
DIR_LABEL=Gtk.Label("Use Keypad")
class controlWindow(Gtk.Window):
    def __init__(self):      
        Gtk.Window.__init__(self,title="Bot Commander")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(240,150) 
        box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        grid1=Gtk.Grid()
        title_box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        button_box=Gtk.Box()
        dir_grid=Gtk.Grid()
        button_box.set_homogeneous(False)
        button_grid=Gtk.Grid()
##Window Label Section
        label1=Gtk.Label("Robot Commander")
        title_box.pack_start(label1,True,True,0)
##Button Section
        button1=Gtk.Button.new_with_label("1")
        button2=Gtk.Button(None,image=DOWN_IMG)
        button3=Gtk.Button.new_with_label("3")
        button4=Gtk.Button(None,image=LEFT_IMG)
        button5=Gtk.Button.new_with_label("5")
        button6=Gtk.Button(None,image=RIGHT_IMG)
        button7=Gtk.Button.new_with_label("7")
        button8=Gtk.Button(None,image=UP_IMG)
        button9=Gtk.Button.new_with_label("9")
        button0=Gtk.Button.new_with_label("0")

        button8.connect("pressed",self.button8_pressed)
        button8.connect("released", self.button_released)
        self.connect("key-press-event", self.key_watch)
        self.connect("key-release-event", self.key_release)

        button_grid.add(button0)
        button_grid.attach_next_to(button2,button0,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button1,button2,Gtk.PositionType.LEFT,1,1)
        button_grid.attach_next_to(button3,button2,Gtk.PositionType.RIGHT,1,1)
        button_grid.attach_next_to(button4,button1,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button5,button2,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button6,button3,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button7,button4,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button8,button5,Gtk.PositionType.TOP,1,1)
        button_grid.attach_next_to(button9,button6,Gtk.PositionType.TOP,1,1)

        button_box.pack_start(button_grid,True,True,0)
        
        box1.pack_start(title_box,True,True,0)
        box1.pack_start(button_box,True,True,0)
        
        self.add(box1)
        
    def button8_pressed(self,widget):
        print("UP Pressed")
        
    def button_released(self,widget):
        print("UP Released")

        
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
                    
cwindow=controlWindow()
cwindow.connect("delete-event", Gtk.main_quit)
cwindow.show_all()
Gtk.main()
