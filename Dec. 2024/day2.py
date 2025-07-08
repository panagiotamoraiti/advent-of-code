print(f"Day 2!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")


def check_each_level(levels):
    safe = 0
    if levels: # Check if list is not empty
        # Create sorted lists
        levels_sorted_increasing = sorted(levels)
        levels_sorted_decreasing = sorted(levels, reverse=True)
        
        # Check if levels are sorted either in increasing or decreasing order
        if levels == levels_sorted_increasing or levels == levels_sorted_decreasing:
            # Calculate differencies between levels
            difs = [abs(level-levels[index-1]) for (index, level) in enumerate(levels) if index!=0]

            # Check if differencies between levels is greater equal to 1 or less equal to 3
            if not any(dif<1 or dif>3 for dif in difs):
                safe = 1
    return safe


def find_safe_reports(txt_file):
    # Open the text file and read each line in a list, convert str to int
    with open(txt_file,'r') as file:
        reports = file.read().split("\n")
        count_safe = 0
        for report in reports:
            levels = report.split()
            levels = [int(level) for level in levels] # Convert str to int

            # Check each level and if it is safe
            safe_report = check_each_level(levels)

            if not safe_report:
                # Check if the level can become safe by removing an element 
                for index in range(len(levels)):
                    levels_removed = levels.copy()

                    # Remove an element and check again
                    levels_removed.pop(index)
                    safe_report = check_each_level(levels_removed)

                    # If level can be removed in order the report to become safe continue
                    if safe_report:
                        break

            count_safe += safe_report
    return count_safe


input = 'practice/input_day2.txt'
safe_reports = find_safe_reports(input)

print(f"Number of safe reports is {safe_reports}.")
print(f"-----------------------------------------------------------------------")