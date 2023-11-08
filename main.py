def main():
    file = "./books/frankenstein.txt"

    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        letter_counts = {}

        for word in words:
            for letter in word.lower():
                if letter not in letter_counts:
                    letter_counts[letter] = 0
                letter_counts[letter] += 1

        print_report(file, word_count, letter_counts)

def print_report(file: str, word_count: int, letter_counts: dict[str, int]):
    letter_list = list(letter_counts)
    letter_list.sort()

    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    for letter in letter_list:
        if not letter.isalpha():
            continue
        print(f"The '{letter}' character was found {letter_counts[letter]} times")
    print("--- End report ---")

main()