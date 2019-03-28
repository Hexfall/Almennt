with open("temp/results.txt") as read:
    results = read.read().split("SELECT '")
    done = set()
    for i in results[1:]:
        s = ""
        for j in i:
            if j == "'":
                break
            s += j
        done.add(s)
    done = list(done)
    done.sort()
with open("temp/done.txt", "w") as write:
    write.write("\n".join(done))