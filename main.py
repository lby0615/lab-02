# Author: Boyuan Lai bjl5716@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 4
# Breakout: 12Í
def getLetterGrade():
  grade = float(input("Enter your CMPSC 131 grade: "))

  if grade <=100.0 and grade >= 93.0:
    print ("Your letter grade for CMPSC 131 is A+.")
  elif grade < 93.0 and grade >= 90.0:
    print ("Your letter grade for CMPSC 131 is A.")
  elif grade < 90.0 and grade >= 87.0:
    print ("Your letter grade for CMPSC 131 is B+.")
  elif grade < 87.0 and grade >= 83.0:
    print ("Your letter grade for CMPSC 131 is B.")
  elif grade < 83.0 and grade >= 80.0:
    print ("Your letter grade for CMPSC 131 is B-.")
  elif grade < 80.0 and grade >= 77.0:
    print ("Your letter grade for CMPSC 131 is C+.")
  elif grade < 77.0 and grade >= 70.0:
    print ("Your letter grade for CMPSC 131 is C.")
  elif grade < 70.0 and grade >= 60.0:
    print ("Your letter grade for CMPSC 131 is D.")
  else:
    print ("Your letter grade for CMPSC 131 is F.")
  

if __name__ == "__main__":
  getLetterGrade()






