print(f"Day 4!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")

import re

def xmas_search(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read()
        
        filtered_text = []
        for line in text:
            filtered_line = ''.join([char for char in line if char in {'X', 'M', 'A', 'S', '\n'}])
            filtered_text.append(filtered_line)

        filtered_text = ''.join(filtered_text)
        text_in_rows = filtered_text.split("\n")

        # Remove empty rows
        text_in_rows = [row for row in text_in_rows if row != ""]
        
        # Initialize counter to 0
        xmas_times = 0

        # Iterate over the rows of txt file
        for row in text_in_rows:
            # Find Horizontal XMAS (Written Forwards or Backwards)
            xmas_word = re.findall("XMAS", row)
            xmas_word_back = re.findall("SAMX", row)

            xmas_times += len(xmas_word)
            xmas_times += len(xmas_word_back)

        # Transpose rows into columns (iterate over the columns and join characters into an str)
        text_in_columns = ["".join(row[i] for row in text_in_rows) for i in range(len(text_in_rows[0]))]

        for column in text_in_columns:
            # Find Horizontal XMAS (Written Forwards or Backwards)
            xmas_word = re.findall("XMAS", column)
            xmas_word_back = re.findall("SAMX", column)

            xmas_times += len(xmas_word)
            xmas_times += len(xmas_word_back)

        # Convert text into a grid of characters
        grid = [list(row) for row in text_in_rows]

        # Gather all possible text in diagonals
        text_in_diagonals = []

        # Length of rows, columns
        rows, columns = len(grid[0]), len(grid[1])

        # Primary diagonals
        for d in range(-rows + 1, columns):  # offsets for diagonals
            text_in_diagonals.append([grid[r][c] for r in range(rows) for c in range(columns) if r - c == d])
        
        # Secondary diagonals
        for d in range(rows + columns - 1):
            text_in_diagonals.append([grid[r][c] for r in range(rows) for c in range(columns) if r + c == d])

        text_in_diagonals = [''.join(diag_text) for diag_text in text_in_diagonals]

        for diag in text_in_diagonals:
            # Find Horizontal XMAS (Written Forwards or Backwards)
            xmas_word = re.findall("XMAS", diag)
            xmas_word_back = re.findall("SAMX", diag)

            xmas_times += len(xmas_word)
            xmas_times += len(xmas_word_back)

    return xmas_times


def mas_shape_x_search(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read()
        
        filtered_text = []
        for line in text:
            filtered_line = ''.join([char for char in line if char in {'X', 'M', 'A', 'S', '\n'}])
            filtered_text.append(filtered_line)

        filtered_text = ''.join(filtered_text)
        text_in_rows = filtered_text.split("\n")

        # Remove empty rows
        text_in_rows = [row for row in text_in_rows if row != ""]
        
        # Transpose rows into columns (iterate over the columns and join characters into an str)
        text_in_columns = ["".join(row[i] for row in text_in_rows) for i in range(len(text_in_rows[0]))]

        # Initialize counter to 0
        xmas_times = 0

        # Iterate over the rows of txt file
        for i in range(len(text_in_rows)):
            # Find Horizontal XMAS (Written Forwards or Backwards)
            xmas_word = re.finditer("A", text_in_rows[i])
            for match in xmas_word:
                if 0 < match.start() < len(text_in_columns) - 1 and 0 < i < len(text_in_rows) - 1:
                    prev_row_prev_col = text_in_rows[i-1][match.start()-1]
                    prev_row_next_col = text_in_rows[i-1][match.start()+1]
                    next_row_prev_col = text_in_rows[i+1][match.start()-1]
                    next_row_next_col = text_in_rows[i+1][match.start()+1]

                    if (prev_row_prev_col == "M" and next_row_next_col == "S") or (prev_row_prev_col == "S" and next_row_next_col == "M"):
                        if (prev_row_next_col == "M" and next_row_prev_col == "S") or (prev_row_next_col == "S" and next_row_prev_col == "M"):
                            xmas_times += 1

    return xmas_times


input = 'practice/input_day4.txt'
# input = 'practice/test.txt'
num_xmas = xmas_search(input)
num_mas_shape_x = mas_shape_x_search(input)

print(f"The word XMAS appears {num_xmas} times.")
print(f"The word XMAS appears {num_mas_shape_x} times.")
print(f"-----------------------------------------------------------------------")
