n1 = int(input())
n2 = int(input())

def factorial_div(a,b):
    fact_a = 1
    fact_b = 1
    for n in range(a,0,-1): #if we have 3! we iterate 3,2,1 with step -1 so we go backwards and till 0 cuz we want 1 included
        fact_a *= n  # 3 * 2 * 1
    for k in range(b,0,-1):
        fact_b *= k
    res = fact_a / fact_b
    return f"{res:.2f}"

print(factorial_div(n1,n2))

