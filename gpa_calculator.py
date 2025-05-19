"Computes a student's GPA for 6 courses."

grade_points_dict = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "F": 0
}

Credit_Units = []
Grades = []

Grade_Points = []
Weighted_Grades = []

for i in range(6):
    grade = input(f"Input the grade of the {i+1}th course(A, B, C, D or F): ").upper()
    
    while grade.upper() not in grade_points_dict:
        print("Invalid grade. Please try again.")
        grade = input(f"Input the grade of the {i+1}th course(A, B, C, D or F): ").upper()

    credit_unit = input("Input the credit unit for the course: ")

    while credit_unit.isalpha() or int(credit_unit) < 0:
        print("Invalid grade. Please try again.")
        credit_unit = input("Input the credit unit for the course: ")

    Grades.append(grade)
    Credit_Units.append(int(credit_unit))

    print("\n")


for i in range(6):
    grade_point = grade_points_dict[Grades[i]]
    weighted_point = grade_point * Credit_Units[i]

    Grade_Points.append(grade_point)
    Weighted_Grades.append(weighted_point)


GPA = sum(Weighted_Grades)/sum(Credit_Units)
print(f"Your GPA is: {round(GPA, 2)}")
