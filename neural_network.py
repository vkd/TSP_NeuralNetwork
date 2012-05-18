'''Core of Neural Network with Hopfild's model and annealing algorithm'''

import random
import math

class NeuralNetworkTSP:
	'Travelling Salesman Problem by neural network'

	__count_sities = 0

	"Hopfild's constants"
	__A = 0.0
	__B = 0.0
	__C = 0.0
	__D = 0.0

	__state = []
	__distances = []


	def __init_network(self, d):
		self.__count_sities = len(d)
		self.__distances = d

		self.__A = self.__B = len(d) * 60.
		self.__C = 0.7
		self.__D = 100.

		self.__init_states()


	def __step_function(self, x):
		if x <= 0.0:
			return 0.0
		return 1.0


	def __step_function_float(self, x):
		return 0.5 * (1. + math.tanh(x / 50))


	def __init_states(self):
		'Initialization begin state of neural network'
		self.__state = []
		for i in range(self.__count_sities):
			self.__state.append([])

			for j in range(self.__count_sities):
				next_rand = random.random() #Return the next random floating point number in the range [0.0, 1.0)
				#if next_rand < 0.5:
				#	next_rand = 0
				#else:
				#	next_rand = 1

				self.__state[i].append(next_rand)# / float(self.__count_sities)) 


	def __calc_W(self, x, i, y, j):
		"Calculation W in Hopfild's model"
		return - self.__A * self.__sigma(x, y) * (1.0 - self.__sigma(i, j)) \
			   - self.__B * self.__sigma(i, j) * (1.0 - self.__sigma(x, y)) \
			   - self.__C * self.__distances[x][y] * (self.__sigma(i, j - 1) + self.__sigma(i, j + 1)) \
			   + self.__D


	def __sigma(self, i, j):
		'Return 1.0 if i equal j'
		i %= self.__count_sities
		j %= self.__count_sities
		if i == j:
			return 1.0
		return 0.0


	def __update_state(self):
		"Update states all neurals in Hopfild's model"
		is_change = True

		for x in range(self.__count_sities):
			for i in range(self.__count_sities):
				cur_signal = 0.0

				for y in range(self.__count_sities):
					for j in range(self.__count_sities):

						if i == j and x == y:
							continue
						cur_signal += self.__calc_W(x, i, y, j) * self.__state[y][j]

				if self.__state[x][i] != self.__step_function(cur_signal):
					is_change = False
				self.__state[x][i] = self.__step_function(cur_signal)

		return is_change


	def __Hopfild_network_run(self):
		"Run Hopfild's neural network"
		i = 0
		changed = False
		while i < 100 and not changed:
			changed = self.__update_state()
			i += 1
		print i


	def __check_for_correct(self):
		'Check state of neural network on correct way'
		for i in range(self.__count_sities):
			temp = 0
			for j in range(self.__count_sities):
				if self.__state[i][j] == 1.0:
					temp += 1
				if self.__state[j][i] == 1.0:
					temp += 1
			if temp != 2:
				return False
		return True


	def __annealing_network_run(self, update_progressbar):
		'Run neural network by annealing algorithm'
		d_max = math.sqrt(2) * 400.
		max_T = 200.
		T = max_T
		d_T = 0.02

		X = 0
		update_progressbar(max_T, T)

		while T > 0.:
			U_xi = []
			V_xi = []

			for i in range(self.__count_sities):
				temp = 0.0
				for Y in range(self.__count_sities):
					if X != Y:
						temp -= d_max * self.__state[Y][i]
						temp -= self.__distances[X][Y] * (self.__state[Y][(i - 1) % self.__count_sities] 
														+ self.__state[Y][(i + 1) % self.__count_sities])
				U_xi.append(temp)

				V_xi.append(math.exp(U_xi[i] / T))

			sum_V = sum(V_xi)

			if sum_V == 0.0:
				break

			for i in range(self.__count_sities):
				self.__state[X][i] = V_xi[i] / sum_V

			T -= d_T
			X += 1
			X %= self.__count_sities
			update_progressbar(max_T, T)


	def run(self, dist, annealing, update_progressbar):
		'Run neural network for calculation shortest way'

		self.__init_network(dist)

		if not annealing:
			self.__Hopfild_network_run()
		else:
			self.__annealing_network_run(update_progressbar)

		for j in range(self.__count_sities):
			print self.__state[j]

		way = []

		correct = self.__check_for_correct()

		if correct:
			for j in range(self.__count_sities):
				for i in range(self.__count_sities):
					if self.__state[i][j] == 1.0:
						way.append(i)
						break


		way_distance_length = 0
		if correct:
			way_distance_length = self.__way_distance(way)
			print way_distance_length

		return correct, way, way_distance_length


	def __way_distance(self, way):
		'Calculation distance in correct way'
		way_distance_length = 0
		for i in range(self.__count_sities):
			way_distance_length += self.__distances[way[i]][way[(i + 1) % self.__count_sities]]
		return way_distance_length


	def distance(self, pointA, pointB):
		'Calculation distance between two sities'
		return math.sqrt((float(pointA[0]) - float(pointB[0])) ** 2 + (float(pointA[1]) - float(pointB[1])) ** 2)


	def createDistList(self, points):
		'Create array of distances between all sities'
		d = []
		for i in range(len(points)):
			d.append([])
			for j in range(len(points)):
				d[i].append(self.distance(points[i], points[j]))
		return d