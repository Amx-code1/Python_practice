class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
        
player1 = PlayerCharacter('Cindy',44)
player2 = PlayerCharacter('tom',21)

print(player1.age)
print(player2.run)