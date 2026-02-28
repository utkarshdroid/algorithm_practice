# # You are in charge of a display advertising billing system.
# #  You are given an array of strings, where each string contains a comma-separated click count and a domain name.

# # The Goal:
# # Write a function that calculates the total number of clicks for a given domain 
# # and all of its top-level parent domains. Return a dictionary (or hash map) of the totals for every domain and subdomain.

# # Assumptions & Rules:
# # A domain like mobile.sports.yahoo.com is comprised of the subdomains:
# #  mobile.sports.yahoo.com, sports.yahoo.com, yahoo.com, and com.

# # The clicks from mobile.sports.yahoo.com should be added to the 
# # totals of all of those parent domains.

# # The output can be in any order.
# Gemini said
# That is completely fair. Graphs and trees are notoriously tricky, and they involve a whole different way of thinking about data. It is highly common to hit a wall with them, so tabling it until you feel more comfortable is a smart move. We will keep that one in our back pocket for later!

# Let's pivot to another absolute classic Karat interview category: String Parsing and Hash Maps. This one will let you practice those defaultdict skills we just talked about.

# The Problem: Domain Click Counts (Part 1)
# You are in charge of a display advertising billing system. You are given an array of strings, where each string contains a comma-separated click count and a domain name.

# The Goal:
# Write a function that calculates the total number of clicks for a given domain and all of its top-level parent domains. Return a dictionary (or hash map) of the totals for every domain and subdomain.

# Assumptions & Rules:
# A domain like mobile.sports.yahoo.com is comprised of the subdomains: mobile.sports.yahoo.com, sports.yahoo.com, yahoo.com, and com.

# The clicks from mobile.sports.yahoo.com should be added to the totals of all of those parent domains.

# The output can be in any order.

# Example Input:
# Python
# counts = [
#     "900,google.com",
#     "60,mail.yahoo.com",
#     "10,mobile.sports.yahoo.com",
#     "40,sports.yahoo.com",
#     "300,yahoo.com",
#     "10,stackoverflow.com",
#     "20,overflow.com",
#     "5,com.com",
#     "2,en.wikipedia.org",
#     "1,m.wikipedia.org",
#     "1,wikipedia.org",
#     "311,org",
# ]
# Expected Output:
# Python
# {
#     "com": 1345,
#     "google.com": 900,
#     "yahoo.com": 410,
#     "mail.yahoo.com": 60,
#     "mobile.sports.yahoo.com": 10,
#     "sports.yahoo.com": 50,
#     "stackoverflow.com": 10,
#     "overflow.com": 20,
#     "com.com": 5,
#     "org": 315,
#     "wikipedia.org": 4,
#     "en.wikipedia.org": 2,
#     "m.wikipedia.org": 1
# }
# Explanation of the output:
# Let's look at yahoo.com. Its total is 410. Why?

# 300 clicks directly from "yahoo.com"

# 60 clicks from "mail.yahoo.com"

# 40 clicks from "sports.yahoo.com"

# 10 clicks from "https://www.google.com/url?sa=E&source=gmail&q=mobile.sports.yahoo.com"

# All of those add up to 410.



counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,wikipedia.org",
    "311,org",
]

from typing import List
from collections import defaultdict

def get_site_click_count(counts: List)->dict[str,int]:
    site_count_dict = defaultdict(int)
    for count_site in counts:
        count , site = count_site.split(",")
        site = site.replace("https://","")
        site = site.partition("/")[0]
        site_split = site.split(".")
        for i in range(len(site_split)):
            sub_site = ".".join(site_split[i:])
            site_count_dict[sub_site] += int(count)
    return site_count_dict

print(get_site_click_count(counts))