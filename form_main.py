from Tkinter import *

import neural_network

import ttk

class FormMain():
	'Main Form for TSP neural network'

	__SIZE_WINDOW = '600x400'
	__SIZE_MAP_HEIGHT = 400
	__SIZE_MAP_WIDTH = __SIZE_MAP_HEIGHT

	__form_main = 0
	__core_nn = 0


	def __init__(self):
		self.__core_nn = neural_network.NeuralNetworkTSP()

		self.__form_main = Tk()
		self.__form_main.resizable(False, False)
		self.__form_main.geometry(self.__SIZE_WINDOW)

		self.__init_form()


	def __init_form(self):
		mapFrame = Frame(self.__form_main,
						height = self.__SIZE_MAP_HEIGHT,
						width = self.__SIZE_MAP_WIDTH,
						bg = 'white')
		mapFrame.pack(side = 'left')

		panelFrame = Frame(self.__form_main)
								#bg = 'orange')

		panelFrame.pack(side = 'right',
							 fill = 'both',
							 expand = 1)

		buttonCalc = ttk.Button(panelFrame,
							text = "Calc")
		#					command = print_out)
		buttonCalc.bind("<Button-1>", self.__calc_nn)
		#buttonCalc.place(x = 0, y = 0)
		buttonCalc.pack(side = 'top')

		buttonExit = ttk.Button(panelFrame,
							text = 'Quit')
		buttonExit.bind('<Button-1>', self.__quit)
		buttonExit.pack(side = 'bottom')


	def __calc_nn(self, event):
		ps = [[0., 6.], [6., 7.], [4., 2.], [7., 0.], [10., 4.]]  #1, 2, 5, 4, 3

		dist = self.__core_nn.createDistList(ps)

		self.__core_nn.run(dist)


	def __quit(self, event):
		self.__form_main.quit()


	def run(self):
		self.__form_main.mainloop()

