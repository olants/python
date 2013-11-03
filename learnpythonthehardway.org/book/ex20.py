from sys import argv

script, input_file = argv
# new function read file
def print_all(f):
	print f.read()
# function rewind seek
def rewind(f):
	f.seek(0)
# read file a line by line
def print_a_line(line_count, f):
	print line_count, f.readline()
# open file
current_file = open(input_file)

print "First let's print the whole file:\n"
# print all file
print_all(current_file)

print "Now let's rewind, kind of like a type."
# rewind file
rewind(current_file)

print "Let's print three lines:"
# read file line by line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
