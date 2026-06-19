Student_Count=int(input("Enter Number of Student Details you want to store : "))
Students=[]
for i in range(0,Student_Count):
    print(f"Student {i+1} Details")
    student={}
    student["name"]=input("Enter Student name :")
    student["cgpa"]=float(input("Enter your Cgpa :"))
    student["role"]=input("Enter what is your role specification:")
    student["student_id"]=tuple(input(f"Enter Student {i+1} ID/Roll_Number:"))
    project=[]
    project.append(input("Project 1: "))
    project.append(input("Project 2: "))
    student["projects"]=project
    Skills=set(input("Enter Your are pro:").split())
    student["Skills"]=Skills
    Students.append(student)
print("=========Student Details========")
for stu in Students:
    print("Student RollNumber:","".join(student["student_id"]))
    print("Student Name:",student["name"])
    print("CGPA:",student["cgpa"])
    print("Searching_Role:",student["role"])
    print("Projects Done:",student["projects"])
    print("Had Skills :",student["Skills"])
print("====Eligiblity For Placement=====")
for student in Students:
    if (student["cgpa"] >= 7 and "Python" in student["Skills"]):
        print("".join(student["student_id"]),student["name"],"Eligible")
    else:
        print("".join(student["student_id"]),student["name"],"Not Eligible not having required skill")

# Challenge 1: Count total students
print("Total number Students: ",len(Students))
# Challenge 2: Find topper
topper = Students[0]
for student in Students:
    if student["cgpa"] > topper["cgpa"]:
        topper = student
print("Topper:",topper["name"],"- CGPA:",topper["cgpa"])

# Challenge 3: Display all unique skills
all_skills = set()
for student in Students:
    all_skills.update(student["Skills"])
print("All Unique Skills:",all_skills)
# CHALLENGE 4 : Search Student
search_name = input("\nEnter Student Name To Search: ")
found = False
for student in Students:
    if ( student["name"].lower()== search_name.lower()):
        print("\nStudent Found")
        print("ID:","".join(student["student_id"]))
        print("CGPA:",student["cgpa"])
        print("Role:",student["role"])
        found = True
        break

if not found:
    print("Student Not Found")

# CHALLENGE 5 :JSON-like Structure
print("\nJSON Like Structure")
for student in Students:
    print({"name": student["name"],
        "cgpa": student["cgpa"],
        "role": student["role"],
        "student_id": "".join(student["student_id"]),
        "projects": student["projects"],
        "skills": list(student["Skills"])
    })
