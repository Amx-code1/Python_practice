class PlayerCharacter:
    membership = True
    def __init__(self,name,age):
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')
        
    def run(self, hello):
        print(f'my name is {self.name}')
        
        
player1 = PlayerCharacter('Cindy',44)
player2 = PlayerCharacter('tom',21)
player2.attack = 50
# print(player1.age)
print(player2.shout())
print(player1.run('hello'))
# print(player2.run())