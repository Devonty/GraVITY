G_ = 6.6743 * 10 ** -11  # м**3 кг**-1 с**-2


class Cords:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def get_cords(self):
		return self.x, self.y

	def distance_in2(self, other):
		# a**2 + b**2 = c**2
		# return c**2
		delta_cord = self - other
		return (delta_cord.x ** 2 + delta_cord.y ** 2) * 10

	def __add__(self, other):
		return Cords(x=self.x + other.x,
		             y=self.y + other.y)

	def __sub__(self, other):
		return Cords(x=self.x - other.x,
		             y=self.y - other.y)

	def __mul__(self, other: int):
		return Cords(x=self.x * other,
		             y=self.y * other)

	def __truediv__(self, other: int):
		return Cords(x=self.x / other,
		             y=self.y / other)

	def __str__(self):
		return self.__class__.__name__ + f" x: {self.x} y: {self.y}"


class Speed(Cords):

	def __add__(self, other):
		return Speed(x=self.x + other.x,
		             y=self.y + other.y)

	def __sub__(self, other):
		return Speed(x=self.x - other.x,
		             y=self.y - other.y)

	def __mul__(self, other: int):
		return Speed(x=self.x * other,
		             y=self.y * other)

	def __truediv__(self, other: int):
		return Speed(x=self.x / other,
		             y=self.y / other)


class Acceleration(Speed):

	def __add__(self, other):
		return Acceleration(x=self.x + other.x,
		                    y=self.y + other.y)

	def __sub__(self, other):
		return Acceleration(x=self.x - other.x,
		                    y=self.y - other.y)

	def __mul__(self, other: int):
		return Acceleration(x=self.x * other,
		                    y=self.y * other)

	def __truediv__(self, other: int):
		return Acceleration(x=self.x / other,
		                    y=self.y / other)


'''class Force:
	def __init__(self, force=0, acceleration = Acceleration()):
		self.force = force
		self.vector = acceleration

	def get_acceleration(self, mass):
		return force / mass

	def __add__(self, other):
		return Force(force=self.force + other.force)

	def __sub__(self, other):
		return Force(force=self.force - other.force)

	def __mul__(self, other: int):
		return Force(force=self.force * other)

	def __truediv__(self, other: int):
		return Force(force=self.force / other)'''