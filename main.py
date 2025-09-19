import sys
from stats import count_words, count_characters, sort_dicts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return str(file_contents)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    contents = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = count_words(contents)
    print(f"Found {word_count} total words")
    char_count =  count_characters(contents)
    sorted_char_count = sort_dicts(char_count)
    print("--------- Character Count -------")
    for entry in sorted_char_count:
        print(f"{entry['char']}: {entry['num']}")

if __name__=="__main__":
    main()