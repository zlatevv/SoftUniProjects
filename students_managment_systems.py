students = {}
def add_students(name, age, grades, subjects):
    subjects_list = subjects.split()
    grades_list = [float(grade) for grade in grades.split()]
    sum_grades = sum(grades_list)
    average_grade = int(sum_grades) / len(grades_list)
    students[name] = int(age), average_grade, subjects_list
    student_info = f"Name: {name}, Age: {int(age)}, Average Grade: {average_grade:.2f}, Subjects: {', '.join(subjects_list)}"
    
    return student_info
def update_students(name):
    if name in students:
        current_age, current_average_grade, current_subjects = students[name]
        boolen1 = input("Do you want to change the age? (y/n) ")
        if boolen1.lower() == "y":
        
            new_age = int(input("Enter the new age:"))
            print(f"Age has been changed to {new_age}")
        else:
            new_age = current_age
        boolen2 = input("Do you want to change the grades? (y/n) ")

        if boolen2.lower() == "y":
            new_grades = input("Enter the new grades: ").split()
            new_grades_list = [float(grade) for grade in new_grades]
            new_average_grade = sum(new_grades_list) / len(new_grades_list)
            print(f"Average grade has been changed to {new_average_grade:.2f}")
        else:
            new_average_grade = current_average_grade
        boolen3 = input("Do you want to change the subjects? (y/n) ")
        if boolen3.lower() == "y":
            new_subjects = input("Enter the subjects:").split()
            print(f"Subjects have been changed to {', '.join(new_subjects)}")
            
        else:
            new_subjects = current_subjects
        students[name] = (new_age, new_average_grade, new_subjects)
    else:
        return "No such student."
def delete_students(name):
    if name in students:

        del students[name]
        return f"{name} has been removed!"
    else:
        return "No such student."
def search_student(name):
    if name in students:
        age, average_grade, subjects = students[name]
        formatted_subjects = ", ".join(subjects)
        return f"name: {name}, age: {age}, average grade: {average_grade:.2f}, subjects: {formatted_subjects}"
    else:
        return "No such student."
def all_student_records():
    if not students:
        return "No student records to show for now."
    else:
        records = []
        for name, (age, average_grade, subjects) in students.items():
            formatted_subjects = ", ".join(subjects)
            records.append(f"Name: {name}, age: {age}, average grade: {average_grade:.2f}, subjects: {formatted_subjects}")
        return "\n".join(records)
            

while True:
    print("1. Add a student")
    print("2. Update a student's information")
    print("3. Delete a student")
    print("4. Search for a student")
    print("5. All student records")
    print("6. Exit")
    command = int(input("Which one do you choose:"))
    if command == 1:
        name = input("Enter the student's name:")
        age = int(input(f"Enter {name}'s age:"))
        grades = input(f"Enter {name}'s grades:")
        subjects = input(f"Enter {name}'s subjects:")
        print(add_students(name, age, grades, subjects))
    elif command == 2:
        name = input("Enter the student's name:")
        print(update_students(name))
    elif command == 3:
        name = input("Enter the student's name:")
        print(delete_students(name))
    elif command == 4:
        name = input("Enter the student's name:")
        print(search_student(name))
    elif command == 5:
        print(all_student_records())
    elif command == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    print()