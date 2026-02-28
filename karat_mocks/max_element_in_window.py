# Given a list of transaction amounts and a window size k, 
# return a list containing the maximum value for each window.
# You must solve this in $O(N)$ time.
#  A nested loop ($O(NK)$) or using max(window) at every step will be rejected.
# 🎯 The MissionWrite a function sliding_window_max(data, k) that returns the maximums.
# The Data:
# amounts = [10, 2, 5, 8, 12, 7, 15, 20]
# k = 3


# Expected Result for 
# $k=3$
# :Window [10, 2, 5] -> Max: 10
# Window [2, 5, 8] -> Max: 8
# Window [5, 8, 12] -> Max: 12
# Window [8, 12, 7] -> Max: 12
# Window [12, 7, 15] -> Max: 15
# Window [7, 15, 20] -> Max: 20
# 
# 
#  "Pro-Tip": The Monotonic QueueTo solve this in $O(N)$,
#  you cannot use a simple sum. You need a Double-Ended Queue (deque) 
# to maintain the indices of "potential maximums.
# "The Logic:Maintain a Deque: Store indices of elements in the current window.
# Keep it Monotonic: Before adding a new element, 
# remove all elements from the back of the deque that are smaller than the new element (
# they can never be the maximum again).
# Check the Front: The front of the deque will always be the index of 
# the maximum element for the current window.
# Expire Old Indices: If the index at the front of the deque is outside the window 
# (i.e., front_index <= i - k), remove it.

amounts = [10, 2, 5, 8, 12, 7, 15, 20]
k = 3

from collections import deque
from typing import List
def peak_transaction_finder(amounts:List, k:int)->List:
    if not amounts or k <= 0:
        return []
    if k == 1:
        return amounts
    results = []
    dq = deque()
    for i in range(0, len(amounts)):
        if dq and dq[0]<= i-k:
            dq.popleft()
        while dq and amounts[dq[-1]] < amounts[i]:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            results.append(amounts[dq[0]])
    return results

print(peak_transaction_finder(amounts=amounts, k=k))

        
        


                

