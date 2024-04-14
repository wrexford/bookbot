#First boot.dev project, the bookbot
from string import ascii_lowercase as alc
from operator import itemgetter 

def print_report(path, word_count, alpha_dict):
    print(f"---Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char, value in sorted(alpha_dict.items(), key=itemgetter(1), reverse=True):
        print(f"The '{char}' character was found {value} times")
    print("---End report---")
    pass

def char_count_fun(book_text):
    #Create blank dict
    alpha_dict = {}
    #make everything lowercase
    book_text = book_text.lower()
    #Populate dict with char count
    for char in alc:
        alpha_dict[char] = book_text.count(char)
    return alpha_dict

def word_count_fun(book):
    word_count = len(book.split())
    return word_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = word_count_fun(book_text)
    alpha_dict = char_count_fun(book_text)
    print_report(path, word_count, alpha_dict)

    
if __name__ == "__main__":
    main()