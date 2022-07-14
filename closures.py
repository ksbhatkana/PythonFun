def power_number(power):
	def base_number(number):
    	return number**power
  	return base_number
	
cube = power_number(3)
print(cube(4))

square = power_number(2)
print(square(5))



#This is possible in Python since Python functions are first class. 
#It means that Python treats functions as values, so you can assign a function to a variable, pass it as a function argument or return it by another function.
