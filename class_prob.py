flower_levels = {
	"Orchid" : 15,
	"Rose" : 25,
	"Jasmine" : 40	
}

class Flower:
	def __init__(self):
		self.flower_name = None
		self.price_per_kg = None
		self.stock_available = None

	def get_flower_name(self):
		return self.flower_name

	def set_flower_name(self, flower_name):
		self.flower_name = flower_name

	def get_price_per_kg(self):
		return self.price_per_kg

	def set_price_per_kg(self, price_per_kg):
		self.price_per_kg = price_per_kg

	def get_stock_available(self):
		return self.stock_available

	def set_stock_available(self, stock_available):
		self.stock_available = stock_available

	def validate_flower(self):
		if self.flower_name in flower_levels.keys():
			return True
		return False

	def validate_stock(self, required_quantity):
		if required_quantity <= self.stock_available:
			return True
		return False

	def sell_flower(self, required_quantity):
		if self.validate_flower() and self.validate_stock(required_quantity):
			self.stock_available -= required_quantity

	def check_level(self):
		if self.stock_available > flower_levels[self.flower_name] :
			return True
		return False


flower_1 = Flower()
flower_1.set_flower_name('Orchid')
flower_1.set_stock_available(30)
flower_1.set_price_per_kg(10)
print(flower_1.get_flower_name(), flower_1.get_stock_available(), flower_1.get_price_per_kg())

flower_1.sell_flower(10)
print(flower_1.get_flower_name(), flower_1.get_stock_available(), flower_1.get_price_per_kg())
