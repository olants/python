#import function argv from module
from sys import argv
#assign content for vars
script, filename = argv
#use function to open file
txt = open(filename)
#print filename
print "Here's your file %r:" % filename
#print content of file
print txt.read()
#print string
print "Type the filename again:"
#get name for new file
file_again = raw_input("> ")
#open new file
txt_again = open(file_again)
#print content of new file
print txt_again.read()
