# Badge Records & Course Enrollment Problems

---

## The Problem: Badge Records (Part 1)

We are working on a security system for a badged-access room in our company's building.

Given an unordered list of names and their badge actions (`"enter"` or `"exit"`), you need to find two groups of people:

- **Group 1:** People who exited the room without a recorded entry. (This includes someone who exits, and then exits again).
- **Group 2:** People who entered the room without a recorded exit. (This includes someone who enters, and then enters again, or is still in the room at the end of the records).

### Assumptions & Rules

- You can assume the records are chronological.
- A person can only be in the room or outside the room.
- Return the two groups in any order (e.g., as two sets or lists).

### Example Input

```python
badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]
```

### Expected Output

```python
# Group 1 (Invalid Exits), Group 2 (Invalid Enters)
["Martha"], ["Paul", "Curtis"]
```

### Explanation

- **Martha** exited right at the beginning without entering. (Group 1)
- **Paul** entered, and then entered again without exiting first. (Group 2)
- **Curtis** entered, but never exited by the end of the log. (Group 2)
- **Jennifer** entered and exited perfectly. (Neither)

---

## The Escalation: Badge Records (Part 2)

We are adding a new security rule. We want to find employees who might be behaving suspiciously.

### The Rule

Find anyone who badges into the room **3 or more times within any 1-hour timeframe**.

### The Input

You are given a new list of records. This time, it only contains badge entries. Each record is a pair containing the employee's name and the time of their entry.

The time is represented as an integer in military time (e.g., `830` means 8:30 AM, `1355` means 1:55 PM, `2200` means 10:00 PM).

The list is **not** guaranteed to be in chronological order.

### The Goal

Return a dictionary/map where the key is the name of the suspicious employee, and the value is a list of the times they badged in during that specific 1-hour window. If a person has multiple 1-hour windows with 3+ entries, returning any one of those windows is acceptable.

### Example Input

```python
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
```

### Expected Output

```python
{
  "John":     ["835", "855", "915", "930"],  # All within a 1-hour window (8:35 to 9:35)
  "Paul":     ["1315", "1355", "1405"],      # Within 13:15 to 14:15
  "Jennifer": ["1315", "1335", "1405"]       # Within 13:15 to 14:15
}
```

---

## Course Enrollment: Shared Courses

You are a developer for a university. Your system has a log of students and the courses they are currently enrolled in.

### The Goal

Given an unordered list of `[student_ID, course_name]` pairs, write a function that outputs all possible pairs of students and the courses they share.

### Assumptions & Rules

- Every student ID should be paired with every other student ID exactly once.
- If two students do not share any courses, they should still appear in the output with an empty list.
- The order of the output or the order of the pairs does not matter.

### Example Input

```python
student_course_pairs = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["58", "Mechanics"],
  ["58", "Art History"],
  ["17", "Software Design"],
  ["58", "Operating Systems"],
  ["17", "Linear Algebra"],
  ["17", "Art History"]
]
```

### Expected Output

```python
{
  ("58", "94"): ["Art History", "Operating Systems"],
  ("58", "17"): ["Linear Algebra", "Art History"],
  ("94", "17"): ["Art History"]
}
```

### Explanation

- **Student 58** is taking: Linear Algebra, Mechanics, Art History, Operating Systems.
- **Student 94** is taking: Art History, Operating Systems.
- **Student 17** is taking: Software Design, Linear Algebra, Art History.
- The intersection of courses for students 58 and 94 is **Art History** and **Operating Systems**



----
🧩 The Problem: Craftier Students
You are given a list of class time slots, where each slot has a start time and an end time [start_time, end_time].

The Goal: Find the maximum number of classes a student can attend without any scheduling conflicts (meaning no two selected intervals overlap).

Example Input:

Python
classes = [[1, 4], [2, 5], [6, 7], [3, 8]]
Expected Output: 2 (By selecting [1, 4] and [6, 7])