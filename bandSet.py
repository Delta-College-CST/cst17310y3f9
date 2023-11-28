# Process candidates to form a band

# List candidates for a band members and their abilities
candidate1 = {"guitar", "sax", "vocals"}
candidate2 = {"vocals", "keyboard", "drums"}
candidate3 = {"drums","bass","keyboard","vocals"}
candidate4 = {"bass","vocals","guitar"}

# Find skills common to all (Set intersection)
commonSkills = candidate1 & candidate2 & candidate3 & candidate4
print(commonSkills)

# Determine total set of abilities (Set union)
allSkills = candidate1 | candidate2 | candidate3 | candidate4
print(allSkills)
