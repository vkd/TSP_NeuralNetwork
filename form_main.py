from Tkinter import *

import load_strings
import neural_network


import ttk
import random

class FormMain():
	'Main Form for TSP neural network'

	__SIZE_WINDOW = '600x400'
	__SIZE_MAP_HEIGHT = 400
	__SIZE_MAP_WIDTH = __SIZE_MAP_HEIGHT

	__form_main = 0
	__core_nn = 0
	__canvas_map = None

	__sities = []
	__way = []
	__way_length = 0

	__strings = None


	def __init__(self):
		self.__core_nn = neural_network.NeuralNetworkTSP()

		self.__strings = load_strings.LoadStrings('strings')

		self.__form_main = Tk()
		self.__form_main.resizable(False, False)
		self.__form_main.geometry(self.__SIZE_WINDOW)
		self.__form_main.title(self.__strings.getString('FORM_MAIN_TITLE'))
		self.__form_main.iconbitmap(default = 'tsp_ico.ico')

		#self.__sities = [[40, 70], [220, 40], [160, 190], [240, 130], [380, 150], [260, 380], [100, 344], [280, 300]]  #1, 2, 5, 4, 3

		self.__init_form()



	def __init_form(self):
		mapFrame = Frame(self.__form_main,
						height = self.__SIZE_MAP_HEIGHT,
						width = self.__SIZE_MAP_WIDTH,
						bg = 'green')
		mapFrame.pack(side = 'left')

		self.__canvas_map = Canvas(mapFrame,
						height = self.__SIZE_MAP_HEIGHT,
						width = self.__SIZE_MAP_WIDTH,
						bg = 'white',
						bd = 5,
						relief = 'ridge')
		self.__canvas_map.bind('<Button-1>', self.__canvas_click)
		self.__canvas_map.pack()#side = 'left',
		#				fill = 'both',
		#				expand = 1)

		panelFrame = Frame(self.__form_main)
								#bg = 'orange')

		panelFrame.pack(side = 'right',
							 fill = 'both',
							 expand = 1)

		buttonCalc = ttk.Button(panelFrame,
							text = self.__strings.getString('BUTTON_CALC'))
		#					command = print_out)
		buttonCalc.bind("<Button-1>", self.__calc_nn)
		#buttonCalc.place(x = 0, y = 0)
		buttonCalc.pack(side = 'top')

		buttonDelLast = ttk.Button(panelFrame,
							text = self.__strings.getString('BUTTON_DEL_LAST'))
		buttonDelLast.bind("<Button-1>", self.__canvas_del_last)
		buttonDelLast.pack(side = 'top')

		buttonClear = ttk.Button(panelFrame,
							text = self.__strings.getString('BUTTON_CLEAR'))
		buttonClear.bind("<Button-1>", self.__canvas_clear)
		buttonClear.pack(side = 'top')

		buttonAddTenRand = ttk.Button(panelFrame,
							text = self.__strings.getString('BUTTON_ADD_N_RAND'))
		buttonAddTenRand.bind('<Button-1>', self.__canvas_add_n_rand)
		buttonAddTenRand.pack(side = 'top')

		buttonExit = ttk.Button(panelFrame,
							text = self.__strings.getString('BUTTON_QUIT'))
		buttonExit.bind('<Button-1>', self.__quit)
		buttonExit.pack(side = 'bottom')

		self.__repaint_canvas(False)

	def __repaint_canvas(self, with_lines):
		__point_radius = 7

		self.__canvas_map.delete('all')
		__points = []


		if with_lines:
			lenght = len(self.__way)
			for i in range(lenght):
				self.__canvas_map.create_line(self.__sities[self.__way[i]][0],
														self.__sities[self.__way[i]][1],
														self.__sities[self.__way[(i + 1) % lenght]][0],
														self.__sities[self.__way[(i + 1) % lenght]][1],
														fill = 'black',
														width = 2)


		lenght = len(self.__sities)
		self.__canvas_map.create_text(360, 380, text = str(self.__way_length))

		for i in range(lenght):
			self.__canvas_map.create_oval(self.__sities[i][0] - __point_radius,
													self.__sities[i][1] - __point_radius,
													self.__sities[i][0] + __point_radius,
													self.__sities[i][1] + __point_radius,
													fill = 'purple')
			self.__canvas_map.create_text(self.__sities[i][0],
													self.__sities[i][1] - 13,
													text = str(i + 1))


	def __calc_nn(self, event):

		dist = self.__core_nn.createDistList(self.__sities)

		correct = False

		for _ in range(1):
			if correct:
				break
			correct, self.__way, self.__way_length = self.__core_nn.run(dist, True)

		print correct, self.__way
		self.__repaint_canvas(correct)


	def __quit(self, event):
		self.__form_main.quit()

	def __canvas_click(self, event):
		sity = []
		sity.append(event.x)
		sity.append(event.y)
		self.__sities.append(sity)
		self.__repaint_canvas(False)

	def __canvas_del_last(self, event):
		if len(self.__sities) > 0:
			self.__sities.pop()
			self.__way_length = 0
			self.__repaint_canvas(False)

	def __canvas_clear(self, event):
		self.__sities = []
		self.__way_length = 0
		self.__repaint_canvas(False)

	def __canvas_add_n_rand(self, event):
		for _ in range(7):
			self.__sities.append([int(random.random() * (self.__SIZE_MAP_WIDTH - 10)) + 5,
										 int(random.random() * (self.__SIZE_MAP_WIDTH - 10)) + 5])
		self.__repaint_canvas(False)


	def run(self):
		self.__form_main.mainloop()

