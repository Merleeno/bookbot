import sys
from stats import get_num_words, get_letters, sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_letters(text)
    chars_list = sorted_chars(char_counts)

    

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()