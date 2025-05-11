class PlayerCharacter:
    membership = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
        return 'done'
        
player1 = PlayerCharacter('Cindy',44)
player2 = PlayerCharacter('tom',21)
player2.attack = 50
# print(player1.age)
print(player2.membership)
# print(player2.run())