def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            ctr+=1
            lst.append(word)
    print("LIST OF WORDS WHERE THE FIRST AND LAST LETTER IS SAME ARE\n",lst) 
    return ctr   
count=match_words(["tenant","mango","radar","malyalam","sweat"])

print("LIST OF WORDS WHERE THE FIRST AND LAST LETTER IS SAME ARE",count)