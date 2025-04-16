word=input("ENTER THE WORD ")
char=input("Enter the specific alphabet ")
i=0
count=0
while(i<len(word)):
    if(word[i]==char):
        count=count+1  
    i=i+1
print("THE NUMBER OF TIMES ",char," HAS OCCURED IS ",count)    
