n = int(input())
a = input().split(" ")

for i in range(0, n):
    min = int(a[i])
    index = i
    for j in range(i, n):
        if min > int(a[j]):
            min = int(a[j])
            index = j
    a[index] = a[i]
    a[i] = min
print(" ".join(map(str, a)))