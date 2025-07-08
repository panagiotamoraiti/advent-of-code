print(f"Day 3!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")

import re

def scan_corrupted_memory(txt_file):
    # Open the text file and read text
    with open(txt_file,'r') as file:
        memory = file.read()

        # Find valid expressions inside text
        valid_expressions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)

        # Extract digits
        digits = [re.findall("[0-9]{1,3}", el) for el in valid_expressions]

        # Multiply pairs and add the result
        mul_list = [int(el[0])*int(el[1]) for el in digits]
        sum_all_muls = sum(mul_list)

    return sum_all_muls


def scan_corrupted_memory_conditions(txt_file):
    # Open the text file and read each line in a list, convert str to int
    with open(txt_file,'r') as file:
        memory = file.read()

        # Find valid expressions inside text
        valid_expressions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", memory)

        # Keep a bool variable to see which expressions will be included
        activate = True

        # Keep here indices to include, 1st list index where there is a do(), 2nd list index where there is a don't()
        expressions_to_keep = [[], []]

        # We start including expressions from the beginning, append 0 index
        expressions_to_keep[0].append(0)

        # Iterate through expressions
        for i, el in enumerate(valid_expressions):

            # If you find do() and you have found don't() before, keep all the following expressions from this point (append index)
            if el == "do()" and not activate:
                activate = True
                expressions_to_keep[0].append(i)

            # If you find don't() and you have found do() before, discard all the following expressions from this point (append index)
            if el == "don\'t()" and activate:
                activate = False
                expressions_to_keep[1].append(i)

        # Based on the indexes in expressions_to_keep, keep only the specific ranges you have found
        # Keep range is each pair of indexes, [expressions_to_keep[0]:expressions_to_keep[1]+1]
        valid_expressions_updated = []
        for i, el in enumerate(expressions_to_keep[0]):
            valid_expressions_updated += valid_expressions[expressions_to_keep[0][i]:expressions_to_keep[1][i]+1]

        # Extract digits
        digits = [re.findall("[0-9]{1,3}", el) for el in valid_expressions_updated]

        # Remove empty expressions
        digits = [el for el in digits if el != []]

        # Multiply pairs and add the result
        mul_list = [int(el[0])*int(el[1]) for el in digits]
        sum_all_muls = sum(mul_list)

    return sum_all_muls


input = 'practice/input_day3.txt'
result = scan_corrupted_memory(input)
result_conditions = scan_corrupted_memory_conditions(input)

print(f"The result of adding all multiplications is {result}.")
print(f"The result of adding all multiplications is {result_conditions}.")
print(f"-----------------------------------------------------------------------")