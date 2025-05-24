class user:
    def sign_in(self):
        print('logged in')
        
class Wizard(user):
    pass

class Archer(user):
    pass

Wizard1 =Wizard()
# print(Wizard1)
print(Wizard1.sign_in())