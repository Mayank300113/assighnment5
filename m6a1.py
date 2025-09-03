
student_scores ={"John": 90, "Lucy": 40}
name = input("Enter the student's name: ")

if name in student_scores:
      print( name + " 's marks: " + str(student_scores[name]) )
else:
    print("Student not found.")
input("Press enter to exit")#Just for downloading