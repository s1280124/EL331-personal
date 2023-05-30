# s1280160_Yusei Ichikawa_33.333%
# s1280124_Toshiki Ogata_33.333%
# s1260247_Shouya Hurukawa_33.333%

import re

# regular expression (more if needed)
regex = r''
regex += r"(^January$|^February$|^March$|^April$|^May$|^June$)|"
regex += r"(^July$|^August$|^September$|^October$|^November$|^December$)|"
regex += r"(^Sun|^Mon|^Tues|^Wednes|^Thurs|^Fri|^Satur)day|"
regex += r"(^second|^minute|^hour|^day|^week|^month|^year)|"
regex += r"(^morning|^afternoon|^noon|^night)|"
regex += r"(^birthday|^Christmas)"
pattern = re.compile(regex)

# Counters
total = 0
of_time = 0
of_place = 0

# Load .txt for dataset
with open('./dataset.txt', 'r') as f:
    dataset = f.read().split('\n')

# Split by example sentence + remove commas and commas
for sentence in dataset:
    sentence = sentence.replace('.', '').replace(',', '')

# Split by word
    words = sentence.split(' ')

# If on, check if the next few words match the regular expression
    for i in range(len(words)):
        if words[i] == 'on':
            total += 1

            finish = min(i+6, len(words)-1) # Look 5 doors down if possible
            for j in range(i+1, finish+1):
                if bool(pattern.search(words[j])):
                    of_time += 1
                    break
                if j+1 == finish+1:
                    of_place += 1

print()
print(f"Number of \"on\" : {total}")
print(f"Adverbials of place : {of_place}/{total}")
print(f"Adverbials of time : {of_time}/{total}")

# Comparison of of_place and of_time
if of_place > of_time:
    print("There are more adverbials of place.")
elif of_place < of_time:
    print("There are more adverbials of time.")
else:
    print("The number of adverbials of place and time is equal.")
print()
