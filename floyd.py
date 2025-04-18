row=int(input("ENTTER THE NUMBER OF ROWS"))
initial__number=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(initial__number,end=" ")
        initial__number=initial__number+1
    print()    