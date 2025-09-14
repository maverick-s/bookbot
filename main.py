from stats import num_words, char_count, report
import sys

def get_book_text(filepath):
     return filepath.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        text = get_book_text(f)
    word_count = num_words(text)

    character_count = report(char_count(text))

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count -----------")
    print(word_count)
    print("--------- Character Count ---------")
    for k, v in character_count.items():
        if k.isalpha() == True:
            print(f"{k}: {v}")
        else:
            continue

    print("============= END =============")

main()