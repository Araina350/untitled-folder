s1=[1,2,3,4,5]
s2=['q','w','e','r','t','y']
s3=list(zip(s1,s2))
print(s3,"\n")
list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
comp=["Infosys","Zomato"]  
money=[1234567986868540,1354566565764430]  
new={comp:money for comp,
            money in zip(comp,money)}
print("\n{}".format(new))