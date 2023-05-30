import os
import re


# Refactoring
def build_sentences(text_data: str):
    texts = re.split("\n", text_data)

    for i in range(len(texts)):
        if texts[i] == "":
            texts[i] = "EL331"
            
    sentences = re.split(" EL331 | EL331|EL331 |EL331", " ".join(texts))

    return sentences


# Remove unfavorable characters (un-used)
def clean_text(texts):
    for i in range(len(texts)):
        texts[i] = re.sub("\"|“|”|-|^\'|_", "", texts[i])

    return texts


# Main method
def main():
    filenames = os.listdir("./before_refactoring")

    for fn in filenames:
        if fn == ".gitkeep":
            continue
        
        with open(f"./before_refactoring/{fn}", "r", encoding="utf-8") as f:
            text_data = str(f.read())

        sentences = build_sentences(text_data)

        with open(f"./after_refactoring/{fn}", "w", encoding="utf-8") as f:
            f.write("\n".join(sentences))

        print(f"Done {fn}")


if __name__ == "__main__":
    main()
    