# The Data (The "Dependency Graph"):Each tuple (A, B) means Service A depends on Service B. 
# (B must start before A).Pythondependencies = [
#     ("AuthService", "Database"),
#     ("Gateway", "AuthService"),
#     ("Billing", "Database"),
#     ("Gateway", "Billing"),
#     ("Database", "FileStorage")
# ]
# 🎯 The MissionWrite a function find_start_order(dependencies) that returns a list of service names in a
#  valid starting order.Requirements:The Order: If Service A depends on Service B, B must appear in the 
# list before A.Completeness: Every service mentioned in the graph must appear in your final list exactly once.
# Cycle Detection: Financial systems hate loops. If there is a circular dependency
#  (e.g., A depends on B, and B depends on A), return an empty list [].
# ⚠️ Staff-Level ExpectationsEfficiency:
#  Aim for $O(V + E)$ where $V$ is the number of services and $E$ is the number of dependency links.
# Data Structures: You will likely need an Adjacency List and an In-degree Map 
# (counting how many things each service is waiting for).
# Composure: Don't get lost in the pointers. Build the graph first, then solve the order.
# Expected Output
#  for the data above:
# ['FileStorage', 'Database', 'AuthService', 'Billing', 'Gateway'] (or similar valid order).