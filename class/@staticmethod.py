class Playercharacter:
    membership = True 
    def __init__(self,name,age):
        if (self.membership):
            self.name = name
            self.age = age
        
    def run(self):
        print('fast')
        return 'done'
    
    @classmethod
    def adding_things(cls,num1,num2):
        return cls('teddy',num1+num2)
    
    @staticmethod
    def adding_things2(num1,num2):
        return num1+num2
    
player1 = Playercharacter('cindy',44)
player2 = Playercharacter( 'tom',21)
player2.attack = 50
# print(player2.membership)
player3 = player1.adding_things2(2,3)
print(player3)
# print(player1.membership)