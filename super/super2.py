class user:
    
    def __init__(self,email):
        self.email = email
        
    def sign_in(self):
        print('logged in')

        
class Wizard(user):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        user.attack(self)
        print(f'attacking with power of {self.power}')    
class Archer(user):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows-left - {self.num_arrows}')

Wizard1 =Wizard('Merlin',60,'merlin@gmail.com')
# print(Wizard1)

print(Wizard1.email)