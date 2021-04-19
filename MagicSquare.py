#Program to print Magic square
n = 3
MagicSquare =[[0,0,0],[0,0,0],[0,0,0]]

middle = round (n/2)

def Check(number):
    if number < 0:
        number = n + number
    elif number > n-1:
        number = number - n
    else:
        number = number
    return number
row = 0
coloumn = middle-1
#print(MagicSquare[row][coloumn])
#print("row "+str(row)+" coloumn "+str(coloumn))

for value in range(n*n):
    value = value+1
    #print(value)
    if MagicSquare[row][coloumn]==0 :
        MagicSquare[row][coloumn]= value
        #print("row "+str(row)+" coloumn "+str(coloumn))
        row = Check(row - 1)
        coloumn = Check(coloumn + 1)
    else :
        row = Check(row+2)
        coloumn = Check(coloumn-1)
        MagicSquare[row][coloumn]= value
        row = Check(row - 1)
        coloumn = Check(coloumn + 1)
        #print("row "+str(row)+" coloumn "+str(coloumn))
    
    
# print(MagicSquare)
for row in range(0,n):
    print("|",end="")
    for coloumn in range(0,n):
        print(MagicSquare[row][coloumn],end=" ") 
        print("|",end="")
    print()
