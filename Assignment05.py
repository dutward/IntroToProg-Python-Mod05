# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JeffHoward,11/10/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json
import io as _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {} # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)

except FileNotFoundError as e: #custom error message if file name/path not found
    print("File does not exist in this location\n")
    print("Please try again\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e: #generic message for other types of errors
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:
    print(MENU) # Present the menu of choices
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  #register a student for class - gather first, last and class name
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): #check for non-alphabet entry in first name
                raise ValueError("Error - The last name should not contain numbers.\n")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): #check for non-alphabet entry in last name
                raise ValueError("Error - The last name should not contain numbers.\n")

            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name,
                        'last_name': student_last_name,
                        'course_name': course_name}
            students.append(student_data)

            print(f"You have registered {student_data['first_name']} {student_data['last_name']} "
                  f"for {student_data['course_name']}.")

        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        continue

    # Present the current data
    elif menu_choice == "2":

        # Print all users registered for the class including those recently added
        print("-" * 50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("Your data has been saved successfully.")
            continue

        except TypeError as e: #catch errors where data is not in JSON format
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        except Exception as e: #generic message for other types of errors
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        finally:
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4") #in case user enters anything other than numbers 1-4

print("Program Ended")
