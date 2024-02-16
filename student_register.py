# I found its better to gather all student IDs before opening a file.
# I have wrapped the code within a Try, except block (supporting error catching)

try:
    student_ids = []
    num_students = int(input("How many students are you registering?: "))

    for _ in range(num_students):
        student_id = input(f"Please enter the student's ID: ")
        student_ids.append(student_id)
    
    with open("reg_form.txt", "w") as f:
        f.write("-- Student Register --\n")
        for student_id in student_ids:
            f.write(f"Student ID: {student_id}\n")
            f.write("___________________\n")
            
    print("Program Complete")

except ValueError:
    print("Please enter a valid number of students.")
except IOError as e:
    print(f"The error: {e}")
