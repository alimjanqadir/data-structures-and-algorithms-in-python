def fib(position):
	if position == 0: return 0
	if position == 1: return 1
	first = 0
	second = 1
	next = first + second
	for x in xrange(2, position):
		first =  second
		second = next
		next = first + second
	return next
	
def fib_recursive(position):
	if position < 0: return 0
	if position == 1: return 1
	return fib_recursive(position - 2) + fib_recursive(position - 1) 

print fib_recursive(9)
print fib_recursive(11)
print fib_recursive(0)
