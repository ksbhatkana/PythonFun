def power_number(power):
	def base_number(number):
    	return number**power
  	return base_number
	
cube = power_number(3)
print(cube(4))

square = power_number(2)
print(square(5))
