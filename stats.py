def get_num_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    char_counts = {}

    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_by_count(dict_item):
    return dict_item["count"]

def sorted_chars(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_by_count)
    
    return chars_list