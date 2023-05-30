# Unit6.1 (adjectives)
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
total_1 = 0
of_time = 0
of_place = 0


def adjectives(pos):
    global total_1, of_time, of_place

    words = [t[0] for t in pos]

    for i in range(len(words)):
        if words[i] == 'on':
            total_1 += 1

            finish = min(i+6, len(words)-1) # Look 5 doors down if possible
            for j in range(i+1, finish+1):
                if bool(pattern.search(words[j])):
                    of_time += 1
                    break
                if j+1 == finish+1:
                    of_place += 1


def get_adjectives_result():
    result = (total_1, of_place, of_time)
    return result


def reset_adjectives():
    global total_1, of_time, of_place
    total_1, of_time, of_place = 0, 0, 0


# Unit6.2 (verbs)
total_2 = 0
present_total = 0
past_total = 0
future_total = 0

present_total_alt = 0
past_total_alt = 0
future_total_alt = 0

reigai = ['found', 'had', 'Had']

def verbs(pos):
    global total_2
    global present_total, past_total, future_total
    global present_total_alt, past_total_alt, future_total_alt
    total_2 += 1

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


def get_verbs_result():
    result = [(total_2, present_total, past_total, future_total),
              (total_2, present_total_alt, past_total_alt, future_total_alt)]

    return result


def reset_verbs():
    global total_2
    global present_total, past_total, future_total
    global present_total_alt, past_total_alt, future_total_alt

    total_2 = 0
    present_total, past_total, future_total = 0, 0, 0
    present_total_alt, past_total_alt, future_total_alt = 0, 0, 0
