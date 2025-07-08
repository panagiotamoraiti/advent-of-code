print(f"Day 1!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")

# Open the text file and put each word into two lists
listA = []
listB = []
with open('practice/input_day1.txt','r') as file:
    for line in file: 
        index = 0    
        for word in line.split():        
            if not index:
                listA.append(int(word))
            else:
                listB.append(int(word))
            index += 1

# Sort lists
listA = sorted(listA)
listB = sorted(listB)

# Create a list with element-wise distances between the two lists
distances = [abs(xi - yi) for xi, yi in zip(listA, listB)]

# Sum distances
sum_dist = sum(distances)
print(f"The total distance between the two lists is {sum_dist}.")

# Check if there are elements in listA that appear more than once
setA = set(listA)
if len(listA) == len(setA):
    print(f"Every element of listA is unique.")

# Find how many times a number of listA appears in listB
num_times_in_listB = [listB.count(xi) for xi in listA]

# Calculate the similarity score
similarity_score = [xi*num_times_in_listB[index] for (index, xi) in enumerate(listA)]
# similarity_score = [xi * yi for xi, yi in zip(listA, num_times_in_listB)]

# Sum similarity scores
total_similarity_score = sum(similarity_score)
print(f"The total similarity score is {total_similarity_score}.")
print(f"-----------------------------------------------------------------------")
