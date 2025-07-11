import string

def find_longest_words(text):
    if not text.strip():
        return []

    clean_text = text.translate(str.maketrans("", "", string.punctuation))

    words = clean_text.split()

    max_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_len]

    return [(word, len(word)) for word in longest_words]

def main():
    text_input = input("Enter Text: ")

    longest = find_longest_words(text_input)

    if not longest:
        print("No valid words found.")
    elif len(longest) == 1:
        word, length = longest[0]
        print(f"The longest word is: {word}  ({length}charaters)")
    else:
        print("The longest words are:")
        for word, length in longest:
            print(f"{word}  ({length} characters)")

if __name__ == "__main__":
    main()
