# Demonstrate "bubbling" largest element to end of list

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

print(fruit)

end = len(fruit)-1
for i in range (end):
    if fruit[i] > fruit[i+1]:
        temp = fruit[i]
        fruit[i] = fruit[i+1]
        fruit[i+1] = temp

print(fruit)
