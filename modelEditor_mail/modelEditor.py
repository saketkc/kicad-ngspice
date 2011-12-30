#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import newModel
import openModel

# Create a new model
def newEditor(e=None):
# Read model information (name and type)
  model= newModel.ModelInfo(root)
# Create model file
  if model.status:
    modelParam = newModel.ModelParam(root,model.modelName,model.modelType)

# Open an existing model
def openEditor(e=None):
  model= openModel.ExistingModelInfo(root)
# Open model file
  if model.status:
    modelParam = openModel.ExistingModelParam(root,model.modelName)

# Exit an model editor
def exitEditor(e=None):
  if tkMessageBox.askokcancel("QUIT","Do you really wish to quit?"):
    root.destroy()

# Display help content
def helpEditor(e=None):
  pass

# Display help content
def aboutEditor():
  tkMessageBox.showinfo("About Editor","Created by Yogesh Dilip Save and Shalini Shrivastava")

# Create and configure a graphical window
root = Tk()
root.title("Ngspice Model Editor")
root.geometry("600x400")

# Create and configure a menu
menu = Menu(root)
root.config(menu=menu)

# Create File menu
filemenu= Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New   F2", command=newEditor)
filemenu.add_command(label="Open  F3", command=openEditor)
filemenu.add_separator()
filemenu.add_command(label="Exit  F4", command=exitEditor)

# Create help menu
helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help  F1",command=helpEditor)
helpmenu.add_command(label="About...",command=aboutEditor)

# Protocol for deletion of main window
root.protocol("WM_DELETE_WINDOW",exitEditor)

# Create shortcut keys
root.bind("<F2>", newEditor)
root.bind("<F3>", openEditor)
root.bind("<F4>", exitEditor)
root.bind("<F1>", helpEditor)

mainloop()
