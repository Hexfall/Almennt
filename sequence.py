Seq = [1,2,3]
n = int(input("Enter the length of the sequence: ")) - 1
for i in range(2, n):
    Seq.append(Seq[i-2] + Seq[i-1] + Seq[i])
for i in Seq:
    print(i)