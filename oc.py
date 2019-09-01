def check(s, k):
    for i in range (0, len(s)):
        if (s[i] != s[i % k]):
            return False
    return True
def countCommonDivisors(a, b):
    ct = 0
    n = len(a)
    m = len(b)
    for i in range(1, min(n, m) + 1):
        if (n % i == 0 and m % i == 0):
            if (a[0 : i] == b[0 : i]) :
                if (check(a, i) and check(b, i)) :
                    ct = ct + 1
    return ct
a = input()
b = input()
print(countCommonDivisors(a, b))