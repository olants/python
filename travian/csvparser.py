from numpy import genfromtxt
title = ['level','wood-small','clay-small','iron-small','crop-small','total','pop-small','culture-small','production','resoourse per production']
my_data = genfromtxt('wood.csv', delimiter=',')
i = 0

print title
print title[0]
print len(title)

def output_function(i):
#	for i in range(i, len(my_data)):
		j = 0
		total = 0
		for j in range(j, len(title) - 1):
			print title[j],":",  my_data[i][j]
		for j in range(1, 5):
			total = total + my_data[i][j]
	#		print total
		print "Total resources need", total

level = input("Enter level: ")
output_function(level - 1)
