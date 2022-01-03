# https://quera.ir/problemset/298/

def is_prime(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5)+2, 2):
            if number % i == 0:
                return False
        return True


def prime_factors(number: int):
    output: str = ""
    factor = 2
    while number > 1:
        power = 0
        while number % factor == 0 and is_prime(factor):
            power += 1
            number //= factor
        if power > 1:
            output = output + \
                f"*{factor}^{power}" if output else f"{factor}^{power}"
        elif power == 1:
            output = output + \
                f"*{factor}" if output else f"{factor}"
        factor = 3 if factor == 2 else factor+2
    return output


print(prime_factors(int(input())))
