lower=int(input("ENTER THE LOWER RANGE"))
upper=int(input("ENTER THE UPPER RANGE"))
print("THE PRIME NUMBERS BETWEEN ",lower," AND ",upper," are:" )
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)    