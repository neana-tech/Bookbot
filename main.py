def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_text_count(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_sorted_list(chars_dict)
    print(f"{num_words} words found in the document")
    print(chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_text_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars [lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def chars_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list

main()