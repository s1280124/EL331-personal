import re
import nltk
import os
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Exceptions (add as needed)
reigai = ['found', 'had', 'Had']

# counter
total = 0
present_total = 0
past_total = 0
future_total = 0

present_total_alt = 0
past_total_alt = 0
future_total_alt = 0

# Load .txt for dataset
filenames = os.listdir("./datasets")

for name in filenames:
    with open(f'./datasets/{name}', 'r') as f:
        sentence = re.split('[,\.\?]',f.read())
        sentence = [content for content in sentence if content != '']

    for text in sentence:

        morph = nltk.word_tokenize(text)
        pos = nltk.pos_tag(morph)
        total += 1

        present = 999
        past = 999
        future = 999
        last = -1

        for i in range(len(pos)):

            word, tag = pos[i]
            if tag in ['VBN'] or word in reigai:
                last = i

        # If a word is judged by nltk to be a past participle
        if last != -1:
            for i in range(len(pos)):

                word, tag = pos[i]
                if word in ['Have', 'have', 'Has', 'has']:
                    present = i

                if word in ['Had', 'had']:
                    past = i

                if word in ['Will', 'will', 'Shall', 'shall']:
                    future = i

            if future < present and present < last:
                future_total += 1
            elif present < last:
                present_total += 1
            elif past < last:
                past_total += 1
            elif past == last:
                past_total_alt += 1

        # If no word is judged by nltk to be a past participle
        else:
            for i in range(len(pos)):

                word, tag = pos[i]
                if tag in ['VB', 'VBG', 'VBP', 'VBZ']:
                    if future != 999:
                        future_total_alt += 1
                        break
                    else:
                        present_total_alt += 1
                        break
                if tag in ['VBD', 'VBN']:
                    past_total_alt += 1
                    break
                if word in ['Will', 'will', 'Shall', 'shall']:
                    future = i

# outputs
print(f"perfect aspect: {present_total+past_total+future_total}/{total}")
print(f"{'present': <7} > {present_total}")
print(f"{'past': <7} > {past_total}")
print(f"{'future': <7} > {future_total}")
print()
print(f"non-perfect aspect: {present_total_alt+past_total_alt+future_total_alt}/{total}")
print(f"{'present': <7} > {present_total_alt}")
print(f"{'past': <7} > {past_total_alt}")
print(f"{'future': <7} > {future_total_alt}")
