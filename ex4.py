#number of cars
cars = 100
#space in a car, 4 per car
space_in_a_car = 4.0 #floating point if there's decimals, otherwise just integer
#number of drivers
drivers = 30
#number of total passengers
passengers = 90
#only so much cars, some empty
cars_not_driven = cars - drivers
#number of drivers = number of cars driven
cars_driven = drivers
#total capacity = number of car * cars driven
carpool_capacity = cars_driven * space_in_a_car
#avg passengers per car, since there might not be enough people
average_passengers_per_car = passengers/cars_driven #there's no variable called car_poop_capacity


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."