# EASY FUNCTIONS

# 1. Tuple Basics
def swap_pairs(t):
    swapped = []
    i = 0
    while i < len(t) - 1:
        swapped.append(t[i + 1])
        swapped.append(t[i])
        i += 2
    if len(t) % 2 != 0:
        swapped.append(t[-1])
    return tuple(swapped)

# Test cases:
print(swap_pairs((1, 2, 3, 4)))  
print(swap_pairs((1, 2, 3)))     


# 2. Tuple Unpacking
def get_stats(numbers):
    if not numbers:
        return (None, None, 0, 0.0)
    total = sum(numbers)
    average = total / len(numbers)
    return (min(numbers), max(numbers), total, average)

# Test case:
print(get_stats([1, 2, 3, 4, 5]))  


# MEDIUM FUNCTIONS

# 1. Named Tuples
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))


# 2. Tuple as Keys
def count_coordinate_occurrences(coords):
    result = {}
    for point in coords:
        if point in result:
            result[point] += 1
        else:
            result[point] = 1
    return result

coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
