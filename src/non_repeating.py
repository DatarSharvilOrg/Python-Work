def first_non_repeating_char(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        if count == 1: 
            return char
    return "None"
text = input("Enter a sentence: ").lower()
print(first_non_repeating_char(text))