# This program accepts two airport codes for a flight
# and returns the city names in a summaryl

airportData = {}   # Airport info dictionary

# Load dictionary from file
datafile = open("airports.txt", "r")
for inputStrItem in datafile:
    inputLineArr = inputStrItem.split(",")
    
    code = inputLineArr[0]    # Split line into string array
    city = inputLineArr[1]    # 1st element is code; 2nd is city

    city = city.strip()       # Clean up input - remove whitespace

    airportData.update({code: city})  # Add to dictionary
    
datafile.close()

doAgain = "y"

# Continue processing per user's request
while doAgain == "y":

    # Prompt user for airport information
    airportFrom = input("Enter airport code - flying FROM: ")
    airportTo   = input("Enter airport code - flying TO: ")

    # Write output summary
    print()
    print("Flight:")
    print("   FROM:",airportFrom, "(",airportData[airportFrom],")")
    print("     TO:",airportTo  , "(",airportData[airportTo]  ,")")
    print()
    
    # Prompt to do again
    doAgain = input("Search again (y or n)?")
    print()

# End program
print("Thank you.")
