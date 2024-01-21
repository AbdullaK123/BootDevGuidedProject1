from string import ascii_lowercase

def letter_count(text):
    count_dict = {char:0 for char in ascii_lowercase}
    for word in text.lower().split():
        for char in word:
            if char in ascii_lowercase:
                count_dict[char] += 1
    return count_dict


def main():
    with open('books/Frankenstein.txt', 'r') as file:
        content = file.read()
        words = content.split()
        letter_count_dict = letter_count(content)
        print(f"There are {len(words)} words in this book.\n")
        for char in letter_count_dict:
            print(f"The letter {char} was found {letter_count_dict[char]} times.\n")


        
main()