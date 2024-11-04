size = int(input())

n = []
a = []

for i in range(1, size + 1):
    n.append(int(input()))
    a.append(list(map(int, input().split(" "))))

def merge(a1, a2, size1, size2):
    result = []
    left_index = 0
    right_index = 0
    while(left_index != size1 or right_index != size2):
        if(left_index == size1):
            result.append(a2[right_index])
            right_index += 1
        elif(right_index == size2):
            result.append(a1[left_index])
            left_index += 1
        elif(a1[left_index] <= a2[right_index]):
            result.append(a1[left_index])
            left_index += 1
        elif(a1[left_index] > a2[right_index]):
            result.append(a2[right_index])
            right_index += 1
    return result   
print(a[0])
if(size == 1):    
    middle_array = (map(str, a[0]))
else:
    middle_array = merge(a[0], a[1], n[0], n[1])
if(size > 2):
    for i in range(2, size):
        middle_array = merge(middle_array, a[i], len(middle_array), n[i])
print(" ".join(map(str, middle_array)))