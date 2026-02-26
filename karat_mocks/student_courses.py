
# You are a developer for a university. Your system has a log of students and the courses they are currently enrolled in.

# The Goal:
# Given an unordered list of [student_ID, course_name] pairs, write a function that outputs all possible pairs of students and the courses they share.

# Assumptions & Rules:

# Every student ID should be paired with every other student ID exactly once.

# If two students do not share any courses, they should still appear in the output with an empty list.

# The order of the output or the order of the pairs does not matter.

# Example Input:

# Python
# student_course_pairs = [
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["58", "Mechanics"],
#   ["58", "Art History"],
#   ["17", "Software Design"],
#   ["58", "Operating Systems"],
#   ["17", "Linear Algebra"],
#   ["17", "Art History"]
# ]
# Expected Output:

# Python
# {
#   ("58", "94"): ["Art History", "Operating Systems"],
#   ("58", "17"): ["Linear Algebra", "Art History"],
#   ("94", "17"): ["Art History"]
# }
# Explanation: * Student 58 is taking: Linear Algebra, Mechanics, Art History, Operating Systems.

# Student 94 is taking: Art History, Operating Systems.

# The intersection of their courses is Art History and Operating Systems.

student_course_pairs = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["58", "Mechanics"],
  ["58", "Art History"],
  ["17", "Software Design"],
  ["58", "Operating Systems"],
  ["17", "Linear Algebra"],
  ["17", "Art History"]
]
from typing import List
from collections import defaultdict
from itertools import combinations  


def get_student_pairs_with_same_courses(student_course_pairs:List) -> dict: 
    student_group_dict=defaultdict(set)
    for student,course in student_course_pairs: 
        student_group_dict[student].add(course)
    
    all_students: List = list(student_group_dict.keys())
    student_course_group_dict= {}

    for s in  list(combinations(all_students,2)):
        same_subjects = student_group_dict[s[0]].intersection(student_group_dict[s[1]])
        student_course_group_dict[s] = list(same_subjects)
    return student_course_group_dict


print(get_student_pairs_with_same_courses(student_course_pairs=student_course_pairs))