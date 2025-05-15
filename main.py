from stats import count_chars, count_words, sort_chars_count
import sys


def get_book_text(path: str) -> str:
    try:
        with open(path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        return ""
    except IOError:
        print(f"Error: An error occurred while reading the file {path}.")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    content = get_book_text(path)
    num_words = count_words(content)
    chars_count = count_chars(content)
    sorted_chars_count = sort_chars_count(chars_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()