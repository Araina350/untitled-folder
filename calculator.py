print("ENTER THE OPERATION")
print("a:ADD")
print("b:Subtract")
print("c:Multiply")
print("d,Divide")
ch=input("ENTER YOUR CHOICE FROM ABOVE: ")
num1=int(input("ENTER THE FIRST NUMBER"))
num2=int(input("ENTER THE SECOND NUMBER"))
if ch == "a":
    print(num1,"+",num2,"=",add(num1,num2))
elif ch == "b":
    print(num1,"-",num2,"=",subtract(num1,num2)) 
elif ch =="c":
    print(num1,"*",num2,"=",multiply(num1,num2))    
else :
    print(num1,"/",num2,"=",divide(num1,num2))   
def add(P,Q):  
    return P+Q  
def subtract (P,Q):  
    return P-Q  
def multiply(P,Q):  
    return P*Q  
def divide(P,Q):  
    return P/Q           