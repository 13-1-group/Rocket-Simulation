from orbit import Orbit, Factory

# orbit 1
obj1 = Orbit('Elliptical')
factory1 = Factory() 
print(factory1.build(obj1))
print('---')


# orbit 2
obj2 = Orbit('Parabolic')
factory2 = Factory() 
print(factory2.build(obj2))
print(factory2.build(obj2))
print('---')
