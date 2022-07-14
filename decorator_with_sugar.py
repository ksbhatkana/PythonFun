def decorator_function(any_function):
	def wrapper_function():
		print('This is awesome function')
	return wrapper_function

@decorator_function
def func1():
	print('This is function1')
	
@decorator_function
def func2():
	print('This is function2')
	
func1()
