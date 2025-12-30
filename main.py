import csv
import pandas
program_is_on=True
go=""
pass_marks=0
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
        choice=(input("Choose your option:\n1. Add New Student\n2. View Grades\n3. Grade of Selected Student\n4. Remove Student\n5. Calculate average grade\n6. Check for pass or fail\n7.Exit\n--> "))
        if choice=='1':
            student_name=input("Enter name of student: ")
            student_name=student_name.strip().upper()

            try:
               eng=int(input("Enter the marks of English: "))
               maths=int(input("Enter the marks of Mathematics: "))
               science=int(input("Enter the marks of Science: "))
            except ValueError:
               print("Please print numeric values only")
               go_on()
               continue
            with open("grades.csv","a",newline="") as file:
              writer = csv.writer(file)
              if file.tell() == 0:
                writer.writerow(["NAME","ENGLISH","MATHEMATICS","SCIENCE"])
              else:
                 pass
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
            grades_data=pandas.read_csv("grades.csv")
            with open("average_grade.csv","w",newline="") as file:
               write=csv.writer(file)
               write.writerow(["NAME","AVERAGE_SCORE"])
               for (index,row) in grades_data.iterrows():
                row_eng=row.ENGLISH
                row_math=row.MATHEMATICS
                row_sci=row.SCIENCE
                total=(row_eng+row_math+row_sci)
                avg=int(total/3)
                write.writerow([row.NAME,avg])
            average_grades=pandas.read_csv("average_grade.csv")
            print(average_grades)
            go_on()
        
        elif choice=="6":
          pass_marks=int(input("Enter the pass marks: "))
          try:
            average_grades=pandas.read_csv("average_grade.csv")
            with open("remarks_grade.csv","w",newline="") as file:
                write=csv.writer(file)
                write.writerow(["NAME","OVERALL GRADE","REMARK"])
                for (index,row) in average_grades.iterrows():
                  if row.AVERAGE_SCORE>=pass_marks:
                     remark="PASSED"
                  else:
                     remark="FAILED"
                  if 100>=row.AVERAGE_SCORE>89:
                     overall="A"
                  elif 89>=row.AVERAGE_SCORE>79:
                     overall='B'
                  elif 79>=row.AVERAGE_SCORE>69:
                     overall='C'
                  elif 69>=row.AVERAGE_SCORE>59:
                     overall="D"
                  elif 59>=row.AVERAGE_SCORE>49:
                     overall="E"
                  else:
                     overall="F"
                  write.writerow([row.NAME,overall,remark])
            remarks=pandas.read_csv("remarks_grade.csv")
            print(remarks)
            go_on()
          except FileNotFoundError:
            print("Please calculate average first at option no. 5")
            go_on()

        elif choice=="7":
            print("Exiting program...")
            program_is_on=False
 
        else:
            print("Invalid input")
    
    except KeyboardInterrupt:
        print("Program Interrupted...")
