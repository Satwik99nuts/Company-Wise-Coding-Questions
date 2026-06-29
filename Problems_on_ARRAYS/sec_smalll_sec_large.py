def sec_largest(arra):
    largest = None
    second_largest = None

    for number in arra:
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (
            second_largest is None or number > second_largest
        ):
            second_largest = number

    if second_largest is None:
        raise ValueError("The array must contain at least two distinct numbers")

    return second_largest


def sec_smallest(arra):
    smallest = None
    second_smallest = None

    for number in arra:
        if smallest is None or number < smallest:
            second_smallest = smallest
            smallest = number
        elif number != smallest and (
            second_smallest is None or number < second_smallest
        ):
            second_smallest = number

    if second_smallest is None:
        raise ValueError("The array must contain at least two distinct numbers")

    return second_smallest


arra = list(map(int, input().lstrip("\ufeff").split()))

try:
    print("Second largest:", sec_largest(arra))
    print("Second smallest:", sec_smallest(arra))
except ValueError as error:
    print(error)
