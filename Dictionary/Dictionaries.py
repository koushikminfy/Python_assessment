# EASY FUNCTIONS

# 1. Dictionary Basics
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Test case:
print(invert_dictionary({"a": 1, "b": 2, "c": 3})) 


# 2. Dictionary Operations
def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  


# MEDIUM FUNCTIONS

# 1. Dictionary Comprehensions
def word_frequencies(text):
    words = text.split()
    return {word: words.count(word) for word in set(words)}

text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))


# 2. Nested Dictionaries
def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)

contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")

print(contacts)
