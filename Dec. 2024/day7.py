print(f"Day 7!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")

from itertools import product

def find_calibration_result(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read().split('\n')

    # Extract numbers from rows
    numbers = [[int(num) for num in item.replace(':', '').split()] for item in text]

    # Separate results and numbers of equations
    results = [res[0] for res in numbers]
    numbers = [num[1:] for num in numbers]

    operators = ['+', '*']
    total_result = 0
    
    for equation, result in zip(numbers, results):
        # Find all possible combinations
        combinations = list(product(operators, repeat=len(equation) - 1)) 
        valid = False
        for combination in combinations:
            possible_result = equation[0]
            for i, op in enumerate(combination):
                if op == '+':
                    possible_result += equation[i + 1]
                elif op == '*':
                    possible_result *= equation[i + 1]

            if possible_result == result:
                valid = True

        if valid:
            total_result += result
    return total_result


def find_calibration_result_new_operation(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read().split('\n')

    # Extract numbers from rows
    numbers = [[int(num) for num in item.replace(':', '').split()] for item in text]

    # Separate results and numbers of equations
    results = [res[0] for res in numbers]
    numbers = [num[1:] for num in numbers]

    operators = ['+', '*', '||']
    total_result = 0
    
    for equation, result in zip(numbers, results):
        # Find all possible combinations
        combinations = list(product(operators, repeat=len(equation) - 1)) 
        valid = False
        for combination in combinations:
            possible_result = equation[0]
            for i, op in enumerate(combination):
                if op == '+':
                    possible_result += equation[i + 1]
                elif op == '*':
                    possible_result *= equation[i + 1]
                elif op == '||':
                    possible_result = str(possible_result) + str(equation[i + 1])
                    possible_result = int(possible_result)

            if possible_result == result:
                valid = True

        if valid:
            total_result += result
    return total_result
    
input = 'practice/input_day7.txt'
# input = 'practice/test.txt'
total_result = find_calibration_result(input)
total_result_new = find_calibration_result_new_operation(input)

print(f"The total calibration result is {total_result}.")
print(f"The total calibration result when new operation is included is {total_result_new}.")
print(f"-----------------------------------------------------------------------")
