from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict_by_value_desc
import sys

def get_book_text(p):
    with open(p) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    t = get_book_text(path)
    
    print(f"Found {get_num_words(t)} total words")
    
    print("--------- Character Count -------")
    t = t.lower()
    s = sort_dict_by_value_desc(get_num_chars(t))
    for i in s:
        print(f"{i['char']}: {i['num']}")

    print("============= END ===============")


main()