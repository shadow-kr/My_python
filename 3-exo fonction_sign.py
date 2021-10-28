print("\t condition if")
def sign(x):
    if(x>0):
        print(x,"est posetif")
    elif(x==0):
        print(x,"est null")
    else:
        print(x,"est negatif")
    return x

        
a=sign(5)
b=sign(-3)
c=sign(0)

print("\n \t Boucle for")
for i in range(0,4,2):# de 0 à 3 avec un pas de 2
     print(i,": golden wind")
     
print("\t Boucle while")   
k=0
while k<10:
    print(k)
    k+= 1 #k+
    


