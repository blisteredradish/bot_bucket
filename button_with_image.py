from gi.repository import Gtk

HOME=Gtk.Image.new_from_file('./go-home.png')
NEXT=Gtk.Image.new_from_file('./go-next.png')

class ThisWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="this window")
##        bt0=Gtk.Button(None,image=Gtk.Image(stock=Gtk.STOCK_OPEN))
        grid0=Gtk.Grid()
        bt0=Gtk.Button(None,image=HOME)
        bt1=Gtk.Button(None,image=NEXT)
        bt0.connect("clicked",self.home_clicked)

        grid0.attach(bt0, 0,0,1,1)
        grid0.attach(bt1, 1,0,1,1)
        self.add(grid0)

    def home_clicked(self,widget):
        print("HOME")

this=ThisWindow()
this.connect("delete-event", Gtk.main_quit)
this.show_all()
Gtk.main()
