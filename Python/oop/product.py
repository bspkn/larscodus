class product(object):
	def __init__(self, price, name, weight, brand, cost):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = 'for sale'
		self.discount = 'none'			
		self.show() # optional displays all information about all products
	
	# chainable method displays all information for an object/instance
	def show(self):
		print 'Brand:', self.brand
		print 'Item Name:', self.name
		print 'Price:', '$'+str(self.price)
		print 'Weight:', self.weight
		print 'Cost:', '$'+str(self.cost)
		print 'Status:', self.status
		print 'Discount:', self.discount
		print '' # spacer for output
		return self
	
	# chainable method sets status value to sold
	def sell(self):
		self.status = 'sold'
		return self

	# method calculates and returns price including tax
	# must pass in an argument when calling this method
	def tax(self, salesTax):
		return '$'+str(self.price + (self.price * salesTax))
	 
	# chainable method takes argument when called
	# based on argument will set status, price, and discount
	def Return(self, reason):
		if reason == 'defective':
			self.status = 'defective'
			self.price = 0
		elif reason == 'open box':
			self.status = 'used'
			self.price *= 0.8
			self.discount = 'Discounted 20%'
		else:
			reason == 'like new'
		return self	 		

product01 = product(189, 'Air Max', '13 oz', 'Nike', 76)
product02 = product(2399, 'MacBook Pro', '4 lbs', 'Apple', 1100)
product03 = product(190700, '911 Turbo S', 'TBD', 'Porsche', 125000)

print 'Total price including tax for your Air Max is', product01.tax(0.1)
print product02.Return('open box').show()
print product03.sell().show()