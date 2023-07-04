"""Brings a base to a given power in log N time."""


def power(base, pow, multiply=lambda x, y: x * y):
    answer = 1
    while pow > 0:
        if pow % 2 == 1:  # odd
            answer = multiply(answer, base)
            pow -= 1
        else:  # even
            pow //= 2
            base = multiply(base, base)
    return answer


def _print(x, y):
    print(f"{x} ** {y} = {x ** y} | {power(x, y)}")


if __name__ == "__main__":
    _print(1, 0)
    _print(1, 10)
    _print(2, 10)
    _print(3, 10)
    _print(4, 10)
    _print(5, 10)
    _print(6, 10)
