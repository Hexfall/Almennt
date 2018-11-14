for _ in range(int(input())):
    k, m, num = [int(i) for i in input().split()]
    done = set()
    for i in range(2, m + 1):
        num += int(str(num)[::-1])
        num = int("".join(sorted(str(num))))
        if num in done:
            print("{} R {}".format(k, i))
            break
        elif len(str(num)) > 7:
            if (str(num)[:4] == "1233" and str(num)[-4:] == "4444") or (str(num)[:4] == "5566" and str(num)[-4:] == "7777"):
                print("{} C {}".format(k, i))
                break
        done.add(num)
    else:
        print("{} {}".format(k, num))