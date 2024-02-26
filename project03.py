A = 4
B = 3
C = 2
D = 1
F = 0
grades = ['F', 'D', 'C', 'B', 'A']
student_records = [['Alejandra Dani', [B, D, B, B, A]],
                   ['Nayeli Cora', [C, D, A, D, B]],
                   ['Hazel Kaia', [A, A, C, B, A]],
                   ['Emma Jude', [B, A, B, A, B]]]
print(f"Emma's record: {student_records[0]}")
print(f"Emma's grades: {student_records[0][1]}")
student_records[0][1][0] = B
print(f"Emma's grades: {student_records[0][1]}")
student_grades = []
for grade_report in student_records:
    # print(grade_report)
    for grade in grade_report[1]:
        student_grades.append(grade)
print(student_grades)
student_grades.sort()
print(student_grades)
for grade_report in student_records:
    index_of_min = min(grade_report[1])
    index_of_max = max(grade_report[1])
    print(f"{grade_report[0]}: min {grades[index_of_min]}, "
          f"max {grades[index_of_max]}")



