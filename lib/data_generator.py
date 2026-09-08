# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    return ((student_id, name, s_major) for student_id, name, s_major in student_list if major == s_major)
    pass
