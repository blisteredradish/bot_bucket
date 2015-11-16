from gi.repository import Gtk
import serial
bwidth=80
bheight=40
ser = serial.Serial('/dev/ttyUSB0', 9600)

class KeyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Light Switch 2000")
        self.set_size_request(240,150)
        self.set_position(Gtk.WindowPosition.CENTER)
        hb=Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title='Light Switch 2000'
        self.set_titlebar(hb)

        grid=Gtk.Grid()
        self.add(grid)

        button1=Gtk.Button(label=" One Off ")
        button1.set_size_request(bwidth,bheight)
        button2=Gtk.Button(label=" Two Off ")
        button2.set_size_request(bwidth,bheight)
        button3=Gtk.Button(label=" Three Off ")
        button3.set_size_request(bwidth,bheight)
        button4=Gtk.Button(label=" One On ")
        button4.set_size_request(bwidth,bheight)
        button5=Gtk.Button(label=" Two On ")
        button5.set_size_request(bwidth,bheight)
        button6=Gtk.Button(label=" Three On ")
        button6.set_size_request(bwidth,bheight)
        button7=Gtk.Button(label=" Cycle ")
        button7.set_size_request(bwidth,bheight)
        button8=Gtk.Button(label=" All On ")
        button8.set_size_request(bwidth,bheight)
        button9=Gtk.Button(label=" Cycle ")
        button9.set_size_request(bwidth,bheight)
        button0=Gtk.Button(label=" All Off ")
        button0.set_size_request(bwidth,bheight)

        grid.add(button1)
        grid.attach_next_to(button2,button1,Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button3,button2,Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button4,button1,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button5,button2,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button6,button3,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button7,button4,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button8,button5,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button9,button6,Gtk.PositionType.TOP, 1, 1)
        grid.attach_next_to(button0,button2,Gtk.PositionType.BOTTOM, 1, 1,)

        button1.connect("clicked", self.on_button1_clicked)
        button2.connect("clicked", self.on_button2_clicked)
        button3.connect("clicked", self.on_button3_clicked)
        button4.connect("clicked", self.on_button4_clicked)
        button5.connect("clicked", self.on_button5_clicked)
        button6.connect("clicked", self.on_button6_clicked)
        button7.connect("clicked", self.on_button7_clicked)
        button8.connect("clicked", self.on_button8_clicked)
        button9.connect("clicked", self.on_button9_clicked)
        button0.connect("clicked", self.on_button0_clicked)

    def on_button1_clicked(self, widget):
        ser.write(b'1')
    def on_button2_clicked(self, widget):
        ser.write(b'2')
    def on_button3_clicked(self, widget):
        ser.write(b'3')
    def on_button4_clicked(self, widget):
        ser.write(b'4')
    def on_button5_clicked(self, widget):
        ser.write(b'5')
    def on_button6_clicked(self, widget):
        ser.write(b'6')
    def on_button7_clicked(self, widget):
        ser.write(b'7')
    def on_button8_clicked(self, widget):
        ser.write(b'8')
    def on_button9_clicked(self, widget):
        ser.write(b'9')
    def on_button0_clicked(self, widget):
        ser.write(b'0')

win=KeyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
