# This program reads scouting data for a robotics event
# and performs various sorts

# Global declarations of lists
teams  = []    # Team number
scores = []    # Event score data

datafile = open("robotScoutData.txt", "r") # Open file for reading

# Build parallel lists from data file
def buildListsFromFile():
    for line in datafile:

        # Read one line of data - one worker
        aTeamStr, aScoreStr = line.split(",")

        # Convert numeric strings to numbers
        aTeam  = int(aTeamStr)
        aScore = float(aScoreStr)

        # Add data to lists in parallel
        teams.append(aTeam)
        scores.append(aScore)

# Bubble Sort - Sort parallel arrays by ascending team name
def sortTeamASC():
    for end in range (len(teams)-1,0,-1):
        for i in range (end):
            if teams[i] > teams[i+1]:

                # Swap both lists synchronously
                tempInt = teams[i]
                teams[i] = teams[i+1]
                teams[i+1] = tempInt
                
                tempFloat = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = tempFloat

# Bubble Sort - Sort parallel arrays by descending score
def sortScoreDESC():
    for end in range (len(scores)-1,0,-1):
        for i in range (end):
            if scores[i] < scores[i+1]:
                
                # Swap both lists synchronously
                tempInt = teams[i]
                teams[i] = teams[i+1]
                teams[i+1] = tempInt
                
                tempFloat = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = tempFloat

# Write data
def writeDataReport():
    print("TEAM    SCORE")          # Reporting heading
    for i in range(len(teams)):
        print ("%4d  %7.2f" %(teams[i], scores[i]))


################### Mainline Routine ###################

buildListsFromFile()

sortTeamASC()
writeDataReport()

print("\n")  # Blank lines

sortScoreDESC()
writeDataReport()
