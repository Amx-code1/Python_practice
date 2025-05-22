class Playercharacter:
    membership = True 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print('fast')
        return 'done'
    
player1 = Playercharacter('cindy',44)
player2 = Playercharacter( 'tom',21)
player2.attack = 50
print(player2.membership)