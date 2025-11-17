import sys
from stats import count_words, character_count, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    def get_book_text(filepath):
        with open(filepath) as file_contents:
            return file_contents.read()


    
    book = get_book_text(filepath)

    word_count = count_words(book)


    character_counts = character_count(book)


    sorted_list = sort_on(character_counts)


    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for character in sorted_list:
        print(f'{character["character"]}: {character["count"]}')
    
    print(sys.argv)


main()