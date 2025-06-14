def get_num_words(book_contents):
    word_count = book_contents.split()
    return len(word_count)
def get_char_count(book_contents):
    lower_char = book_contents.lower()
    char_count = {}
    for char in lower_char:
            if char in char_count:
                char_count[char] += 1
            else: 
                char_count[char] = 1 
    return char_count
def sort_on(dict):
    return dict["num"]
def sorted_lists(char_count):
    sorted_dict = []
    for ch in char_count:
        sorted_dict.append({"char": ch, "num": char_count[ch]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict




