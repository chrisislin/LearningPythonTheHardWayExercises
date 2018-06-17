x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
#string inside string
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

#string inside string
print "I said: %r" %x

#string inside string
print "I also said: '%s'." %y

hilarious = False
#string inside string, also didn't print this yet
joke_evaluation = "Isn't that joke so funny?! %r"

#error if there is no %
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e