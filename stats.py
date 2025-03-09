def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    res = {}
    for key in text:
        if key in res:
            res[key] += 1
        else:
            res[key] = 1

    return res

def sort_on(dict):
    return dict["num"]

def sort_dict_by_value_desc(d):
    chars_list = list()

    for k, v in d.items():
        if k.isalpha():
            chars_list.append({"char": k, "num": v})
        
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list