try:
  num1,num2=eval(input("ENTER YOUR NUMBERS SEPARATED BY A COMMA"))
  result=num1/num2
  print(result)
except ZeroDivisionError:
  print("DIVISION BY ZERO IS AN ERROR")  
except SyntaxError:
  ("THERE IS NO COMMA PLEASE ENTER NUMBER LIKE THIS 1,2")  
except:
  print("WRONG INPUT")  
else:
  print("NO ERROR")  
finally:
  print("THIS WILL BE EXECUTED FLAWLESSLY")  