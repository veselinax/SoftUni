n1 = int(input())
n2 = int(input())
n3 = int(input())

def smallest_num(a,b,c):
    if a < b and a < c:
        res = a
    elif b < a and b < c:
        res = b
    else:
        res = c
    return res

print(smallest_num(n1,n2,n3))