# This program identifies a Delta CST course name given a code.

# Declare course info dictionary.  Key is ID; value is name.
cstCourses = {
  "CST173":"Introduction to Programming",
  "CST183":"Principles of Computer Programming I",
  "CST185":"Android Application Development",
  "CST186":"Introduction to Game Programming",
  "CST283":"Principles of Computer Programming II" }

# Prompt user for course ID and write course name
targetCourseID = input("Enter course ID (CSTxxx): ")
print(targetCourseID, "is", cstCourses[targetCourseID])
