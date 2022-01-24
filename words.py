words = ["hello", "Hi", "yees", "enter", "ENter"]


def print_upper_words(words, must_start_with):
    """Prints each word in uppercase"""
    for word in words:
        first = word[0].lower()
        if first in must_start_with:
            print(word.upper())


print_upper_words(["hello", "Hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
