class user:
    def sign_in(self):
        print('logged in')
        
    def attack(self):# this is overwrited in output 
        print('do nothing')
        
class Wizard(user):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')    
class Archer(user):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows-left - {self.num_arrows}')

Wizard1 =Wizard('Merlin',60)
Archer1 =Archer('Robin', 30)
# print(Wizard1)

print(Wizard1.attack())