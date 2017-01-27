class car:

	price_raise = 2.5

	def __init__(self, model, price, color):
		self.model = model
		self.price = price
		self.color = color

	def price_increase(self):
		self.price = int(self.price * self.price_raise)

	def __add__(self, other):
		return self.price + other.price
		
	def __len__(self):
		return len(self.color)


class tuktuk(car):

	price_raise = 2.0

	def __init__(self, model, price, color, mileage):
		
		car.__init__(self, model, price, color) 
		self.mileage = mileage

class vehicles(car):
	def __init__(self, model, price, color, car_no=None):
		car.__init__(self, model, price)

###################################################
#danders



wish = car('toyota', 700, 'blue')
range_rover = car('landrover', 3000, 'black' )

piaggio = tuktuk('piaggo', 150, 'grey', 10000)

print len(wish)
