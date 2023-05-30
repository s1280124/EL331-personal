import unit6
import json
import os
import re
import statistics
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
print()


morph, pos = None, None

token_count = 0 
word_count = 0
types = set()
one_sentence_count = 0
one_sentence_lengths = []

# global variable
m1_upper_count = 0
m2_nnp_count = 0
m2_correct_nnp_count = 0
m5_comman_count = 0
m6_semicolon_count = 0
m7_symbol_count = 0
m8_slang_count = 0

slangs = ["GOAT", "lit", "snatched", "IRL", "IMO", "LOL", "lol", "DM", "TBH",
           "troll", "sus", "tripledemic", "Mpox", "shrinkflation", "nomophobia",
           "sharent", "finfluencer", "copypasta", "deplatform", "stan", "ICYMI",
           "IKYKY", "JOMO", "phubbing", "rizz", "cringe", "adorkable", "totes",
           "OMG", "ROFL", "IDK", "JK", "ASAP", "TGIF", "ELI5", "RIP", "TMI",
           "bucks", "fam", "mate", "flick", "abs", "dope", "cuz", "Gotcha",
           "Dunno", "kinda", "sorta", "long-winded", "Deuce-what-the-deuce",
           "jabber", "jabbering", "jabbered", "Ravenous", "towhead"]


# Number of all upper words per number of all words
def marker1(word):
    global m1_upper_count
    if re.match(r"^[A-Z]+$", word):
        m1_upper_count += 1


# Number of proper nouns per number of first char is upper
def marker2(word, tag):
    global m2_nnp_count, m2_correct_nnp_count
    if tag in ["NNP", "NNPS"]:
        m2_nnp_count += 1
        if re.match(r"^[A-Z]$", word[0]):
            m2_correct_nnp_count += 1


# Number of verbs on for time per number of adjectives on for place
def marker3(pos):
    unit6.adjectives(pos)
    pass


# Number of perfect_aspect per number of non-perfect_aspect
def marker4(pos):
    unit6.verbs(pos)
    pass


# Number of "," per total number of tokens
def marker5(word):
    global m5_comman_count
    if word == ",":
        m5_comman_count += 1


# Number of ";" per total number of tokens
def marker6(word):
    global m6_semicolon_count
    if word == ";":
        m6_semicolon_count += 1


# Number of "!" per total number of tokens 
def marker7(word):
    global m7_symbol_count
    if word == "!":
        m7_symbol_count += 1


# Number of slang per total number of tokens
def marker8(word):
    global m8_slang_count
    if word in slangs:
        m8_slang_count += 1


# Number of types per total number of tokens
def marker9():
    pass # not need impl beause it can calc by global variable.


# Median number of words that make up one sentence
def marker10():
    pass # not need impl beause it can calc by global variable.


# Reset global variables
def reset_marker():
    global token_count, word_count, types
    global one_sentence_count, one_sentence_lengths
    global m1_upper_count, m2_nnp_count, m2_correct_nnp_count
    global m5_comman_count, m6_semicolon_count, m7_symbol_count
    global m8_slang_count

    token_count = 0
    word_count = 0
    types = set()
    one_sentence_count = 0
    one_sentence_lengths = []

    m1_upper_count = 0
    m2_nnp_count = 0
    m2_correct_nnp_count = 0
    m5_comman_count = 0
    m6_semicolon_count = 0
    m7_symbol_count = 0
    m8_slang_count = 0


# Common method
def analyse(sentence):
    global token_count, word_count, types
    global one_sentence_count, one_sentence_lengths

    token_count += len(pos)
    temp, one_sentences = "", []
    for word, tag in pos:
        if word not in [".", ",", "!", "?"]:
            types.add(word)
            word_count += 1
        
        temp = f"{temp} {word}"
        if word == ".":
            one_sentences.append(temp)
            one_sentence_lengths.append(len(temp.split(" ")))
            temp = ""
        elif word == "!":
            one_sentences.append(temp)
            one_sentence_lengths.append(len(temp.split(" ")))
            temp = ""
        elif word == "?":
            one_sentences.append(temp)
            one_sentence_lengths.append(len(temp.split(" ")))
            temp = ""
       
        marker1(word)
        marker2(word, tag)
        marker5(word)
        marker6(word)
        marker7(word)
        marker8(word)

    marker3(pos)
    marker4(pos)
    marker9()
    marker10()

    one_sentence_count += len(one_sentences)


def save_characteristics(characteristics, author):
    on_total, of_place, of_time = unit6.get_adjectives_result()
    perfect_aspect, non_perfect_aspect = unit6.get_verbs_result()

    characteristics["author"] = author
    try: characteristics["m1"] = round((m1_upper_count/word_count)*100, 5)
    except: characteristics["m1"] = 0
    try: characteristics["m2"] = round((m2_correct_nnp_count/m2_nnp_count)*100, 5)
    except: characteristics["m2"] = 0
    try: characteristics["m3_1"] = round((of_place/on_total)*100, 5)
    except: characteristics["m3_1"] = 0
    try: characteristics["m3_2"] = round((of_time/on_total)*100, 5)
    except: characteristics["m3_2"] = 0
    try: characteristics["m4_1"] = round((perfect_aspect[1]/perfect_aspect[0])*100, 5)
    except: characteristics["m4_1"] = 0
    try: characteristics["m4_2"] = round((perfect_aspect[2]/perfect_aspect[0])*100, 5)
    except: characteristics["m4_2"] = 0
    try: characteristics["m4_3"] = round((perfect_aspect[3]/perfect_aspect[0])*100, 5)
    except: characteristics["m4_3"] = 0
    try: characteristics["m4_4"] = round((non_perfect_aspect[1]/non_perfect_aspect[0])*100, 5)
    except: characteristics["m4_4"] = 0
    try: characteristics["m4_5"] = round((non_perfect_aspect[2]/non_perfect_aspect[0])*100, 5)
    except: characteristics["m4_5"] = 0
    try: characteristics["m4_6"] = round((non_perfect_aspect[3]/non_perfect_aspect[0])*100, 5)
    except: characteristics["m4_6"] = 0
    try: characteristics["m5"] = round((m5_comman_count/token_count)*100, 5)
    except: characteristics["m5"] = 0
    try: characteristics["m6"] = round((m6_semicolon_count/token_count)*100, 5)
    except: characteristics["m6"] = 0
    try: characteristics["m7"] = round((m7_symbol_count/token_count)*100, 5)
    except: characteristics["m7"] = 0
    try: characteristics["m8"] = round((m8_slang_count/word_count)*100, 5)
    except: characteristics["m8"] = 0
    try: characteristics["m9"] = round((len(types)/word_count)*100, 5)
    except: characteristics["m9"] = 0
    try: characteristics["m10"] = int(statistics.median(one_sentence_lengths))
    except: characteristics["m10"] = 0

    return characteristics


def print_characteristics():
    with open('./datasets/characteristics.json') as f:
        characteristics = json.load(f)

    print()
    print(f"Marker01: {characteristics['m1']}%")
    print(f"Marker02: {characteristics['m2']}%")
    print(f"Marker03.1: {characteristics['m3_1']}%")
    print(f"Marker03.2: {characteristics['m3_2']}%")
    print(f"Marker04.1: {characteristics['m4_1']}%")
    print(f"Marker04.2: {characteristics['m4_2']}%")
    print(f"Marker04.3: {characteristics['m4_3']}%")
    print(f"Marker04.4: {characteristics['m4_4']}%")
    print(f"Marker04.5: {characteristics['m4_5']}%")
    print(f"Marker04.6: {characteristics['m4_6']}%")
    print(f"Marker05: {characteristics['m5']}%")
    print(f"Marker06: {characteristics['m6']}%")
    print(f"Marker07: {characteristics['m7']}%")
    print(f"Marker08: {characteristics['m8']}%")
    print(f"Marker09: {characteristics['m9']}%")
    print(f"Marker10: {characteristics['m10']}")


# Main method
def main():
    global morph, pos, token_count, one_sentence_count

    authors = os.listdir("./datasets")
    try: authors.remove("characteristics.json")
    except: pass

    author = ""

    while True:
        print("Select the number for you want to create characteristics.")
        for i in range(len(authors)):
            print(f"{i}: {authors[i]}")

        try:
            print("Input number > ", end="")
            i = int(input())
            author = authors[i]
            break
        except:
            continue
    
    filenames = os.listdir(f"./datasets/{author}")
    characteristics = {}
    print()

    for fn in filenames:
        with open(f"./datasets/{author}/{fn}", "r", encoding="utf-8") as f:
            text_data = f.read()
    
        sentences = re.split("\n", text_data)
        print(f"Start analysis characteristics ({fn})")
        for sentence in sentences:
            
            morph = nltk.word_tokenize(sentence)
            pos = nltk.pos_tag(morph)

            analyse(sentence)

    characteristics = save_characteristics(characteristics, author)

    with open('./datasets/characteristics.json', 'w', encoding="utf-8") as f:
        json.dump(characteristics, f, indent=4)    

    print_characteristics()

if __name__ == "__main__":
    main()
