j=0
Plateau= [ [True , False , False , False ] ,
           [ False , True , True , False ] ]

def VoisinCase(Plateau, x, y):
    Tab = [[5,5,5,5],[5,5,5,5]]
    i= 0
     
    if (x==0):



        if (Plateau [x-1][y]==False):
            
        
            Tab[0][i]= x-1
            Tab[1][i]=y
            i=i+1
            print(Tab)
        
    if (x==0):

        if (Plateau [x+1][y]==False):
            Tab[0][i]=x+1
            Tab[1][i]=y
            i=i+1
    if (y<3):

        if (Plateau [x][y+1]==False):
            Tab[0][i]=x
            Tab[1][i]=y+1
            i=i+1
        else:
            i=i
    
    if (y>3):

        if (Plateau [x][y-1]==False):
            Tab[0][i]=x
            Tab[1][i]=y-1
            i=i+1


        return Tab


while( j< len(VoisinCase(Plateau,1,3))) :
    print (VoisinCase(Plateau,1,3)[0][j])
    print (VoisinCase(Plateau,1,3)[1] [j])
    break