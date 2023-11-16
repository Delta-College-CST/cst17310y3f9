# This program performs a variety of dictionay operations on student
# quiz data.  Quiz scores 0..10.  
# For the dictionaries:  key = student number; value = quiz score.

# Initial set of quiz scores
quizzes = {1:9, 5:8, 3:9, 6:10 }

quizzes.update({4:7})    # Add student 4 with a grade of 7

quizzes.update({5:9})    # Update student 5 score to a 9

del quizzes[3]           # Delete quiz entry for student 3

quizzes.update({2:10})   # Add student 2 with a grade of 10

# Iterate through dictionary; access key and write value
for student in quizzes:
    print("Student:",student,"  Score:",quizzes[student])


