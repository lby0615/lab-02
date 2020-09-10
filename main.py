# Author: Boyuan Lai bjl5716@psu.edu
# Collaborator: Miranda Hanson mkh5823@psu.edu
# Collaborator: Aaryan Darshin Bavishi aqb6298@psu.edu
# Section: 6
# Breakout: 11
def getLetterGrade(grade):
  
  if grade >= 93.0:
    return ("Your letter grade for CMPSC 131 is A.")
  elif grade < 93.0 and grade >= 90.0:
    return ("Your letter grade for CMPSC 131 is A-.")
  elif grade < 90.0 and grade >= 87.0:
    return ("Your letter grade for CMPSC 131 is B+.")
  elif grade < 87.0 and grade >= 83.0:
    return ("Your letter grade for CMPSC 131 is B.")
  elif grade < 83.0 and grade >= 80.0:
    return ("Your letter grade for CMPSC 131 is B-.")
  elif grade < 80.0 and grade >= 77.0:
    return ("Your letter grade for CMPSC 131 is C+.")
  elif grade < 77.0 and grade >= 70.0:
    return ("Your letter grade for CMPSC 131 is C.")
  elif grade < 70.0 and grade >= 60.0:
    return ("Your letter grade for CMPSC 131 is D.")
  else:
    return ("Your letter grade for CMPSC 131 is F.")

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print (getLetterGrade(grade))
  
if __name__ == "__main__":
  run()