print(f"Day 5!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")


def find_correct_updates(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read().split('\n')

    # Extract printing rules and aequence of updates
    rules = [el for el in text if '|' in el]
    updates = [el for el in text if '|' not in el and el != '']

    # correct_order = rules[0]
    correct_order = []
    numbers_in_first_part = []
    numbers_in_second_part = []

    flag = True

    for i, rule in enumerate(rules):
        # Find the smallest number, the number that doesn't appear at the second part of any rule
        numbers_in_first_part.append(rule[:2])
        numbers_in_second_part.append(rule[3:5])

    numbers_in_first_part = set(numbers_in_first_part)
    numbers_in_second_part = set(numbers_in_second_part)

    total_unique_numbers = len(set(list(numbers_in_first_part) + list(numbers_in_second_part)))

    max_el = rules[0][3:5]
    for i in range(1379):
        for rule in rules:
            if max_el in rule[:2]:
                max_el = rule[3:5]
        # print(max_el)
            
    while flag:
        min_el = max_el
        min_el_prev = max_el

        for i in range(2):
            for rule in rules:
                if min_el in rule[3:5]:
                    min_el = rule[:2]

                    if min_el in correct_order:
                        min_el = min_el_prev
                    else:
                        min_el_prev = min_el
        else:
            correct_order.append(min_el)

        if len(correct_order) == total_unique_numbers:
            flag = False

    sum_of_middle_pages_of_correct_updates = 0
    # print(correct_order)

    for update in updates:
        correct = True
        update = update.split(',')
        # print()
        # print(update)

        for i, num in enumerate(update):
            if i < len(update)-1:
                if correct_order.index(num) < correct_order.index(update[i+1]):
                    # print(num)
                    # print(correct_order.index(num))
                    # print(correct_order.index(update[i+1]))
                    continue
                else:
                    correct = False
                    break
        
        if correct:
            middle_element_index = int((len(update)-1)/2)
            middle_element = update[middle_element_index]
            # print("Middle is ", middle_element)
            sum_of_middle_pages_of_correct_updates += int(middle_element)

    return sum_of_middle_pages_of_correct_updates


# input = 'practice/input_day5.txt'
input = 'practice/test.txt'
sum_of_middle_pages_of_correct_updates = find_correct_updates(input)

print(f"The sum of middle pages of correctly-ordered updates is {sum_of_middle_pages_of_correct_updates}.")
print(f"-----------------------------------------------------------------------")
