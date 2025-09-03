# assighnment5

Task1:

student_scores ={"John": 90, "Lucy": 40}
name = input("Enter the student's name: ")

if name in student_scores:
      print( name + " 's marks: " + str(student_scores[name]) )
else:
    print("Student not found.")
input("Press enter to exit")#Just for downloading

Over here their is a dictionary :
"John": 90, "Lucy": 40
and a variable called name that stores the name of the student given by the user.
If the name of the student is found in the dictionary it prints its name and score
Else it prints Student not found.


Task 2:

def process_list():

  original_list = list(range(1, 11))

  extracted_list = original_list[:5]

  reversed_list = extracted_list[::-1]

  print("Original list:",original_list)
  print("Extracted list:", extracted_list)
  print("Reversed list:", reversed_list)

process_list()
input("Press enter to exit")#Just for downloading                                                

Over here process list is a container that stores all the 3 lists

 original_list = list(range(1, 11))
creates the list that will be extracted and reversed
  extracted_list = original_list[:5]
  extracts the first five values from the original list
 reversed_list = extracted_list[::-1]
 reverses the list

