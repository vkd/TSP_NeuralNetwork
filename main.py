from Tkinter import *
import ttk

def print_out():
	print "my console"

root = Tk()
root.resizable(False, False)
root.geometry('300x200')
b = ttk.Button(root,
					text = "My first buiion",
					command = print_out)
b.pack()
root.mainloop()
