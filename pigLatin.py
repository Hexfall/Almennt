while(True):
    inp = input("Enter a word: ")
    if inp == ".":
        break
    tail = ""
    if inp[:1] == 'a' or inp[:1] == 'e' or inp[:1] == 'i' or inp[:1] == 'o' or inp[:1] == 'u':
        print(inp + "yay")
    else:
        while(inp != ""):
            if inp[:1] == 'a' or inp[:1] == 'e' or inp[:1] == 'i' or inp[:1] == 'o' or inp[:1] == 'u':
                break
            else:
                tail += inp[:1]
                inp = inp[1:]
        if (inp == ""):
            print(tail)
        else:    
            print(inp + tail + "ay")