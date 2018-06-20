#animal is an object
class animal(object):
	pass

#dog, cat, person are all objects
class Dog(animal):
	def __init__(self, name):
		self.name = name

class Cat(animal):
	def __init__(self, name):
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

#gets Person name as parameter, and salary
class Employee(Person):
	def __init__(self,name,salary):
		super(Employee, self).__init__(name)
		self.salary = salary

#fish is object, other fishes are like this fish
class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass

##rover is dog
rover = Dog ("Rover")
satan = Cat ("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
#initialize it
crouse = Salmon()
harry = Halibut()