import re

# 正規表現 (必要に応じて増やす)
regex = r''
regex += r"(^January|^February|^March|^April|^May|^June)|"
regex += r"(^July|^August|^September|^October|^November|^December)|"
regex += r"(^Sun|^Mon|^Tues|^Wednes|^Thurs|^Fri|^Satur)day|"
regex += r"(^second|^minute|^hour|^day|^week|^month|^year)|"
regex += r"(^seconds|^minutes|^hours|^days|^weeks|^months|^years)|"
regex += r"(^morning|^afternoon|^noon|^night)|"
regex += r"(^birthday|^Christmas)"
pattern = re.compile(regex)

# カウンター
total = 0
of_time = 0
of_place = 0

# データセット用 .txt の読み込み
with open('./dataset.txt', 'r') as f:
    dataset = f.read().split('\n')

# 例文ごとに分割 + カンマとコンマを取り除く
for sentence in dataset:
    sentence = sentence.replace('.', '').replace(',', '')

    # 単語ごとに分割
    words = sentence.split(' ')

    # on があれば、それ以降の数単語が正規表現とマッチするか確認する
    for i in range(len(words)):
        if words[i] == 'on':
            total += 1

            finish = min(i+6, len(words)-1) # 可能なら5つ先まで見る
            for j in range(i+1, finish+1):
                if bool(pattern.search(words[j])):
                    of_time += 1
                    break
                if j+1 == finish+1:
                    of_place += 1
                
print(f"adverbials of place: {of_place}/{total}")
print(f"adverbials of time: {of_time}/{total}")