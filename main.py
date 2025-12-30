import csv
import pandas
program_is_on=True
go=""
def go_on():
    global go
    global program_is_on
    go=input("Do you want to continue? (Y/N) ")
    go=go.upper()
    if go=="Y":
        program_is_on=True
    elif go=="N":
        program_is_on=False
        print("Exiting program")
    else:
        print("Invalid input")
while program_is_on:
    try:
        choice=(input("Choose your option:\n1. Add New Student\n2. View Grades\n3. Grade of Selected Student\n4. Remove Student\n5.Exit\n--> "))
        if choice=='1':
            student_name=input("Enter name of student: ")
            student_name=student_name.upper()
            eng=int(input("Enter the marks of English: "))
            maths=int(input("Enter the marks of Mathematics: "))
            science=int(input("Enter the marks of Science: "))
            with open("grades.csv","a",newline="") as file:

              writer = csv.writer(file)
              writer.writerow([student_name,eng,maths,science])
              print(f"Student has been added")
            go_on()

        elif choice=='2':
            grades_data=pandas.read_csv("grades.csv")
            if grades_data.empty:
                print("No data found")
            else:
                print(grades_data)
            go_on()

        elif choice=="3":
            grades_data=pandas.read_csv("grades.csv")
            student_name=input("Enter name of student: ")
            student_name=student_name.upper()
            student_row=grades_data[grades_data["NAME"]==student_name]
            if student_row.empty:
                print("Name not found")
            else:
                print(student_row)
            go_on()
    
        elif choice=="4":
            grades_data=pandas.read_csv("grades.csv")
            student_name=input("Enter name of student you want to delete: ")
            student_name=student_name.upper()
            student_row=grades_data[grades_data["NAME"] == student_name]
            if student_row.empty:
               print("Invalid name, not found in system")
            else:
               grades = grades_data[grades_data["NAME"] != student_name]
               grades.to_csv("grades.csv", index=False)
               print(f"{student_name} has been deleted.")
            go_on()

        elif choice=="5":
            program_is_on=False
        

        else:
            print("Invalid input")
    
    except KeyboardInterrupt:
        print("Program Interrupted...")