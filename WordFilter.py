words = ["tree", "button", "cat", "window", "defenestrate"]

#Use a list comprehension to filter out words longer than four letter
filtered_words = [word for word in words if len(word) <= 4]

#Display the filtered list
print(filtered_words)