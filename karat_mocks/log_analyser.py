# Write a script to process these logs and return a Feature Summary dictionary for each user.

# Requirements:
# Parsing: Extract the user_id and the duration from each string.

# Data Cleaning: * If duration is "null", ignore that specific log entry.

# Convert duration to an integer.

# Aggregation: For each user, calculate:

# total_duration: Sum of all valid durations.

# avg_duration: Average duration (rounded to 2 decimal places).

# activity_count: Number of valid log entries.

# Output Format: A dictionary where keys are user_id and values are the feature dictionaries.

# Example Output Structure:

# Python
# {
#     101: {'total_duration': 1500, 'avg_duration': 750.0, 'activity_count': 2},
#     ...
# }

import json
raw_logs = [
    "user_id:101, action:login, timestamp:2026-02-28 10:00:00, duration:null",
    "user_id:102, action:login, timestamp:2026-02-28 10:05:00, duration:45",
    "user_id:101, action:logout, timestamp:2026-02-28 10:30:00, duration:1200",
    "user_id:103, action:login, timestamp:2026-02-28 10:45:00, duration:60",
    "user_id:102, action:logout, timestamp:2026-02-28 11:00:00, duration:null",
    "user_id:101, action:login, timestamp:2026-02-28 12:00:00, duration:300"
]

def process_logs(logs):
    user_stats = {}

    for line in logs:
        try:
            # 1. Flexible Parsing
            parts = {item.split(':')[0].strip(): item.split(':')[1].strip() 
                     for item in line.split(',')}
            print(parts)
            user_id = int(parts['user_id'])
            duration_raw = parts['duration']

            # 2. Skip nulls and validate
            if duration_raw == 'null':
                continue
            
            duration = int(duration_raw)

            # 3. Single-Pass Aggregation
            stats = user_stats.get(user_id, {'total_duration': 0, 'activity_count': 0})
            stats['total_duration'] += duration
            stats['activity_count'] += 1
            user_stats[user_id] = stats

        except (KeyError, ValueError, IndexError):
            # Defensive coding: skip malformed lines
            continue

    # 4. Final Finalization
    for uid in user_stats:
        count = user_stats[uid]['activity_count']
        user_stats[uid]['avg_duration'] = round(user_stats[uid]['total_duration'] / count, 2)

    return user_stats

print(process_logs(raw_logs))
    