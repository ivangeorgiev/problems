from collections.abc import Iterator


def numbers() -> Iterator[(int, int)]:
    given_digits = set("123456")
    for six_digit_number in range(10000, 1000000):
        digits = str(six_digit_number)
        if set(digits) != given_digits:
            continue
        for num_digits_x in range(1, 6):
            yield int(digits[:num_digits_x]), int(digits[num_digits_x:])

def is_valid_combination(x: int, y: int):
    digits = set(f"{x}{y}")
    return digits == {1,2,3,4,5,6}


def compute_expr(x: int, y: int) -> int:
    return round(x*y*(x-y) - (x + y)*x/y)

max_e = None
max_combination = None
for x,y in numbers():
    e = compute_expr(x, y)
    if max_e is None or max_e < e:
        max_e = e
        max_combination = x, y
x_max, y_max = max_combination
print(f"x = {x_max}, y = {y_max}, E = {max_e}")
