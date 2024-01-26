student_grades = {}
student_scores = {
    "aman":97,
    "anil":81,
    "jai":100,
    "sai":39,
    "sri":95,
    "rajiv":76,
    "sujatha":65,
    "srikanth":58,
}

for key in student_scores:
    if student_scores[key] == 100:
        student_grades[key] = "Amazing outstanding performance"
    elif student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    elif student_scores[key] >60:
        student_grades[key] = "can do better"
    elif student_scores[key] > 50:
        student_grades[key] = "Pass"
    else:
        student_grades[key] = "Fail"

print(student_grades)