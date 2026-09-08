Student Data Management System
Overview
The Student Data Management System is a Python-based application designed to efficiently store, filter, and process student records. This project demonstrates the power of Python's built-in data structures and memory-efficient processing techniques. It utilizes lists, tuples, sets, list comprehensions, set comprehensions, and generator expressions to handle data dynamically.

Features
Structured Storage: Manages student records using immutable tuples within lists.

Dynamic Filtering: Uses list comprehensions to quickly find students by their major.

Memory-Efficient Processing: Employs generator expressions to evaluate and process large datasets lazily.

Unique Attribute Tracking: Leverages set comprehensions to instantly isolate unique data, such as a list of all distinct majors.

Clean Formatting: Provides modular functions to format and display student data in a readable, standardized layout.

Setup & Installation
Ensure you have Python installed on your machine (python --version).

Clone the repository:

Bash
git clone [<repo-url>](https://github.com/mattnmcintosh/course-7-module-1-python-data-structures-lab)
cd course-7-module-1-python-data-structures-lab
Install dependencies:

Bash
pipenv install
Enter the virtual environment:

Bash
pipenv shell
Run the test suite:

Bash
pytest -x
Project Structure
The application is modular, with data operations separated into specific files:

student_data.py: Contains the primary data structure (a list of tuples representing student IDs, Names, and Majors).

filter.py: Contains filter_students_by_major(), which uses list comprehensions to return a filtered list of students based on a target major.

data_processing.py: Handles UI and string formatting. Contains format_student_data() for string generation and display_students() to print the formatted data to the console.

set_operations.py: Contains unique_majors(), utilizing set comprehensions to extract a mathematically unique set of majors from the student dataset.

data_generator.py: Contains student_generator(), a generator expression designed for memory-efficient, lazy evaluation of student records by major.

Usage Examples
Filtering Students by Major (filter.py)

Python
from filter import filter_students_by_major

students = [(101, "Alice", "Computer Science"), (102, "Bob", "Mathematics")]
cs_students = filter_students_by_major(students, "Computer Science")
# Output: [(101, 'Alice', 'Computer Science')]
Getting Unique Majors (set_operations.py)

Python
from set_operations import unique_majors

majors = unique_majors(students)
# Output: {"Computer Science", "Mathematics"}
Formatting and Displaying Data (data_processing.py)

Python
from data_processing import format_student_data

print(format_student_data((101, "Alice", "Computer Science")))
# Output: "ID: 101 | Name: Alice | Major: Computer Science"
Using the Lazy Generator (data_generator.py)

Python
from data_generator import student_generator

# Creates a generator object instead of building a full list in memory
cs_gen = student_generator(students, "Computer Science")

for student in cs_gen:
    print(student)