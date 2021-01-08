# create a vechiele class and  with max_speed and mileage instance attributes
# define property that should have the same value for every class instance
#bus class and car class & access the super class attributes

class Vechile:
    colour= "White"
    def __init__(obj,name,speed,mil):
        obj.veh_name = name
        obj.max_speed = speed
        obj.mileage = mil

class Bus(Vechile):
    pass

class Car(Vechile):
    pass

b = Bus("School volvo",180,12)
print('Name:',b.veh_name)
print('Max Speed:',b.max_speed)
print('Mileage:',b.mileage)
print("colour:",b.colour)
print()

c = Car("BMW",240,20)
print('Name:',c.veh_name)
print('Max Speed:',c.max_speed)
print('Mileage:',c.mileage)
print("colour:",c.colour)


