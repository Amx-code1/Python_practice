class Playercharacter:
    membership = True 
    def __init__(self,name = 'anonymous',age = 0):
        if (age > 18):
            self.name = name
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name} ')
    
player1 = Playercharacter()
player2 = Playercharacter()
player2.attack = 50
print(player2.shout())
print(player1.shout())
print(player1.shout())