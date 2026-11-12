numbers = [2, 5, 8, 10, 12, 15]

even = [x for x in numbers if x % 2 == 0]
squares = [x**2 for x in even]
result = [x for x in squares if x > 100]

print("Even numbers:", even)
print("Squares:", squares)
print("Squares greater than 100:", result)