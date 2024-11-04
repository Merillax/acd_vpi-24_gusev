inp = input()
n = int(inp[0])
k = int(inp[2])
def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
f = fact(n) / (fact(k) * fact(n - k))
print(int(f))