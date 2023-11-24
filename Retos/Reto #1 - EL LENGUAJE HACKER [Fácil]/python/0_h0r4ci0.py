sentence = input("Enter a sentence: ")

alphabet = {
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "#",
    "i": "!",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "|\/|",
    "n": "|\|",
    "o": "0",
    "p": "|>",
    "q": "0,",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "><",
    "y": "`/",
    "z": "2"
}

for letter in sentence:
    if letter in alphabet:
        sentence = sentence.replace(letter, alphabet[letter])
print(sentence)
