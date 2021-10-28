#Pour ecrire dans un fichier on fait "w" veut dir write ecrire
k=open("C:/Users/Toshiba/Pictures/python_tester/dio.txt","w")
k.write("hello mate")#ecrire le message suivant
k.close()

#Pour lire le fichier on fait "r"
k=open("C:/Users/Toshiba/Pictures/python_tester/dio.txt","r")
print(k.read())
k.close()

print('=====================Autre methodes======================')
#ecrire sans a fermer le fichier apres : methode direct
with open("C:/Users/Toshiba/Pictures/python_tester/dio.txt","r") as f:
    print(f.read())

print('==========================================================') 
#on ecrit une boucle :
with open("C:/Users/Toshiba/Pictures/python_tester/jo.txt","w") as j:
   for i in range(5):
       j.write("{}^2= {} \n".format(i, i**2))# le premier {}=i et le deuxieme {}=i**2
#on affiche le fichier boucle
with open("C:/Users/Toshiba/Pictures/python_tester/jo.txt","r") as j:      
       print(j.read())
   