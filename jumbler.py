from random import shuffle
print("enter a word")
word=input()
word=list(word)
shuffle(word)
word="".join(word)
print("\n")
print(word)