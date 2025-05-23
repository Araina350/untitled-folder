class vehicle:
    def __init__(self,speed_max,mileage):
        self.speed_max=speed_max
        self.mileage=mileage
modelX=vehicle(300,30)
print("MODEL MAX SPEED:",modelX.speed_max)
print("MODEL MILEAGE",modelX.mileage)