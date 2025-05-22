class Playercharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        return self
    
    def speak(self):
        print(f'my  name is {self.name}, and I am {self.age} years old')
    
player1 = Playercharacter('aman',22)

player1.name ='!!!'
player1.speak = 'BOOOOO'
print(player1.speak)