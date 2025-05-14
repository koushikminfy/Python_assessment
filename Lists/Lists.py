# EASY FUNCTIONS

# 1. List Operations
def filter_even_numbers(numbers):
    even_num = []
    for i in numbers:
        if i % 2 == 0:
            even_num.append(i)
    return even_num

# Test cases:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []


# 2. List Manipulation
def merge_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# Test cases:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  


# MEDIUM FUNCTIONS

# 1. List Comprehensions
def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

# Test cases:
print(generate_matrix(3, 3))



# 2. Nested Lists
def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# Test cases:
print(transpose_matrix(matrix))
