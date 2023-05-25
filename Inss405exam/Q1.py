def calculate_mean(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total/count

def calculate_addition(numbers):
    return sum(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        middle_number_1 = length // 2
        middle_number_2 = middle_number_1 - 1
        return (sorted_numbers[middle_number_1] + sorted_numbers[middle_number_2]) / 2
    else:
        middle_index = length // 2
        return sorted_numbers[middle_index]

def collect_numbers(num_inputs):
    numbers = []
    for i in range(num_inputs):
        number = float(input("Enter a number: "))
        numbers.append(number)
    return numbers

# Collect input from the user
num_inputs = 10
input_numbers = collect_numbers(num_inputs)

# Calculate average, sum, and median
average = calculate_mean(input_numbers)
sum_value = calculate_addition(input_numbers)
median = calculate_median(input_numbers)

# Print the results
print("Numbers:", input_numbers)
print("Mean:", average)
print("Sum:", sum_value)
print("Median:", median)