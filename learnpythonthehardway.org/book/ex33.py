n_element =  int(raw_input("Enter number of elements: "))
#n_element = 2
numbers = []
i = 0

def some_func(some_var):
	i = 0
	for i in range (0, some_var):
#	while i < some_var:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

some_func(n_element)

print "The numbers: "

for num in numbers:
	print num
