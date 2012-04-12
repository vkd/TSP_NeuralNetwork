import random
import math

class Neural_Network_TSP:

	#__W__ = []
	__start_init_type_statement__ = 0.0
	__start_init_type_statement_one__ = 1.0
	__count_sities__ = 0
	__function__ = 0

	__A__ = __B__ = 200.0
	#__B__ = 200.0
	__C__ = 2.0
	__D__ = 90.0

	__state__ = []
	__dist__ = []


	def __init__(self, d, step_function):
		self.__count_sities__ = len(d)
		self.__function__ = step_function
		self.__dist__ = d

		self.__init_states__()


	def __init_states__(self):
		#random.seed()
		for i in range(self.__count_sities__):
			#__W__.append([])
			self.__state__.append([])
			for j in range(self.__count_sities__):
				#__W__[i].append(__start_init_type_statement__)
				self.__state__[i].append(0.0)#random.random()) #Return the next random floating point number in the range [0.0, 1.0)


	def __calc_W__(self, x, i, y, j):
		#print 'd' + str(self.__dist__[x][y])
		return - self.__A__ * self.__sigma__(x, y) * (self.__start_init_type_statement_one__ - self.__sigma__(i, j)) \
			   - self.__B__ * self.__sigma__(i, j) * (self.__start_init_type_statement_one__ - self.__sigma__(x, y)) \
			   - self.__C__ * self.__dist__[x][y] * (self.__sigma__(i, j - 1) + self.__sigma__(i, j + 1)) \
			   + self.__D__


	def __sigma__(self, i, j):
		i %= self.__count_sities__
		j %= self.__count_sities__
		if i == j:
			return self.__start_init_type_statement_one__
		return self.__start_init_type_statement__


	def __update_state__(self):
		is_change = True

		for x in range(self.__count_sities__):
			for i in range(self.__count_sities__):
				cur_signal = self.__start_init_type_statement__

				for y in range(self.__count_sities__):
					for j in range(self.__count_sities__):
						#print 'w' + str(self.__calc_W__(x, i, y, j))
						if i == j and x == y:
							continue
						cur_signal += self.__calc_W__(x, i, y, j) * self.__state__[y][j]

				cur_signal += 10
				print cur_signal#str(self.__calc_W__(x, i, 0, 0)) + ' ' + str(self.__state__[0][0]) + ' = ' + str(cur_signal)
				if self.__state__[x][i] != self.__function__(cur_signal):
					is_change = False
				self.__state__[x][i] = self.__function__(cur_signal)

		return is_change


	def run(self):
		i = 0
		changed = False
		while i < 1000 and not changed:
			changed = self.__update_state__()
			i += 1
			print '---------'

		for j in range(self.__count_sities__):
			print self.__state__[j]

		print i

		#return step_function(x)


def f(x):
	if x <= 0.0:
		return 0.0
	return 1.0

def ftanh(x):
	return 0.5 * (1 + math.tanh(x / 50))

dist = [[0., 70., 30., 50.],
		[70., 0., 70., 40.],
		[30., 70., 0., 30.],
		[50., 40., 30., 0.]]

#dist = [[0., 70., 50.],
#		[70., 0., 40.],
#		[50., 40., 0.]]

#print random.random()
nn = Neural_Network_TSP(dist, f)
nn.run()
