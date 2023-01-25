"""HackerRank solution for grading students problem"""


def gradingStudents(grades: list) -> list:
    """To grade students.

    Args:
        grades (list): List of marks of students.

    Returns:
        list: Converted to marks.

    """
    out_grades = []
    for grade in grades:
        skip = False
        if grade < 38:
            out_grades.append(grade)
            continue
        for i in range(3):
            if (grade + i) % 5 == 0:
                out_grades.append(grade + i)
                skip = True
                break
        if not skip:
            out_grades.append(grade)
    return out_grades


print(gradingStudents([73, 67, 38, 33]))
