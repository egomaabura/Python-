def convert_to_japanese_calender(n):
    if n < 1869 or 2020 < n:
        print("1869～2020年を入力してください。")
    elif 1869 <= n <= 1911:
        print(f"明治{n - 1867}年")
    elif 1912 <= n <= 1925:
        print(f"大正{n - 1911}年")
    elif 1926 <= n <= 1988:
        print(f"昭和{n - 1925}年")
    elif 1989 <= n <= 2018:
        print(f"平成{n - 1988}年")
    elif 2019 <= n <= 2020:
        print(f"令和{n - 2018}年")

convert_to_japanese_calender(int(input("西暦：")))