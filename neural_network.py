import random
import math

class NeuralNetworkTSP:
	'Travelling Salesman Problem by neural network'

	#__W__ = []
	__start_init_type_statement = 0.0
	__start_init_type_statement_one = 1.0
	__count_sities = 0
	#__function = 0

	__A = 0.0
	__B = 0.0
	__C = 0.0
	__D = 0.0

	__state = []
	__dist = []


	#def __init__(self):


	def __init_network(self, d):
		self.__count_sities = len(d)
		#self.__function = step_function
		self.__dist = d

		self.__A = self.__B = len(d) * 100.0
		self.__C = 20.0
		self.__D = 100.0

		self.__init_states()


	def __step_function(self, x):
		if x <= 0.0:
			return 0.0
		return 1.0

		#return 0.5 * (1 + math.tanh(x / 50))


	def __init_states(self):
		#random.seed()
		self.__state = []
		for i in range(self.__count_sities):
			#__W.append([])
			self.__state.append([])
			for j in range(self.__count_sities):
				#__W[i].append(__start_init_type_statement)
				self.__state[i].append(random.random()) #Return the next random floating point number in the range [0.0, 1.0)


	def __calc_W(self, x, i, y, j):
		#print 'd' + str(self.__dist__[x][y])
		return - self.__A * self.__sigma(x, y) * (self.__start_init_type_statement_one - self.__sigma(i, j)) \
			   - self.__B * self.__sigma(i, j) * (self.__start_init_type_statement_one - self.__sigma(x, y)) \
			   - self.__C * self.__dist[x][y] * (self.__sigma(i, j - 1) + self.__sigma(i, j + 1)) \
			   + self.__D


	def __sigma(self, i, j):
		i %= self.__count_sities
		j %= self.__count_sities
		if i == j:
			return self.__start_init_type_statement_one
		return self.__start_init_type_statement


	def __update_state(self):
		is_change = True

		for x in range(self.__count_sities):
			for i in range(self.__count_sities):
				cur_signal = self.__start_init_type_statement

				for y in range(self.__count_sities):
					for j in range(self.__count_sities):
						#print 'w' + str(self.__calc_W(x, i, y, j))
						if i == j and x == y:
							continue
						cur_signal += self.__calc_W(x, i, y, j) * self.__state[y][j]

				cur_signal += 1
				#print cur_signal#str(self.__calc_W(x, i, 0, 0)) + ' ' + str(self.__state[0][0]) + ' = ' + str(cur_signal)
				if self.__state[x][i] != self.__step_function(cur_signal):
					is_change = False
				self.__state[x][i] = self.__step_function(cur_signal)

		return is_change


	def run(self, dist):

		self.__init_network(dist)

		i = 0
		changed = False
		while i < 1000 and not changed:
			changed = self.__update_state()
			i += 1
			#print '---------'

		for j in range(self.__count_sities):
			print self.__state[j]

		print i

		#return step_function(x)


	def distance(self, pointA, pointB):
		return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


	def createDistList(self, points):
		d = []
		for i in range(len(points)):
			d.append([])
			for j in range(len(points)):
				d[i].append(self.distance(points[i], points[j]))
		return d