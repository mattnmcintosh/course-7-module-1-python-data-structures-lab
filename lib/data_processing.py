# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    id, name, major = student
    return f"ID: {id} | Name: {name} | Major: {major}"
    pass

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))
    pass

def create_student_id_map(student_list):
    """
    Return a dictionary mapping student IDs to their name and major 
    using a dictionary comprehension.
    """
    return {student_id: {"name": name, "major": major} for student_id, name, major in student_list}


def group_students_by_major(student_list):
    """
    Return a dictionary grouping student names by their respective major 
    using a dictionary comprehension.
    """
    unique_majors = {major for _, _, major in student_list}
    return {
        major: [name for _, name, m in student_list if m == major] 
        for major in unique_majors
    }