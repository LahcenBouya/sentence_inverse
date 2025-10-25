sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"the reverse sentence is: {" ".join(words[::-1])}")