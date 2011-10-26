#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
class Base:
    def callback(self,widget,data):
        print "This is %s" 
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)
        self.window.set_title("KICAD-NGSPICE)"
        self.button=gtk.Button("Hello World")
        self.button.connect("clicked", self.callback, "button")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.add(self.button)
        self.button.show()
        self.window.show()
    def main(self):
        gtk.main()
    def delete_event(self, widget, event, data=None):
        return False
    def destroy(self, widget, data=None):
        gtk.main_quit()
print __name__
if __name__ == "__main__":
    base=Base()
    base.main()
