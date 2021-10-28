#pour afficher une barre de chargement
#lol tqdm=T9ADOUM it's in arabic

from tqdm import tqdm
import time


for i in tqdm(range (10)):
    print(i)
    time.sleep(0.5)
    