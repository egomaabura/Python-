def convert(num, base):
    ans = ""
    while num > 0:
        ans = str(num % base) + ans
        num //= base
    
    return ans


num = int(input("整数を入力してください。："))
base = int(input("変換したい基数を入力してください。："))

ans = convert(num, base)
print(*ans, sep="")