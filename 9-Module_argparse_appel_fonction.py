
import argparse


#run 9-Module_argparse_appel_fonction.py -c

def plus(ora):
    ari = 3
    x = ari + 2 
    print(x)
    
def mois(ora):
    
    ari = 3
    x = ari - 2
    print(x)

  
def main(ora):
   
    if ora.plus: plus(ora)
    elif ora.mois: mois(ora)
   
 

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--plus',  action='store_true',help='plus')
    parser.add_argument('-m', '--mois',  action='store_true',help='mois')

    
    args = parser.parse_args()
    main(args)