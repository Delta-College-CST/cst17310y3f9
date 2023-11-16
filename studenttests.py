# This program performs a variey of dictionary operations.
# For the dictionaries:  key = student ID; value = test score.

tests = {101:86, 103:77, 111:96, 109:82 }

# Iterate through dictionary and access all keys
for student in tests:
    print(student)

# Update an existing dictionary element - using update()
tests.update({103:79})

# Add new element to dictionary - using update() and index
tests.update({103:85})
tests[101] = 89

# Add new dictionary elements from a dictionary
makeups = {105:92, 108:87, 113:81}
tests.update(makeups)

# Update existing dictionary elements from a dictionary
corrections = {108:88, 111:98}
tests.update(corrections)

# Remove a dictionary element using key
del tests[105]

# Iterate through dictionary; access key and write value
for studentID in tests:
    print("Key:",studentID,"  Value:",tests[studentID])

# Returns a list containing the dictionary's keys
keylist = tests.keys()
print(keylist)

#Returns a list of all the values in the dictionary
valuelist = tests.values()
print(valuelist)



