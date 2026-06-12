# ============================================
#        STUDENT GRADING SYSTEM
# ============================================

students = {}

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    subjects = {}
    num_subjects = int(input("How many subjects? "))
    
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        score = float(input(f"Enter score for {subject}: "))
        
        # Validate score
        while score < 0 or score > 100:
            print("❌ Score must be between 0 and 100!")
            score = float(input(f"Enter score for {subject}: "))
        
        subjects[subject] = score
    
    students[name] = subjects
    print(f"✅ {name} added successfully!")

def get_grade(score):
    if score >= 80:
        return "A", "Excellent"
    elif score >= 70:
        return "B", "Very Good"
    elif score >= 60:
        return "C", "Good"
    elif score >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"

def view_student():
    print("\n--- View Student Report ---")
    name = input("Enter student name: ")
    
    if name not in students:
        print(f"❌ Student '{name}' not found!")
        return
    
    subjects = students[name]
    total = sum(subjects.values())
    average = total / len(subjects)
    grade, remark = get_grade(average)
    
    print(f"""
╔══════════════════════════════════╗
       REPORT CARD - {name}
╚══════════════════════════════════╝
""")
    print(f"{'Subject':<20} {'Score':<10} {'Grade':<10} {'Remark'}")
    print("-" * 55)
    
    for subject, score in subjects.items():
        s_grade, s_remark = get_grade(score)
        print(f"{subject:<20} {score:<10} {s_grade:<10} {s_remark}")
    
    print("-" * 55)
    print(f"{'Total:':<20} {total:<10}")
    print(f"{'Average:':<20} {average:.2f}")
    print(f"{'Final Grade:':<20} {grade}")
    print(f"{'Remark:':<20} {remark}")
    print("=" * 55)

def view_all_students():
    if not students:
        print("❌ No students found!")
        return
    
    print(f"\n{'Name':<20} {'Average':<10} {'Grade':<10} {'Remark'}")
    print("-" * 50)
    
    for name, subjects in students.items():
        average = sum(subjects.values()) / len(subjects)
        grade, remark = get_grade(average)
        print(f"{name:<20} {average:<10.2f} {grade:<10} {remark}")

def top_student():
    if not students:
        print("❌ No students found!")
        return
    
    top = max(students, key=lambda name: sum(students[name].values()) / len(students[name]))
    average = sum(students[top].values()) / len(students[top])
    grade, remark = get_grade(average)
    
    print(f"""
🏆 TOP STUDENT
==============================
Name:    {top}
Average: {average:.2f}
Grade:   {grade}
Remark:  {remark}
==============================""")

def delete_student():
    print("\n--- Delete Student ---")
    name = input("Enter student name to delete: ")
    
    if name in students:
        del students[name]
        print(f"✅ {name} deleted successfully!")
    else:
        print(f"❌ Student '{name}' not found!")

# ============ MAIN MENU ============
while True:
    print("""
==============================
    STUDENT GRADING SYSTEM
==============================
1. Add Student
2. View Student Report
3. View All Students
4. Top Student
5. Delete Student
6. Exit
==============================""")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        view_all_students()
    elif choice == "4":
        top_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("\n👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1-6.")