def hotel_cost (nights):
    return 100*nights
def plane_cost(city):
    if "Charlotte" == city:
        return 183
    if "Tampa" == city:
        return 223
    if "Pittsburgh" == city:
        return 230
    if "LA" == city:
        return 436
def trip_cost(nights,city):
    return hotel_cost(nights)+plane_cost(city)  
print("Cost of hotel is ",hotel_cost(12))
print("Cost of plane is ",plane_cost("Pittsburgh"))
print("Total cost is ",trip_cost(12,"Pittsburgh"))