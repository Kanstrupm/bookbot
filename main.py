import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



from stats import count_words
from stats import count_character
from stats import sort_dict_value

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = (get_book_text(filepath))
    word_count = count_words(book_text)
    char_count = count_character(book_text)
    sort_char = sort_dict_value(char_count)
    


    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")


    for item in sort_char:
        char = item["char"]
        count = item["count"]

        if char.isalpha():
            print (f"{char}: {count}")
    print ("============= END ===============")


main()