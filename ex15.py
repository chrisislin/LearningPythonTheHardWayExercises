from sys import argv
script, filename = argv

#only opens the filename
txt = open(filename)

#reads the name of the file, the contents inside the file
print "Here's your file %r:" %filename
print txt.read()

#txt2 = raw_input(open(filename))
#print txt2
#do it again
# print "Type the filename again."
# file_again = raw_input("> ")

# txt_again = open(file_again)
# print txt_again.read()