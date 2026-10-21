txt = input("Enter a sentence: ")
count_vowel = lambda txt: sum(1 for char in txt.lower() if char in 'aeiou')
print(count_vowel(txt))