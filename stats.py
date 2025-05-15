def count_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict[str, int]:
    chars_count = {}

    for i in range(0, len(text)):
        char = text[i].lower()
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    
    return chars_count

def sort_chars_count(dict: dict[str, int]):
    sorted_list = []

    for char in dict:
        sorted_list.append({
            "char": char,
            "num": dict[char]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]
