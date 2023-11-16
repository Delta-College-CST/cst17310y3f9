# This program identifies a season from a code.

# Declare season dictionary
seasons = { "SP":"Spring","SU":"Summer","FA":"Fall","WI":"Winter" }

# Prompt user for season code and write corresponding name
thisSeason = input("Enter season: ")
print("It is", seasons[thisSeason])
