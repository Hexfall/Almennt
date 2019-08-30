def right_shift(shift_str):
    return shift_str[1:] + shift_str[0]

string = input()
solution = len(string)
unq_letters = len(set(string))
if unq_letters == 1 or unq_letters == len(string):
    print(unq_letters)
    exit()
letter_count = {}
for letter in string:
    if letter in letter_count.keys():
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
min_count = min(letter_count.values())
for key in letter_count.keys():
    letter_count[key] = letter_count[key] // min_count
cycle_factor = sum(letter_count.values())
possible_ranges = [i for i in range(cycle_factor, len(string), cycle_factor) if len(string) % i == 0]
for cycle in possible_ranges:
    segments = [string[i:i + cycle] for i in range(0, len(string), cycle)]
    for index in range(1, len(segments)):
        if segments[index] != right_shift(segments[index - 1]):
            continue
    solution = cycle
    break
print(solution)