class Matrix():
	def __init__(self, matrix):
		self.matrix = matrix
		self.rows = len(matrix)
		cols = []
		for row in matrix:
			cols.append(len(row))
		
		cols = set(cols)
		if len(cols) > 1:
			raise ValueError("Columns has uneven elements")

		else:
			self.cols = len(self.matrix[0])
	

	def __str__(self):
		res = ""
		for row in range(len(self.matrix)):
			for column in range(len(self.matrix[row])):
				if row == (len(self.matrix) -1)  and column == (len(self.matrix[row]) -1):
					res += f"{self.matrix[row][column]}"
					return res
				elif column == len(self.matrix[row]) - 1:
					res += f"{self.matrix[row][column]}"
					res += "\n"
				else:
					res += f"{self.matrix[row][column]} "
					
	

	def __add__(self, other):
		if other.rows != self.rows:
			return ValueError("Cannot add two matrices with different length of rows: {0} {1}".format(other.rows, self.rows))
		
		if  other.cols != self.cols:
			return ValueError("Cannot add two matrices with different length of cols: {0} {1}".format(other.cols, self.cols))

		m = []
		for row in range(self.rows):
			m.append([])
			for col in range(self.cols):
				m[row].append([])
				temp = self.matrix[row][col] + other.matrix[row][col]
				m[row][col] = temp

		return Matrix(m)
	

	def __sub__(self, other):
		if other.rows != self.rows:
			return ValueError("Cannot subtract two matrices with different length of rows: {0} {1}".format(other.rows, self.rows))
		
		if  other.cols != self.cols:
			return ValueError("Cannot subtract two matrices with different length of cols: {0} {1}".format(other.cols, self.cols))

		m = []
		for row in range(self.rows):
			m.append([])
			for col in range(self.cols):
				m[row].append([])
				temp = self.matrix[row][col] - other.matrix[row][col]
				m[row][col] = temp

		return Matrix(m)


	def __mul__(self, other):
		m = []
		temp = 0
		if type(other) is int or type(other) is float:
			for row in range(self.rows):
				m.append([])
				for col in range(self.cols):
					m[row].append([])
					temp = self.matrix[row][col] * other
					m[row][col] = temp

			return Matrix(m)
		elif type(other) is Matrix:
			if self.cols != other.rows:
				print(f"{self.rows} is not equal to {other.cols}")
			else:
				for row in range(self.rows):
					m.append([])
					for col in range(len(other.matrix[0])):
						m[row].append([])
						for x in range(self.cols):
							temp += self.matrix[row][x] * other.matrix[x][col]

						m[row][col] = temp
						temp = 0
			
			return Matrix(m)


# How to use the Matrix
if __name__ == "__main__":
	a = [
		[1, 2],
		[3, 4]
	]

	b = [
		[1, 2],
		[3, 4]
	 	] 

	m = Matrix(a)
	n = Matrix(b)

	print(f"Addition => \n{m + n}")
	print(f"Subtraction => \n{m - n}")
	print(f"Scalar Multliplication => \n{m * 5}")
	print(f"Matrix-Matrix Multiplication => \n{m * n}")