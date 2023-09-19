class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        #print("The make of the vehicle is ",self.make,"\n""The model of the vehicle is ",self.model,"\n""The year the vehicle was manufactured is ",self.year)
        print('The make of the vehicle is {}\nThe model of the vehicle is {}\nThe year the vehicle was manufactured is {}'.format(self.make,self.model,self.year))


class Car(Vehicle):
    def __init__(self, make, model, year,num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_car_info(self):
        print("The number of doors the car has",self.num_doors)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year,engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def display_motorcycle_info(self):
        print("The engine size of the motorcycle in liters",self.engine_size)

if __name__ == "__main__":

    veh1 = Vehicle("Mersedes","C500",2023)
    veh1.display_info()
    
    car1 = Car("BMW","iX3",2019,4)
    car1.display_info()
    car1.display_car_info()

    mot1 = Motorcycle("HARLEY","9400 NW",2022,"800cc")
    mot1.display_info()
    mot1.display_motorcycle_info()
