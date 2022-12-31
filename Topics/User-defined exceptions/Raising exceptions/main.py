class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    total = a + b
    if total < 0:
        raise NegativeSumError
    else:
        return total
