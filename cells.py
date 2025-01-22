import pygame, random

BLUE=(147, 202, 237)
GREY=(82, 78, 80)
class Cells:
	def __init__(self, width, height, cell_size):
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.cell_size = cell_size
		self.cells = [[0 for col in range(self.columns)] for row in range(self.rows)]

	def draw(self, window):
		for row in range(self.rows):
			for column in range(self.columns):
				color = BLUE if self.cells[row][column] == 1 else GREY
				pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size -1, self.cell_size - 1))

	def ran_gen(self):
		for row in range(self.rows):
			for column in range(self.columns):
				self.cells[row][column] = random.choice([0, 0, 1, 0,1,0,0,0,1,1])

	def clear(self):
		for row in range(self.rows):
			for column in range(self.columns):
				self.cells[row][column] = 0

	def toggle_cell(self, row, column):
		if 0 <= row < self.rows and 0 <= column < self.columns:
			self.cells[row][column] = not self.cells[row][column]

