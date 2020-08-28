x=9
phrase = str(x) 
Y=0
i=0
while(i <= len(phrase[i])):
    Y=Y+int(phrase[i]) 
    while (Y>=3):
        Y=Y-3
    if(Y==0):
        print(True)

    else:

        print(False)        
    break





    

