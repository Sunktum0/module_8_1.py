def add_everything_up(a, b):
    try:
        if a and b == int or float:
            c = a + b
            rounded_num = round(c, 3)
            return rounded_num
    except TypeError:
        if a or b == str:
            c = str(a) + str(b)
            return c

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))