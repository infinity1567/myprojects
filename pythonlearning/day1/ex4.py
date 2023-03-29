# number of cars
cars=100
#Number of people car can take 
space_in_a_car=4
# Number of drivers
drivers=30
# Number of passengers
passengers=90
#calculates the amount of cars not driven by subtracting the amount of drivers from the amount of cars
cars_not_driven=cars-drivers
#assigns cars_driven variable to # of drivers, makes sense
cars_driven=drivers
#Carpool capacity is the amount of driven cars times the space in one car 
carpool_capacity=cars_driven*space_in_a_car
#Calculates average passengers per car on a given day with x amount of cars driven
average_passengers_per_car=passengers/cars_driven

print("There are ", cars, "cars available.")
print("There will only be ", drivers, "drivers available.")
print("There will be", cars_not_driven ,"empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have ", passengers, "to carpool today.")
print("We need to put about " ,average_passengers_per_car, "in each car.")

