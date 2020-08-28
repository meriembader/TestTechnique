 
string = input("écris quelque chose en miniscule  : ")
string1 = ''
i = 0

while(i < len(string)): 
    if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]
    i = i + 1

print("String en MaJ =  ", string1)