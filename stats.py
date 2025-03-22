def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] = char_dict[char_lower] + 1
    return char_dict

def sort_dict_value(char_dict):
    list_of_dicts = []
    for char, count in char_dict.items():
        list_of_dicts.append({"char": char, "count":count})
    sort_dict = sorted(list_of_dicts, key = lambda x: x["count"], reverse=True)
    
    return sort_dict 
    

    
