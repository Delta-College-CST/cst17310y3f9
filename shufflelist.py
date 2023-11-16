# Demonstrate function that shuffles list elements

# The function shuffles elements of an array.  Make 100
# passes through the list and shuffle random elements.
def shuffle(list):
    import random
    listsize = len(list)
    for n in range(100):

        # Get 2 random list indexes
        fromIndex = random.randrange(0,listsize)
        toIndex   = random.randrange(0,listsize)

        # Swap list elements
        temp = list[fromIndex]
        list[fromIndex] = list[toIndex]
        list[toIndex] = temp
        
    return list

# - - - - - - - - -  MAIN ROUTINE  - - - - - - - - - #

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

print("Initially:")
print(fruit)
print()

# Shuffle the list 5 times
for n in range(5):
    fruit = shuffle(fruit)
    print(fruit)
