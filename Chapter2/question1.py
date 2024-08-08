def is_leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False
        return True


for i in range(1950, 2051):
    if is_leap_year(i):
        print(i, end=" ")

