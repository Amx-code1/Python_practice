class PlayerCharacter:
    def __init__(self,name):
        self.name = name
        
    def run(self):
        print('run')
        
player1 = PlayerCharacter('Cindy')
player2 = PlayerCharacter('tom')

print(player1.name)
print(player2.name)