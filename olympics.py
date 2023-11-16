# This program prompts the user for a three-character country
# code used by the Olympics.  It then returns the associated
# country name

olymCountries = {}   # Country info dictionary

# Load dictionary from file
datafile = open("olympicCountries.txt", "r")
for inputStrItem in datafile:
    inputLineArr = inputStrItem.split(",")
    
    code    = inputLineArr[0]    # Split line into string array
    country = inputLineArr[1]    # 1st element is code; 2nd is country

    country = country.strip()    # Clean up input - remove whitespace

    olymCountries.update({code: country})  # Add to dictionary
    
datafile.close()

doAgain = "y"

# Continue processing per user's request
while doAgain == "y":

    # Prompt user for airport information
    countryCode = input("Enter country code: ")

    # Write output summary
    print()
    print(countryCode, "is",olymCountries[countryCode])
    print()
    
    # Prompt to do again
    doAgain = input("Search again (y or n)?")
    print()

# End program
print("Thank you.  Go USA.")
