fligh_co2 = 0
total_co2 = 0
co2_car = 0
co2_bike = 0
electric_co2 = 0
vehicle_type = " "
bike_size = " "
car_fuel = " "
electric_usage = 0
milage_car = 0
milage_bike = 0
num_flight = 0


def car(a, b):
    if a == 'petrol':
        co2_car = (174.31*b)/1000
        return int(co2_car)
    elif a == 'diesel':
        co2_car = (168.4*b)/1000
        return int(co2_car)
    elif a == 'cng':
        co2_car = (176.24*b)/1000
        return int(co2_car)
    else:
        co2_car = 0
        return int(co2_car)


def bike(c, d):

    if c == 'large':
        co2_bike = (132.45*milage_bike)/1000
        return int(co2_bike)

    elif bike_size == 'medium':
        co2_bike = (100.9*milage_bike)/1000
        return int(co2_bike)
    elif bike_size == 'small':
        co2_bike = (83.06*milage_bike)/1000
        return int(co2_bike)
    else:
        co2_bike = 0
        return int(co2_bike)


def house(e):
    electric_co2 = (930*electric_usage)/1000
    return electric_co2


def plane(f, g):
    fligh_co2 = 0
    i = 1
    while i < f:
        i = i+1
        temp = int(input("enter the distance of each flight-"))
        if temp < 300:
            fligh_co2 = fligh_co2 + (temp*0.25)
        elif temp >= 300 and temp < 2299:
            fligh_co2 = fligh_co2 + (temp*0.14)
        elif temp >= 2299:
            fligh_co2 = fligh_co2 + (temp*0.17)
    return fligh_co2


def leaderboard():
    file = open("leaderboard.txt", "r")
    print("\n")
    print("⬇ Check out the leaderboard ⬇")
    leaderboard = [line.replace('\n', '') for line in file.readlines()]
    for i in leaderboard:
        print(i)
    file.close()



def foodConsumption(diet):
    if diet == 'meat lover':
        return 3300
    elif diet == 'average':
        return 2500
    elif diet == 'no beef':
        return 1900
    elif diet == 'vegetarian':
        return 1700
    elif diet == 'vegan':
        return 1500

name = input("What is your name-")
vehicle_type = input("do u own a car,bike or both -")
vehicle_type = vehicle_type.lower()
if vehicle_type == 'car':
    car_fuel = input("enter the fuel used by the car-")
    car_fuel == car_fuel.lower()
    milage_car = int(input("enter distance traveled by car in km-"))

elif vehicle_type == 'bike':
    bike_size = input(
        "if the bike is greater tha 500cc pls enter 'large', if it is between 125cc and 500 cc pls enter 'medium', if less than or equal to 125 pls enter 'small'- ")
    milage_bike = int(input("enter the distance done by the bike in km-"))
elif vehicle_type == 'both':
    car_fuel = input("enter the fuel used by the car-")
    car_fuel == car_fuel.lower()
    milage_car = int(input("enter distance travled by car in km-"))
    print("Enter the category that you bike falls under: ")
    print("If the bike is greater than 500cc, enter 'large', if it is between 125cc and 500cc enter'medium',if less than or equal to 125cc enter 'small'")
    bike_size = input()
    bike_size = bike_size.lower()
    milage_bike = int(input("enter the distance done by the bike in km-"))

flight = input("do you take flights?-")
flight = flight.lower()
if flight == "yes":
    num_flight = int(input("how many flights do u take in a year "))
    temp = int(input("enter the distance of each flight-"))
    flight_co2 = plane(num_flight, temp)

electric_usage = int(input("enter last months electric usage in KWh-"))
print("Enter your type of diet: ")
print("Meat Lover")
print("Average")
print("No beef")
print("Vegetarian")
print("Vegan")
diet = input("Diet type: ")
diet = diet.lower()


print("co2 emission produced by car in kg = ", car(car_fuel, milage_car))
print("co2 emmision produced by bike in kg = ", bike(bike_size, milage_bike))
print("co2 emmisons by electric usage in kg = ", house(electric_usage))
print("co2 emission produced by flights in kg = ", fligh_co2)
total_co2 = car(car_fuel, milage_car)+bike(bike_size,
                                           milage_bike)+house(electric_usage)+fligh_co2 + foodConsumption(diet)

print("yout total co2 emmision is ", total_co2, "kg")

diff_in_consumption = 0
avg_consumption = 2470
diff_in_consumption = abs(total_co2 - avg_consumption)
if (avg_consumption > total_co2):
    print("Your carbon emission is less than the average carbon emission per capita by ",
          diff_in_consumption, " kgs of carbon dioxide")
else:
    print("Your carbon emission is more than the average carbon emission per captia by ",
          diff_in_consumption, " kgs of carbon dioxide")

leaderboard_choice = input("do u wish to view the leaderboard of the lowest carbon emmisions - ")
leaderboard_choice = leaderboard_choice.lower()
if leaderboard_choice == 'yes':
    leaderboard()
else:
    print("thank you for useing the calculator")










