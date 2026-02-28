# The Scenario: You are given a stream of raw transaction data.
# Each entry is a tuple: (user_id, amount, category, is_valid).
# The Tasks (Combined):Grouping & Summing: Calculate the total amount spent per user.
# Filtering: Ignore any transaction where is_valid is False.
# Cross-Category Mapping: For each user, also keep a unique list of all categories they spent in.
# Anomaly Detection: Add a flag is_whale for any user whose average transaction is greater than $500.
# Efficiency: You must do all of this in one single pass ($O(N)$).The Expanded Input:Pythonraw_data = [
#     ("user_1", 50, "Food", True),
#     ("user_2", 1000, "Tech", True),
#     ("user_1", 25, "Food", True),
#     ("user_3", 10, "Tax", True),
#     ("user_2", 200, "Travel", False), # INVALID - Ignore
#     ("user_1", 600, "Tech", True),
#     ("user_4", 1500, "Audit", True),
#     ("user_3", None, "Tax", True),    # NONE - Handle gracefully
#     ("user_4", 50, "Food", True)
# ]
# 🎯 The MissionWrite a function analyze_transactions(data) that returns a dictionary of dictionaries.
# Expected Output Structure:Python{
#     "user_1": {
#         "total": 675,
#         "categories": {"Food", "Tech"},
#         "is_whale": False  # Avg is 675/3 = 225
#     },
#     "user_4": {
#         "total": 1550,
#         "categories": {"Audit", "Food"},
#         "is_whale": True   # Avg is 1550/2 = 775
#     },
#     ...
# }

raw_data = [
    ("user_1", 50, "Food", True),
    ("user_2", 1000, "Tech", True),
    ("user_1", 25, "Food", True),
    ("user_3", 10, "Tax", True),
    ("user_2", 200, "Travel", False),  # INVALID - Ignore
    ("user_1", 600, "Tech", True),
    ("user_4", 1500, "Audit", True),
    ("user_3", None, "Tax", True),  # NONE - Handle gracefully
    ("user_4", 50, "Food", True),
]
from typing import List

def transform_data_into_json(raw_data:List)-> List:
    user_dict ={}
    for item in raw_data:
        if item[1] is not None and item[-1] is True:
            k = item[0].split("_")[1]
            val = user_dict.get(k, None)
            if val is None:
                user_dict[k]={
                    "user": int(item[0].split("_")[1]),
                    "total":  int(item[1]),
                    "categories":[item[2]],
                }
            else :
                user_dict[k]["total"] = val['total']+int(item[1])
                user_dict[k]["categories"].append(item[2])
    for k,v in user_dict.items():
        user_dict[k]["is_whale"] = v["total"]/len(v["categories"]) > 500
    return user_dict
                  
               
        

print(transform_data_into_json(raw_data))
