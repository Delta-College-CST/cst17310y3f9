# Demonstrate basic Python sets

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A)
print(B)

A.add(9)
B.discard(4)
print(A)
print(B)

print('Union:', A.union(B)) 
print('Intersection:', A.intersection(B)) 

setX = {11, 22, 33, 44, 11}
print(setX)
