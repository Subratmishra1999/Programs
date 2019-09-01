def sumDigits(n):
    if(len(n)==1):
        print(n)
    else:
        c=[int(_) for _ in n]
        sumDigits(str(sum(c)))
n=input()
sumDigits(n)
