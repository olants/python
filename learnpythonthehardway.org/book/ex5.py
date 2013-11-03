my_name = 'Oleksii A. Tsymbaliuk'
my_age = 25 # not a lie
my_height = 172 # cm
my_weight = 62 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actuall that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight)
