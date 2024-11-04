inp = input()
n = int(inp[0])
k = int(inp[2])
def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
f = fact(n + k - 1) / (fact(k) * fact(n - 1))
print(int(f))