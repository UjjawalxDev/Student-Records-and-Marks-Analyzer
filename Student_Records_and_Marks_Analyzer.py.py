# Student Records and Marks Analyzer
# Module 3 Mini-Project

subjects = ("Python", "Maths", "DBMS")   # tuple, subjects ka order fix rahega
student_ids = []                         # list, jis order mein students add hue
students = {}                            # dict, key = student ID


def get_number(message, low, high):    # number tab tak maango jab tak sahi range mein na aaye
    
    while True:
        try:
            value = float(input(message))
            if low <= value <= high:
                return value
            print("Number", low, "se", high, "ke beech mein hona chahiye.")
        except ValueError:
            print("Please enter a valid number.")


def get_result(marks):
    total = sum(marks)
    avg = total / len(marks)

    if avg >= 75:
        result = "Distinction"
    elif avg >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, avg, result


def add_students():
    count = int(get_number("How many students? ", 1, 1000))

    for i in range(count):
        print("\nStudent", i + 1)

        # unique ID lena hai
        while True:
            sid = input("Student ID: ").strip()
            if sid == "":
                print("ID cannot be empty.")
            elif sid in students:
                print("This ID already exists, try another one.")
            else:
                break

        name = input("Name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Name: ").strip()

        marks = []
        for sub in subjects:
            marks.append(get_number(sub + " marks: ", 0, 100))

        students[sid] = {"name": name, "marks": marks}
        student_ids.append(sid)
        print("Student added.")


def show_student(sid):
    record = students[sid]
    total, avg, result = get_result(record["marks"])

    print(sid, "|", record["name"])
    for i in range(len(subjects)):
        print("  " + subjects[i] + ":", record["marks"][i])
    print("  Total:", total, "| Average:", format(avg, ".2f"), "| Result:", result)


def display_records():
    print("\n----- STUDENT REPORT -----")
    if len(students) == 0:
        print("No students recorded.")
        return

    for sid in student_ids:
        show_student(sid)
        print()


def search_student():
    sid = input("Enter student ID to search: ").strip()

    if sid not in students:
        print("Student ID not found.")
        return

    print("\nStudent found")
    show_student(sid)

    # slicing example

    if len(student_ids) >= 2:
        print("First two student IDs:", student_ids[:2])
    print("First subject mark (index 0):", students[sid]["marks"][0])


def update_marks():
    sid = input("Enter student ID to update: ").strip()

    if sid not in students:
        print("Student ID not found.")
        return

    print("Subjects:")
    for i in range(len(subjects)):
        print(i, ".", subjects[i])

    pos = int(get_number("Enter subject position: ", 0, len(subjects) - 1))
    new_mark = get_number("Enter new marks (0-100): ", 0, 100)

    # list mutable hoti hai, isliye seedha change kar sakte hain

    students[sid]["marks"][pos] = new_mark
    print("Marks updated.")


def passed_subjects(sid):
    passed = set()
    marks = students[sid]["marks"]

    for i in range(len(subjects)):
        if marks[i] >= 40:
            passed.add(subjects[i])

    return passed


def set_analysis():
    if len(students) == 0:
        print("No students recorded.")
        return

    all_passed = set()
    for sid in student_ids:
        all_passed.update(passed_subjects(sid))

    print("\nSubjects passed by at least one student:")
    print(sorted(all_passed))

    if len(student_ids) < 2:
        print("At least two students are needed for comparison.")
        return

    print("Available student IDs:", student_ids)
    id1 = input("Enter first student ID: ").strip()
    id2 = input("Enter second student ID: ").strip()

    if id1 not in students or id2 not in students:
        print("One or both IDs are invalid.")
        return

    set1 = passed_subjects(id1)
    set2 = passed_subjects(id2)

    print("Passed by", id1 + ":", sorted(set1))
    print("Passed by", id2 + ":", sorted(set2))
    print("Union:", sorted(set1 | set2))
    print("Intersection:", sorted(set1 & set2))
    print("Difference (first - second):", sorted(set1 - set2))
    print("Symmetric difference:", sorted(set1 ^ set2))


def class_summary():
    print("\n----- CLASS SUMMARY -----")

    if len(students) == 0:
        print("Number of students: 0")
        return

    averages = []
    for sid in student_ids:
        total, avg, result = get_result(students[sid]["marks"])
        averages.append(avg)

    print("Number of students:", len(student_ids))
    print("Class average:", format(sum(averages) / len(averages), ".2f"))
    print("Highest average:", format(max(averages), ".2f"))
    print("Lowest average:", format(min(averages), ".2f"))
    print("Unique subjects:", sorted(set(subjects)))


# ---------- main program ----------

print("Subjects:", subjects)
add_students()
display_records()
class_summary()

while True:
    print("\nMENU")
    print("1. Display all records")
    print("2. Search student")
    print("3. Update marks")
    print("4. Set analysis")
    print("5. Class summary")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        display_records()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        set_analysis()
    elif choice == "5":
        class_summary()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please choose 1 to 6.")



