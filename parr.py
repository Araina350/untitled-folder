class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("Blu",10)
woo=parrot("Woo",15)
print("BLU IS A {}".format(blu.species))
print("WOO IS ALSO A {}".format(woo.species))
print("{} IS {} YEARS OLD".format(blu.name,blu.age))
print("{} IS {} YEARS OLD".format(woo.name,woo.age))