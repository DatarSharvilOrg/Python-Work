import re
def top_frequent_words(txt, n):
    words = re.findall(r'\b\w+\b', txt.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    top_n = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
    for word, count in top_n:
        print(f'{word}: {count}')
txt = input('Enter a sentence: ')
n = int(input('Enter the value of \'n\': '))

top_frequent_words(txt, n)