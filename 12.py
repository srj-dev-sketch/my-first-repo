student_Name =[]
student_Enrolment_Number=[]
subject_Name =[]
subject_Marks=[]
total_Marks=[]
percentage=[]
grade=[]
total_marks=0

number_Of_student =int(input("enter the number of student : ")) #to find the number of student to iterate loop
for i in range(0,number_Of_student):
        total_marks=0
        student_name=input("enter the name of student :") #temp variable to enter the student Name 
        student_Name.append(student_name)

        student_enrolment_number=input("enter the student enrolment number :")#temp variable 
        student_Enrolment_Number.append(student_enrolment_number)

        for j in range(0,5): #to enter the name of subject and their marks 
                subject_name = input("enter the name of subject :")#temp variable
                subject_Name.append(subject_name)

                subject_marks=float(input(f"enter the marks for {subject_name} :"))
                subject_Marks.append(subject_marks)
            
        for k in range(5*i,5*i+5): #to calculate student total marks
                total_marks += subject_Marks[k]
        
        total_Marks.append(total_marks) #to insert total marks into list
        percentage.append(total_marks*100/500) #to find and add the percentage into the list 

        if percentage[i] >89 and percentage[i] <101:
                grade.append("A+")
        elif percentage[i] >79 and percentage[i] <90:
                grade.append("A")
        elif percentage[i] >69 and percentage[i] <80:
                grade.append("B+")
        elif percentage[i] >59 and percentage[i] <70:
                grade.append("B")
        elif percentage[i] >49 and percentage[i] <60:
                grade.append("C+")
        elif percentage[i] >39 and percentage[i] <50:
                grade.append("C")
        else:
                grade.append("fail")
            
for i in range(0,number_Of_student): # to print the result 
        
        print("-----------------------------------------")
        print(f"Name \t\t: {student_Name[i]}")
        print(f"enrolment number \t\t:{student_Enrolment_Number[i]}")
        print("------------------------------------------")

        print("subject \t\t marks")
        for j in range(5*i,5*i+5): #to print the individual marks and subject name
                print(f"{subject_Name[j]} \t\t {subject_Marks[j]}")
        
        print("-------------------------------------------")
        print(f"total marks \t\t {total_Marks[i]}")
        print(f"percentage \t\t {percentage[i]}")
        print("--------------------------------------------")
        print(f"grade \t\t {grade[i]}")

