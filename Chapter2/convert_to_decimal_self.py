num = input("変換したい2進数を入力してください。:")

ans = 0
for i in range(len(num)):
    ans += int(num[i]) * (2 ** (len(num)-i-1))

print(ans)