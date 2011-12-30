import wx
import os
ID_ABOUT=101
ID_OPEN=102
ID_SAVE=103
ID_BUTTON1=300
ID_EXIT=200

# Some classes to use for the notebook pages.  Obviously you would
# want to use something more meaningful for your application, these
# are just for illustration.

class PageOne(wx.Panel):
    def __init__(self, parent):
        #wx.Panel.__init__(self, parent)
	wx.Panel.__init__(self, parent)
	#panel2 = wx.Panel(panel, -1)
	#hbox = wx.BoxSizer(wx.HORIZONTAL)
	
	
	#panel3 = wx.Panel(panel, -1)
	#sizer3 = wx.StaticBoxSizer(wx.StaticBox(self, -1, 'Options'), orient=wx.VERTICAL)
	#vbox3 = wx.BoxSizer(wx.VERTICAL)
	#grid = wx.GridSizer(3, 2, 0, 5)
	#grid.Add(wx.CheckBox(self, -1, 'Case Sensitive'))
	#grid.Add(wx.CheckBox(self, -1, 'Wrap Search'))
	#grid.Add(wx.CheckBox(self, -1, 'Whole Word'))
	#grid.Add(wx.CheckBox(self, -1, 'Incremental'))
	#vbox3.Add(grid)
	#vbox3.Add(wx.CheckBox(self, -1, 'Regular expressions'))
	#sizer3.Add(vbox3, 0, wx.TOP, 4)
	#self.SetSizer(sizer3)
	#vbox.Add(self, 0, wx.BOTTOM, 15)
	#vbox_top.Add(vbox, 1, wx.LEFT, 5)
	#self.SetSizer(vbox_top)
	#hbox2 = wx.BoxSizer(wx.VERTICAL)
	#sizer =  wx.StaticBoxSizer(wx.StaticBox(self, -1, 'DC SWEEP'), orient=wx.VERTICAL)
	#sizer.Add(wx.SpinCtrl(self, -1, '1', (-10, -10), (-0, 1), min=1, max=120), 1)
	#hbox2.Add(
	#hbox2.Add(sizer, 1,wx.TOP,4)
	#self.SetSizer(hbox2)
       # t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))
	#self.Centre()
	#self.Show(True)
	#self.ShowModal()
	#self.Destroy()

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, 'Scale'), orient=wx.HORIZONTAL)
	self.lin = wx.RadioButton(self, -1, 'Lin', style=wx.RB_GROUP)
	self.log = wx.RadioButton(self, -1, 'Log')
	self.dec = wx.RadioButton(self, -1, 'Dec')
	self.octal = wx.RadioButton(self, -1, 'Oct')
	sizer.Add(self.lin)
	sizer.Add(self.log)
	sizer.Add(self.dec)
	sizer.Add(self.octal)
	grid1 = wx.GridSizer(5, 2)
	grid1.Add(sizer,1)
	

	#grid1.Add(sizer2,2)
	grid1.Add(wx.StaticText(self,-1,''))
	#grid1.Add(wx.StaticText(self,-1,''))
	grid1.Add(wx.StaticText(self,-1,'Start Frequency'),1)
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	self.start = wx.SpinCtrl(self, -1, '',  (150, 75), (60, -1))
	hbox.Add(self.start)
	self.startscale = wx.ComboBox(self, -1, value = 'Hz',  choices=['THz', 'GHz', 'MHz', 'KHz', 'Hz'], size=(60, -1), style=wx.CB_DROPDOWN)
	hbox.Add(self.startscale)
	grid1.Add(hbox)
	grid1.Add(wx.StaticText(self,-1,'Stop Frequency'),1)
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	self.stop = wx.SpinCtrl(self, -1, '',  (150, 75), (60, -1))
	hbox.Add(self.stop)
	self.stopscale = wx.ComboBox(self, -1, value = 'Hz',  choices=['THz', 'GHz', 'MHz', 'KHz', 'Hz'], size=(60, -1), style=wx.CB_DROPDOWN)
	hbox.Add(self.stopscale)
	grid1.Add(hbox)
	
	grid1.Add(wx.StaticText(self,-1,'Steps/Decade'),1)
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	self.datapoints = wx.SpinCtrl(self, -1, '',  (150, 75), (60, -1))
	hbox.Add(self.datapoints)
	grid1.Add(hbox)
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	self.button = wx.Button(self,901,"Add Simulation Data")
	hbox.Add(self.button)
	self.button.Bind(wx.EVT_BUTTON, self.enter_simulation)
	grid1.Add(wx.StaticText(self,-1,''),1)
	grid1.Add(hbox)
	self.SetSizer(grid1)
	self.Centre()
	self.Show(True)
    def OnButton(self,e):
	print self.lin.GetValue()
	print self.GetParent().GetParent().control.GetValue()
    def enter_simulation(self,e):
	txtctrl = self.GetParent().GetParent().control
	if self.lin:
	    ac_scale="lin"
	elif self.dec:
	    ac_scale="dec"
	elif self.log:
	    ac_scale = "log"
	elif self.octal:
	    ac_scale = "octal"
	number_of_data_points = str(self.datapoints.GetValue())
	start_frequency = str(self.start.GetValue())+ str(self.startscale.GetValue())
	stop_frequency = str(self.stop.GetValue())+ str(self.stopscale.GetValue())
	appendline_ac = ".ac " + str(ac_scale) + " " + str(number_of_data_points)+" " + str(start_frequency) + " " + str(stop_frequency) + "\n" 
	appendline_end = ".end\n"
	appendline_control=".control\n" + "run\n" + ".endc\n"
	#with open(filename,"a") as myfile:
	txtctrl.AppendText("\n")
	txtctrl.AppendText(appendline_ac)
	txtctrl.AppendText("\n\n")
	txtctrl.AppendText(appendline_end)
	txtctrl.AppendText(appendline_control)


class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))


class MainFrame(wx.Frame):
    def __init__(self):#self,parent,wx.ID_ANY, title
        wx.Frame.__init__(self,None, wx.ID_ANY, title="kicad ngspice")
	self.CreateStatusBar(style=0)
	self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
	filemenu= wx.Menu()
        # use ID_ for future easy reference - much better that "48", "404" etc
        # The & character indicates the short cut key
        filemenu.Append(ID_OPEN, "&Open"," Open a file to edit")
        filemenu.AppendSeparator()
        filemenu.Append(ID_SAVE, "&Save"," Save file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        # Note - previous line stores the whole of the menu into the current object

        # Define the code to be run when a menu option is selected
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, ID_SAVE, self.OnSave); # just "pass" in our demo

	self.aboutme = wx.MessageDialog( self, " Converter for kicad \n"
                            " in wxPython","Beta mode", wx.OK)
        self.doiexit = wx.MessageDialog( self, " Exit - R U Sure? \n",
                        "GOING away ...", wx.YES_NO)

        # dirname is an APPLICATION variable that we're choosing to store
        # in with the frame - it's the parent directory for any file we
        # choose to edit in this frame
        self.dirname = ''


	#self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
	#self.sizer=wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.control,1,wx.EXPAND)
        #self.sizer.Add(self.sizer2,0,wx.EXPAND)
	#self.SetSizer(self.sizer)

        # Here we create a panel and a notebook on the panel
        p = wx.Panel(self)
        nb = wx.Notebook(self)

        # create the page windows as children of the notebook
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "DC")
        nb.AddPage(page2, "AC")
        nb.AddPage(page3, "Transient")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb, 1, wx.EXPAND)
	sizer.Add(self.control,1,wx.EXPAND)
        self.SetSizer(sizer)

	 #wx.Frame.__init__(self,parent,wx.ID_ANY, title)

        # Add a text editor and a status bar
        # Each of these is within the current instance
        # so that we can refer to them later.
	#self.SetAutoLayout(1)
        #self.sizer.Fit(self)

        # Show it !!!
        #self.Show(1)
	self.Maximize()


    def OnAbout(self,e):
        # A modal show will lock out the other windows until it has
        # been dealt with. Very useful in some programming tasks to
        # ensure that things happen in an order that  the programmer
        # expects, but can be very frustrating to the user if it is
        # used to excess!
        self.aboutme.ShowModal() # Shows it
    def OnExit(self,e):
        # A modal with an "are you sure" check - we don't want to exit
        # unless the user confirms the selection in this case ;-)
        igot = self.doiexit.ShowModal() # Shows it
        if igot == wx.ID_YES:
            self.Close(True)  # Closes out this simple application

    def OnOpen(self,e):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'r')
            self.control.SetValue(filehandle.read())
            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
        dlg.Destroy()

    def OnSave(self,e):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.control.GetValue()

            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()

        


if __name__ == "__main__":
    app = wx.App()
    
    MainFrame().Show(1)
    #MainFrame().Maximize()
    #MainFrame().Layout()
    app.MainLoop()
