class Playercharacter:
    def __init__(self,name,age):
        self._name = name
        self._age = age
        
    def run(self):
        return self
    
    def speak(self):
        print(f'my  name is {self._name}, and I am {self._age} years old')
    
player1 = Playercharacter('aman',22)

player1.name ='!!!'
player1.speak = 'BOOOOO'
print(player1.speak)