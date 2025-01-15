def char_count(text):
    lowered_string = text.lower()
    count_dict = {}
    for char in lowered_string:
        # check if it's an alphabet character 
        if char.isalpha():
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1

    return count_dict


def word_count(text):
    words = text.split()
    wc = 0
    for word in words:
        wc += 1
    return wc

def sort_on(dict):
    return dict["num"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    #print(word_count(file_contents))
    #print(char_count(file_contents))
    words_count =  word_count(file_contents)
    char_count_dict = char_count(file_contents)

    list_of_dicts = []
    for char, num in char_count_dict.items():
        list_of_dicts.append({"char": char, "num": num})

    list_of_dicts.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count} words found in the document")
    print("")
    for item in list_of_dicts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
