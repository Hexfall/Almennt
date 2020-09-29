Vowels = [
    "a",
    "e",
    "i",
    "o",
    "u",
]

letters = list(input())
for i in range(len(letters)):
    if letters[i] in Vowels:
        letters[i + 1] = ""
        letters[i + 2] = ""
print("".join(letters))