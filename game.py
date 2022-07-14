import pygame
from config import *
from speedThings import *
from planet import Planet
import random as rd
import time
import math


class Game:
	def __init__(self):
		self.turn_now = 0
		self.fps = FPS
		self.pause = False
		self.planets = list()
		self.last_update_time = time.time()

		for _ in range(10):
			pltn = Planet()
			pltn.set_pos(rd.randint(HEIGHT / 4, HEIGHT * 3 / 4), rd.randint(WIDTH / 4, WIDTH * 3 / 4))
			pltn.mass = rd.randint(10000000000, 100000000000)
			self.planets.append(pltn)

		pltn = Planet()
		pltn.set_pos(HEIGHT / 2, WIDTH / 2)
		pltn.speed = Speed()
		pltn.mass = 10**14
		pltn.radius = 20
		self.planets.append(pltn)

	def mainloop(self):
		pygame.init()
		pygame.display.set_caption('Gravity')
		self.screen = pygame.display.set_mode((HEIGHT, WIDTH))

		# ЛКМ Удерживается
		self.left_mouse_button_pressed = False
		# Последняя позиция мыши
		self.x_mouse = 0
		self.y_mouse = 0

		# Событие обновления
		UPDATE = pygame.USEREVENT + 1
		pygame.time.set_timer(UPDATE, 100)

		self.running = True
		clock = pygame.time.Clock()
		while self.running:
			#self.screen.fill((0, 0, 0))
			self.turn_now += 1
			for event in pygame.event.get():

				if event.type == pygame.QUIT:  # Выход
					self.running = False

				if event.type == pygame.MOUSEBUTTONDOWN:  # Нажата кнопка мыши
					pass

				if event.type == pygame.MOUSEBUTTONUP:
					pass

				if event.type == pygame.MOUSEMOTION:
					pass

				if event.type == UPDATE:
					if not self.pause:
						self.update()

				self.render()
				pygame.display.flip()
				clock.tick(self.fps)

	def render(self):
		for plnt in self.planets:
			plnt.render(self.screen)

	def update(self):
		time_now = time.time()
		delta_time = time_now - self.last_update_time

		for i in range(len(self.planets)):
			for j in range(i + 1, len(self.planets)):
				plntI = self.planets[i]
				plntJ = self.planets[j]
				dist_in2 = plntI.cords.distance_in2(plntJ.cords)
				force = G_ * (plntJ.mass * plntI.mass) / dist_in2


				delta_cordsI = plntJ.cords - plntI.cords  # I -> J
				delta_cordsJ = plntI.cords - plntJ.cords  # J -> I

				acceI = Acceleration() + delta_cordsI * (force / plntI.mass)
				acceJ = Acceleration() + delta_cordsJ * (force / plntJ.mass)

				plntI.add_acce(acceI)
				plntJ.add_acce(acceJ)
		# Движение
		for plnt in self.planets:
			plnt.update(delta_time)
		self.last_update_time = time.time()
