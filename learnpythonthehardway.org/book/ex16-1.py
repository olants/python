from sys import argv

script, filename = argv
#filename = raw_input("Enter name of file to read file: ")
txt = open(filename)
print txt.read()
