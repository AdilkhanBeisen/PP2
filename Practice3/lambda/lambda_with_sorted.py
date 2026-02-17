# lambda_with_sorted.py
# Using lambda with sorted()

students = [
    ("Azamat", 85),
    ("Ali", 90),
    ("Dana", 78)
]

#Sort by score (ascending)
sorted_by_score = sorted(students, key=lambda x: x[1])
print("Sorted by score (ascending):", sorted_by_score)


#Sort by score (descending)
sorted_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted by score (descending):", sorted_by_score_desc)


#Sort by name (alphabetically)
sorted_by_name = sorted(students, key=lambda x: x[0])
print("Sorted by name:", sorted_by_name)


#Sort by length of name
sorted_by_name_length = sorted(students, key=lambda x: len(x[0]))
print("Sorted by name length:", sorted_by_name_length)