def add_words():
    

maxlength = 100
words = []

while len(words) < maxlength:
    sentence = input().split()
    words.append(sentence)

print(words)