def PalindromeNumber(x):
    orginal_num=x
    reverse_num=0

    if x<0:
        return False
    while x>0:
        reverse_num=reverse_num*10+x%10
        x//=10

    return reverse_num==orginal_num

print(PalindromeNumber(121))

print(PalindromeNumber(-121))

print(PalindromeNumber(10))

print("****************************")
def isPolindrom(x):
    s=str(x)
    return s==s[::-1]

print(isPolindrom(343))
print(isPolindrom(232))
print(isPolindrom(23))

