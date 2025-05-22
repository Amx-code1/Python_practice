class Playercharacter:
    membership = True 
    def __init__(self,name,age):
        if (self.membership):
            self.name = name
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name} ')
        return 'done'
    
player1 = Playercharacter('cindy',44)
player2 = Playercharacter( 'tom',21)
player2.attack = 50
print(player2.shout())
print(player1.shout())