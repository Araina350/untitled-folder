
medc = input("Do you have a medical certificate? (Yes or No): ").strip()
atten=int(input("Enter your attendance"))
if medc == "Y":
    print("YOU ARE ALLOWED TO APPEAR FOR THE EXAM")
else:
    if atten>=75:
         print("YOU ARE ALLOWED TO APPEAR FOR THE EXAM")
    else:
         print("YOU ARE NOT ALLOWED TO APPEAR FOR THE EXAM")

