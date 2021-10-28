#argparse utulisé pour donner les valeur des variable avec commandes et ajouter des helps
import argparse
import math


# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--x', type=int, help='hola c est le premier paramtre')
parser.add_argument('--y', type=int, help='hawdy guv c est le deuxieme paramtre')

#pour entrer une liste de valeur on utilise nargs=nb de valeurs
parser.add_argument('--values', type=int, nargs=3)


# Parse the argument
args = parser.parse_args()

# Print "Product" + the user input argument
product = args.x * args.y
print('Product:', product)

print('x= ',args.x ,'y= ', args.y, '\ndonc le Product:', product)

#affiche la liste
print('Sum:', args.values)




'''Remarque pour executer se fichier

run 9-Module_argparse_pour_commande_terminal --x 3 --y 2 --value 1 2 3



1-clic sur f5 pour executer --> on aura message mais cest bon
2-run utiliser_argparse_pour_commande_terminal --x 4 --y 2
    ici on a donner à x=4 et y=2
3-run utiliser_argparse_pour_commande_terminal -h 
    cette commande te donnera le help qui te dit chaque argument a quoi il sert




if __name__ == '__main__':
    
Cette condition est utilisée pour développer un module pouvant à la fois être exécuté directement mais aussi être importé par un autre module pour apporter ses fonctions.
'''




