# EASY FUNCTIONS

# 1. Function Basics
def calculate_avg(numbers):
    total = 0
    if not numbers:
        return 0
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print(calculate_avg([5, 10, 15, 20]))    
print(calculate_avg([]))                 


# 2. Default Parameters
def greet_user(name, greet="Hello"):
    return f"{greet},{name}!"

print(greet_user("Alice"))              
print(greet_user("Bob", "Hi"))          



# MEDIUM FUNCTIONS

# 1. Variable Arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        amount = total * (discount / 100)
        total = total - amount
        return f"{total}({discount}% off)"
    return total

print(calculate_total(10, 20, 30))                    
print(calculate_total(10, 20, 30, discount=10))        


# 2. Closures
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))   
print(triple(5))   