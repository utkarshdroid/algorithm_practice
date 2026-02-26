
# The Escalation: Badge Records (Part 2)
# We are adding a new security rule. We want to find employees who might be behaving suspiciously.

# The Rule: Find anyone who badges into the room 3 or more times within any 1-hour timeframe.

# The Input:
# You are given a new list of records. This time, it only contains badge entries. 
# Each record is a pair containing the employee's name and the time of their entry.

# The time is represented as an integer in military time (e.g., 830 means 8:30 AM, 1355 means 1:55 PM, 2200 means 10:00 PM).

# The list is not guaranteed to be in chronological order.

# The Goal:
# Return a dictionary/map where the key is the name of the suspicious employee, and 
# the value is a list of the times they badged in during that specific 1-hour window. 
# If a person has multiple 1-hour windows with 3+ entries, returning any one of those windows is acceptable.

# Example Input:

# Python
# badge_times = [
#   ["Paul",     "1355"],
#   ["Jennifer", "1910"],
#   ["John",     "835"],
#   ["Paul",     "1315"],
#   ["Jennifer", "1335"],
#   ["Paul",     "1405"],
#   ["Paul",     "1630"],
#   ["John",     "855"],
#   ["John",     "915"],
#   ["John",     "930"],
#   ["Jennifer", "1315"],
#   ["Jennifer", "1405"],
#   ["Jennifer", "1630"],
# ]
# Expected Output:

# Python
# {
#   "John": ["835", "855", "915", "930"], # All within a 1-hour window (8:30 to 9:30)
#   "Paul": ["1315", "1355", "1405"]      # Within 13:15 to 14:15
# }
# (Notice Jennifer is not included because her times 1315, 1335, and 1405 span 50 minutes, 
# but wait—she also has 1910 and 1630. Her times do NOT cluster into a group of 3 within a single hour).


from typing import List


badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",     "835"],
  ["Paul",     "1315"],
  ["Jennifer", "1335"],
  ["Paul",     "1405"],
  ["Paul",     "1630"],
  ["John",     "855"],
  ["John",     "915"],
  ["John",     "930"],
  ["Jennifer", "1315"],
  ["Jennifer", "1405"],
  ["Jennifer", "1630"],
]


def identify_multiple_entries(user_entries:List) -> dict: 
    user_entries.sort(key= int) 
    i= 0 
    j =i+2
    while(j<len(user_entries)):
        if int(user_entries[j])- int(user_entries[i]) < 100:
            return [user_entries[i:j+1]]
        i = j+1
     
    return []

def capture_multiple_entries_within_an_hour(badge_times:List) -> dict : 
    user_entry_dict = {}
    for user in badge_times:
        if user_entry_dict.get(user[0],[]) == []:
            user_entry_dict[user[0]]  = [user[1]]
        else : 
            user_entry_dict[user[0]].append(user[1])

    out_dict = {}
    for k,v in user_entry_dict.items():
        entries = identify_multiple_entries(v)
        if entries!= []:
            out_dict[k] = entries

    return out_dict

print(capture_multiple_entries_within_an_hour(badge_times=badge_times))

    
