import random

class Neural_Network_TSP:

	#__W__ = []
	__start_init_type_statement__ = 0.0
	__start_init_type_statement_one__ = 1.0
	__count_sities__ = 0
	__function__ = 0

	__A__ = 100.0
	__B__ = 100.0
	__C__ = 100.0
	__D__ = 100.0

	__state__ = []
	__dist__ = []


	def __init__(self, d, step_function):
		self.__count_sities__ = len(d)
		self.__function__ = step_function
		self.__dist__ = d

		self.__init_states__()


	def __init_states__(self):
		random.seed()
		for i in range(self.__count_sities__):
			#__W__.append([])
			self.__state__.append([])
			for j in range(self.__count_sities__):
				#__W__[i].append(__start_init_type_statement__)
				self.__state__[i].append(random.random()) #Return the next random floating point number in the range [0.0, 1.0)


	def __calc_W__(x, i, y, j):
		return - self.__A__ * self.__sigma__(x, y) * (self.__start_init_type_statement_one__ - self.__sigma__(i, j)) \
			   - self.__B__ * self.__sigma__(i, j) * (self.__start_init_type_statement_one__ - self.__sigma__(x, y)) \
			   - self.__C__ * self.__dist__[x][y] * (self.__sigma__(i, j - 1) + self.__sigma__(i, j + 1)) \
			   + self.__D__


	def __sigma__(i, j):
		i %= self.__count_sities__
		j %= self.__count_sities__
		if i == j:
			return self.__start_init_type_statement_one__
		return self.__start_init_type_statement__


	def __update_state__():
		for x in range(self.__count_sities__):
			for i in range(self.__count_sities__):
				cur_signal = self.__start_init_type_statement__

				for y in range(self.__count_sities__):
					for j in range(self.__count_sities__):
						cur_signal += self.__calc_W__(x, i, y, j) * self.__state__[y][j]

				self.__state__[x][i] = self.__function__(cur_signal)



	def run():
		self.__update_state__()
		#return step_function(x)


def f(x):
	if x == 0.0:
		return 0.0
	return 1.0

dist = [[0., 2., 5.],
		[2., 0., 4.],
		[5., 4., 0.]]

#print random.random()
nn = Neural_Network_TSP(dist, f)
