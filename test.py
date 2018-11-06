input()
words = input().split()
for i in range(len(words)):
    if words[i] != str(i + 1) and words[i] != 'mumble':
        print("something is fishy")
        break
else:
    print("makes sense") 