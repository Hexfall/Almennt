oFill = open("words.txt")
sFill = open("sentences.txt", "w")
for i in oFill:
    if len(i) != 1:
        sFill.write(i[:-1] + " ")
        print(i[:-1],end=" ")
    else:
        sFill.write("\n")
        print()