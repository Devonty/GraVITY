import pygame
from speedThings import *
from config import *
import random as rd

class Planet:
	def __init__(self, mass = 100000000000):
		self.color = pygame.Color((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
		self.mass = mass  # кг
		self.speed = Speed(rd.randint(-40, 40), rd.randint(-40, 40))
		self.last_turn = 0
		self.sum_acce = Acceleration()
		self.cords = Cords()
		self.radius = 10


	def set_pos(self, x, y):
		self.cords = Cords(x, y)

	def update(self, delta_time=0.1):
		# boost
		self.speed = self.speed + self.sum_acce * delta_time
		# move
		self.cords += self.speed * delta_time
		# clean
		self.sum_acce = Acceleration()

	def add_acce(self, acce):
		self.sum_acce = self.sum_acce + acce

	def render(self, screen):
		pygame.draw.circle(screen, self.color, self.cords.get_cords(), self.radius)
		pygame.draw.line(screen, self.color, self.cords.get_cords(), (self.cords + self.speed).get_cords())

