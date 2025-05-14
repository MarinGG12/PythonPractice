def search(x, y):
    if y in x:
        return "found"
    else:
        return "not found"

text = input("Enter a sentence: ")
word = input("Enter the word to search: ")

print(search(text, word))