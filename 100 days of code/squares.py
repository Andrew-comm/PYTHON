def get_squared_numbers(numbers):
    squared_numbers = []
    for i in numbers:
        squared_numbers.append(i*i)
    return squared_numbers


numbers = [2, 4, 5, 6]
print(get_squared_numbers(numbers))
