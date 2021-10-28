class gamer:
    #on cree le constructeur
    def __init__(self, name, hp,sp):
        #self est une base de données qui contient les elements contenus
        #self sert a affecter ces éléments name,hp... à la classe 
        self.name = name
        self.hp = hp
        self.sp = sp
        self.weapon = None
        print("hello ", self.name,"\thp:",self.hp, "\tsp:",self.sp)
    #methode  get:pour retourner un élément
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_sp(self):
        return self.sp
    
    #methode set:pour modifier
    def domage(self,domage):
        self.hp -=domage
        print('domage inflected:',domage)
        
    def attack_player(self,target_player):
        att = target_player.domage(self.sp-80)
        #domage(sp-80) --> hp=hp-sp-80
        
        
        
 
#palyers 
player1 = gamer("johnny",200,100)
player2 = gamer("gyro",300,200)
print('\n')


# game
player1.attack_player(player2)
print(player1.get_name(), 'attacks', player2.get_name())

print('P1->level of health:',player1.get_hp())
print('\n')

print('P2->level of health:',player2.get_hp())
print('\n')


class weapon:
    def __init__(self,w_name,w_attak):
        
        self.w_name = w_name
        self.w_attak = w_attak
        
    def get_w_name(self):
        return self.w_name
    def get_w_attak(self):
        return self.w_attak
    
knife = weapon('knife',30)
        
