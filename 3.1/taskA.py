def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
inp = int(input())
print(fact(inp))