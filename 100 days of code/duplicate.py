numbers = [3, 2, 4, 6, 3, 8]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(str(numbers[i]) + " is a duplicate number")
            break

