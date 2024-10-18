word = input("enter a word: ")
word_length = len(word)
if word_length < 4:
    score = 1
    print(f"score: {score}")
elif 4 <= word_length <6:
    score = 3
    print(f"score: {score}")
elif 6 <= word_length < 8:
    score = 4
    print(f"score: {score}")
else:
    score = 10
    print(f"score: {score}")
