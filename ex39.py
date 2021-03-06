states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

cities ['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

print '-' * 10
print "Michigan's abbrev is: ", states['Michigan']
print "Florida's abb is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbrev
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state,abbrev)

#prints every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)

#does both
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])

print '-' * 10
#abb by state
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

#city default
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" %city