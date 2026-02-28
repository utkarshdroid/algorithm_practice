# In a Weighted Moving Average (WMA), newer data is considered more important than older data.
# The Scenario:You have a list of stock prices and a window size $k$. You need to calculate the average,
# but the newest element in the window gets the highest weight.
# The Weights for $k=3$:Newest element: Weight of 3Middle element:
# Weight of Oldest element:
#  Weight of 1Denominator: S
# um of weights $(1 + 2 + 3 = 6)$The Formula for $k=3$:$$WMA = \frac{(P_t \times 3) + (P_{t-1} \times 2) + (P_{t-2} \times 1)}{1+2+3}$$🎯 The MissionWrite a function calculate_wma(data, k) that returns the weighted averages.⚠️ The Logic Rules:Strictly $O(N)$: You cannot use a nested loop. You must update the weighted sum in a single pass. (This is significantly harder than the SMA).No Nulls: To keep this focused on the math, assume the data has no None values.Startup Phase: For indices where the window isn't full (e.g., index 0 and 1 for $k=3$), just return None or skip them (as is standard in ML libraries like pandas).The Data:Pythonprices = [10, 20, 30, 40, 50]
# k = 3
# Step-by-Step for $k=3$:At index 2: Window is [10, 20, 30].
# Calculation: $((30 \times 3) + (20 \times 2) + (10 \times 1)) / 6 = 140 / 6 = 23.33$At index 3:
# Window is [20, 30, 40].
# Calculation: $((40 \times 3) + (30 \times 2) + (20 \times 1)) / 6 = 200 / 6 = 33.33$

prices = [10, 20, 30, 40, 50]
k = 3
from typing import List

def calculate_wma_optimized(prices, k):
    if not prices or k <= 0 or len(prices) < k:
        return []

    n = len(prices)
    result = []
    
    # 1. Pre-calculate the fixed divisor
    divisor = (k * (k + 1)) / 2
    
    # 2. Initial Window Setup
    current_sum = 0      # Sum of values: (P1 + P2 + P3)
    weighted_sum = 0     # Weighted: (1*P1 + 2*P2 + 3*P3)
    
    for i in range(k):
        current_sum += prices[i]
        weighted_sum += prices[i] * (i + 1)
    
    result.append(weighted_sum / divisor)
    
    # 3. The O(N) Slide
    for i in range(k, n):
        # Value leaving the window (was at weight 1)
        old_val = prices[i - k]
        # Value entering the window (will be at weight k)
        new_val = prices[i]
        
        # MATH TRICK: 
        # By subtracting the current_sum, we reduce every weight by 1.
        # Then we add the new value * k.
        weighted_sum = weighted_sum - current_sum + (new_val * k)
        
        # Update current_sum for the next iteration
        current_sum = current_sum - old_val + new_val
        
        result.append(weighted_sum / divisor)
        
    return result

# --- Test ---
prices = [10, 20, 30, 40, 50]
k = 3
print(calculate_wma_optimized(prices, k))
# Expected for k=3: [23.33, 33.33, 43.33]
