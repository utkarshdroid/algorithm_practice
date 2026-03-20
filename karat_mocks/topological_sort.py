# tasks = ["Fetch_Data", "Validate", "Audit", "Report"]

# dependencies = [("Fetch_Data", "Validate"), ("Validate", "Audit"), ("Audit", "Report")]

# The Scenario: You have 4 tasks to complete for a financial audit.
#  Some tasks depend on others.
#  Find one valid order to complete all tasks.

# Input:

# tasks = ["Fetch_Data", "Validate", "Audit", "Report"]

# dependencies = [("Fetch_Data", "Validate"), ("Validate", "Audit"), ("Audit", "Report")]

# The Goal:
# Return a list of tasks in a valid order.

# Expected Output:
# ["Fetch_Data", "Validate", "Audit", "Report"]

tasks = ["Fetch_Data", "Validate", "Audit", "Report"]

dependencies = [("Fetch_Data", "Validate"), ("Validate", "Audit"), ("Audit", "Report")]

from typing import List 
from collections import deque

def get_topological_sort(tasks, dependencies):
  
    adj = {task: [] for task in tasks}
    for parent, child in dependencies:
        adj[parent].append(child)

    # 2. State tracking: 0=Unvisited, 1=Visiting (Current Path), 2=Visited (Finished)
    state = {task: 0 for task in tasks}
    stack = []

    def dfs(node):
        state[node] = 1  # Mark as "Visiting"
        
        for neighbor in adj[node]:
            if state[neighbor] == 1:
                return True  # CYCLE DETECTED!
            if state[neighbor] == 0:
                if dfs(neighbor):
                    return True
        
        state[node] = 2  # Mark as "Finished"
        stack.append(node)
        return False

    # 3. Main loop: Use the original 'tasks' list to ensure all nodes are covered
    for task in tasks:
        if state[task] == 0:
            if dfs(task):
                print("Error: Cycle detected, topological sort impossible.")
                return []

    # Stack is currently [Leaf -> Root], so we return the reverse
    return stack[::-1]

# Test Case
tasks = ["Fetch_Data", "Validate", "Audit", "Report", "Isolated_Task"]
dependencies = [("Fetch_Data", "Validate"), ("Validate", "Audit"), ("Audit", "Report")]
print(get_topological_sort(tasks, dependencies))