class vehicle:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
class Bus(vehicle):
    pass
School_bus = Bus("School_Volvo",100,12)        
print("Vehicle name:",School_bus.name,"Speed:",School_bus.speed,"Mileage:",School_bus.mileage)