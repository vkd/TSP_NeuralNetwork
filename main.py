from Tkinter import *
import ttk

__SIZE_WINDOW__ = '600x400'

__SIZE_MAP_HEIGHT__ = 400
__SIZE_MAP_WIDTH__ = __SIZE_MAP_HEIGHT__

def print_out(event):
	print "my console: "

def quit(event):
	root.quit()

root = Tk()
root.resizable(False, False)
root.geometry(__SIZE_WINDOW__)

mapFrame = Frame(root,
					  height = __SIZE_MAP_HEIGHT__,
					  width = __SIZE_MAP_WIDTH__,
					  bg = 'white')
mapFrame.pack(side = 'left')

panelFrame = Frame(root)
						 #bg = 'orange')

panelFrame.pack(side = 'right',
					 fill = 'both',
					 expand = 1)

b = ttk.Button(panelFrame,
					text = "My first button")
					#command = print_out)
b.bind("<Button-1>", print_out)
b.place(x = 0, y = 0)
#b.pack(side = 'top')

b2 = ttk.Button(panelFrame,
					text = 'Quit')
b2.bind('<Button-1>', quit)
b2.pack(side = 'bottom')

root.mainloop()
