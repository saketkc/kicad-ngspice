import pygtk
pygtk.require('2.0')
import gtk

class TextViewExample:

    def convert(filename):
        fw = open(filename, 'r')
        output = open ('netlist_output.cir','w')
        for line in fw:
            cc = re.search("\w\d_\w\d_\w\d",line)
            newline=line
            if cc:
                nline = re.split("[_]", line)
                newline = ""
                for i in range(0,len(nline)):
                    if (i==0):
                        newline=newline+nline[i] + "  "
                    else:
                        if (i==(len(nline)-1)):
                            newline=newline+nline[i].replace("  "," ")
                        else:
                            nline=newline+nline[i]+" "
            else:
                newline = line
                line = line.replace("  "," ").strip()
                correct_cccs=re.split("[_]",line)
                split_line = re.split(" ",line)
                print correct_cccs[0]
                try:
                    re.match("^\d",correct_cccs[1])
                    value=int(correct_cccs[1])
                    var=split_line[5].split("_")
                    newline=split_line[0]+"  " + split_line[-3] + " " + split_line[-2]  + " " + var[0]+ " " + var[1]+"\n"
                except:
                    #else:
                    if (len(split_line)==6):
                        if ((split_line[1]=="1")or(split_line[1]=="3")):
                            newline=split_line[0] + "  " + "3 " + "4 " + "1 " + "2 " + split_line[5] + "\n"
            if (newline.strip()!= ".end"):
                output.write(newline)
        output.close()
        fw.close()
    def toggle_editable(self,checkbutton,textview):
        textview.set_editable(checkbutton.get_active())
    def toggle_cursor_visible(self,checkbutton,textview):
        textview.set_editable(checkbutton.get_active())
    def toggle_left_margin(self,checkbutton,textview):
        if checkbutton.get_active():
            textview.set_left_margin(20)
        else:
            textview.set_left_margin(0)
    def toggle_right_margin(self,checkbutton,textview):
        if checkbutton.get_active():
            textview.set_right_margin(20)
        else:
            textview.set_right_margin(0)
    def new_wrap_mode(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_wrap_mode(val)
    def new_justification(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_justification(val)
    def close_application(self,widget):
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)
        window.connect("destroy",self.close_application)
        window.set_title("convert ")
        window.set_border_width(10)
        box1=gtk.VBox(False,0)
        boxV2=gtk.VBox(False,10)

        window.add(box1)
        #window.add(boxV2)
        box1.show()
        boxV2.show()
        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box1.pack_start(boxV2,True,True,0)
        box2.show()
        sw1 = gtk.ScrolledWindow()
        sw2 = gtk.ScrolledWindow()
        sw1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        sw2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview1 = gtk.TextView()
        textbuffer1 = textview1.get_buffer()
        textview2 = gtk.TextView()
        textbuffer2 = textview2.get_buffer()
        sw1.add(textview1)
        sw2.add(textview2)
        sw1.show()
        sw2.show()
        textview1.show()
        textview2.show()
        box2.pack_start(sw1)
        boxV2.pack_start(sw2)
        infile=open("netlist_output.cir","r")
        if infile:
            string = infile.read()
            infile.close()
            textbuffer1.set_text(string)
            textbuffer2.set_text(string)
        hbox = gtk.HButtonBox()
        box2.pack_start(hbox, False, False, 0)
        hbox.show()
        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()
        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()
        button = gtk.Button("close")
        button.connect("clicked", self.close_application)
        box2.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()
def main():
    gtk.main()
    return 0
if __name__ == "__main__":
    TextViewExample()
    main()
