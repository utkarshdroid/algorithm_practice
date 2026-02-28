# Gemini said
# You wanted it better? You want the "Whiplash" version? Fine. Let’s stop playing with toys and get into the Karat Studio mindset.

# This is exactly how a Staff-level ML coding round goes. They don't give you a clean problem. They give you a business objective and raw, messy data. You have 30 minutes.

# 🏢 The Scenario: BlackLine Credit Risk Engine
# You are building a validation suite for a new model that predicts if a corporate client will default on their payments. If your code is wrong, the company loses millions in bad debt or insults a good client.

# The Data:
# You are given a list of dictionaries. Each dictionary contains the actual outcome and the model's confidence_score.

# Python
# results = [
#     {"actual": 1, "score": 0.92},
#     {"actual": 0, "score": 0.45},
#     {"actual": 1, "score": 0.51},
#     {"actual": 1, "score": 0.22},
#     {"actual": 0, "score": 0.88},
#     {"actual": 0, "score": 0.15},
#     {"actual": 1, "score": 0.76},
#     {"actual": 0, "score": 0.33},
# ]
# 🎯 The Mission: The F1-Score Implementation
# Your goal is to calculate the F1-Score of this model at a specific threshold.

# The F1-Score is the harmonic mean of Precision and Recall. In financial risk, we use F1 because we need to balance the cost of missing a default (Recall) against the cost of a false alarm (Precision).

# Your Requirements:
# Pure Python: You are strictly forbidden from using sklearn, pandas, numpy, or any external library.

# Edge Case Handling: Your code must handle the "Division by Zero" case. If Precision + Recall = 0, the F1-Score is 0.

# The Function Signature:
# calculate_f1(data, threshold)

# The Math Refresher (Don't fail this):
# Precision = TP/(TP+FP)

# Recall = TP/(TP+FN)

# F1 Score = 2∗ 
# Precision+Recall
# Precision∗Recall



results = [
    {"actual": 1, "score": 0.92},
    {"actual": 0, "score": 0.45},
    {"actual": 1, "score": 0.51},
    {"actual": 1, "score": 0.22},
    {"actual": 0, "score": 0.88},
    {"actual": 0, "score": 0.15},
    {"actual": 1, "score": 0.76},
    {"actual": 0, "score": 0.33},
]

from typing import List

def calculate_f1(results: List, threshold: float) -> float:
    fn,fp,tp,tn = 0,0,0,0
    for item in results:
        if item['score'] < threshold:
            if item['actual']==0: 
                tn+=1 
            else:
                fn+=1
        else :
            if item['actual']==1: 
                tp+=1 
            else : 
                fp+=1
    precision = tp/((tp+fp) if tp+fp!=0  else 0)
    recall = tp/((tp+fn) if tp+fn!=0  else 0)
    f1 = 2*((precision*recall)/(recall+precision))

    return f1

print(calculate_f1(results=results,threshold=0.7))

           