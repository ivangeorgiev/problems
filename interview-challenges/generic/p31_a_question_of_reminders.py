def get_numbers():
    requirements = {i: i-1 for i in range(3,10)}
    num = 9
    while True:
        is_compliant = True
        for divisor, reminder in requirements.items():
            is_compliant = (num % divisor) == reminder
            if not is_compliant:
                break
        if is_compliant:
            yield num
        num += 10


numbers = get_numbers()
for _ in range(3):
    print(next(numbers))
