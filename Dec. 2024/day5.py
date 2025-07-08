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

    sum_of_middle_pages_of_correct_updates = 0
    sum_of_middle_pages_of_incorrect_updates = 0

    incorrect_updates = []

    for update in updates:
        correct = True
        update = update.split(',')

        for i, el in enumerate(update):
            if i > 0:
                if f'{update[i-1]}|{el}' in rules:
                    continue
                else:
                    correct = False
                    incorrect_updates.append(update)
                    break
        
        if correct:
            middle_element_index = int((len(update)-1)/2)
            middle_element = update[middle_element_index]
            # print("Middle is ", middle_element)
            sum_of_middle_pages_of_correct_updates += int(middle_element)


    correct_updates = []
    for index, update in enumerate(incorrect_updates):
        correct = False
        while not correct:
            for i, el in enumerate(update):
                if i > 0:
                    if f'{update[i-1]}|{el}' in rules:
                        continue
                    else:
                        prev = update[i-1] 
                        next = el

                        update[i-1] = next
                        update[i] = prev

            for i, el in enumerate(update):
                if i > 0:
                    if f'{update[i-1]}|{el}' in rules:
                        correct = True
                        continue
                    else:
                        correct = False
                        break
                        
        correct_updates.append(update)   

    # print(correct_updates)
    for update in correct_updates:
        middle_element_index = int((len(update)-1)/2)
        middle_element = update[middle_element_index]
        sum_of_middle_pages_of_incorrect_updates += int(middle_element)

    return sum_of_middle_pages_of_correct_updates, sum_of_middle_pages_of_incorrect_updates


input = 'practice/input_day5.txt'
# input = 'practice/test.txt'
sum_of_middle_pages_of_correct_updates, sum_of_middle_pages_of_incorrect_updates = find_correct_updates(input)

print(f"The sum of middle pages of correctly-ordered updates is {sum_of_middle_pages_of_correct_updates}.")
print(f"The sum of middle pages of incorrectly-ordered updates is {sum_of_middle_pages_of_incorrect_updates}.")
print(f"-----------------------------------------------------------------------")
