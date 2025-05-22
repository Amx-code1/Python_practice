class Playercharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
player1 = Playercharacter('aman',22)
print(player1.name)
print(player1.age)

player2 = {'name': 'aman','age': 22}
print(player2['name'])
print(player2['age'])