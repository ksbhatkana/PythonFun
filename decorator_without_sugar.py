def decorator_function(any_function):
	def wrapper_function():
		print('This is awesome function')
	return wrapper_function

def func1():
	print('This is function1')
	
def func2():
	print('This is function2')
	
called = decorator_function(func1)
called()
