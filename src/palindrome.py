word = input("Enter a word: ")
is_palindrome = lambda word: word.lower()[::-1] == word
print(is_palindrome(word))