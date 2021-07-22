words = input("").split(" ")
vowels = ['a', 'e', 'i', 'o', 'u']
def translate(words):
    first = words[0]
    if first in vowels:
        words = words.lower()
        words += "fu"
        return words
    else:
        words = words.lower()
        for letter in words:
            if letter in vowels:
                index_value = words.index(letter)
                break
        words = words[index_value:] + words[:index_value] + "mu"
        return words
for word in words:
    print(translate(word), end=" ")
