class Vehicle():
    plate = ""
    year = 0
    weight = 0.0
    fee = 0.0
    def __init__(self, the_license, the_year):
        self.plate = the_license
        self.year = the_year
    def get_license(self):
        return self.plate
    def get_year(self):
        return self.year
    def get_weight(self):
        return self.weight
    def get_fee(self):
        return self.fee
    def set_weight(self, w):
        self.weight = w
    def set_fee(self, f):
        self.fee = f
    def __str__(self):
        return "Vehicle: {}  {}  Weight={}  Fee=${}".format(self.plate, self.year, self.weight, self.fee)

class Car(Vehicle):
    def __init__(self, the_license, the_year, the_style):
        Vehicle.__init__(self, the_license, the_year)
        self.style = the_style
    def set_weight(self, w):
        self.weight = w
        if w < 3000:
            self.fee = 30
        elif w < 5000:
            self.fee = 40
        else:
            self.fee = 50
    def __str__(self):
        return "Car: {} {} {}  Weight={}  Fee=${}".format(self.plate, self.year, self.style, self.weight, self.fee)
        
class Truck(Vehicle):
    def __init__(self, the_license, the_year, the_wheels):
        Vehicle.__init__(self, the_license, the_year)
        self.wheels = the_wheels
    def set_weight(self, w):
        self.weight = w
        if w < 3000:
            self.fee = 40
        elif w < 5000:
            self.fee = 50
        elif w < 10000:
            self.fee = 60
        else:
            self.fee = 70
    def __str__(self):
        return "Truck: {} {} {} wheels Weight={} Fee=${}".format(self.plate, self.year, self.wheels, self.weight, self.fee)

class Motorbike(Vehicle):
    CC = 0
    def __init__(self, the_license, the_year):
        Vehicle.__init__(self, the_license, the_year)
    def get_CC(self):
        return self.CC
    def set_CC(self, cc):
        self.CC = cc
        if cc < 50:
            self.fee = 10
        elif cc < 200:
            self.fee = 20
        else:
            self.fee = 35
    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${}".format(self.plate, self.year, self.CC, self.fee)

def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {}".format(c1.get_weight() ))
    print(t1)
    print("The fee for the truck is: {}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {}".format(b1.get_CC() ))
    print()
    #Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE
    l = [v1, c1, t1, b1]
    for i in l:
        print(i)
    v1 = c1
    print(v1)
    print()
main()