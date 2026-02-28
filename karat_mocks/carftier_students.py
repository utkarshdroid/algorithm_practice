# 🧩 The Problem: Craftier Students
# You are given a list of class time slots, where each slot has a start time and an end time 
# [start_time, end_time].

# The Goal: Find the maximum number of classes a student can attend without any scheduling 
# conflicts (meaning no two selected intervals overlap).

# Example Input:

# Python
# classes = [[1, 4], [2, 5], [6, 7], [3, 8]]
# Expected Output: 2 (By selecting [1, 4] and [6, 7])


classes = [[1, 2], [3, 10], [4, 11], [5, 12]]
from typing import List

def get_group_of_classes_for_students(classes : List) -> int: 
    classes.sort(key=lambda x: x[1])
    count = 1
    last_end_time = classes[0][1] 
    for i in range(1, len(classes)):
        if classes[i][0] >= last_end_time: 
            count += 1
            last_end_time = classes[i][1] 
            
    return count


meetings = [[1, 5], [5, 10], [2, 6], [3, 8]]
from heapq import heapify

def count_number_of_advisors(meetings: List)-> int: 
    meetings.sort(key=lambda x:x[0])
    print(meetings)

sol = count_number_of_advisors(meetings=meetings)
# print(sol)