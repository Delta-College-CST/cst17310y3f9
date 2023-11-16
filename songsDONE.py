# This program reads a file of songs and writes the contents
# in various orders.

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

songList = []

# Load list from file.  String newline from input line.
datafile = open("mysongs.txt", "r")
for aSong in datafile:
    aSong = aSong.strip()
    songList.append(aSong)
    
# Sort ascending and write
songList.sort()
print(songList)

print("\n\n")  # Space

# Sort descending and write
songList.sort(reverse=True)
print(songList)

print("\n\n")  # Space

# Shuffle list and write
songList = shuffle(songList)
print(songList)
