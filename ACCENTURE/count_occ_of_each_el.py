# Given an array, count how often every distinct value appears.
# Example: [10, 5, 10, 15, 10, 5] -> {10: 3, 5: 2, 15: 1}


def count_each_element(numbers):
    """Return a dictionary mapping each value to its occurrence count."""
    counts = {}

    for number in numbers:
        # Start a new value at 0, then add this occurrence.
        counts[number] = counts.get(number, 0) + 1

    return counts


values = [10, 5, 10, 15, 10, 5]
print(count_each_element(values))  # {10: 3, 5: 2, 15: 1}
