# The Scenario: You have a stream of financial transaction totals.
# You need to calculate a Simple Moving Average (SMA) of size k,
#  but you must handle missing data (None) gracefully.

# Python
# # Input
# data = [10, 20, None, 30, 40, None, 50]
# k = 3

# # Expected Logic for k=3:
# # Index 0: [10] -> 10.0
# # Index 1: [10, 20] -> 15.0
# # Index 2: [10, 20, None] -> 15.0 (None is ignored, denom is 2)
# # Index 3: [20, None, 30] -> 25.0 (None is ignored, denom is 2)
# # Index 4: [None, 30, 40] -> 35.0
# Your Task:
# Write calculate_sma(data, k).

# ⚠️ The Constraints:
# Single Pass: Do not re-sum the window inside the loop (O(N×K)). Use a Sliding Window approach (O(N)).

# None Handling: If a value is None, it doesn't contribute to the sum or the count (denominator).

# Pure Python: No numpy.

data = [None, None, 100, 200, None, 300, None, None, 400, 500]
# data = [100, None, 400, 500, 11, 14, None, None, 700, None, 1000]

from typing import List


def calculate_sma_of_given_window(data: List, window_size: int) -> List:
    n = len(data)
    sma_output = []
    running_sum = 0 if data[0] is None else data[0]
    running_count = 0
    # A running count will only get updated incase of none is not encountered
    # Running count is not part of window
    for idx, val in enumerate(data):
        if val is not None:
            running_sum += val
            running_count += 1
            if idx >= window_size:
                old_val= data[idx-window_size]
                if old_val is not None :
                    running_sum -= old_val
                    running_count -= 1
            
            if running_count == 0 :
                    sma_output.append(None)
            else : 
                    sma_output.append(running_sum/running_count)
       


    return sma_output


print(calculate_sma_of_given_window(data=data, window_size=3))
