Cgpa=float(input("Enter your Cgpa"))
Back_log=int(input("Enter No.of back_log"))
Required_skills={"Python","Git","Sql"}
skills=set(input("Enter your Skills"))
if cgpa>=8.0:
    print("You have Eligible cgpa")
    if Back_log == 0:
        print("You are not having any back_log")
        if Required_skills.issubset(skills):
            print("You have all the skills")
            print("Your are Eligible for the placement")
        else:
            missed=Required_skills-skills
            print(f"You are having good cgpa and no backlog but you are not having required skill{missed}")
    else:
        print("You are having good cgpa but having backlog ")
else:
    print("Not having Cgpa So not eligible for Placement")
