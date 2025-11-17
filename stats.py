def count_words(text_string):
    words = text_string.split()
    return len(words)   

def character_count(text_string):
    count_dict = {}
    for character in text_string:
        if character.lower() not in count_dict:
            count_dict[character.lower()] = 1
        else:
            count_dict[character.lower()] += 1
    return count_dict

def sort_on(count_dict):
    sortable_list = []

    def sort_key(key):
        return key["count"]

    for key in count_dict:
        if key.isalpha() == True:
            temp_dict = {"character": key, "count": count_dict[key]}
            sortable_list.append(temp_dict)
    sortable_list.sort(reverse=True, key=sort_key)
    return sortable_list


        
