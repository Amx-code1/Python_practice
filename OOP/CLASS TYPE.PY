print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

class BigObject:
    pass

Obj1 = BigObject()

print(type(BigObject))
print(type(Obj1))