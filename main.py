def main():

    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)
    total_words = get_word_count(file_contents)
    letter_count_dict = get_letter_count_dict(file_contents)
    sorted_letter_count_dict = get_sorted_letter_count_dict(letter_count_dict)

    print(f"--- File report commencing ---\n")
    print(f"A total of {total_words} words were found.\n")
    
    for character in sorted_letter_count_dict:
        print(f"The letter '{character}' appeared {letter_count_dict[character]} times.")

    print("\n--- File report terminating ---")

def get_file_contents(file_path):
    with open(file_path) as f:
       return f.read()
    
def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_letter_count_dict(file_contents):
    contents_lower = file_contents.lower()
    letter_count_dict = {}
    
    for character in contents_lower:
        if character.isalpha():
            if character not in letter_count_dict:
                letter_count_dict[character] = 1
            else:
                letter_count_dict[character] += 1
    return letter_count_dict         

def get_sorted_letter_count_dict(letter_count_dict):

    sorted_by_value = sorted(letter_count_dict, key=letter_count_dict.get, reverse = True)
    return sorted_by_value
    
main()


