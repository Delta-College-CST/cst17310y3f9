# Demonstrate swapping two list elements

fruit = ["orange",  "mango", "watermelon","kiwi", "pineapple", "banana"]

print(fruit)

temp = fruit[2]
fruit[2] = fruit[3]
fruit[3] = temp

print(fruit)
