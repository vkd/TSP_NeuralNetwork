class LoadStrings:
	'Load text strings from file'

	__output_dict = {}

	def __init__(self, filename):
		for line in open(filename):
			index = line.find('=')
			if index == -1:
				continue

			const = line[:index]
			string = line[index + 1 : -1] #from '=' to '\n'(without this)

			self.__output_dict[const] = string

	def getString(self, const):
		if const not in self.__output_dict:
			return '***NONE***'
		return self.__output_dict[const]